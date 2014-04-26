Title: Effecive C++ 笔记 Chapter2
Date: 2014-04-26 19:23
Category: CPP
Tags: CPP

##构造/析构/赋值预算

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

由于编译器会自动创建默认的构造、拷贝、赋值、析构等函数，如果我们要求某个类不能被调用这些函数，该怎么办？ 一个直接的想法是将这些函数定义成private成员变量，但是这个方法有个问题，就是通过友元的方式仍可以调用。另一种方法是定义一个base class.

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

通过该继承该base class，可以实现拒绝调用拷贝和赋值拷贝函数的调用的作用。

###为多态基类声明virtual析构函数

若基类含有的是非虚析构函数，那么当<code>Base * p = new Derived(); delete p;</code>时，p默认只会调用Base的析构函数，那么在Derived中出现的内存资源不会被释放，造成内存泄露。因此将Base类中的析构函数定义为虚析构函数，且在继承类中继承该虚函数，并实现，这样delete的时候，就会先调用继承类虚构函数，然后再调用Base类虚构函数。

关于虚函数：
> 预实现出virtual函数，对象必须携带某种信息，主要用来在运行期决定哪个virtual函数该被调用。这份信息通常是由一个所谓的vptr(virtual table pointer)指针指出。vptr指向一个由函数指针构成的数组，称为vtbl（virtual table）。每个带有virtual函数的class都有一个相应的vtbl。当对象调用某一virtual函数，实际被调用的函数取决于该对象的vptr所指的那个vtbl——编译器在其中寻找适当的函数指针。

STL中很多类不存在虚构造函数，如string， vector， list， set， tr1:unordered_map等。 因此继承他们的时候要格外小心。