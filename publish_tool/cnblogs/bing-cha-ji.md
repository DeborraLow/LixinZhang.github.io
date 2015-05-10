Title: 并查集
Date: 2011-03-16 02:40
Author: 糖拌咸鱼
Slug: bing-cha-ji

　　在一些应用问题中，需要将n个不同的元素划分成一组不相交的集合。开始时，每个元素自成一个单元素集合，然后按一定规律将归于同一组元素的集合合并。在此过程中要反复用到查询某个元素归属于哪个集合的运算。适合于描述这类问题的抽象数据类型称为并查集。

</p>

　　并查集支持3中操作：

</p>

（1）Union(root1,root2)
把子集合root2并入集合root1中，要求root1与root2互不相交，否则不执行合并。

</p>

（2）Find（x）搜索单元素x所在的集合，并返回该集合的名字。

</p>

（3）UFSets（sz）
构造一个并查集，并将所有元素的元素初始化为只有一个单元素的子集合。

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>using namespace std;int * UFSets(int sz){    int* parent = new int[sz];    for(int i=0;i<sz;i++) parent[i]=-1;    return parent;}int Find(int * parent,int x){    while(parent[x]>=0) x=parent[x];    return x;}void Union(int * parent,int root1, int root2){    int temp;    int r1=Find(parent,root1),r2=Find(parent,root2);    if(r1!=r2)     {        temp=parent[r1]+parent[r2];        if(parent[r2]<parent[r1])        {            parent[r1]=r2;            parent[r2]=temp;        }        else        {            parent[r2]=r1;            parent[r1]=temp;        }    }}int main(){    int *parent=UFSets(10);    Union(parent,1,4);    Union(parent,1,9);    Union(parent,4,9);    Union(parent,2,6);    Union(parent,2,5);    for(int i=0;i<10;i++)    {        cout<<parent[i]<<"  ";    }    cout<<endl;    return 0;}

</p>
<p>

</div>

</p>

</p>

