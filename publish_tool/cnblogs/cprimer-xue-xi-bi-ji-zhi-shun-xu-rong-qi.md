Title: C++Primer 学习笔记之顺序容器
Date: 2011-02-20 02:24
Author: 糖拌咸鱼
Slug: cprimer-xue-xi-bi-ji-zhi-shun-xu-rong-qi

　　顺序容器，它将单一类型元素聚集起来成为容器，然后根据位置来存储和访问这些元素，这就是顺序容器。标准库里定义了三种类型：vector(支持快速随机访问)、list(支持快速插入、删除)、deque(双端队列)容器只定义了少量操作，大多数额外的操作由算法库提供。容器内元素的类型约束；1、元素类型必须支持赋值运算；2、元素类型的对象必须可以复制。这是容器元素类型的最低要求，如果想支持一些其他特殊要求，则必须具备相关的性质。

</p>

可以定义容器的容器vector\< vector\<int\> \> lines;//必须使用"\>
\>"中间的空格，否则会出现变异错误

</p>

**迭代器运算:**

</p>

　　关系操作符只适用于vector和deque容器，它们可以根据元素位置直接有效地访问指定的容器元素。而list容器的迭代器既不支持算术运算（加法或者减法），也不支持关系运算（\<=,\<,\>=,\>），它只提供前置和后置的自增、自减运算以及相等（不等）运算。

</p>

**迭代器范围：**

</p>

　　c++使用一对迭代器标记迭代器范围，通常命名为first和last或beg和end。该范围内的元素包括迭代器first指向的元素，以及从first开始一直到迭代器last指向的位置之前的所有元素，此类元素范围称为左闭合区间[first,last)。

</p>

**顺序容器的操作：**

</p>

　　在容器中添加元素；在容器中删除元素；设置容器大小；获取容器内的第一个和最后一个元素。对于begin()、end()、rbegin()、rend()四个操作，均有const版本。如果容器时const,则其返回类型要加上const\_前缀。c.push\_back(t)
在容器c的尾部添加值为t的元素,返回void类型。c.push\_front(t)
在容器c的前端添加值为t的元素，返回void类型。但是只有list和deque具有这样的性质。

</p>

<div class="cnblogs_code">

</p>
<p>
    //容器的顺序遍历vector<int>::reverse_iterator iterReverse=vect.rbegin();//定义反向迭代器while(iterReverse!=vect.rend()){    cout<<*iterReverse<<endl;    iterReverse++;}vector<int>::iterator iter = vect.begin();//定义正向迭代器while(iter!=vect.end()){    cout<<*iter<<endl;    iter++;}

</p>
<p>

</div>

</p>

　　在容器中的指定位置添加元素：使用insert函数：由于迭代器可能指向超出容器末端的下一位置没这事一个不存在的元素，因此insert函数是在其指向位置之前而非其后插入元素。mylist.insert(iter,element);

</p>

<div class="cnblogs_code">

</p>
<p>
    //获取中心位置迭代器，需要注意的list不允许如下的迭代器的加法vector<int>::iterator middle=vectCpy.begin()+vect.size()/2;vectCpy.insert(middle,1001);//在中间位置添加一个元素    

</p>
<p>

</div>

</p>
  
　　插入一段元素：

<div class="cnblogs_code">

</p>
<p>
    vectCpy.insert(vectCpy.begin(),10,9);//在第一个元素后面添加10个初值为9的元素int num[3]={555,666,777};vectCpy.insert(vectCpy.end(),num,num+3);//在vectCpy后面加入一段来自num数组里的元素vectCpy.insert(vectCpy.end(),vect.begin(),vect.end());//在vectCpy后加入一段来自迭代器对间的元素

</p>
<p>

</div>

</p>
  
　　需要注意的是，添加元素可能会导致某些或全部迭代器失效，假设所有迭代器失效是最安全的做法。不要存储end操作返回的迭代器，为了避免存储end迭代器，可以在每次做完插入运算重新计算end迭代器值。  

