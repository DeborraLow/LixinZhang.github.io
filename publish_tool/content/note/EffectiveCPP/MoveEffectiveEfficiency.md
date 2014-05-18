Title: More Effective C++ 笔记(chapter4 效率）
Date: 2014-05-18 14:23
Category: CPP
Tags: CPP

##效率

###谨记80-20法则

<code>80-20</code>法则是说一个程序的80%的资源用在了20%的代码上。 因此，优化程序需要找到程序的瓶颈问题，比如<code>I/O</code>bound 还是<code>CPU</code>bound的。书中建议使用一些程序分析器（program profiler)，分析那些函数最耗时，被调用的最频繁，从而找到优化方法。

###考虑使用lazy evaluation (缓式评估)

<code>lazy evalution</code>即尽量延迟实际运算的时间，除非必须立即返回结果或是进行真正的运算，可以fake。

####引用计数

    :::cpp
    string s1 = "helloworld";
    string s2 = s1;

当执行到<code>s2 = s1;</code> 的时候，调用string的复制运算符，理论上应该进行一份新数据的拷贝。 当出现大量的频繁的copy constructor的时候，成本代价是非常大的。于是考虑通过引用计数的形式，使s2与s1同时指向一份数据，这样就可以避免频繁的copy constructor了。但，当必须使用不同的副本的情况下，例如调用<code>s2.upper()</code>之类的函数之时，我们再在其实现中构造一个新的副本，这样延缓了新副本构造的时间。

####区分读与写

一般读操作由于不修改内部值，因此引用计数很好用，但写的时候再进行副本创建。但是如果区分读与写很困难，比如<code>opetartor[]</code>既可以读也可以写。

####Lazy Fetching(缓式取出)

    :::cpp
    class Object{
    public:
        Object(int id):p(NULL){}
        //const 函数不能修改任何成员值
        const string& field1() const{
            if (p == NULL){
                //real computation, read from database and construct the p
            }
            //p[0] = 'A'; //OK if and only if the member variable is mutable
            return *p;
        }

    private:
         mutable string *p;
    };

所谓的缓式取出，其实就是说当你构造一个对象的时候，里面可能很多成员函数用来得到某些值，而这些成员函数都需要一定的计算才将构造好的成员对象返还给你。然而，很多情况，我们并没有使用所有的构造好的成员变量，那么这些没有使用的成员变量的构造代价就useless了。因此，我们只在实际需要的情况下，才去构造这些值。注意一下<code>mutable</code>的使用，其含义是其可被任意函数修改，默认const函数是不能修改成员变量的，因此必须用<code>mutable</code>来修饰成员变量，才可以在const函数中对其进行修改。

这节还提到了一个很hack的C语言的方法来替代<code>mutable</code>——fack一个this指针，然后去除其const。

    :::cpp
    const string& field2() const{
        Object * const fakethis = const_cast<Object * const> (this);
        //Object *  fakethis = const_cast<Object * > (this); // also ok
        if(p2 == NULL){
            fakethis->p2 = new string("world");
        }
        return *p2;
    }

###分期摊还预期的计算成本
与上节不同，不强调<code>拖延策略</code>，而是超前做一些事情（over-eager evaluation)，举了几个例子：

1. 当一个对象包含取得其最大值，最小值，平均值之类的。 一种做法每次都重新遍历整个数据集去选取，另外一种做法则是保存一份值，并实时更新。这样，对于频繁调用min，max，mean之类的函数尤其有效。

2. 使用cache技术

3. 预开启富裕的空间，如stl中stack等的实现，当空间不足时，会预开辟一块空间，而不是值适应当前需求。

###了解临时对象的来源

####为了能使函数调用成功而产生的临时对象
    
    :::cpp
    string byReference(string & s){
        s[0] = 'A';
        return s;
    }

    string byConstReference(const string & s){
        //s[0] = 'B'; //error, modify const value
        return s;
    }

    string byValue(string s){
        s[0] = 'C';
        return s;
    }
     

    int main(){
        char teststr[] = "helloworld";
        string s = byValue(teststr);
        //string s2 = byReference(teststr); //error
        string s3 = byConstReference(teststr);
        string s4 = byConstReference(s);
        return 0;
    }

