Title: C++Primer 学习笔记之关联容器
Date: 2011-02-21 05:41
Author: 糖拌咸鱼
Slug: cprimer-xue-xi-bi-ji-zhi-guan-lian-rong-qi

**关联容器**<span></span>

</p>

<span> </span>　　关联容器支持通过键来高效地查找和读取元素。两个基本的关联容器类型是map和set。map的元素以键-值对的形式组织：键用作元素在map的索引，而值则表示所存储和读取的数据。set仅包含一个键，并有效地支持关于某个键是否存在的查询。set和map类型的对象不允许为同一个键添加第二个元素。如果一个键必须对应多个实例，则需使用multimap或mutiset类型，这两种类型允许多个元素拥有相同的键。

</p>

**pair类型：**在头文件utility中定义。

</p>

pair的创建和使用：

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<utility>pair<string,int> author("Peter",30);cout<<author.first<<"\t"<<author.second<<endl;//可以直接访问数据成员//使用typedef进行简化typedef pair<string,string> Student;Student s1,s2("aaa","bbb");s1.first="ccc";s1.second="ddd";//使用make_pair函数生成一个新的pair对象string first="eee",second="fff";Student s3=make_pair(first,second);

</p>
<p>

</div>

</p>

**map类型：**map是键-值对的集合。

</p>

map\<K,V\>::key\_type 在map中用做索引的键的类型

</p>

map\<K,V\>::mapped\_type 在map中用作关联的值的类型

</p>

map\<K,V\>::value\_type 一个pair类型

</p>

map迭代器进行解引用将产生pair类型的对象：

</p>

<div class="cnblogs_code">

</p>
<p>
    map<string,int>::iterator map_it = word_count.begin();cout<<map_it->first<<" "<<map_it->second<<endl;

</p>
<p>

</div>

</p>

**使用下标访问map对象：**

</p>

添加键-值对，有两种实现方法。可以用insert成员实现，或者，先用下标操作符获取元素，然后给获取的元素赋值。

</p>

使用下标访问map与使用下标访问数组或vector的行为截然不同；用下标访问不存在的元素将导致在map容器中添加一个新的元素，它的键即为该下标的值。

</p>

方法一：

</p>

<div class="cnblogs_code">

</p>
<p>
    map<string,int> word_count;word_count["Peter"]=10;//相当于增加一个键值对//创建一个map对象,用来记录每个单词出现的次数,十分简洁。map<string,int> word_count;string word;while(cin>>word){    ++word_count[word];}

</p>
<p>

</div>

</p>

方法二：使用insert:

</p>

<div class="cnblogs_code">

</p>
<p>
    map<string,int> word_count;word_count.insert(map<string,int>::value_type("aaa",1));//用insert方法重写单词统计程序map<string,int> word_count;string word;while(cin>>word){    pair<map<string,int>::iterator,bool> ret=word_count.insert(make_pair<string,int>(word,1));    if(!ret.second)//如果没插入成功，证明原来已经存在键值,将统计值+1    {        ++ret.first->second;// first是一个迭代器，指向插入的键    }}

</p>
<p>

</div>

</p>

**查找并读取map中的元素：**

</p>

** **用下标操作符，是一种比较简单的方法，但是该方法有副作用，就是当该键不在map容器中，那么下标操作会插入一个具有该键的新元素。

</p>

map容器提供了两种操作：count和find

</p>

m.count(k)
返回m中k的出现次数，对于map对象只能是1或0，而对于mutimap容器，则可能会出现更多的值。

</p>

m.find(k) 返回按k索引返回的迭代器

</p>

count方法用于在map中查找指定键是否存在的问题，而find方法适合用于解决在map容器中查找指定键对应的元素的问题。

</p>

<div class="cnblogs_code">

</p>
<p>
    //读取元素而又不插入新元素int occurs;map<string,int>::iterator it= word_count.find("foobar");//不存在，则返回end迭代器if(it!=word_count.end())//可能找不到{    occurs=it.second;}

</p>
<p>

</div>

</p>

**从map对象中删除元素**：

</p>

m.erase(k)
删除m中键为k的元素。返回值为被删除元素的个数，对于map容器而言，其值必然是0或1。

</p>

m.erase(p) 从m中删除迭代器p所指向的元素。返回值为void类型。

</p>

m.erase(b,e) 从m中删除一段由一对迭代器范围的元素。返回值为void类型。

</p>

**map对象的迭代遍历:**

</p>

<strong>

</strong>

</p>

<div class="cnblogs_code">

<strong>
</p>
<p>
    map<string,int> word_count;word_count["aaa"]=1;word_count["bbb"]=2;word_count["ccc"]=3;map<string,int>::const_iterator iter = word_count.begin();while(iter!=word_count.end()){    cout<<iter->second<<endl;    iter++;}

</p>
<p>
</strong>

</div>

</p>

**set类型：**

</p>

map容器是键-值对的集合，而set容器只是单纯的键的集合。当只想知道一个值是否存在时，使用set容器是最合适的。

</p>

在set中添加元素：

</p>

<div class="cnblogs_code">

</p>
<p>
    set<int> set1;pair<set<int>::iterator,bool> p=set1.insert(1);//返回pair类型对象，包含一个迭代器和一个布尔值set1.insert(2);int arr[]={1,2,3};set<int> set2;set2.insert(arr,arr+3);//返回void类型

</p>
<p>

</div>

</p>

从set中获取元素:与map方法使用类似，使用find和count函数。

</p>

**multimap和multiset类型：**

</p>

　　map和set容器中，一个键只能对应一个实例。而multimap和multiset类型则允许一个键对应多个实例。其支持的操作分别于map和set的操作相同，只有一个例外：multiply不支持下标运算。

</p>

