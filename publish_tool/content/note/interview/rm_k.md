Title: 删除K个数字，使剩下的数字串最大(Hulu面试题)
Date: 2014-08-19 9:23
Category: Algorithm
Tags: 面试题

##删除K个数字，使剩下的数字串最大

转自：[http://blog.csdn.net/lxmky/article/details/8031780](http://blog.csdn.net/lxmky/article/details/8031780)

###题目描述：
一个n位的数，去掉其中的k位，问怎样去掉使得留下来的那个（n-k）位的数最大？

###分析：
可以直接用贪心来求解，每次寻找从头开始的连续递减序列，删除递减序列的最后一个元素，重复K次，最后剩下的数字串组成的数字最大。

比如：
<pre>
“13787323”
第一次，递减序列只有1，删除1，得到3787323
第二次，递减序列只有3，删除3，得到787323
第三次，递减序列只有7，删除7，得到87323
第四次，递减序列是8732，删除2，得到8733
</pre>

###source code

    ```cpp
    #include <stdio.h>
    #include <iostream>
    using namespace std;

    char *itoa(int value, char *string, int radix)
    {
        int rt=0;
        if(string==NULL)
            return NULL;
        if(radix<=0 || radix>30)
            return NULL;
        rt = snprintf(string, radix, "%d", value);
        if(rt>radix)
            return NULL;
        string[rt]='\0';
        return string;
    }

    bool cmp(char a, char b, bool reverse){
        if (reverse) {
            return a<=b;
        }else{
            return a>=b;
        }
    }

    int num_after_remove_k(char num_str[], int k, int num_len, bool (*cmp)(char, char, bool), bool reverse)
    {
        const char RMFLAG = 'x';
        while(k>0){
            int cur = 0;
            int pre = 0;
            while(cur < num_len && 
                (num_str[cur] == RMFLAG || (*cmp)(num_str[cur], num_str[pre], reverse))) {
                if (num_str[cur] != RMFLAG)
                    pre = cur;
                cur++;
            }
            num_str[pre] = RMFLAG;
            k--;
        }
        int res = 0;
        for(int i=0; i<num_len; i++){
            if (num_str[i] == RMFLAG) continue;
            res *= 10;
            res += (num_str[i] - '0');
        }
        return res;
    }

    int maxnum_after_remove_k(int num, int k){
        if (num == 0 || k <= 0) return 0;
        bool flag = true;
        if(num < 0){
            flag = false;
            num = -num;
        }
        char num_str[32];
        itoa(num, num_str, 10);
        int num_len = strlen(num_str);
        return num_after_remove_k(num_str, k, num_len, &cmp, flag) * (flag?1:-1);
    }

    int main()
    {
        cout<<maxnum_after_remove_k(236311, 3);
        return 0;
    }
