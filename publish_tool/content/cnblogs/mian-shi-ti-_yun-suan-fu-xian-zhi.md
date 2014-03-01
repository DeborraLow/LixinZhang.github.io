Title: 面试题_运算符限制
Date: 2011-03-08 02:47
Author: 糖拌咸鱼
Slug: mian-shi-ti-_yun-suan-fu-xian-zhi

**<span size="3" style="font-size: small;"><span
lang="ZH-CN">题目1：写一个函数，求两个整数的之和，要求在函数体内不得使用＋、－、×、÷。</span></span>**

</p>

<span size="3" style="font-size: small;"><span
lang="ZH-CN">思路：模拟二进制加法，先加不进位得A，然后算进位得B，然后（B\<\<1）+A即得到两个数之和。A可以由两个数的\^得到，B可以有A&B得到。</span></span>

</p>

**<span size="3" style="font-size: small;"><span
lang="ZH-CN"> </span></span>**

</p>

<div class="cnblogs_code">

</p>
<p>
    int plus(int num1,int num2){    if(num2==0) return num1;    return plus(num1^num2,(num1&num2)<<1);}

</p>
<p>

</div>

</p>

**<span size="3" style="font-size: small;"><span
lang="ZH-CN"><span>题目：求</span>1+2+…+n<span>，要求不能使用乘除法、</span>for<span>、</span>while<span>、</span>if<span>、</span>else<span>、</span>switch<span>、</span>case<span>等关键字以及条件判断语句（</span>A?B:C<span>）</span></span></span>**

</p>

<span size="3" style="font-size: small;"><span
lang="ZH-CN">思路：网上很多事用模板元计算，这里给出另一种方法，利用A&&B的特点，即A若为False则B不会执行，用以来终止递归。</span></span>

</p>

<b><span size="3" style="font-size: small;"><span lang="ZH-CN"><span>

<div class="cnblogs_code">

</p>
<p>
    int work(int n,int & ans){    ans+=n;    n && work(n-1, ans);    return ans;}

</p>
<p>

</div>

</p>
  
</span></span></span></b>

</p>

