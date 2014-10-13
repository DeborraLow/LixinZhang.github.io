Title: Subarray常见变形
Date: 2014-10-11 12:54
Category: Algorithm
Tags: Leetcode

##Subarray常见变形

求子序列的问题，很多可以转化为前缀和问题。
前缀和$$sum[i] = arr[0] + arr[1] + arr[2] + … arr[i]$$

补充几道题：

###最长连续子序列
仍然可以转化为前缀和问题。

###Find the subarray which abs(sum) is biggest. 
求前缀和数组中，最大和最小值，其差为最大

###Find the subarray which sum equals to zero. 
利用hash表，O(n)， 前缀和数组，找两个前缀和相等的位置

###Find the subarray which sum is closest to zero. 
对前缀和数组进行排序，然后找离最近的两个位置。

###环形最大子序列和
因为所有数组总和S不变，所以考虑两种情况，跨循环点（S - minsubarray），不跨循环点（正常求maxsubarray）

###Maximum Product Subarray(Leetcode 新题)
F[2][N], F[0][i]表示以i结尾的连续子序列的最大乘积，F[1][i]表示以i结尾的连续子序列的最小乘积，那么当前i的状态转移方程可以写为：

$$$F[0][i] = maxThree(F[0][i-1] * A[i], F[1][i-1] * A[i], A[i])$$$
$$$F[1][i] = minThree(F[0][i-1] * A[i], F[1][i-1] * A[i], A[i])$$$

改进一下，跟最大子序列和的subarray问题一样，只用一个单变量记录状态也是可以的，这样就保证了O(1)空间+ one-pass。

```cpp
class Solution {
public:
    int minThree(int a, int b, int c){
        return min(min(a,b),c);
    }
    int maxThree(int a, int b, int c){
        return max(max(a,b), c);
    }
    int maxProduct(int A[], int n) {
        if(n <= 0) return 0;
        if(n <= 1) return A[0];
        int pre_max = A[0];
        int pre_min = A[0];
        int res = A[0];
        for(int i=1; i<n; i++){
            int next_max = maxThree(pre_max * A[i], pre_min * A[i], A[i]);
            pre_min = minThree(pre_max * A[i], pre_min * A[i], A[i]);
            pre_max = next_max;
            res = max(pre_max, res);
        }
        return res;
    }
};
```