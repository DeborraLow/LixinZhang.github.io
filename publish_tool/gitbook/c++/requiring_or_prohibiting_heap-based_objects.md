# Requiring or prohibiting heap-based objects.
要求（或禁止）对象产生于heap之中
这一节很有意思，很多比较又想象力的想法，虽然最终都被否了，但是挺开阔思路的。

##要求对象产生于heap之中
将类的析构定义为private的，然后再定义一个<code>destory</code>伪析构函数帮助释放内存。但缺点是回影响很多类的定义，比如说继承。

##判断某个对象是否位于Heap之中
1. 重载new操作符，加入一个<code>onTheHeap</code>的变量，然后通过维护该变量，来判断这个对象是否位于heap内。但是重载new，若定义一个对象数组，则会很麻烦，具体细节看书。
2. 利用程序的地址空间的线性序列的特性，stack高地址往低地址成长，heap由低地址往高地址成长。


```cpp
bool onHeap(const void * address){
    char onthestack;
    return address < &onthestack;
}

```
上述代码中，通过新定义一个onthestack栈对象，来判断这个对象的地址与当前对象地址的位置关系，从而判断是否为栈对象。然后，该方法有缺陷，就是忽略了static objects。 一个常见的内存空间布局如下图：
![https://sdfpaw.dm2301.livefilestore.com/y2phPSIJgXzwht8NykY1ubfpSRYNSn26YftDz4qiE9Jdb5He6K2id8UZ-PGfJZwjyhKbGNcwnNXsFNo5o_wde-djkF2MvxjkBvNh5Gsw6E5YAg/QQ20140629-1.png?psid=1](https://sdfpaw.dm2301.livefilestore.com/y2phPSIJgXzwht8NykY1ubfpSRYNSn26YftDz4qiE9Jdb5He6K2id8UZ-PGfJZwjyhKbGNcwnNXsFNo5o_wde-djkF2MvxjkBvNh5Gsw6E5YAg/QQ20140629-1.png?psid=1)

##禁止对象产生于heap之中

重载new和delete操作符，然后将其重载函数放在private之中，当然也破坏了继承和包含的机制了。
