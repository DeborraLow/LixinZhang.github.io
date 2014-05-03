Title: C++中的类型转换
Date: 2014-05-04 18:23
Category: CPP
Tags: CPP

##隐式类型转换(implicit type conversion)
如：

    :::cpp
    int ival; double dval;
    ival>=dval; //convert ival to double
    if(ival); // convert to bool
    while(ival);
    ival = dval;
    ival + dval;
    const int ci = ival;
    const int &i = ival;
    const int * p = &ci;

##显示转换

###dynamic_cast

dynamic_cast 支持运行时识别指针或引用所指向的对象。 其将基类类型对象的引用或指针转换为同一继承层次中其他类型的引用和指针。与<code>dynamic_cast</code>一起使用的指针必须是有效的——它必须为0或者指向某一对象。

    :::cpp
    class Base{
    public:
        Base(int n){
            num = n;
        }
        inline virtual void test(){};
        int num;
    };

    class Derived : public Base{
    public:
        Derived(int n):Base(n-1){
            num = n;
        }
        inline virtual void test(){
            cout<<"test"<<endl;
        }
        void sayhi(){
            cout<<"hi"<<endl;
            cout<<num<<endl;
        }
        int num;
    };

    Base * base = new Base(10);
    Base * derived = new Derived(10);
    dynamic_cast<Derived *>(derived)->sayhi();
    ((Derived *)derived)->sayhi();
    Derived * dynamicDerived = dynamic_cast<Derived *> (base);
    assert(dynamicDerived==NULL);//类型检查，转换失败
    dynamicDerived->sayhi();//error

    Derived * staticDerived = static_cast<Derived *> (base);
    assert(staticDerived==NULL);//非法转换，但是staticDerived非NULL，能通过遍历，运行时错误
    staticDerived->sayhi();//error

当按如下创建一个对象b，<code>Base * derived = new Derived(10);</code> 。则默认<code>derived->sayhi()</code>无法通过编译，因为derived默认所指向的base类中不包含<code>sayhi()</code>。这时候可以利用<code>dynamic_cast</code>将其转换为Derived对象，使<code>sayhi</code>函数可用。

与其他强制转换类型不同，<code>dynamic_cast</code>涉及运行时类型检查，如果绑定到引用或指针的对象不是目标类型的对象，则dynamic_cast失败，返回值为0或抛出一个bad_cast异常。因此上述代码中，<code>Derived * staticDerived = static_cast<Derived *> (base);</code>转换并不考虑类型检查，因此上述转换为错误的，将一个base对象强制转换成Derived，必然缺失了Derived具有的函数。使用<code>dynamic_cast</code>由于做类型检查，因此非法转换后的值为NULL，而static_cast不能检查转换类型。

###const_cast

转换掉表达式的const性质。

    :::cpp    
    const char str[] = "hello";
    char nonconstStr[] = "world";
    const int number = 10;
    //const int &newnum = number;
    //int & newnum = number;
    int newnum = number;
    const char * newstr = str;
    char * newstr2 = const_cast<char *>(str);
    char * newstr3 = nonconstStr;
    //newstr3[0] = 'T'; //合法
    //newstr2[0] = 'T'; //error, 就算强制移除了const，其指针指向的对象仍然是const的，不能改变其值


默认const对象是无法赋值给非const变量的，因此<code>const_cast</code>提供去掉const值的const属性，即可以赋值给非const变量。这里记录下<code>const int number = 10; int tmp = number;</code>是合法，因为tmp与number并非指向同一个对象，而引用和指针则不行。

###static_cast

编译器隐式执行的任何类型转换都可以由<code>static_cast</code>显示完成。 
    
    :::cpp
    double d = 97.0;
    char ch = static_cast<char>(d); //也可以用隐式转换替换

    void * p = &d;
    double *dp = static_cast(double *)(p); //隐式转换 not work

###reinterpret_cast
以下来至[reinterpret_cast](http://baike.baidu.com/view/1263731.htm)

操作符修改了操作数类型,但仅仅是重新解释了给出的对象的比特模型而没有进行二进制转换。
    
    :::cpp
    int *n= new int ;
    double *d=reinterpret_cast<double*> (n);


在进行计算以后, d 包含无用值. 这是因为 reinterpret_cast 仅仅是复制 n 的比特位到 d, 没有进行必要的分析。因此, 需要谨慎使用 reinterpret_cast.

static_cast 与 reinterpret_cast reinterpret_cast是为了映射到一个完全不同类型的意思，这个关键词在我们需要把类型映射回原有类型时用到它。我们映射到的类型仅仅是为了故弄玄虚和其他目的，这是所有映射中最危险的。(这句话是C++编程思想中的原话)

static_cast和reinterpret_cast的区别主要在于多重继承，比如

    ::cpp
    class A {
        public:
        int m_a;
    };
    class B {
        public:
        int m_b;
    };
     
    class C : public A, public B {};
    C c;
    printf("%p, %p, %p", &c, reinterpret_cast<B*>(&c), static_cast <B*>(&c));

前两个的输出值是相同的，最后一个则会在原基础上偏移4个字节，这是因为static_cast计算了父子类指针转换的偏移量，并将之转换到正确的地址（c里面有m_a,m_b，转换为B*指针后指到m_b处），而reinterpret_cast却不会做这一层转换。

因此, 你需要谨慎使用 reinterpret_cast.    

###旧式强制类型转换
    
    :::cpp
    int (num);
    (int) num;

