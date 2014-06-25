# String Sorts

##LSD string sort
###原理
1. LSD算法是典型的针对固定长度字符串排序的方法，如对IP地址，账号的排序。
2. 主要的的思想，从右向左，对每个位置的字符进行rerank。
3. rerank, 采用一个counter记录每个字符所对应字符串rerank后的起始位置。这个方法有小技巧和逻辑性，值得一读。<code>Pay attention!</code>

###特性
1. LSD是稳定的排序算法
2. LSD算法需要使用7WN+3WR的数组访问以及N+R的内存空间。W为key string的长度，N为待排序元素个数，由于实际应用中R远远小于N，因此近似时间复杂度为WN。

###Source Code
```cpp
void LSD_sort(string arr[], int N, int W) {
    const int R = 256;
    string * aux = new string [N];
    for(int i=W-1; i>=0; i--){
        int counter[R] = {0};
        for(int j=0; j<N; j++){
            counter[arr[j][i]+1] += 1;
        }
        for(int j=1; j<R; j++){
            counter[j] += counter[j-1];
        }
        for(int j=0; j<N; j++){
            aux[counter[arr[j][i]]++] = arr[j];
        }
        for(int j=0; j<N; j++){
            arr[j] = aux[j];
        }
    }
    delete [] aux;
}
```

##MSD string Sort
