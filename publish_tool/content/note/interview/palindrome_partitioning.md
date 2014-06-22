Title: DP-palindrome-partitioning II 
Date: 2014-06-21 16:23
Category: Algorithm
Tags: 面试题

##Description
Leetcode 题目： [palindrome-partitioning II](https://oj.leetcode.com/problems/palindrome-partitioning-ii/)

> Given a string s, partition s such that every substring of the partition is a palindrome.
> Return the minimum cuts needed for a palindrome partitioning of s.

> For example, given s = "aab",
> Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


由于之前，刚刚做过[DP-括号匹配(网易有道面试题)](http://lixinzhang.github.io/dp-gua-hao-pi-pei-wang-yi-you-dao-mian-shi-ti.html)，感觉可以利用相似的dp策略来做。后来，经历了各种超时，内存溢出，才去发现有更好的解决办法，可以针对时间和空间分别进行优化，感觉做这道题目比较有收获。

##Solution

###思路0
首先，求回文的时候，可以借助DP的思想，可以加快check回文的速度：

$$flag[i][j] = flag[i+1][j-1] \\&\\&  s[i]==s[j]$$

顺便附带一道相关题目[longest-palindromic-substring](https://oj.leetcode.com/problems/longest-palindromic-substring/)。

    :::cpp
    //利用dp性质f[i][j] = f[i+1][j-1] && S[i] == S[j]
    class Solution {
    public:
        string longestPalindrome(string s) {
            bool check[1001][1001] = {false};
            for(int i=0; i<s.size(); i++){
                check[i][i] = true;
            }
            int res_low=0, res_high=0;
            for(int step=1; step<s.size(); step++){
                for(int i=0; i<s.size()-step; i++){
                    int j = i + step;
                    if (s[i] == s[j] && (i+1==j || check[i+1][j-1] == true)){
                        check[i][j] = true;
                        if (j-i+1 > res_high-res_low+1){
                            res_low = i;
                            res_high = j;
                        }
                    } 
                }
            }
            return s.substr(res_low, res_high - res_low + 1);
        }
    };
        

###思路1
定义$$$F[i][j]$$$表示字符串$$$s$$$从位置$$$i$$$到$$$j$$$所需要的最少<code>cut</code>数，则有如下递推关系：

$$
F[i][j] = \\left\\{ \begin{array}{ll}
1 & \\textrm{if s[i..j] is Palindrome}\\\
min(F[i][k] + F[k+1][j]) & \\textrm{others}\\\
\\end{array} \\right.
$$

####复杂度分析####

Time：$$$O(n^3)$$$  

Space：$$$O(n^2)\*int + O(n^2)\*int$$$

Leetcode：无法Accpeted， 时间空间，均无法满足要求

####参考程序####
    :::cpp
    class Solution {
    public:
        int minCut(string s) {
            int ** F = new int * [s.size()];
            bool ** valid = new bool * [s.size()];
            for(int i=0; i<s.size(); i++){
                F[i] = new int [s.size()];
                valid[i] = new bool [s.size()];
                F[i][i] = 1;
                valid[i][i] = 1;
            }
            for(int step=1; step<s.size(); step++){
                for(int i=0; i<s.size()-step; i++){
                    int j = i + step;
                    F[i][j] = s.size();
                    if(valid[i+1][j-1] && (s[i] == s[j])){
                        F[i][j] = 1;
                        valid[i][j] = true;
                        continue;
                    }
                    for(int k=i; k<j; k++){
                        if ( F[i][k] + F[k+1][j] < F[i][j]){
                                F[i][j] = F[i][k] + F[k+1][j];
                                if(F[i][j] == 2) break;
                            }
                    }
                }
            }
            bool res =  F[0][s.size()-1] - 1;
            
            for(int i=0; i<s.size(); i++){
                delete [] F[i];
                delete [] valid[i];
            }
            return res;
        }
    };


###思路2
定义$$$F[i]$$$表示从字符串$$$s$$$从位置i到结尾的最少需要的cut数，则有：
$$F[i]=min(F[j]+1) ,{i<j<n}$$

由于每次求F[i]的时候，是基于之前的状态j，那么状态j必须提前计算完毕，因此最外层循环从后往前。

####复杂度分析####

Time：$$$O(n^2)$$$  

Space：$$$O(n)\*int + O(n^2)\*bool$$$

Leetcode：Accpeted

####参考程序####
    :::cpp
    class Solution {
    public:
        int minCut(string s) {
            int F[2000];
            bool flag[2000][2000] = {false};
            for(int i=0; i<s.size(); i++){
                F[i] = s.size() - i -1;
                flag[i][i] = true;
            }
            F[s.size()] = -1;
            for(int i=s.size()-1; i>=0; i--){
                for(int j=i; j<s.size(); j++){
                    if(i==j || (j==i+1 && s[j] == s[i]) || (flag[i+1][j-1] && s[i]==s[j])){
                        flag[i][j] = true;
                        F[i] = min(F[i], F[j+1] + 1);
                    }
                }
            }
            return F[0];
        }
    };
    
