Title: Effective C++ 笔记 Chapter6
Date: 2014-08-01 9:23
Category: CPP
Tags: CPP

##继承与面向对象设计

###避免遮掩继承而来的名称

* local变量的作用于会掩盖外部同名变量，且与变量的类型无关。

看个例子：

    :::cpp
    #include<iostream>
    using namespace std;

    class Base{
    public:
        void fun(int num){
            cout<<"Base:"<<num<<endl;
        }
        void fun(double num){
            cout<<"Base:"<<num<<endl;
        }
    };


    class Derived : public Base {
    public :
        //using Base::fun;
        void fun(int num){
            cout<<"Derived"<<endl;
        }
        void fun(){
            cout<<"Derived"<<endl;
        }
    };

    int main(){
        Derived d = Derived();
        d.fun();
        d.fun(10);
        d.fun(10.1);
        return 0;
    }

继承类<code>Derived</code>中的变量相当于local，而<code>Base</code>类中的相当于global。因此<code>Derived</code>的类函数名称默认会掩盖掉<code>Base</code>中的同名函数，因此外部调用Derived对象的时候只能看得见<code>void fun(int num)</code>和<code>void fun()</code>，而Base类中的<code>void fun(double num)</code>即使参数不同也被掩盖掉。如果想暴露这个函数，就必须在Derived中声明<code>using Base::fun;</code>。


###避免遮掩继承而来的名称

1. 接口继承与实现继承不同。在public继承下，derived classes总是继承base class的接口。
2. 纯虚函数只具体指定接口继承。
3. 非纯虚函数具体指定接口继承及<code>缺省</code>是实现继承。
4. 非虚函数具体指定接口继承以及<code>强制性</code>实现继承。

###绝不重新定义继承而来的缺省参数值

    :::cpp
    class Base{
    public:
        virtual void fun(int num=100){
            cout<<"Base:"<<num<<endl;
        }
    };


    class Derived : public Base {
    public :
        virtual void fun(int num = 10){
            cout<<"Derived:"<<num<<endl;
        }
    };

    int main(){
        Base * b = new Derived();
        Derived * d = new Derived();
        b->fun(); //echo Derived:100
        d->fun(); //echo Derived:10
        return 0;
    }

C++涉及两种类型，静态类型与动态类型。<code>Base * b = new Derived();</code>中，<code>b</code>本身为静态类型，而所指的对象类型为动态类型。而缺省参数值都是静态绑定的，因此即使<code>b</code>以多态的方式调用<code>Derived</code>中的函数，然而<code>num</code>的默认值仍未Base类中定义的缺省参数。

###Private 继承

Private继承意味着<code>is-implemented-in-terms-of</code>(根据某物实现出)，它通常比复合（has-a）的级别低。但是当继承类需要访问基类的protected成员，或需要重新定义继承而来的virtual函数时，这么设计是合理的。

Private继承并不代表<code>is a</code>的关系，如：

    :::cpp
    class Person {

    };

    class Student : private Person {

    };

    void testPerson(Person & p){

    }
    Person p;
    Student s;
    testPerson(p);
    testPerson(s);//Error

由于Student是<code>private</code>继承，因此无法通过函数<code>testPerson</code>, 若改为<code>public</code>继承则可以。
