Title: 面试题_旋转字符串
Date: 2011-03-09 07:50
Author: 糖拌咸鱼
Slug: mian-shi-ti-_xuan-zhuan-zi-fu-chuan

<span>**题目：**定义字符串的左旋转操作：把字符串前面的若干个字符移动到字符串的尾部。如把字符串</span>abcdef<span>左旋转</span>2<span>位得到字符串</span>cdefab<span>。请实现字符串左旋转的函数。要求时间对长度为</span>n<span>的字符串操作的复杂度为</span>O(n)<span>，辅助内存为</span>O(1)<span>。</span>

</p>

**思路**:将字符串看做AB两部分，将A反转，再将B反转，最后将反转后的A+反转后的B一起反转就OK了。

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>#include<assert.h>using namespace std;const int MAX=100;//反转从start到end的字符串svoid Reversal(int start,int end,char *s){    assert(s!=NULL);    int halfLength=(end+1+start)/2;    for(int i=start;i<halfLength;i++)    {        char temp=s[i];        s[i]=s[end+start-i];        s[end+start-i]=temp;    }}int main(){    char str[MAX];    int leftLength,i,j,length;    while(cin>>str>>leftLength)    {        length =strlen(str);        if(leftLength<=0||leftLength>=length) break;        Reversal(0,leftLength-1,str);        Reversal(leftLength,length-1,str);        Reversal(0,length-1,str);        cout<<str<<endl;    }        return 0;}

</p>
<p>

</div>

</p>

</p>

