# Search

##查找两个有序数组的中位数,Median of Two Sorted Arrays
[https://oj.leetcode.com/problems/median-of-two-sorted-arrays/](https://oj.leetcode.com/problems/median-of-two-sorted-arrays/)

###Source Code

```cpp
//Baidu面试的时候，被问到过这道题。
class Solution {
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        int total_len = (m + n);
        if (total_len % 2 == 1){
            return find_KthItem_in_sorted_arrays(A, m , B, n, total_len / 2 + 1);
        }else{
            int mid_1 = find_KthItem_in_sorted_arrays(A, m , B, n, total_len / 2);
            int mid_2 = find_KthItem_in_sorted_arrays(A, m , B, n, total_len / 2 + 1);
            return (mid_1 + mid_2) / 2.0;
        }
    }
    //更通用的两个有序的列表中，找第k大的元素的方法，这里假设数组A长度大于数组B，若长度A<B，则调换下位置即可
    int find_KthItem_in_sorted_arrays(int A[], int m, int B[], int n, int k){
        if (m<n) return find_KthItem_in_sorted_arrays(B, n, A, m, k);
        if (n==0) return A[k-1];
        if (k==1) return min(A[0], B[0]);

        //由于保证A的长度大于B，所以k - kth_b一定为正数，而kth_b需要min(k/2, n);
        int kth_b = min(k/2, n);
        int kth_a = k - kth_b;

        if(A[kth_a-1] > B[kth_b-1]){
            //当去掉B的前kth_b元素的时候，使用的方法是B的指针位置+kth_b，偏移量，
            //这个方法很好，避免再记录low等index用于标记
            return find_KthItem_in_sorted_arrays(A, m, B+kth_b, n-kth_b, kth_a);
        }
        else if(A[kth_a-1] < B[kth_b-1]){
            return find_KthItem_in_sorted_arrays(A+kth_a, m-kth_a, B, n, kth_b);
        }
        else {
            return A[kth_a-1];
        }

    }
};
```
