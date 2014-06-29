# Inherit

##多继承

```cpp
class B{
public:
    virtual void print(){
        cout<<"B"<<endl;
    }
};

class C{
public:
    virtual void print(){
        cout<<"C"<<endl;
    }
};

class D : public B, public C{
public:
    void print2(){
        cout<<"D"<<endl;
    }
};


int main(){
    //D d; d.print(); error
    B * b = new D();
    b->print();
    return 0;
}
```

1. 在发生多继承的情况下，如果继承类D，实例化一个对象，那么由于其两个父类都包含print这个成员函数，因此它不知道应该调用哪一个，于是编译时会出错
2. 利用虚函数多态的机制，D中包含了两张指向B，C的虚函数表。因此，<code>B * b = new D();</code>均是合法的操作。

##虚继承
参考:[http://www.cnblogs.com/BeyondAnyTime/archive/2012/06/05/2537451.html](http://www.cnblogs.com/BeyondAnyTime/archive/2012/06/05/2537451.html)
###为什么要引入虚拟继承
虚拟继承是多重继承中特有的概念。虚拟基类是为解决多重继承而出现的。如:类D继承自类B1、B2，而类B1、B2都继承自类A，因此在类D中两次出现类A中的变量和函数。为了节省内存空间，可以将B1、B2对A的继承定义为虚拟继承，而A就成了虚拟基类。实现的代码如下：

class A

class B1:public virtual A;

class B2:public virtual A;

class D:public B1,public B2;

虚拟继承在一般的应用中很少用到，所以也往往被忽视，这也主要是因为在C++中，多重继承是不推荐的，也并不常用，而一旦离开了多重继承，虚拟继承就完全失去了存在的必要因为这样只会降低效率和占用更多的空间。

###附一些求size的常见类型
* 空类及只包含成员函数: sizeof(class) = 1
* 包含虚函数： sizeof(class) = 指针的大小(64位机器为8，32位机器为4)

```cpp
class Test{
public:
    virtual void test(){

    }
};
```
* 普通继承： sizeof(class) = 指针的大小(64位机器为8，32位机器为4)

```cpp
class C{
public
    virtual void print(){
        cout<<"C"<<endl;
    }
};

class D : public B{
public:
    void print2(){
        cout<<"D"<<endl;
    }
};
```
* 多重继承 sizeof(class) = 两个指针大小

```cpp
class D : virtual public B, virtual public C{
public:
    virtual void print2(){
        cout<<"D"<<endl;
    }
};
```

* 菱形虚继承，这个应该是虚继承的关键，虚继承的子类共享内存。

下面的sizeof(D) 为24，即8(指向C的指针)+8(指向D的指针)+8(int的4+补对齐)
```cpp
class A{
public:
    int a;
};

class B: virtual public A{
public:
    virtual void print(){
        cout<<"B"<<endl;
    }
};

class C: virtual public A{
public:
    virtual void print(){
        cout<<"C"<<endl;
    }
};

class D : public B, public C{
public:
    void print2(){
        cout<<"D"<<endl;
    }
};

```

若将上面代码中的B与C的虚继承去掉，则sizeof(D)为32，因为32=8(指向C的指针)+8(指向D的指针)+8(C中继承来的int的4+补对齐)+8(D中继承来的int的4+补对齐)
