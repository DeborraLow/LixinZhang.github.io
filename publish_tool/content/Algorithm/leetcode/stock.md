Title: stock买进卖出系列
Date: 2014-08-31 12:54
Category: Algorithm
Tags: Leetcode

##Best Time to Buy and Sell Stock
Link:
[https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/)

###分析

####方法1
计算A[i+1] - A[i]，然后转化最大连续子序列问题。
思路转化：构造新的数据B[i] = A[i+1]-A[i], 则 B[i..j]的和即为A[j+1]-A[j] + A[j] - A[j-1] ... A[i+1] - A[i] = A[j] - A[i]
于是题目变成最大子段和的问题
####Source Code

```cpp
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if(prices.size() <= 1) return 0;
        vector<int> sub_prices;
        //sub_prices.push_back(prices[0]);
        for(int i=0; i<prices.size()-1; i++){
            sub_prices.push_back(prices[i+1] - prices[i]);
        }
        vector<int> sub_sum(sub_prices.size(), 0);
        sub_sum[0] = sub_prices[0];
        int max_profix = sub_sum[0];
        for(int i=1; i<sub_prices.size(); i++)
        {
            if (sub_sum[i-1] > 0){
                sub_sum[i] = sub_prices[i] + sub_sum[i-1];
            }else{
                sub_sum[i] = sub_prices[i];
            }
            max_profix = max(sub_sum[i], max_profix);
        }
        return max_profix > 0 ? max_profix : 0;
    }
};
```
###方法二
贪心，max(当前点i与前面0到i-1点中最小值的差值),可以动态维护当前点之前的最小值。

这个方法，就很简单。
####Source Code

```cpp
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int pre_min = 90000000;
        int ans = 0;
        for(int i=0; i<prices.size(); i++)
        {
            ans = max(prices[i]-pre_min, ans);
            pre_min = min(pre_min, prices[i]);
        }
        return ans;
    }
};
```


##Best Time to Buy and Sell Stock I
Link:
[https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

###分析

与该问题的I问题相似，用贪心方法，加和所有临近两项的差值大于0的差值。

证明贪心是有效的：B[i] = A[i+1]-A[i]，其实把这题抽象为求B的K段子段和的题目。
假设B[i..k]>0, B[k..j] < 0, B[j..p]>0等同于sum(B[i..k]) + sum(B[j..p]), 因为B[i..k] = A[k] - A[i]
因此遇到B[i] < 0的情况，就相当于划分出了一个新的子段。

###Source Code

```cpp
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if (prices.size() <= 1) return 0;
        int res = 0;
        for(int i=0; i<prices.size()-1; i++)
        {
            res += max(prices[i+1] - prices[i], 0);
        }
        return res > 0 ? res : 0;
    }
};
```

##Best Time to Buy and Sell Stock III
Link:
[https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

###分析

题目要求是两段，然后可以计算得出两个序列：
<code>pre_max_prices[i]</code>表示以<code>i</code>结尾[0, i]的最大子段和。

<code>post_max_prices[i]</code>表示以<code>i</code>结尾[i, LEN]的最大子段和。

于是最优解

$$twice_max_profix = max(pre_max_prices[i-1] + post_max_prices[i+1])$$

当然也可以分为一段，因此最后的结果为max(once_max_profix, twice_max_profix)。

<code>这个思路非常重要，记得要想着去枚举分割点。</code>

一道类似的题目：
[http://lintcode.com/en/problem/maximum-subarray-difference/](http://lintcode.com/en/problem/maximum-subarray-difference/)

枚举一个分割点，左边求最大，右边求最小。或左边求最小，右边求最大。

###Source Code

```cpp
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if(prices.size() <= 1) return 0;
                
        vector<int> pre(prices.size(), 0), post(prices.size(), 0);
        int len = prices.size();
        pre[0] = 0;
        post[len-1] = 0;
        int pre_min = prices[0];
        int post_max = prices[len-1];
        int singleTrans = 0;
        for(int i=1; i<prices.size(); i++){
            pre[i] = prices[i] - pre_min;
            pre[i] = max(pre[i-1], pre[i]);
            pre_min = min(pre_min,  prices[i]);
            singleTrans = max(singleTrans, pre[i]);
        }
        for(int i=len-2; i>=0; i--){
            post[i] = post_max - prices[i];
            post[i] = max(post[i+1], post[i]);
            post_max = max(post_max, prices[i]);
        }
        int doubleTrans = 0;
        for(int i=0; i<len-1; i++){
            doubleTrans = max(doubleTrans, pre[i] + post[i+1]);
        }
        //cout<<singleTrans<<"\t"<<doubleTrans;
        return max(singleTrans, doubleTrans);
    }
};
```
