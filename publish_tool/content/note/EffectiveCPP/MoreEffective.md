Title: More Effective C++ 笔记(Chapter1_2)
Date: 2014-05-12 19:23
Category: CPP
Tags: CPP


###绝对不要以多态方式处理数组
这节主要就是在讲解数组的取地址的访问形式。
直接在代码上看这个问题：
    
    :::cpp
    class Base{
    public:
        virtual void print(){
            cout<<"base"<<endl;
        }
        virtual ~Base(){
            cout<<"Destructor Base"<<endl;
        }
    };

    class Derived : public Base{
    public:
        virtual void print(){
            cout<<"derived"<<endl;
        }
        int tmp;
        virtual ~Derived(){
            cout<<"Destructor Derived"<<endl;
        }
    };

    void havefun(Base arr[], int N){
        for(int i=0; i<N; i++){
            arr[i].print();
        }
    }


    int main(){
        cout<<sizeof(Base)<<endl; //8 
        cout<<sizeof(Derived)<<endl; //16
        Base bases[10];
        havefun(bases, 10); //没问题
        Derived derives[10];
        havefun(derives, 10); //错误，因为arr[i]，表示*(arr+i),取的地址是arr的地址+sizeof(Base)*i.由于sizeof(Base)与sizeof(Derived)是不同的，因此出错。

        //引用和指针是实现多态的基本方式
        Base &bb = derives[0];
        Base * p = new Derived();
        Base * parr = new Derived[10];
        havefun(parr, 10); //错误，与上诉类似

        //delete [] parr; //错误，引文delete数组可以理解为 for 1 to n : delete object. 仍然要进行类似arr[i]的操作。
        return 0;
    }

###对定制的“类型转换函数”保持警觉

两种函数允许编译器执行隐式类型转换：单自变量<code>constructors</code>和隐式类型转换操作符。所谓单自变量<code>constructors</code>是指能够以单一自变量成功调用的<code>constructors</code>。

    :::cpp
    class Name{
    public:
        Name(const string s){
        }
        Name(const char * s){

        }
        Name(const int number){

        }
        operator string() const{
            string tmp="operator";
            return tmp;
        }
    };
    int main(){
        string oriName = "peter"; 
        Name name = oriName; //基于构造函数的隐式类型转换
        Name name2 = "peter"; //基于构造函数的隐式类型转换
        Name name3 = 12;//基于构造函数的隐式类型转换
        string s = name; //基于操作符的隐式类型转换
        return 0;
    }

有的时候，我们希望阻止这种隐式的类型转换。 有两种方式，例如如果我们想阻止<code>Name name = "peter";</code>所产生的隐式类型转换，可以只使用<code>Name(const string s)</code>，丢弃<code>Name(const char * s)</code>，使得string类型作为一种代理类（proxy classes）的方式解决隐式类型转换的问题。 其次，使用<code>explicit</code>关键字作用于构造函数，阻止其类型转换，如：
    :::cpp
    class Name{
    public:
        Name(const string s){
        }
    }


###区别increment/decrement操作符的前置(prefix)与后置(postfix)形式
C++提供自定义类的<code>++A与A++</code>的支持

    :::cpp
    class UPInt{
    public:
        UPInt & operator++(); //++A
        const UPInt operator++(int); //A++
        UPInt & operator--();
        const UPInt operator--(int);    
    };

    UPInt& UPInt::operator++(){
        *this += 1;
        return *this;
    }

    const UPInt UPInt::operator++(int){
        UPInt oldValue = *this;
        ++(*this);
        return oldValue;
    }

    UPInt i;
    i++;
    ++i;

通过上面的代码，可以看出以下几点：

1. C++为了提供<code>++A与A++</code>的支持，提供使用<code>operator++(int)</code>中的默认int参数来区分前置与后置。

2. <code>++A与A++</code>区别，通过代码很容易看出来，<code>++A</code>返回的是处理过后的源对象引用，而<code>A++</code>则是返回的旧值，而且在实际实现过程中是调用了前置的实现，这样的好处是，维护同一个自增的逻辑。且很明显后置要比前置耗费资源，因此建议使用前置提高效率。

3. 第2条的说明也解释了为什么<code>++++i</code>合法，而<code>i++++</code>是非法的。因为<code>i++</code>返回的是一个旧值，你对旧值++是与原意不符的，容易产生混淆。

###了解各种不同意义的new和delete
主要提及了<code>new</code>和<code>delete</code>操作符的三种用法：

####new operator
做两件事情：第一，分配足够的内存，用来放置某类型的对象。第二，调用一个constructor，为刚才分配的内存中的那个对象设置初值。

    :::cpp
    string * str = new string("hello world");

####operator new
C++提供了一种类似C语言中的<code>malloc与free</code>函数的功能。它唯一的任务就是分配内存

    :::cpp
    void * p= operator new(10);

####Placement new
引用[stackOverflow](http://stackoverflow.com/questions/222557/what-uses-are-there-for-placement-new)中的解释

You may want to do this for optimizations (it is faster not to re-allocate all the time) but you need to re-construct an object multiple times. If you need to keep re-allocating it might be more efficient to allocate more than you need, even though you don't want to use it yet.

> Standard C++ also supports placement new operator, which constructs an object on a pre-allocated buffer. This is useful when building a memory pool, a garbage collector or simply when performance and exception safety are paramount (there's no danger of allocation failure since the memory has already been allocated, and constructing an object on a pre-allocated buffer takes less time):

    :::cpp
    char *buf  = new char[sizeof(string)]; // pre-allocated buffer
    string *p = new (buf) string("hi");    // placement new
    string *q = new string("hi");          // ordinary heap allocation

You may also want to be sure there can be no allocation failure at a certain part of critical code (maybe you work on a pacemaker for example). In that case you would want to use placement new.

Deallocation in placement new

You should not deallocate every object that is using the memory buffer. Instead you should delete[] only the original buffer. You would have to then call the destructors directly of your classes manually. For a good suggestion on this please see Stroustrup's FAQ on: Is there a "placement delete"?



