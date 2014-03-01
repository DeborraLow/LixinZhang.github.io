Title: 把二元查找树转变成排序的双向链表
Date: 2013-02-16 13:16
Author: 糖拌咸鱼
Slug: ba-er-yuan-cha-zhao-shu-zhuan-bian-cheng-pai-xu-de-shuang-xiang-lian-biao

题目:  
输入一棵二元查找树,将该二元查找树转换成一个排序的双向链表。  
要求不能创建任何新的结点,只调整指针的指向。  
       10  
     /       \\  
   6         14  
 /    \\      /    \\  
4    8   12   16  
转换成双向链表  
4=6=8=10=12=14=16

</p>

 

</p>

分析:

</p>

一想到二叉查找树，要求产出一个sorted的链表，自然联想到前序遍历。

</p>

在对当前节点处理的时候，进行链接操作。

</p>

Solution:

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:cpp;gutter:true;}
#include<iostream>using namespace std;struct BSTreeNode {    int m_nValue;    BSTreeNode * m_pLeft;    BSTreeNode * m_pRight;    BSTreeNode(int value){        m_nValue = value;        m_pLeft = NULL;        m_pRight = NULL;    }};BSTreeNode * BSTreeNodeList[7];BSTreeNode * buildTestTree() {    int values [7] = {10,6,14,4,8,12,16};    for(int i=0;i<sizeof(values)/sizeof(int);i++){        BSTreeNodeList[i] = new BSTreeNode(values[i]);    }    BSTreeNode * root = BSTreeNodeList[0];    root->m_pLeft = BSTreeNodeList[1];    root->m_pRight = BSTreeNodeList[2];    BSTreeNodeList[1]->m_pLeft = BSTreeNodeList[3];    BSTreeNodeList[1]->m_pRight = BSTreeNodeList[4];    BSTreeNodeList[2]->m_pLeft = BSTreeNodeList[5];    BSTreeNodeList[2]->m_pRight = BSTreeNodeList[6];    return root;}BSTreeNode * tail = NULL;BSTreeNode * head = NULL;void scan(BSTreeNode * root) {    if (root == NULL) return ;    scan(root->m_pLeft);    if(tail == NULL) head = root;    root->m_pLeft = tail;    if (tail != NULL) tail->m_pRight = root;    tail = root;    scan(root->m_pRight);}int main(){    BSTreeNode * root = buildTestTree();    scan(root);    BSTreeNode * p = head;    while(p!=NULL){        cout<<p->m_nValue<<endl;        p = p->m_pRight;    }    cout<<"------------"<<endl;    p = tail;    while(p!=NULL){        cout<<p->m_nValue<<endl;        p = p->m_pLeft;    }    return 0;}
```

</p>
<p>

</div>

</p>

　　

</p>

