Title: Effecive C++ 笔记 Chapter1 
Date: 2014-04-26 16:23
Category: CPP
Tags: CPP
##让自己习惯C++
###视C++为一个语言联邦
* C++主要包括四个次语言:
    * <code>C</code>
    * <code>Object-Oriented C++</code>
    * <code>Template C++</code>
    * <code>STL</code>

###尽量以const,enum,inline替换#define
* 使用如下<code>#define ASPECT_RATIO 1.653</code>语句时，程序在编译时会将所有的<code>ASPECT_RATIO</code>替换为<code>1.653</code>。这样，在调试程序的时候，很难确定<code>1.653</code>到底是哪来的，是<code>ASPECT_RATIO</code>定义的，还是从其他define过来的。其原因是<strong>你所使用的名称并为进入记号表</strong>。 解决的方法是使用常量替换上述宏<code>const double AspectRatio = 1.653</code>。
* 无法使用define来创建类的专属变量，因为<code>#define</code>并不重视作用域。
    
        :::cpp
        class Test{
        public :
            Test(){
            }
            static const int NumTruns = 1;
        };
        
* 使用enum hack的方法，这个hack方法不错。

        :::cpp
        class Test{
        public :
            Test(){
            }
            enum {numTurns = 5};
            int arr[numTurns];
        };
        
* 用inline替换<code>#define 函数</code>，如<code>#define CALL_WITH_MAX(a,b) f((a)>(b) ? (a) : (b))</code>，在定义，切记对括号的正确使用，因为define是替换，如果不加括号，就容易出问题。使用<code>inline</code>来替换它
        
        :::cpp
        template<typename T>
        inline void callWithMax(const T& a, const T& b){
            f(a>b?a:b);
        }
        
###尽可能使用const
* const常出现的问题

        :::cpp
        char greeting[] = "hello";
        char * p = greeting;
        const char * p = greeting; //non-const pointer, const data
        char * const p = greeting; /const pointer, non-const data
        const char * const p = greeting; //const pointer, const data
        
  理解的方法，<code>const</code>在<code>*</code>号左边指const值，在星号右边指pointer本身是const的。
       
        :::cpp
        const std::vector<int>::iterator iter; //const pointer
        std::vector<int>::const_iterator iter; // const data, 一般用于遍历的时候用
        
        
* <strong>const 成员函数不能修改类的成员变量，怎么理解？ </strong></code> 因为，对于const成员函数，const改变了隐含的<code>this</code>形参的类型，即将this指针改变成了指向其对象本身的const指针，即<code>const ClassA * const this</code>，因此this所指向的对象值是不能改变的，即<code>this->member = rhs</code>非法。<code>mutable</code>可以解决这个问题，即将成员变量声明为mutable即可。mutable的中文意思是“可变的，易变的”，跟constant（既C++中的const）是反义词。在C++中，mutable也是为了突破const的限制而设置的。被mutable修饰的变量，将永远处于可变的状态，即使在一个const函数中。
  
###确定对象被使用前已先被初始化
* 先看一段代码：

        :::cpp
        class ABEntry{
        public :
            AbEntry(const std::string & name, const std::list<PhoneNumber> & phones);
        private :
            std::string theName;
            std::list<PhoneNumber> thePhones;
            int numTimesConsulted;
        }
        ABEntry::ABEntry(const std::string & name, const std::list<PhoneNumber> & phones, int numTimesConsulted){
        //这些是赋值，而非初始化，也成为伪初始化
            theName = name;
            thePhones = phones;
            numTimesConsulted = 0;
        }
        
* C++规定，对象的成员变量的初始化动作发生在进入构造函数本体之前。初始化发生的时间更早，发生于这些成员的default构造函数被自动调用之时。<code>numTimesConsulted</code>为内置类型，不保证你所看到的那个赋值操作的时间点之前获得处置。
* 使用成员初始化列表（member initialisation list）,且如果成员变量为const或references，由于一定需要初始值，就必须使用成员初始化列表。

        :::cpp
        ABEntry::ABEntry(const std::string & name, const std::list<PhoneNumber> & phones, int numTimesConsulted):theName(name), thePhones(phones), numTimesConsulted(0){}
        
#### static对象
* static对象，其寿命从被构造出来直到程序结束为止，在全局内存区。函数内的static对象为<code>local static</code>对象，其他对象为<code>non-local static</code>对象。static对象的析构函数会在main函数结束时候调用。
* 一个问题：对于A,B两个源文件，A,B均包含<code>non-local static</code>对象，当互相引用时，它所用的<code>non-local static</code>对象可能尚未初始化。为了解决这个问题，将每个<code>non-local static</code>对象搬到自己的专属函数内（该对象在此函数内被声明为static），这些函数返回一个reference指向它所含的对象，用户使用该函数。这是设计模式中<code>Singleton</code>模式的一种常见实现手法。
* 上步的方法，这些函数“内置static对象”，在多线程模式下会有问题（多个线程同时访问该函数），其初始化会存在不确定问题。
* 无论是<code>local static</code>还是<code>non-local static</code>对象，在多线程环境下“等待某事发生”都会有麻烦。处理方法：在程序单线程启动之前，先调用所有的<code>reference-returning </code>函数。

            