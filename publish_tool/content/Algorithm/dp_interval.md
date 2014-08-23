Title: 区间形DP
Date: 2014-08-15 18:23
Category: Algorithm
Tags: Dynamic Programming

区间形DP特征：
$$F[i][j] = F[i][k] + F[k+1][j] + CostFunction(i,j)$$

##石子合并
###题目描述
有n堆石子排成一列，每堆石子有一个重量w[i], 每次合并可以合并相邻的两堆石子，一次合并的代价为两堆石子的重量和w[i]+w[i+1]。问安排怎样的合并顺序，能够使得总合并代价达到最小。

###分析
设状态为$$$F[i][j]$$$，表示第i堆到第j堆石子合并之后的最小分值，那么其上一状态一定是由两个子堆合并而来，那么枚举中间分割位置$$$k$$$为决策状态,因此状态转移方程：
$$F[i][j] = F[i][k] + F[k+1][j] + sum(i,j)$$
其中$$$sum(i,j)$$$为两个自堆合并时，所产生的分值。

此类DP，先计算小区间，然后再通过小区间迭代得到大区间的值。

###同类型的一道面试题
说有n个节点n条边组成一个圈，每个节点上面有一个数，边上有一个+或*，如果消掉某条边，其相邻两个节点就用这个运算符合并。这样一路消边到底，问用什么过程能让最后得到的数最大。

###源代码

```cpp
#include<iostream>
using namespace std;
const int INT_MAX = 99999999;
int mergeStore(int F[][101], int store[], int sum[][101], int n){
    //dynamic programming
    //F[i][j] = F[i][k] + F[k+1][j] + sum(i,j);
    //F[i][j]表示将第    
    //init
    for(int i=0; i<n; i++) F[i][i] = 0;
    for(int step = 1; step < n ; step++)
    {
        for(int i=0; i<n-step; i++){
        	int j = i+step;
            F[i][j] = INT_MAX;
            for(int k=i; k<j; k++){
            	F[i][j] = min(F[i][k] + F[k+1][j] + sum[i][j], F[i][j]);
            }
        }
    }
    return F[0][n-1];
}
void initSum(int sum[][101], int store[], int n){
    for(int i=0; i<n; i++){
        sum[i][i] = store[i];
        for(int j=i+1; j<n; j++){
        	sum[i][j] = sum[i][j-1] + store[j];
        }
    }
}
int main(){
    int n, tmp;
    int store[101];
    int F[101][101];
    int sum[101][101];
    cin >> n;
    for(int i=0; i<n; i++){
    	cin >> tmp;
        store[i] = tmp;
    }
    //init sum
    initSum(sum, store, n);
    cout<<mergeStore(F, store, sum, n)<<endl;

    return 0;
}
```
