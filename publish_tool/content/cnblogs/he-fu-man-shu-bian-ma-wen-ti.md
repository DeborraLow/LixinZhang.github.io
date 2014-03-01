Title: 赫夫曼树编码问题
Date: 2011-03-14 15:08
Author: 糖拌咸鱼
Slug: he-fu-man-shu-bian-ma-wen-ti

**<span style="font-size: 16px;">定义:</span>**

</p>

　　结点的带权路径长度为从该结点到树根之间的路径长度与结点上权的乘积。树的带权路径长度为树中所有叶子结点的带权路径长度之和。假设有n个权值，试构造一棵有n个叶子结点的二叉树，每个叶子结点带权为wi，则其中带权路径长度最小的二叉树称做最优二叉树或赫夫曼树。 

</p>

 构造赫夫曼树的方法：  

</p>

（1）根据给定的n个权值{w1,w2,w3......}构成n棵二叉树的集合F={T1,T2,T3,T4......}，其中每棵二叉树Ti中只有一个带权为wi的根结点，其左右子树均空。

</p>

（2）在F中选取两棵根结点的权值最小的树作为左右子树构造一棵新的二叉树，且置新的二叉树的根结点的权值为其左、右子树上根结点的权值之和。

</p>

（3）在F中删除这两棵树，同时将新得到的二叉树加入F中。

</p>

（4）重复（2）和（3），直到F只含一棵树为止。这棵树便是赫夫曼树。

</p>

**<span style="font-size: 16px;">代码实现：</span>**

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>#include<assert.h>using namespace std;struct HuffmanNode{    unsigned int weight;    unsigned int parent,leftChild,rightChild;    HuffmanNode()    {        weight=0;parent=0;leftChild=0;rightChild=0;    }};void Select(const HuffmanNode* & nodelist,const int length,int & a, int &b){    int min=1000000,min2=1000000;    for(int i=0;i<length;i++)    {        if(min>nodelist[i].weight&&nodelist[i].parent==0)         {            min=nodelist[i].weight;            a=i;        }    }    for(int j=0;j<length;j++)    {        if(j!=a&&min2>nodelist[j].weight&&nodelist[j].parent==0)        {            min2=nodelist[j].weight;            b=j;        }    }}char ** HuffmanCoding(const int *w, const int n){    assert(w!=NULL);    int i,min1,min2;    int m = 2*n-1;    HuffmanNode * nodelist = new HuffmanNode[m]();    for(i=0;i<n;i++)    {        nodelist[i].weight=w[i];        nodelist[i].parent=0;    }    for(i=n;i<m;i++)    {        Select(nodelist,i,min1,min2);        nodelist[min1].parent=i;        nodelist[min2].parent=i;        nodelist[i].weight=nodelist[min1].weight+nodelist[min2].weight;        nodelist[i].rightChild=min2;        nodelist[i].leftChild=min1;        nodelist[i].parent=0;    }    char temp [20];    char ** code = new char * [n];    for(i=0;i<n;i++)    {        int j=i;        int index=0;        while(j!=m-1)        {            if(j==nodelist[nodelist[j].parent].leftChild) temp[index++]='0';            else temp[index++]='1';            j=nodelist[j].parent;        }        temp[index]='\0';        code[i] = new char[index+1];        strcpy(code[i],temp);    }    delete nodelist;    return code;}int main(){    const int size=6;    char word[size]={'A','B','C','D','E','F'};//编码字符    int w[size]={4,3,2,1,7,8};//权重    char ** code;    code=HuffmanCoding(w,size);    assert(code!=NULL);    for(int i=0;i<size;i++)    {        cout<<word[i]<<" is coded as "<<code[i]<<endl;    }    //注意二级指针的释放问题    for(int j=0;j<size;j++)    {        delete []code[j];    }    delete []code;    return 0;}

</p>
<p>

</div>

</p>

</p>

