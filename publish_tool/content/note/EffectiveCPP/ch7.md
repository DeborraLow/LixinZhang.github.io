Title: Effective C++ 笔记 Chapter6
Date: 2014-08-02 18:23
Category: CPP
Tags: CPP


##模板与泛型编程

###了解隐式接口与编译期多态

1. classes和templates都支持接口(interface)和多态(polymorphism)
2. 对class而言接口是显示的(explicit)，以函数签名为中心。多态则是通过virtual函数发生于<code>运行期</code>。
3. 对于template参数而言，接口是隐式的（implicit），奠基于有效表达式。多态则是通过template具现化和函数重载解析发生于<code>编译器</code>。

###了解typename的双重含义

*. 声明template参数时，关键字<code>class</code>与<code>typename</code>可互换，如:

    :::cpp
    template<class T>
    template<typename T>

    *. 当标示嵌套从属类型名称时，必须使用<code>typename</code>, 如：
        
        :::cpp
        template<typename T>
    void print2nd(const T&container) {
        for(typename T::const_iterator iter=container.begin(); iter!=container.end(); iter++){
            cout<<(*iter)<<endl;
        }
    }

    int main(){
        std::vector<int> v;
        v.push_back(1);
        v.push_back(2);
        v.push_back(3);
        v.push_back(4);
        print2nd(v);
        return 0;
    }

<code>typename T::const_iterator iter</code>不使用<code>typename</code>，或者使用<code>class</code>编译均报错。这里的<code>T</code>指代<code>vector\<int\></code>，属于嵌套模板类型。

###学习处理模板化基类内的名称

看下面的例子，定义一个模板化的基类MsgSender，然后定义继承类LoggingMsgSender：

    :::cpp
    template<typename Company>
    class MsgSender{
    public:
        void sendmsg(){
            Company c;
            c.saysomething();
        }
    };


    template<typename Company>
    class LoggingMsgSender: public MsgSender<Company>{
    public:
        void sendLoggingMsg(){
            sendmsg(); //编译error
        }
    };

上述代码直接编译会报错，原因是继承类<code>LoggingMsgSender</code>在继承<code>MsgSender<Company></code>，并不知道它继承什么样的class，在<code>MsgSender<Company></code>未具现化之前，无法判断是够存在一个sendmsg函数。因此，我们需要明确的指出来，有三种方式：

用this指针明确告知存在。
    :::cpp
    template<typename Company>
    class LoggingMsgSender: public MsgSender<Company>{
    public:
        void sendLoggingMsg(){
            this->sendmsg();
        }
    };

用using声明存在。
    :::cpp
    template<typename Company>
    class LoggingMsgSender: public MsgSender<Company>{
    using MsgSender<Company>::sendmsg;
    public:
        void sendLoggingMsg(){
            sendmsg();
        }
    };

直接使用基类，但是也关掉了多态性质，因此不提倡这种方法。
    :::cpp
    template<typename Company>
    class LoggingMsgSender: public MsgSender<Company>{
    public:
        void sendLoggingMsg(){
            MsgSender<Company>::sendmsg();
        }
    };

在看一下：

    :::cpp
    class CompanyA{
    };
    int main(){
    LoggingMsgSender<CompanyA> sender;
    //sender.sendLoggingMsg();
    return 0;
    }

如不调用<code>sender.sendLoggingMsg()</code>，现在完成的情况就可以通过编译，然而若调用<code>sender.sendLoggingMsg()</code>，则会编译出错，原因很简单，找不到<code>CompanyA</code>是否存在<code>saysomething</code>函数。 因此，模板的诊断可以发生在定义时，也可能发生在具体实现时。最后，在<code>CompanyA</code>类中添加缺失的函数。

    :::cpp
    class CompanyA{
    public:
        void saysomething(){
            cout<<"hi"<<endl;
        }
    };

