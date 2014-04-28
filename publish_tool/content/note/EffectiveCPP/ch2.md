Title: Effecive C++ 笔记 Chapter2
Date: 2014-04-26 19:23
Category: CPP
Tags: CPP

##构造/析构/赋值运算

###了解C++默默编写并调用的哪些函数

当创建一个空的类，构造函数默认会为该类创建4个public的inline函数。
        
    :::cpp
    class Empty{};
    //等价于
    class Empty {
    public :
        Empty(){...} //默认构造函数
        Empty(const Empty & rhs) {...} //拷贝构造函数
        ~Empty(){...} //析构函数
        Empty & operator=(const Empty & rhs){...} //拷贝赋值操作符
    }

编译器创建的拷贝构造函数、赋值函数只是将来源对象的每个non-static对象成员变量拷贝到目标对象。因此，当类成员变量包含引用和常量的时候，简单靠编译器自动创建的拷贝构造函数与赋值函数变无法使用，需要自己手动定义。

###若不想使用编译器自动生成的函数，就该明确拒绝

由于编译器会自动创建默认的构造、拷贝、赋值、析构等函数，如果我们要求某个类不能被调用这些函数，该怎么办？ 一个直接的想法是将这些函数定义成private成员函数，但是这个方法有个问题，就是通过友元的方式仍可以调用。另一种方法是定义一个base class.

    :::cpp
    class Uncopyable{
    protected : //允许继承对象构造和析构
        Uncopyable(){}
        ~Uncopyable(){}
    private :
        Uncopyable(cosnt Uncopyable &);
        Uncopyable & operator=(const Uncopyable &);
    };
    class Test:private Uncopyable{
        ...
    };

通过私有继承该base class，可以实现拒绝调用拷贝和赋值拷贝函数的调用的作用。

###为多态基类声明virtual析构函数

若基类含有的是非虚析构函数，那么当<code>Base * p = new Derived(); delete p;</code>时，p默认只会调用Base的析构函数，那么在Derived中出现的内存资源不会被释放，造成内存泄露。因此将Base类中的析构函数定义为虚析构函数，且在继承类中继承该虚函数，并实现，这样delete的时候，就会先调用继承类虚构函数，然后再调用Base类虚构函数。

关于虚函数：
> 预实现出virtual函数，对象必须携带某种信息，主要用来在运行期决定哪个virtual函数该被调用。这份信息通常是由一个所谓的vptr(virtual table pointer)指针指出。vptr指向一个由函数指针构成的数组，称为vtbl（virtual table）。每个带有virtual函数的class都有一个相应的vtbl。当对象调用某一virtual函数，实际被调用的函数取决于该对象的vptr所指的那个vtbl——编译器在其中寻找适当的函数指针。

STL中很多类不存在虚构造函数，如string， vector， list， set， tr1:unordered_map等。 因此继承他们的时候要格外小心。

###别让异常逃离析构函数

当析构函数释放多个资源的时候，如<code>vector<widget> v </code>如果第一个对象释放时抛出了异常，接下来的对象也应该进行释放，如果释放过程中又抛出了异常，多个异常对于c++会产生不明确的行为。因此，应该在析构函数中合理的捕捉异常，要么捕捉后，abort退出，要么打日志记录下来，即不让该异常传播。如果客户需要对某个操作函数运行期间抛出的异常做出反应，那么class应该提够一个普通函数（而非在析构函数中）执行该操作。

###不在构造和析构函数过程中调用virtual函数

