Title: 面试题_分层遍历二叉树
Date: 2011-03-31 14:41
Author: 糖拌咸鱼
Slug: mian-shi-ti-_fen-ceng-bian-li-er-cha-shu

编程之美上的题目。

</p>

问题1：给定一棵二叉树，要求按分层遍历该二叉树，即从上到下按层次访问该二叉树（每一行将单输出一行），每一层要求访问的顺序为从左向右，并将节点依次编号。

</p>

问题2:写一个函数，打印二叉树中某层次的节点（从左向右），其中根结点为第1层。

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>#include<queue>using namespace std;struct Tnode{    Tnode * leftChild;    Tnode * rightChild;    int value;    Tnode():leftChild(NULL),rightChild(NULL)    {        value=0;    }    Tnode(int i):leftChild(NULL),rightChild(NULL)    {        value=i;    }};//代码之美上的。输出第level层的所有元素void printNodeAtLevel(Tnode * root, int level){    if(root==NULL||level<0)    {        return ;    }    if(level==1)    {        cout<<root->value<<" ";        return ;    }    printNodeAtLevel(root->leftChild,level-1);    printNodeAtLevel(root->rightChild,level-1);}int main(){    //建树    Tnode * node1=new Tnode(1);    Tnode * node2= new Tnode(2);    Tnode * node3= new Tnode(3);    Tnode * node4= new Tnode(4);    Tnode * node5= new Tnode(5);    Tnode * node6= new Tnode(6);    Tnode * node7= new Tnode(7);    Tnode * node8= new Tnode(8);    node1->leftChild=node2;    node1->rightChild=node3;    node2->leftChild=node4;    node2->rightChild=node5;    node3->rightChild=node6;    node5->leftChild=node7;    node5->rightChild=node8;    //按层序遍历二叉树，并在每一层所有元素的后面打印一个换行符    //编程之美上写的是类似递归的思想，其实也是在用递归栈来记录层数，    //那么不如自己用个队列来实时追踪当前元素所在层    queue<Tnode*> que;    queue<int> level;//用一个辅助队列记录当前元素的所在层    que.push(node1);    level.push(1);    int currentLevel=1;    while(!que.empty())    {        Tnode * temp=que.front();        que.pop();        int l=level.front();        level.pop();        if(currentLevel<l)         {            cout<<endl;            currentLevel=l;        }        cout<<temp->value<<"  ";        if(temp->leftChild!=NULL)         {            que.push(temp->leftChild);            level.push(l+1);        }        if(temp->rightChild!=NULL)        {            que.push(temp->rightChild);            level.push(l+1);        }    }    cout<<endl;//    printNodeAtLevel(node1,3);    return 0;}

</p>
<p>

</div>

</p>

