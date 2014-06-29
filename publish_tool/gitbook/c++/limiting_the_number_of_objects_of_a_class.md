# Limiting the number of objects of a class
限制某个class所能产生的对象数量

##产生零个或一个对象
###原则：
1. 将类的构造函数定义为private（防止构造多个）
2. 为这个类产生一个提供static对象的接口（只允许访问至多一个）

###两种方式
举个打印机的例子，代码和说明如下。
```cpp
#include<iostream>
using namespace std;

class Printer{
public:
    void print(){
        cout<<"Message"<<endl;
    }
    //将Printer & thePrinter()这个函数声明为友员函数，否则它无法调用私有的构造函数
    friend Printer & thePrinter();
    static Printer & thePrinterInClass(){
        static Printer p;
        return p;
    }
    ~Printer(){
        cout<<"Desctructor"<<endl;
    }
private:
    Printer(){

    }
};
//放在全局区域
Printer & thePrinter(){
    static Printer p;
    return p;
}
```
但是将<code>thePrinter</code>函数放在class外面还是里面有比较大的不同。放在类外面有优势：
1. 由于类的静态函数中的静态成员会在编译期进行初始化，那么无论我们后来用不用，他都会被构造出来。而放在外面作为一个全局函数而言，则只会在调用该函数的时候，构造出来。
2. 由于类的静态成员的构造顺序根据编译器不同，会有很多不可预测的事情，无法保证有序性，而对于全局函数而言则可以。

由于<code>thePrinter</code>函数很短小，因此考虑是够可以使用<code>inline</code>技术，作者有如下说明：
> 函数如果带有内部连接，可能会程序中被复制，也就是说程序的目标代码(object code)可能会带有内部连接的函数复制一份以上的代码，而此复行为也包括函数内的static对象。结果程序可能会出现多份该static对象的拷贝。因此，千万不要产生内含local static对象的inline non-member fucntions

##不同的对象构造状态
1. 它自己
2. 派生物的"base class"成分
3. 内嵌于较大对象之中

###设计一个产生有限个数对象的类
利用计数机制与<code>pseudo-constructors</code>

```cpp
class Printer {
public:
    class TooManyObjects{};
    // pseudo-constructors,使用伪构造函数产生对象
    // 将构造函数声明为private，防止由于继承等导致的混淆的对象计数
    static Printer * makePrinter();
    static Printer * makePrinter(const Printer& rhs);

    private:
    static size_t numObjects;
    static const size_t maxObjects;
    Printer();
    Printer(const Printer& rhs);
};
// see below
// Obligatory definitions of class statics size_t Printer::numObjects = 0;
const size_t Printer::maxObjects = 10;
size_t Printer::numObjects = 0;

Printer::Printer() {
    if (numObjects >= maxObjects) {
        throw TooManyObjects();
    }
}
Printer::Printer(const Printer& rhs) {
    if (numObjects >= maxObjects) {
        throw TooManyObjects();
    }
}
Printer * Printer::makePrinter() {
    return new Printer;
}
Printer * Printer::makePrinter(const Printer& rhs) {
    return new Printer(rhs);
}
```

* 使用伪构造函数产生对象,将构造函数声明为private，防止由于继承等导致的混淆的对象计数。如下代码中，均是非法的。
```cpp
class PrinterB: public Printer{
};
class PrinterC{
public:
    Printer A;
};
//PrinterB b; 非法
//PrinterC c; 非法
```
* 上条很好的解释了对象的不同构造状态的影响

###设计一个通用的用来计算对象个数的Base Class
```cpp
template<class BeingCounted> class Counted {
public:
	class TooManyObjects {}; /* for throwing exceptions */
	static size_t objectCount()
	{
		return(numObjects);
	}
protected:
	Counted();
	Counted( const Counted & rhs );
	~Counted()
	{
		--numObjects;
	}

private:
	static size_t	numObjects;
	static const size_t maxObjects;
	void		init(); /* to avoid ctor code }; // duplication */
	template<class BeingCounted> Counted<BeingCounted>::Counted()
	{
		init();
	}
	template<class BeingCounted> Counted<BeingCounted>::Counted( const Counted<BeingCounted> & )
	{
		init();
	}
	template<class BeingCounted>
	void Counted<BeingCounted>::init()
	{
		if ( numObjects >= maxObjects )
			throw TooManyObjects();
		++numObjects;
	}
```
使用
```cpp
class Printer: private Counted<Printer> { public:
// pseudo-constructors
static Printer * makePrinter();
static Printer * makePrinter(const Printer& rhs);
~Printer();
void submitJob(const PrintJob& job); void reset();
void performSelfTest();
...
using Counted<Printer>::objectCount;
using Counted<Printer>::TooManyObjects; // see below
private:
Printer();
Printer(const Printer& rhs);
//在实现cpp文件中加入下面这行，设定每个特定类的不同最大可实例化的对象的个数
const size_t Counted<Printer>::maxObjects = 10;
};
```



