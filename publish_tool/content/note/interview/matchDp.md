Title: DP-括号匹配(网易有道面试题)
Date: 2014-06-15 9:23
Category: Algorithm
Tags: 面试题

###Description
> 给你一个字符串，里面只包含"(",")","[","]"四种符号，请问你需要至少添加多少个括号才能使这些括号匹配起来。
如：
[]是匹配的
([])[]是匹配的
((]是不匹配的
([)]是不匹配的

###Solution
这种括号匹配的题目，最直觉的解决方法是利用栈，遇到不匹配，则加一的策略。但是发现是行不通的。仔细分析之后，发现这道题具有如下子结构：
设<code>F[i][j]</code>为字符串<code>str</code>的i到j所需要的最少括号数。则，可能有下面几种情况：

1.两个边界match：如“(XXXXXXXXX)” or "[XXXXXXXXX]"
    
   当$$$i+1 < j$$$时，$$$F[i][j] = F[i+1][j-1]$$$ 
   
   当$$$i+1 = j$$$时，$$$F[i][j] = 0$$$ 
   
2.两个边界不match：如“(XXXXXXXXX]” or “[XXXXXXXXX)” 等。 两个边界不match，那么需要添加一个，或者match左边的，或者match右边的。
   
   match左边, $$$F[i][j] = F[i+1][j] + 1$$$
   
   match右边, $$$F[i][j] = F[i][j-1] + 1$$$
    
3.由于中间某位置字符k，使其分为两部分，如“(XXXXX)(XXXX)”
    
   $$$F[i][j] = F[i][k] + F[k+1][j]$$$
   
最终解，就是上面所有情况求<code>min</code>，我们初始化<code>F[i][i]=1</code>，则可以将第二种情况，归并到第三种情况中，当$$$k=j-1$$$时，$$$F[i][j] = F[i][j-1] + F[j][j]$$$，则表示match了右边。同理 $$$k=i$$$。

有了递推公式，那么求解就很容易了，这里想说一下，这类DP，即枚举中间位置的类型，<strong>其状态应该是两个边界之间的步长</strong>，必须保证小步长比大步长提前计算，例如，求[1,7]的时候，必须已经计算过[5,7]这样短步长的情况，因此最外层的循环，应该时步长从小至大，然后确定两个边界，然后通过递推公式求解。最后附上源代码，大家也可以通过这个OJ平台进行评测，[括号匹配](http://acm.nyist.net/JudgeOnline/problem.php?pid=15)。

    :::cpp
    #include<iostream>
    #include<cstring>
    using namespace std;

    bool checkMatch(char left, char right){
        if(left == '[' && right == ']') return true;
        if(left == '(' && right == ')') return true;
        return false;
    }

    int solution(char str[], int len){
        if (len == 0) return 0;
        int F[101][101];
        for(int i=0; i<len; i++){
            F[i][i] = 1;
        }
        for(int dis=1; dis<len; dis++){
            for(int i=0; i<len-dis; i++){
               int j = i+dis;
               F[i][j] = 999999;
               if(checkMatch(str[i], str[j])){
                   if (i+1 == j) {
                       F[i][j] = 0;
                       continue;
                   }
                   else F[i][j] = F[i+1][j-1];
               }
               for(int k=i; k<j; k++){
                   if (F[i][j] > F[i][k] + F[k+1][j]){
                       F[i][j] = F[i][k] + F[k+1][j];
                   }
               }
           }
        }
        return F[0][len-1];
    }

    int main(){
        //char * testcases[] = {"[]", "([])[]","((]","([)]"};
        int n;
        cin >> n;
        char testcases [101];
        for(int i=0; i<n; i++){
            cin >> testcases;
            cout<<solution(testcases, strlen(testcases))<<endl;
        }
        return 0;
    }
