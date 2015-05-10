Title: 面试题_寻找丑数
Date: 2011-03-07 15:17
Author: 糖拌咸鱼
Slug: mian-shi-ti-_xun-zhao-chou-shu

最近一直在准备面试，因为要实习了，然后我就纠结了，不知道自己到底处在一个什么样的水平，到底应该选择怎样的实习单位。但是，不管怎么样，还是多看看题吧，感觉面试题还是挺好玩的。最近又在看《编程之美》，感觉有些收获，其实编程真的可以很美，呵呵。

</p>

**题目**：我们把只包含因子2、3和5的数称作丑数（Ugly
Number）。例如6、8都是丑数，但14不是，因为它包含因子7。习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第1500个丑数。

</p>

     
看过《编程之美》的人，应该都知道书上的解题思路，它总是先从最容易想到的解决方法入手，然后再一直追问，有没有更好的解决方法。我觉得这个解决问题的思路非常好，任何问题都要一遍一遍的推敲，找到最佳的解决方案，从空间和时间上进行双重的优化。

</p>

   
这道题最简单的思路，就是穷举，穷举所有满足条件的数字。其实，仔细想想，穷举有时可以看成是万能的方法，但是效率也是最低的。

</p>
<p>
``` {.brush: .cpp; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
bool IsUgly(int number){    while(number % 2 == 0)        number /= 2;    while(number % 3 == 0)        number /= 3;    while(number % 5 == 0)        number /= 5;    return (number == 1) ? true : false;}int Method1(int index){    if(index <= 0)        return 0;     int number = 0;    int uglyFound = 0;    while(uglyFound < index)    {        ++number;         if(IsUgly(number))        {            ++uglyFound;        }    }     return number;}
```

</p>

      
上面的方法，效率低的无法让人接受。于是，我们在寻求更好的解决办法。仔细阅读题目，会发现这题貌似有点像找素数的问题，对了，就是这样，我们换个思路，不是去枚举所有符合条件的数，而是去通过条件生成这些数字。根据丑数的定义，丑数应该是另一个丑数乘以2、3或者5的结果（1除外）。因此我们可以创建一个数组，里面的数字是排好序的丑数。里面的每一个丑数是前面的丑数乘以2、3或者5得到的。这个思路的关键点，就是要保证数组里面的丑数是排好序的。假设arr[1..i]是已经排好序的数组，则arr[i]一定是这里面最大的数，那么我们只要去寻找新生成的数字中比arr[i]大的的最小的数。新生成的数是由前面的数字\*2或\*3或\*5得到的。我们定义index2为前面数字\*2中的所有数字中满足大于arr[i]的最小的数的下标，index3,index5类似定义，则应该放在arr[i+1]位置的数字便是min(arr[index2]\*2,arr[index3]\*3,arr[index5]\*5)。

</p>

注意代码里，index2，index3，index5是维持动态向前的，不会产生无效搜索，因为当前找的数字一定比原来找的要大，所以从上一次找到的下标开始进行搜索就可以了。

</p>

具体代码实现如下：

</p>
<p>
``` {.brush: .cpp; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
int Min(int a, int b , int c){    a=a<b?a:b;    if(c<a) return c; else return a;}int Method2(int Mindex){  int index=1; int *arr= new int[Mindex];   arr[0]=1;    int index2=0, index3=0, index5=0;    while(index<Mindex)   {        int min=Min(arr[index2]*2,arr[index3]*3,arr[index5]*5);      arr[index]=min;      while(arr[index2]*2<=arr[index]) index2++;        while(arr[index3]*3<=arr[index]) index3++;        while(arr[index5]*5<=arr[index]) index5++;        index++; }
```

</p>
<p>
``` {.brush: .cpp; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
　　　int ans=arr[Mindex-1];
```

</p>
<p>
``` {.brush: .cpp; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
　　　delete arr; return ans;}
```

</p>

