Title: Effective C++ 笔记 Chapter3
Date: 2014-04-29 9:23
Category: CPP
Tags: CPP

##资源管理

###以对象管理资源

主要是为了解决下述问题，如：

    :::cpp
    void f(){
        Object * o = new Object();
        ...
        delete o;
    }

当<code>...</code>中发生异常，或是存在return，break等语句，导致不能执行到<code>delete o</code>时，那么对象<code>o</code>就会造成资源泄漏。 一个解决的办法就是将其放到一个对象里，利用对象的析构函数来达到释放的目的，因为当对象生命期结束时，析构函数是一定会执行的。 

对资源管理的有用工具就是智能指针，书中主要提及了<code>auto_ptr</code>和<code>shared_ptr</code>，这里加一种<code>unique_ptr</code>。关于<code>unique_ptr</code>，有：

>  auto_ptr class template is deprecated as of C++11. unique_ptr is a new facility with a similar functionality, but with improved security (no fake copy assignments), added features (deleters) and support for arrays. See unique_ptr for additional information.

接下来看一个例子：

    :::cpp
    class object{
    public :
        object(int num=1){this->num=num;}
        ~object(){cout<<num<<endl;}
        int num;
    };

    class state_deleter {  // a deleter class with state
    public:
      template <class T>
      void operator()(T* p) {
        delete [] p;
      }
    };

    int main(){
        std::unique_ptr<object, state_deleter> u1(new object[10]());
        std::auto_ptr<object> u2(new object(2));
        //std::unique_ptr<object, state_deleter> u3 = u1; //unique_ptr取消了"operator ="操作符
        std::auto_ptr<object> u4 = u2; // u4->object, u2=NULL
        assert(u2.get()==NULL);
        return 0;
    }

总结一下几点：

1. 不能有多个<code>auto_ptr</code>或<code>unique_ptr</code>对象同时指向一个原始对象指针(raw pointer),原因是，每个<code>auto_ptr</code>或<code>unique_ptr</code>对象在生命期结束时，都会调用析构析构释放资源，那么对同一原始指针多次释放同一个资源就会出现问题。
* <code>auto_ptr</code>支持赋值操作，如<code>u4=u2</code>,这样raw pointer将会赋值给u4，而u2的所指向raw pointer变为NULL。而<code>unique_ptr</code>取消了这种机制。
* <code>auto_ptr</code>和<code>unique_ptr</code>对象默认均不支持数组对象，<code>unique_ptr</code>需要自定义<code>deleter</code>类，来完成对指针数组的多个对象进行释放，即上述代码提及的那样。
* <code>shared_ptr</code>则是“引用计数型指针”，他支持拷贝，赋值等多个行为，生成的多个对象以引用计数的方式共存，并指向同一个raw pointer，但引用计数为0时，自动释放资源。


###在资源管理类中小心copying行为
上节写的东西，这节也都提及了。主要强调自定义资源管理对象的时候，要注意copy函数（copy构造函数和copy赋值操作符），对待copy操作一般有两种行为：抑制copying，施行引用计数法（reference counting）。

###对原始资源的访问
在本章第一节的代码中出现了<code>assert(u2.get()==NULL);</code>，其实就是对u2原始资源的访问。对原始资源的访问可能经由显式转换或隐式转换。一般而言，显式转换比较安全，但隐式转换对客户比较方便。

###成对使用new和delete时要采用相同的方式
这一节也比较简单，直接摘抄书中原文

> 如果你在new表达式中使用[], 必须在相应的delete表达式中也使用[]。如果你在new表达式中不使用[], 一定不要在相应的delete表达式中使用[].

###以独立语句将newed对象置于智能指针

主要是为了解决：

    :::cpp
    processWidget(std::shared_ptr<Widget>(new Widget), priority());

问题：不知道下面三个子语句的真实调用顺序

1. <code>new Widget</code>, 
2. <code>std::shared_ptr<Widget>(new Widget)</code>
3. <code>priority()</code>

如果编译器的执行顺序为<code>1->3->2</code>，那么1执行完，在执行2的时候程序崩溃了，就会使得1中创建的对象内存泄漏。为了避免这样的错误，因此尽量不要将多个子语句放在一起。我们要明确的知道其执行顺序。改成：

    :::cpp
    std::shared_ptr<Widget>(new Widget) p;
    processWidget(p, priority());

