Title: Subarray常见变形
Date: 2014-10-11 12:54
Category: Algorithm
Tags: Leetcode

##Subarray常见变形

求子序列的问题，很多可以转化为前缀和问题。
前缀和$$sum[i] = sum[0] + sum[1] + sum[2] + … sum[i]$$

补充几道题：

* 最长连续子序列，仍然可以转化为前缀和问题。

* Find the subarray which abs(sum) is biggest. 求前缀和数组中，最大和最小值，其差为最大

* Find the subarray which sum equals to zero. 利用hash表，O(n)， 前缀和数组，找两个前缀和相等的位置

* Find the subarray which sum is closest to zero. 对前缀和数组进行排序，然后找离最近的两个位置。

* 环形最大子序列和，因为所有数组总和S不变，所以考虑两种情况，跨循环点（S - minsubarray），不跨循环点（正常求maxsubarray）