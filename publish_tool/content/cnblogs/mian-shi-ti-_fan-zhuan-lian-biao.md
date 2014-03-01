Title: 面试题_反转链表
Date: 2011-03-09 08:21
Author: 糖拌咸鱼
Slug: mian-shi-ti-_fan-zhuan-lian-biao

<span>**题目**：输入一个链表的头结点，反转该链表，并返回反转后链表的头结点。代码如下：</span>

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>using namespace std;struct Node{    int value;    Node * link;    Node()    {        value=0;        link=NULL;    }};//返回反向链表的头结点Node* Reserve(Node * head){    Node * pre,*next;    pre=head;    head=head->link;    pre->link=NULL;    while(head!=NULL)    {        next=head->link;        head->link=pre;        pre=head;        head=next;    }    return pre;}int main(){    Node *head = new Node;    Node *tail=head;    //生成10个结点元素    for(int i=0;i<10;i++)    {        Node * newNode= new Node;        newNode->value=i+1;        tail->link=newNode;        tail=newNode;    }    //正向遍历链表    Node * interator = head;    while(interator!=NULL)    {        cout<<interator->value<<endl;        interator=interator->link;    }    //将链表反向    interator=Reserve(head);    while(interator!=NULL)    {        cout<<interator->value<<endl;        interator=interator->link;    }    //堆区内存清理    while(head!=NULL)    {        Node * next=head->link;        delete head;        head=next;    }    return 0;}

</p>
<p>

</div>

</p>

