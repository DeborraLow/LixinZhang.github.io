Title: 两路归并的数组和链表实现
Date: 2011-05-07 08:59
Author: 糖拌咸鱼
Slug: liang-lu-gui-bing-de-shu-zu-he-lian-biao-shi-xian

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>#include<assert.h>using namespace std;struct node{    int val;    node * next;    node(int v)    {        val=v;        next=NULL;    }};node * merge(node* list1 , node * list2){    assert(list1!=NULL&&list2!=NULL);    node * res;    if(list1->val<=list2->val)    {        res=list1;        list1=list1->next;    }    else    {        res=list2;        list2=list2->next;    }    node * p = res;    node *p1 =list1,*p2 =list2;    while(p1!=NULL&&p2!=NULL)    {        if(p1->val<=p2->val)        {            p->next=p1;            p=p->next;            p1=p1->next;        }        else        {            p->next=p2;            p=p->next;            p2=p2->next;        }    }    while(p1!=NULL)     {        p->next=p1;        p=p->next;        p1=p1->next;    }    while(p2!=NULL)     {        p->next=p2;        p=p->next;        p2=p2->next;    }    return res;}int * merge(int * arr1,int la, int * arr2,int lb){    int i=0,j=0;    int * arr = new int[la+lb];    int t=0;    while(i<la&&j<lb)    {        if(arr1[i]<=arr2[j])        {            arr[t++]=arr1[i];            i++;        }        else        {            arr[t++]=arr2[j];            j++;        }    }    while(i<la)     {        arr[t++]=arr1[i];        i++;    }    while(j<lb)    {        arr[t++]=arr2[j];        j++;    }    return arr;}void setLinkData(node * & list1 , node * & list2){    node * node1 = new node(2);    node * node2 = new node(3);    node * node3 = new node(7);    node * node4= new node(9);    node1->next=node2;    node2->next=node3;    node3->next=node4;    list1=node1;    node * node5 = new node(1);    node * node6 = new node(4);    node * node7 = new node(6);    node * node8 = new node(8);    node5->next=node6;    node6->next=node7;    node7->next=node8;    list2=node5;}int main(){    node * list1;    node * list2;    setLinkData(list1,list2);    int arr1[]={1,6,15,17,19};    int arr2[]={2,4,6,8,10};    int * arr = merge(arr1,5,arr2,5);    node * ans = merge(list1,list2);    //Print result    int length=10;    for(int i=0;i<10;i++)    {        cout<<*arr<<endl;        arr++;    }    while(ans!=NULL)    {        cout<<ans->val<<endl;        ans=ans->next;    }    return 0;}

</p>
<p>

</div>

</p>

