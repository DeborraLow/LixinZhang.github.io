# Matrix

基于矩阵的翻转、打印路径之类的题目。

##Rotate Image

###Description
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

###Solution
直接模拟，不好做。
有个技巧，先按对角线翻转，然后再按照水平线翻转，可以将其旋转90°。<code>pay attention!</code>， 感觉很难想出来。

###Source Code
```cpp
class Solution {
public:
    void rotate(vector<vector<int> > &matrix) {
        //对角线翻转
        for(int i=0; i<matrix.size(); i++){
            for(int j=0; j<matrix[i].size() -i; j++ ){
                int reverse_i = matrix[i].size() - 1 -j;
                int reverse_j = matrix[i].size() - 1 -i;
                swap(matrix[i][j], matrix[reverse_i][reverse_j]);
            }
        }
        //水平线翻转
        for(int i=0; i<matrix.size()/2; i++){
            for(int j=0; j<matrix[i].size(); j++){
                swap(matrix[i][j], matrix[matrix[i].size() -1 -i][j]);
            }
        }
    }
};
```
