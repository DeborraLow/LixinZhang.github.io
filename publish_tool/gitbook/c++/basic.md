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
