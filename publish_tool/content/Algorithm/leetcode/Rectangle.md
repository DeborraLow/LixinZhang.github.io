Title: 直方图系列
Date: 2014-08-31 12:53
Category: Algorithm
Tags: Leetcode

##Largest Rectangle in Histogram
Link: [https://oj.leetcode.com/problems/largest-rectangle-in-histogram/](https://oj.leetcode.com/problems/largest-rectangle-in-histogram/)

###分析
难点在维护一个栈，这个栈中的元素是直方图的position，而且其元素从栈底到栈顶是递增的。
如：

heap中的元素为[1,2,5,7]
对应的高度为height[1] < height[2] < height[5] < height[7]
当遇到不满足单调性时，弹出元素进行计算。


```cpp
class Solution {
public:
    int largestRectangleArea(vector<int> &height)
    {
        if (height.size() == 0) return 0;
        stack<int> helper;
        int res = 0;
        height.push_back(0);
        for (int i=0; i<height.size(); i++){
            if (helper.empty() || height[helper.top()] <= height[i] ) {
                helper.push(i);
            }
            else{
                while(!helper.empty() && height[helper.top()] > height[i]){
                    int tmp = helper.top();
                    helper.pop();
                    if (!helper.empty()){
                        //前一点不一定与当前点紧挨着，因此之前先pop，然后再top。
                        int pre = helper.top();
                        res = max(res, height[tmp] * (i - pre - 1));
                    }
                    else {
                        res = max(res, height[tmp] * (i));
                    }
                }
                helper.push(i);
            }
        }
        return res;
    }
};
```


##Trapping Rain Water
Link：[https://oj.leetcode.com/problems/trapping-rain-water/](https://oj.leetcode.com/problems/trapping-rain-water/)

###分析
前后两次遍历，记录位置i之前最大的数，和i之后最大的数，然后可以得出本位置可以存放的水有多少。

###Source code

```cpp
class Solution {
public:
    int trap(int A[], int n) {
        vector<int> left_max_height, right_max_height(n,0);
        int tmp_max = 0;
        for(int i=0; i<n; i++){
            left_max_height.push_back(tmp_max);
            tmp_max = max(tmp_max, A[i]);
        }
        tmp_max = 0;
        for(int i=n-1; i>=0; i--){
            right_max_height[i] = tmp_max;
            tmp_max = max(tmp_max, A[i]);
        }
        int total_water = 0;
        for(int i=0; i<n; i++){
            int cur = min(left_max_height[i], right_max_height[i]) - A[i];
            total_water += (cur>0 ? cur : 0);
        }
        return total_water;
    }
};
```

##Container With Most Water

###分析
//第一次写了个n*n的方法，超时了
//题目的意思是找左右两根直线，围起来的面积最大，这个宽度由（j-i）决定，高度由min(height[i], height[j])决定。
//可以两头遍历一遍，当height[low] < height[high]的时候，证明此时围城的面积，最低高度是由height[low]决定的，那么[low, high-1]不可能出现围城更大的面积，因为宽度在减小，高度有由height[low]上限，因此low++。
//同理height[low] > height[high], high--。 这样就可以保证只遍历一次，即时间是O(n)的复杂度。

###Source code

```cpp
class Solution {
public:
    int maxArea(vector<int> &height) {
        if (height.size() == 0) return 0;
        int most_water = 0;
        int low = 0;
        int high = height.size() - 1;
        while(low < high)
        {
            int min_height = min(height[low], height[high]);
            most_water = max(min_height * (high-low), most_water);
            if(height[low] > height[high]){
                high --;
            }else{
                low ++;
            }
        }
        return most_water;
    }
};
```

