Title: Init5-面试题总结
Date: 2014-08-24 19:23
Category: Algorithm
Tags: 面试题

###题目来源
[http://www.itint5.com/](http://www.itint5.com/)
只记录一下这里面的一些比较经典或者是Leetcode等没出现过的题目

##环形路加油
有一个环形公路上有n个加油站，第i个加油站的油量为ai。假设有一辆邮箱体积无穷大的汽车，初始邮箱是空的，汽车从加油站i行驶到加油站i+1需耗油g[i]。

问是否能够选出某个加油站作为起点，使汽车能够绕环形公路行驶一圈返回到该加油站。

实现函数int selectGasStation(int a[], int g[], int n)，如果存在满足条件的加油站，返回该加油站的序号(0-based)。否则返回-1。

提示：n可能达到106，O(n2)的枚举算法会超出时间限制。

###分析

环形，即可以考虑<code>2*N-1</code>的展开处理。
定义$$$c[i] = a[i] - g[i]$$$表示完成某一路段真实耗油量（因为起点加了一些油）。于是，问题转化为求以某一起点slow开始到长度n节点的所有前缀和均为正的问题。

以slow点起始位置，如果在途中的fast点，出现前缀和为负数的情况，那么slow到fast之间的点，则不可能满足约束。因此直接跳过这些点，从<code>slow = fast +1</code>开始找。因此，时间复杂度为$$$O(N)$$$。

###程序

```cpp
#include <vector>
using namespace std;

int selectGasStation(const vector<int> &a, const vector<int> &g) {
    if(a.size() == 0 || g.size() == 0 || a.size() != g.size()) return -1;
    vector<int> c(a.size() * 2 -1);
    int gas_count = a.size();
    for(int i=0; i<gas_count; i++)
    {
        c[i] = a[i] - g[i];
        if (i < gas_count - 1)
            c[i+gas_count] = a[i] - g[i];
    }
    int slow = 0;
    int fast = 0;
    int has_gas = 0;
    while(fast < c.size()){
        has_gas += c[fast];
        if (has_gas < 0) {
            slow = fast+1;
            has_gas = 0;
        }
        if (fast - slow +1 == gas_count) return slow;
        fast++;
    }
    return -1;
}
```


##堆放积木

有n块积木，每块积木有体积vol和重量weight两个属性，用二元组(vol, weight)表示。积木需要搭成竖直的塔状，上面积木的体积和重量必须都比它下面的积木小。问最多可以搭多少个积木。

###分析
排序 + DP
按一个维度排序，然后最长不降递增子序列。

###程序

```cpp
/*积木的定义(请不要在代码中定义该结构)
struct Box {
  int vol, weight;
};*/
 
bool cmp(Box b1, Box b2){
    return b1.vol < b2.vol;
}

bool isvalid(Box & b1, Box & b2){
    return (b1.weight > b2.weight) 
        && (b1.vol > b2.vol);
}

int maxBoxes(vector<Box> &boxes) {
    if(boxes.size() <=1 ) return boxes.size();
    sort(boxes.begin(), boxes.end(), cmp);
    vector<int> f(boxes.size(), 1);
    f[0] = 1;
    int res = 1;
    for(int i=1; i<f.size(); i++){ 
        for(int j=0; j<i; j++){
            f[i] = max(f[i], isvalid(boxes[i], boxes[j]) ? f[j]+1 : 0);
        }
        res = max(res, f[i]);
    }
    return res;
}
```

##两数积全为1
给定一个非负整数a（不超过10^6），是否存在整数b，使得a和b的乘积全为1。如果存在，返回最小的乘积的位数。如果不存在，返回-1。

样例：a=3，存在b=37，使得3*37=111，则函数应返回3（111的位数）。

###分析
一开始，想着正向的方式去枚举质数，然后检验乘积为111*11，发现无论时间规模或者空间规模都不行。

于是，考虑反向枚举111*111，因为这个的候选集合是非常少的。

然后，另一个需要解决的问题是，枚举111*111，但很容易超出数据类型范围。因此，枚举过程中，可以适当的减少候选值的规模，因为$$$X % b$$$的结果等价于$$$(X - X/b * b) % b$$$结果。因此，在迭代过程中，可以逐渐减少数据大小范围。

###程序

```cpp
int findMinAllOne(int a) {
    if (a == 0 || a % 5 == 0 || a % 2 ==0) return -1;
    int base = 1;
    int result = 1;
    while(true){
        if (base % a == 0) return result;
        base = base * 10 + 1;
        if (base > a) base = base - base/a * a;
        result++;
    }
    return -1;
}
```