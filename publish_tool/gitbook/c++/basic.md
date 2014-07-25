# Basic

##赋值问题
###类的静态成员变量、const成员变量，static const成员变量的定义问题

静态成员变量，在初始化之后必须先赋值，然后编译的时候会link不过。

####静态成员变量
在class外定义，如
```cpp
class A{
private:
    static int num;
};
int A::num = 100;
```
####const成员变量
在构造函数的初始化列表中定义，如
```cpp
class A{
public:
    A():num(100);
private:
    const int num;
};
```
####static const(const static) 成员变量
在class外定义，如
```cpp
class A{
private:
    static const int num;
};
int A::num = 100;
```

##volatile关键字

就像大家更熟悉的const一样，volatile是一个类型修饰符（type specifier）。它是被设计用来修饰被不同线程访问和修改的变量。如果没有volatile，基本上会导致这样的结果：要么无法编写多线程程序，要么编译器失去大量优化的机会。

volatile的作用： 作为指令关键字，确保本条指令不会因编译器的优化而省略，且要求每次直接读值.
简单地说就是防止编译器对代码进行优化.比如如下程序：
<pre>
XBYTE[2]=0x55;
XBYTE[2]=0x56;
XBYTE[2]=0x57;
XBYTE[2]=0x58;
</pre>
对外部硬件而言，上述四条语句分别表示不同的操作，会产生四种不同的动作，但是编译器却会对上述四条语句进行优化，认为只有XBYTE[2]=0x58（即忽略前三条语句，只产生一条机器代码）。如果键入volatile，则编译器会逐一的进行编译并产生相应的机器代码（产生四条代码）.