先看段代码：
    
    :::cpp
    class Base{
    public:
        Base(){
            num = 1;
            nonPureVirFunction();
        } 
        ~Base(){
            nonPureVirFunction2();
            //PureVirFunction(); //编译给出warning，运行error
        }
        virtual void nonPureVirFunction(){
            cout<<"base constructor"<<endl;
            cout<<num<<endl;
        };
        virtual void nonPureVirFunction2(){
            cout<<"base destructor"<<endl;
            cout<<num<<endl;
        };
        virtual void PureVirFunction() = 0;
        int num;
    };

    class Derived : public Base{
    public:
        Derived(){
            //nonPureVirFunction();
            num = 10;
        } 
        ~Derived(){
        }
        virtual void nonPureVirFunction(){
            cout<<"derived constructor"<<endl;
            cout<<num<<endl;
        }
        virtual void nonPureVirFunction2(){
            cout<<"derived destructor"<<endl;
            cout<<num<<endl;
        };
        virtual void PureVirFunction(){
            cout<<"derived Pure"<<endl;
        }
    };

    int main(){
        Base * base = new Derived();
        delete base;
        return 0;
    }

上面代码，执行后的结果：
<pre>
warning: delete called on 'Base' that is abstract but has non-virtual destructor [-Wdelete-non-virtual-dtor]
delete base;
^
1 warning generated.
base constructor
1
base destructor
10
</pre>
分析一下： 我们本希望通过多台的虚函数机制，使得我们操作base对象如同操作Derived一样，即构造和析构的时候，可以自动找到继承类的对虚函数的实现。然而实际结果却不是这样。另外，在基类中调用纯虚函数更会有问题，因为会调用一个根本未定义的函数。
这里直接给出<code>C++ primter</code>中给出的关于构造函数与析构函数中的虚函数讲解。
> 运行构造函数或析构函数的时候，对象都是不完整的。为了适应这种不完整，编译器将对象的类型视为在构造和析构期间发生了变化。在基类构造或析构函数中，将派生类对象当做基类类型对待。即如果在构造或析构函数中调用虚函数，其运行的是为构造函数或析构函数自身类型定义的版本。

###令<code>operator=</code>返回一个<code>reference to *this</code>

这个比较简单了，即完成类似<code>a=b=c</code>的连锁赋值，赋值操作符必须返回一个reference指向操作符的左侧实参。 如<code>Widget & operator=(const Widget & rhs)</code>。其他操作符也应该应用这种协议。

###在<code>operator=</code>中处理"自我赋值"

这个也是常见的问题：

    :::cpp
    Widget::operator=(const Widget & rhs){
        delete pb;
        pb = new Bitmap(*rhs.pb);
        return *this;
    }

如上述代码，如果rhs与this指向同一个对象，那么，在delete pb的时候，相当于也把rhs中的pb delete掉了。这样，在new新的对象的时候，就会出现问题了。一种解决方法：

    :::cpp
    Widget::operator=(const Widget & rhs){
        if(this == &rhs) return *this;
        delete pb;
        pb = new Bitmap(*rhs.pb);
        return *this;
    }

上面的方法，保证了<code>自我赋值安全</code>，但没有保证<code>异常安全</code>。何为<code>异常安全</code>，即在<code>delete pb</code>之后的new操作出现问题时，pb被删除掉了，但也没有new成功，这样导致pb指向一块不明确的地址空间。如其他地方又进行了delete pb的，那么就会出现问题。 一个改进的方法是：

    :::cpp
    Widget::operator=(const Widget & rhs){
        Bitmap * porig = pb;
        pb = new Bitmap(*rhs.pb);
        delete porig;
        return *this;
    }

即把delete操作移到后面，这样即使new不成功，还有porig保存着原来的值，不会出现之前提到的问题，这也保证了所说的<code>异常安全</code>性。

###复制对象时勿忘记其每一个成分

这一节主要说的就是当你自定义构造函数的时候，不要忘记了基类所需要的成员变量，因此在继承类的构造函数要记得调用base类的构造函数，类似 

    :::cpp
    Derived::Derived(const int p, const int num p2)
    :Base(p),p(p2) {...}

此外，对于拷贝构造函数、拷贝复制操作符等不要互相调用，应该创建一个公共的第三方函数，共两者调用，一般为<code>private init</code>函数之类的。