从上面代码很容易看出，teststr传递到参数之后，将会产生一个临时变量，且该临时变量会construct和destroy，这是一种类型转换造成的临时变量。注意一点，只用参数值是<code>reference to const</code>即<code>by value</code>的情况下，才会发生这种转换，而<code>reference to non-const</code>则不可以。为什么？假设编译器为此产生一个临时对象，然后该临时对象被传递给函数内部，从表面上看，传递的是引用类型，那么函数对该对象的修改，应该会影响到传入的原始值。然而，由于是产生的临时对象，因此与直观的假设是矛盾的，因此C++禁止对非const引用的对象进行隐式类型转换。

####当函数返回一个对象时，也会产生临时变量
例如：
    
    :::cpp
    const number operator+(const Number & lhs, cosnt Number & rhs);

###协助完成"返回值优化"
协助编译器产生优化效果，如：

    :::cpp
    const Rational & operator* (const Rational & lhs, const Rational & rhs){
        // Rational result(.....); return result; //低效，一定会产生临时对象
        return Rational(......); //编译器可以优化其，避免临时对象的构建
    }

###利用重载技术避免隐式类型转换

由于隐式类型转换，需要进行大量的临时变量的构造与析构，因此可以利用重载避免。尤其是，a = a + 4, 可以重载<code>opetrator +</code>，是一个参数为int类型，而不是利用int隐式转换为a类型。


###了解虚函数、多重继承、虚基类、runtime type identification的成本

####每个包含虚函数的类，都会对应一个虚函数表，这个表有链表或是数组实现，与编译器有关。
![picture](https://sdfpaw.dm2302.livefilestore.com/y2pANtJ3ZmNUgGlEB37XGG2KzE5N0yDaXNDEM_4cW_b7ADy-JHQ2zea_clXyjBdR5guw2QhLMR2jMoSA6VIUzKXxJZZDXG60h5EL-hMPPTC9PU/QQ20140518-1.png?psid=1)

####继承类，虚函数表结构如下：
![pic](https://sdfpaw.dm2303.livefilestore.com/y2pMC4Q5Htu-TQoYwDePZzyzSeUzCXRZSOFZYsFlN6AtHlsIFgiXRexhnLp3pAbDk5c_3lPjQdIjdxZNOnHSDdKGTUykHH9cpVmb6kB-PIINPs/QQ20140518-2.png?psid=1)

![pic](https://sdfpaw.dm2302.livefilestore.com/y2p6oUJ-5v5hXXbMrFp9Dsk2HuhnJea_yORzrNLOekaN6zDsnS4toaqRzyiue6P_yLtW2Rs-YJg0fqv0w7IsnxJq03WgkHC1V3x1NwgBakwQlA/QQ20140518-3.png?psid=1)

####菱形继承类，即多重继承：
![pic](https://sdfpaw.dm2302.livefilestore.com/y2p6oUJ-5v5hXXbMrFp9Dsk2HuhnJea_yORzrNLOekaN6zDsnS4toaqRzyiue6P_yLtW2Rs-YJg0fqv0w7IsnxJq03WgkHC1V3x1NwgBakwQlA/QQ20140518-3.png?psid=1)

![pic](https://sdfpaw.dm2304.livefilestore.com/y2pwMWp0DYbLUNMJAiuRhyhY68QR2GCZg39F5KBoeQ0fzO-JpGklK3M9HFkF3BL2AYN6CtIbFA0LUrJk9EvQ03GM_5lBZKBROCyHwmw58AeeLs/QQ20140518-5.png?psid=1)

####总结：
![summary](https://sdfpaw.dm2302.livefilestore.com/y2p5fCMZ52fHvyFn5hupNL1WSPJ5qtvXr6Ch4af5wg5Mw0wfFr646XT7p-FQgTynzOC_kmJ97fgCxn55zu2AvxXPUflf1nfbHA2v9VYpfm3Hgw/QQ20140518-7.png?psid=1)