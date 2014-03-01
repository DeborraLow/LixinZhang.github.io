Title: 集合的子集和集合的全排列问题
Date: 2011-05-09 01:18
Author: 糖拌咸鱼
Slug: ji-he-de-zi-ji-he-ji-he-de-quan-pai-lie-wen-ti

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>using namespace std;//非递归求解所有的子集void fun(int a[] , int n){    int i = 0 , j ;    while(i < (1<<n)) //2的n次方    {        for(j = 0 ; j < n ; j ++)        {            if(i&(1<<j))            {                cout<<a[j]<<"\t";            }        }        cout<<endl;        i++;    }}//递归求解所有的子集void print(int a[],bool flag[],int k,int length){    if(k>=length)    {        for(int i=0;i<length;i++)        {            if(flag[i]) cout<<a[i]<<"\t";        }        cout<<endl;        return ;    }    for(int j=0;j<2;j++)    {        if(j==0)        {            flag[k]=true;            print(a,flag,k+1,length);            flag[k]=false;        }        else        {            flag[k]=false;            print(a,flag,k+1,length);            flag[k]=true;        }    }}//集合的全排列算法void Perm(int list[], int k ,int length){    if(k>=length)    {        for(int i=0;i<length;i++)            cout<<list[i]<<"\t";        cout<<endl;        return ;    }    for( int j=k;j<length;j++)    {        swap(list[k],list[j]);        Perm(list,k+1,length);        swap(list[k],list[j]);    }}int main(){    int list[]={1,2,3,4};    bool flag[]={false,false,false,false};    fun(list,4);    print(list,flag,0,4);    Perm(list,0,4);    return 0;}

</p>
<p>

</div>

</p>

