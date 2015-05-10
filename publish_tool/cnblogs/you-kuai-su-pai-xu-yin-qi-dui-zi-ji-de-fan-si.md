Title: 由快速排序引起對自己的反思
Date: 2013-03-09 10:54
Author: 糖拌咸鱼
Slug: you-kuai-su-pai-xu-yin-qi-dui-zi-ji-de-fan-si

   
 最早接触快速排序，应该可以追逐到高二那会儿。那时候，由四个同学在一起做noip竞赛，那时候不懂什么叫算法、什么叫优化、什么叫空间效率，只知道快速排序要比其他简单的排序快。于是，为了应对考场时可能会遇到需要排序的问题，自己“学会”了快排。还记得，刚开始怎么也理解不了快速排序的思想，后来果断背下来了，好在代码不长。
当时背算法挺可笑的，但是现在想想我平常理解的算法是不是也是在背算法呢？

</p>

   
 快排，我至少写过50遍，因为不知道什么时候，一直把它当作调试编译环境的测试代码。但是，就在昨天的百度面试中，又被问及了快排，而我在纸上写得却一塌糊涂。面试的题目是，对链表结构的数据进行快速排序。当时有点蒙，因为之前写得都是针对数组这样带有下标的数据结构排序。我之前所写过得那么多遍快排，其中partition的思想，都是从两头low和high向中间靠拢这样的策略，保证找到分割的位置。但是链表不能这么用了，单向链表只能一个方向遍历元素。
面试的时候，我知道很多书中提及的是一种从头利用两个指针一个方向进行寻找partition的方法，但是自己却重来没有认真看过实现细节，总认为自己会一种实现策略就可以了，原理都一样。可是就是同样的思想的算法，换个实现方式，就把我搞糊涂了。
最终，导致这次面试有点悲剧。还有一次，问建堆的复杂度，我知道是O（n）的，却重来没有想过为什么？也重来没自己去证明过。

</p>

   
 在回学校的地铁上，我不断反思，为什么这么基础的算法代码，我却写得一塌糊涂，为什么很多以为很熟悉很熟悉的东西，稍微变换一下，自己就措手不及。究其原因，我觉得就是太自以为是了，以为理解了思想，就不深究其思想的精髓以及忽略對细节的把握。

</p>

   
 最近一直很迷茫，因为最近发现之前自己所设定的研究生计划几乎泡汤，实验室真的不是一般差，我對我的研究方向完全没兴趣，基本不能指望从老师那得到任何收获。另一方面，自己想找实习，却又不想找那种业务开发类型的工作，想找那种底层点、有点理论研究的职位，而自己现在的技术能力却對此还有一定差距。
 现在处在我人生的低谷期，但我相信潮落之后一定有潮起！ 自己要加油了～

</p>

快速排序
针对链表结构的实现（面试回来，自己写的，当时不能快速的写出来，还是自己對其理解不深刻）：

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>#include<stdio.h>using namespace std;struct node {    int value;    node * next;    node(int v){        value = v;        next = NULL;    }};void qsortforlink(node * head, node * tail){    if(head == tail || head == NULL || tail == NULL) return;    node * x = head;    node * p1 = head->next;    node * p2 = head->next;    node * p = head;    while(p2!=NULL && p2!= tail->next){        if(p2->value < x->value) {            p = p1;            swap(p1->value,p2->value);            p1 = p1->next;        }        p2 = p2->next;    }    swap(x->value, p->value);    qsortforlink(head,p);    qsortforlink(p1,tail);}

</p>
<p>
    int main(){    node * head = NULL;    freopen("input.txt","r",stdin);    int arr [800000];    int length = 0;    while(cin>>arr[length++]) {}    int arr [] = {8,7};    head = new node(arr[0]);    node * p = head;    for(int i=1;i<length;i++) {        p->next = new node(arr[i]);        p = p->next;    }    qsortforlink(head,p);}

</p>
<p>

</div>

</p>

 

</p>

<div class="cnblogs_code">

</p>
<p>
    void qsort(int * arr, int low, int high){    if(low >= high) return;    int i = low;    int j = high;    int x = arr[low];    while(i<j){        while(arr[j]>=x && i<j) j--;        arr[i] = arr[j];        while(arr[i]<=x && i<j) i++;        arr[j] = arr[i];    }    arr[i] = x;    qsort(arr,low, i-1);    qsort(arr,i+1,high);}

</p>
<p>

</div>

</p>

 

</p>

<div class="cnblogs_code">

</p>
<p>
    void qsort2(int * arr, int low, int high){    if(low>=high) return;    int j = low+1,i;    int x = arr[low];    for(i=low+1;i<=high;i++){        if (arr[i] < x){            swap(arr[i],arr[j]);            j++;        }    }    j--;    swap(arr[low],arr[j]);    qsort2(arr,low,j-1);    qsort2(arr,j+1,high);}

</p>
<p>

</div>

</p>

 

</p>

