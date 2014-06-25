#Two strings

这里主要记录一些基于动态规划的方法求解的，与两个字符串相关的题目。如最长公共子序列、编辑距离等。

##Distinct Subsequences
###Description
 Given a string S and a string T, count the number of distinct subsequences of T in S.

 A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

 Here is an example:

 S = "rabbbit", T = "rabbit"

 Return 3.

###Solution

定义<code>F[i][j]</code>表示以S的第<code>i</code>个字符与T的第<code>j</code>字符结尾的，S包含T的个数。则有如下递推：

$$
F[i][j] = \\left\\{ \begin{array}{ll}
F[i-1][j] & \\textrm{S[i]<>T[j]}\\\
F[i-1][j] + F[i-1][j-1]) & \\textrm{S[i]=T[j]}\\\
\\end{array} \\right.
$$

当S[i]与T[j]不等时，证明求解F[i][j]时，S[i]是要删除的，因此当前的解应该是i-1状态时的解，即F[i-1][j], 而当S[i]与T[j]相等时，S[i]可能被删除也可能不被删除，如果被删除，则跟前一种情况一样，否则为应为F[i-1][j-1]的结果。这里可能会有疑问，如果S中只有一个S[i]与T[j]对应，那么怎么可以删除呢？ 其实在初始化的时候，需要保证这种情况下的所谓删除得到的F[i-1][j]为0。

初始化很重要，因为我们这里都是基于前一状态的值对当前状态的值进行计算。

###Source Code
```cpp
class Solution {
public:
    int numDistinct(string S, string T) {
        if(S.size() < T.size()) return 0;
        int ** F = new int * [S.size()];
        char flag = T[0];
        int times = 0;
        for(int i=0; i<S.size(); i++){
            F[i] = new int [T.size()];
            for(int j=0; j<T.size(); j++) F[i][j] = 0;
            if(flag == S[i]) {
                times ++;
            }
            F[i][0] = times;
        }
        for(int i=1; i<S.size(); i++){
            for(int j=1; j<T.size(); j++){
                F[i][j] = F[i-1][j];
                if (S[i] == T[j]){
                    F[i][j] = F[i-1][j] + F[i-1][j-1];
                }
                //cout<<i<<"\t"<<j<<"\t"<<F[i][j]<<endl;
            }
        }
        return F[S.size()-1][T.size()-1];
    }
};
```
