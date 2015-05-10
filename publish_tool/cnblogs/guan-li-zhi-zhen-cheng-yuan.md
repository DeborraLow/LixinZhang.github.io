Title: 管理指针成员
Date: 2011-02-26 03:51
Author: 糖拌咸鱼
Slug: guan-li-zhi-zhen-cheng-yuan

大多数c++类采用以下三种方法之一管理指针成员：

</p>

1、指针成员采取常规指针型行为。这样的类具有指针的所有缺陷但无需特殊的复制控制。

</p>

2、类可以实现所谓的“智能指针”行为。指针所指向的对象是共享的，但类能够防止悬垂指针。

</p>

3、类采取值型行为。指针所指向的对象是唯一的，由每个类对象独立管理。

</p>

**<span style="font-size: 18pt;">方法一：简单使用</span>**

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>using namespace std;class HasPtr{public:    HasPtr(int * p,int n)    {        ptr=p;        num=n;    }    void setPtr(int * p)    {        ptr=p;    }    void setNum(int n)    {        num=n;    }    int * const getPtr()    {        return ptr;    }    const int getNum()    {        return num;    }    ~HasPtr()    {        //定义虚构函数，用例释放动态创建的内存        //但这样删除，存在潜在的危险        //因为如果有多个对象共享一个指针成员，当一个对象生命期结束就会执行该虚构函数，从而导致其他共享该指针的对象内的成员成为了野指针        delete ptr;    }private:    int num;    int * ptr;};int main(){    int *obj= new int (10);    HasPtr ptr1(obj,10);    HasPtr ptr2(ptr1);    //目前出现了非常危险的情况。    //ptr1和ptr2的*ptr成员指向同一个对象    //int值是清楚而独立的，而指针却纠缠在一起    delete obj;//删除该指针后，ptr2的ptr指针成员就变为了野指针，很危险    return 0;}

</p>
<p>

</div>

</p>

**<span style="font-size: 18pt;">方法二：使用智能指针</span>**

</p>

　　方法一种带来的危险主要是由于有多个对象作用在了一个共享对象上，如果用户删除该对象，则类就有一个悬垂指针，指向一个不复存在的对象。可以定义一个所谓的智能指针（smart
pointer）类，智能指针负责删除共享对象。

</p>

　**　引入使用计数**

</p>

　　定义智能指针的通用技术是采用一个使用计数（use
count）。智能指针类将一个计数器与指向的对象相关联。使用计数跟踪该类有多少个对象共享同一指针，使用计数为0时，删除对象。<span></span>每次创建类的新对象时，初始化指针并将使用计数置为1.当对象作为另一对象的副本而创建时，复制构造函数复制指针并增加与之相应的使用计数的值，对一个对象进行赋值时，赋值操作符减少左操作数所指对象的使用计数的值，并增加右操作数所指对象的使用计数的值。

</p>

　　**使用计数类**

</p>

<div class="cnblogs_code">

</p>
<p>
    class U_ptr{private:    friend class HasPtr;    int *ip;    size_t use;    U_ptr(int *p):ip(p),use(1){}    ~U_ptr(){delete ip;}}

</p>
<p>

</div>

</p>

　　这个类的所有成员均为private。我们不希望普通用户使用U\_Ptr类，所以它没有任何public成员。将HasPtr类设置为友元，使其成员可以访问U\_Ptr的成员。

</p>

![][]

</p>

<div class="cnblogs_code">

</p>
<p>
    class U_ptr{private:    friend class HasPtr;    int *ip;    size_t use;    U_ptr(int *p):ip(p),use(1){}    ~U_ptr(){delete ip;}};class HasPtr{public:    HasPtr(int *p, int i):ptr(new U_ptr(p)),val(i){}    HasPtr(const HasPtr & right)    {        ptr=right.ptr;        val=right.val;        ++ptr->use;//因为传入的参数是HasPtr的引用，所以对ptr的共享只增加了一个对象    }    HasPtr& operator =(const HasPtr& right)    {        ptr->use--;//当将right赋值给左边时，左边原有的ptr将会被覆盖，所以先use--        if(ptr->use==0) delete ptr;        right.ptr->use++;        ptr=right.ptr;        val=right.val;        return *this;    }    ~HasPtr()    {        ptr->use--;        if(ptr->use==0) delete ptr;//当所有共享对象都不存在时，将其删除    }    int *getPtr() const     {        return ptr->ip;    }    int getInt() const    {        return val;    }    void setPtr(int * p)    {        ptr->ip=p;    }    void setInt(int v)    {        val=v;    }private:    U_ptr *ptr;    int val;};

</p>
<p>

</div>

</p>

智能指针是存储指向动态分配（堆）对象指针的类，另一种智能指针的应用是在面对异常的时候格外有用，因为它能够正确地销毁动态分配的对象。

</p>

例如如下代码：

</p>

<div class="cnblogs_code">

</p>
<p>
    A * pt = new A;f();//.......delete p;

</p>
<p>

</div>

</p>
这个代码一般是正常的，但是如果万一f()出现了问题，抛出了异常，没有被捕捉，在没有\_finally扩展关键字的情况下，是无法执行到delete的。如果用:

</p>

<div class="cnblogs_code">

</p>
<p>
    Ptr<A> a = Ptr<A>(new A);

</p>
<p>

</div>

</p>
代替，则异常抛出后清理堆栈的时候a会被自动析构，同时释放A\*指向的内存。

</p>

<span
style="font-size: 18pt;">**方法三：定义值类型**</span><span></span>

</p>

<span> </span>　　处理指针成员的另一个完全不同的方法，是给指针成员提供值语义。复制值型对象时，会得到一个不同的新副本。对副本所做的改变不会反映在原有对象上。

</p>

<div class="cnblogs_code">

</p>
<p>
    class HasPtr{public:    HasPtr(const int &p ,int i):ptr(new int (p),val(i)){}    HasPtr(const HasPtr &orig):ptr(new int (*orig.ptr)),val(orig.val){}    //赋值操作符不需要分配新对象，它只是必须记得给其指针所指向的对象赋新值，而不是给指针本身赋值。    HasPtr & operator = (const HasPtr & right)    {        *ptr=*right.ptr;        val=right.val;        return * this;    }    ~HasPtr(){delete ptr;}private:    int *ptr;    int val;}；

</p>
<p>

</div>

</p>

  []: http://pic002.cnblogs.com/images/2011/146443/2011022611484093.png
