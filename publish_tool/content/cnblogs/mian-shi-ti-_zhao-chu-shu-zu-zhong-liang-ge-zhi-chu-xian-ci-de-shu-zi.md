Title: 面试题_找出数组中两个只出现一次的数字
Date: 2011-03-09 05:54
Author: 糖拌咸鱼
Slug: mian-shi-ti-_zhao-chu-shu-zu-zhong-liang-ge-zhi-chu-xian-ci-de-shu-zi

<span
lang="ZH-CN">**题目**：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是</span><span
face="Calibri" style="font-family: Calibri;">O(n)</span><span
lang="ZH-CN">，空间复杂度是</span><span face="Calibri"
style="font-family: Calibri;">O(1)</span><span lang="ZH-CN">。</span>

</p>

<span lang="ZH-CN"><span size="3"
style="font-size: small;">**分析**：这是一道很新颖的关于位运算的面试题。</span></span>

</p>

<span lang="ZH-CN"><span size="3"
style="font-size: small;">首先我们考虑这个问题的一个简单版本：一个数组里除了一个数字之外，其他的数字都出现了两次。请写程序找出这个只出现一次的数字。</span></span>

</p>

<span size="3" style="font-size: small;"><span
lang="ZH-CN">这个题目的突破口在哪里？题目为什么要强调有一个数字出现一次，其他的出现两次？我们想到了异或运算的性质：任何一个数字异或它自己都等于</span><span
face="Calibri" style="font-family: Calibri;">0</span><span
lang="ZH-CN">。也就是说，如果我们从头到尾依次异或数组中的每一个数字，那么最终的结果刚好是那个只出现依次的数字，因为那些出现两次的数字全部在异或中抵消掉了。</span></span>

</p>

<span lang="ZH-CN"><span size="3"
style="font-size: small;">有了上面简单问题的解决方案之后，我们回到原始的问题。如果能够把原数组分为两个子数组。在每个子数组中，包含一个只出现一次的数字，而其他数字都出现两次。如果能够这样拆分原数组，按照前面的办法就是分别求出这两个只出现一次的数字了。</span></span>

</p>

<span size="3" style="font-size: small;"><span
lang="ZH-CN">我们还是从头到尾依次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果。因为其他数字都出现了两次，在异或中全部抵消掉了。由于这两个数字肯定不一样，那么这个异或结果肯定不为</span><span
face="Calibri" style="font-family: Calibri;">0</span><span
lang="ZH-CN">，也就是说在这个结果数字的二进制表示中至少就有一位为</span><span
face="Calibri" style="font-family: Calibri;">1</span><span
lang="ZH-CN">。我们在结果数字中找到第一个为</span><span face="Calibri"
style="font-family: Calibri;">1</span><span
lang="ZH-CN">的位的位置，记为第</span><span face="Calibri"
style="font-family: Calibri;">N</span><span
lang="ZH-CN">位。现在我们以第</span><span face="Calibri"
style="font-family: Calibri;">N</span><span
lang="ZH-CN">位是不是</span><span face="Calibri"
style="font-family: Calibri;">1</span><span
lang="ZH-CN">为标准把原数组中的数字分成两个子数组，第一个子数组中每个数字的第</span><span
face="Calibri" style="font-family: Calibri;">N</span><span
lang="ZH-CN">位都为</span><span face="Calibri"
style="font-family: Calibri;">1</span><span
lang="ZH-CN">，而第二个子数组的每个数字的第</span><span face="Calibri"
style="font-family: Calibri;">N</span><span
lang="ZH-CN">位都为</span><span face="Calibri"
style="font-family: Calibri;">0</span><span
lang="ZH-CN">。</span></span>

</p>

<span lang="ZH-CN"><span size="3"
style="font-size: small;">现在我们已经把原数组分成了两个子数组，每个子数组都包含一个只出现一次的数字，而其他数字都出现了两次。因此到此为止，所有的问题我们都已经解决。</span></span>

</p>

<span size="2" style="font-size: x-small;"><span
style="line-height: 19px;">以上转自<http://zhedahht.blog.163.com/blog/static/2541117420071128950682/></span></span>

</p>

<span size="2" style="font-size: x-small;"><span style="line-height: 19px;">

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>using namespace std;int main(){    const int size=10;    int arr[size]={1,1,2,2,3,3,5,5,4,6};    int i,ans=arr[0];    for(i=1;i<size;i++)    ans^=arr[i];    int index=0;    //寻找二进制数从尾部到头部的第一个为1的位置index    while(ans)    {        ans&=1;        if(ans==1) break;        else        {            ans=ans>>1;            index++;        }    }    int cmp=(1<<index);    int ans0=0,ans1=0,k0=0,k1=0;    while((arr[k0]&cmp)==1) k0++;    ans0=arr[k0];    while((arr[k1]&cmp)==0) k1++;    ans1=arr[k1];    for(i=k0+1;i<size;i++)        if ((arr[i]&cmp)==0) ans0^=arr[i];    for(i=k1+1;i<size;i++)        if ((arr[i]&cmp)==cmp) ans1^=arr[i];    cout<<ans0<<"\t"<<ans1<<endl;    return 0;}

</p>
<p>

</div>

</p>
  
</span></span>

</p>

<span lang="ZH-CN">  
</span>

</p>

