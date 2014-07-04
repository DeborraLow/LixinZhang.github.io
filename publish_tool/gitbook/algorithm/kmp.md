# KMP
##基本算法

###思路
采用<code>while(i< len1 && j< len2)</code>的形式，然后当遇到S[i]!=P[j]的时候，i回退到i-j+1(即相当于起始位置++)，然后j回退到0。时间复杂度为O(m*n)。

###Source Code
```cpp
int strstrBase(string &s, string &pattern){
    int i=0, j=0;
    while(i<s.size() && j<pattern.size()){
        if(s[i] == pattern[j]){
            i++; j++;
        }else{
            i = i-j+1;
            j = 0;
        }
    }
    if (j>=pattern.size()) return i-j;
    return -1;
}
```

##KMP算法

###思路
KMP一直不好理解。
它与之前的那种朴素解法的优点是，i和j不需要回退到那么起始的位置。于是，参与一个next辅助数组，来计算当遇到不匹配的时候，j回退到哪个位置，而i则不变或进行中一直向前。从而保证了算法的时间复杂度为O(m+n)
有个问题需要理清楚：

直观上为什么i不要回退，只回退j就行了?
<pre>
   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
S: b a c b a b a b a a b  c  b  a  b
           1 2 3 4 5 6 7
P:         a b a b a c a
</pre>

上例中，当位置S[9]与P[6]不匹配时，j不必回退到1位置，因为我们知道了一些先验知识，如S[5]肯定不会与



###Source Code
```cpp
vector<int> nextGenerator(string &pattern){
    vector<int> next;
    next.push_back(-1);
    int i=0, j=-1;
    while(i<pattern.size()-1){
        if(j == -1 || pattern[i] == pattern[j]){
            i++; j++;
            //next[i] = j;
            next.push_back(j);
        }else{
            j = next[j];
        }
    }
    return next;
}

int kmp(string &s, string & pattern){
    int i=0, j=0;
    vector<int> next = nextGenerator(pattern);
    while(i<int(s.size()) && j<int(pattern.size())){
        if(j == -1 || s[i] == pattern[j]){
            i++; j++;
        }else{
            j = next[j];
        }
    }
    if (j>=pattern.size()) return i-j;
    return -1;
}

```