关键概念：容器元素都是副本在容器中添加元素时，系统是将元素值复制到容器里。类似的，使用一段元素初始化新容器时，新容器存放的事原始元素的副本。本复制的原始值与新容器中的元素各不相干，此后，容器内元素值发生变化时，被复制的原值不会受到影响，反之亦然。

</p>

**容器的比较：**

</p>

　　比较的容器必须具有相同的容器类型，而且其元素类型也必须相同。容器的比较式基于容器内元素的比较。两个容器具有相同的长度而且所有的元素都相等，那么这两个容器就相等。如果两个容器长度不相等，但较短的容器中所有元素都等于较长容器中对应的元素，则称较短的容器小于另一个容器。如果两个容器都是对方的初始子序列，则它们的比较结果取决于所比较的第一个不相等的元素。

</p>

<div class="cnblogs_code">

</p>
<p>
    vector<int> vect;vect.push_back(1);vect.push_back(2);vect.push_back(3);vector<int> vectCpy(vect);if(vectCpy==vect) cout<<"Equal"<<endl;else cout<<"Not Equal"<<endl;

</p>
<p>

</div>

</p>
  

**容器大小的操作：**

</p>

　　容器类型提供resize函数来改变容器所包含的元素个数。如果当前的容器长度大于新的长度值，则该容器后部的元素会被删除，如果当前的容器长度小于新的长度值，则系统会在该容器后部添加新元素。resize操作可能会使迭代器失效。例子：

</p>

<div class="cnblogs_code">

</p>
<p>
    list<int> ilist(10,2);//10个元素容器，初始值均为2ilist.resize(15);//在原有基础上，再后面添加5个元素，初始值为0ilist.resize(25,-1);//在上行的基础上，再后面再添加10个元素，值为-1ilist.resize(5);//在ilist的后部删除20个元素

</p>
<p>

</div>

</p>
  

**访问元素：**

</p>

　　如果容器非空，那么容器类型的front和back成员将返回容器内第一个或最后一个元素的引用

</p>

<div class="cnblogs_code">

</p>
<p>
    int &ref=vect.front();//front和back返回容器内第一个或最后一个元素的引用ref=1000001;//改变引用的元素，vect内元素的值也会改变cout<<vect[0]<<" "<<vect.at(1)<<endl;//只适用于vector和deque,如果给出的下标无效，则会发生outOfRange的异常

</p>
<p>

</div>

</p>
  

**删除元素：**

</p>

　　pop\_front和pop\_back函数用于删除容器内的第一个和最后一个元素。

</p>

　　删除一个或者一段元素更通用的方法是用erase操作，有两个版本：删除由一个迭代器指向的单个元素，或删除由一对迭代器标记的一段元素。erase返回一个迭代器，它指向被删除元素或元素段后面的元素。通常，必须在容器中查找要删除的元素后，才使用erase操作。寻找一个指定元素最简单的方法，是使用标准库中的find方法。必须包含头文件algorithm.h

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<algorithm>list<int>::iterator searchIter= find(mylist.begin(),mylist.end(),1233);if(searchIter!=mylist.end())//有可能找不到{    mylist.erase(searchIter);}

</p>
<p>

</div>

</p>
  

　　删除容器内所有元素：mylist.clear()或者mylist.erase(mylist.begin(),mylist.end());

</p>

**容器的选用：**

</p>

　　vector和deque容器提供了对元素的快速随机访问，但付出的代价是，在容器的任意位置插入或删除元素，比在容器尾部插入和删除元素的开销更大。list类型在任何位置都能快速插入和删除，但付出的代价是元素的随机访问开销较大。其原因就是在内部实现的数据结构中，一个是在内存中顺序地址分批的，而另一个是在类似链表的方式，随机地址分配的，所以导致性质的不同。

</p>

