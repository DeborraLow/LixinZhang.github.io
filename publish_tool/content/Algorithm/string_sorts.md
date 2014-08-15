Title: String Sorts 字符串排序
Date: 2014-08-15 18:23
Category: CPP
Tags: CPP

对字符串的排序，主要涉及一种<code>count</code>技术，即根据字符的有限性通过计数的方式来划分rerank的位置。

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

<code>MSD</code> is most-significant-digit-first.

###原理
1. MSD主要解决当字符串长度不一致时的，更普遍的的字符串排序问题
2. 与LSD不同，MSD方法从左向右进行比较，并且每次比较都会将原字符串序列分成多个partition。然后对每个patition再进行子问题求解。
3. MSD仍需要借助<code>count</code>技术，对不同的字符串进行划分。但存在一个问题，因为利用<code>count</code>技术的时候，需要访问<code>R</code>数组访问，但与长度已经很小的子序列而言是不值得的，因此对于小长度的子问题，直接采用朴素的插入排序求解。

###特性

1. MSD主要针对不同长度的字符串，因此当有字符串到达末尾的时候，即C++/C中的<code>\0</code>时，由于accsi码值为0，因此具有高优先级，使得其自然排序上升。
2. MSD算法会耗费非常多的内存空间，因为在应用<code>    count</code>方法时，count数组不能放在外面作为类成员变量共享（辅助数组aux则可以）。
3. MSD的算法效率与输入数据非常相关，如若第一列就可以很好的区分开256个部分，那么一次就完成了排序；最差的情况是，数组里的所有字符串都相等，那么就不得不一直走到队尾。
4. MSD需要<code>8N+3R ~ 7wN+3WR</code>之间的数组访问次数。 其中w为平均的字符串长度。

![https://sdfpaw.dm2301.livefilestore.com/y2pg0ab5n0cQhaMrbyvGdwW4u3dvM2ZKSluHbZhhK9cWcPwO9tJ_9ble_Bxsdx5l10g02TQQ5gkytn9_JVrvR2Sm_L8A24MbML6Mikdg1CUd-M/QQ20140627-1.png?psid=1](https://sdfpaw.dm2301.livefilestore.com/y2pg0ab5n0cQhaMrbyvGdwW4u3dvM2ZKSluHbZhhK9cWcPwO9tJ_9ble_Bxsdx5l10g02TQQ5gkytn9_JVrvR2Sm_L8A24MbML6Mikdg1CUd-M/QQ20140627-1.png?psid=1)

###Source Code
```cpp
#include<iostream>
#include<string>
using namespace std;

class MSD{
public:
    static void sort(string arr[], int size);
    static void sort(string arr[], int lo, int hi, int d);
    static void insertSort(string arr[], int lo, int hi, int d);
public:
    static string * aux;
    static int * a;
    const static int R;
    const static int M; //cutoff for small subarrays
};


const int MSD::R = 256;
const int MSD::M = 0;
string * MSD::aux = NULL;

void MSD::sort(string arr[], int size){
    if(size <= 1) return;
    MSD::aux = new string[size];
    sort(arr, 0, size-1, 0);
}
void MSD::sort(string arr[], int lo, int hi, int d){
    if(lo >= hi) return ;
    if(hi<lo+M){
        insertSort(arr, lo, hi, d);
        return ;
    }
    int count [R+1] = {0};
    for(int i=lo; i<=hi; i++){
        count[arr[i][d] + 1] ++;
    }
    for(int r=1; r<R+1; r++){
        count[r] += count[r-1];
    }
    for(int i=lo; i<=hi; i++){
        aux[count[arr[i][d]]++] = arr[i];
    }
    for(int i=lo; i<=hi; i++){
        arr[i] = aux[i-lo];
    }
    for(int r=0; r<R; r++){
        MSD::sort(arr, lo+count[r], lo+count[r+1]-1, d+1);
    }
}

void MSD::insertSort(string arr[], int lo, int hi, int d){
    for(int i=lo+1; i<=hi; i++){
        for(int j=i; j>lo; j--){
            if(arr[i][d] > arr[j][d]){
                swap(arr[i], arr[j]);
            }
        }
    }
}

int main(){
    //MSD::R = 10;
    string arr[] = {"she", "sells", "seashells", "by", "the", "sea",
    "shore", "the", "shells", "she", "sells", "are", "surely", "seashells"};
    int len = 14;
    MSD::sort(arr, len);
    for(int i=0; i<len; i++)
        cout<<arr[i]<<endl;
    return 0;
}
```

##Three-way string quicksort

###原理
1. 参考MSD方法的思想，很容易想到一种基于partition的排序方法——<code>quick sort</code>.
2. 我们可以按照每个位置的字符作为比较元素，然后划分为3个partition。根据之前所了解的三路快排，我们知道中间的那份partition包含的元素是相同的，因此在进行子问题递归的时候，比较元素的位置+1。而另外两个，则继续在该位置上进行子问题计算。

###特性

1. 时间赋值度约定于<code>2NlnN</code>

###源代码
```cpp
class Quick3string{
public:
    static void sort(string arr[], int size){
        sort(arr, 0, size-1, 0);
    }
    static void sort(string arr[], int lo, int hi, int d){
        if(lo>=hi) return;
        int lt = lo, gt = hi;
        int v = arr[lo][d];
        int i = lo+1;
        while(i<=gt){
            int t = arr[i][d];
            if(t<v) swap(arr[lt++], arr[i++]);
            else if (t>v) swap(arr[i], arr[gt--]);
            else i++;
        }
        sort(arr, lo, lt-1, d);
        if(v>=0) sort(arr, lt, gt, d+1);
        sort(arr, gt+1, hi, d);
    }
};
```
###Conclution
![https://sdfpaw.dm2301.livefilestore.com/y2pEB9tecW9w8PnfRrPnhN0dGvP_-ZJiSmDQORpXT2gyaHvXDGvNoOzAfTzP34tytKjPcx8ZjUsCx-joMoVKMBV1OtaY2pFRBQLIe38tLtTkr8/QQ20140627-2.png?psid=1](https://sdfpaw.dm2301.livefilestore.com/y2pEB9tecW9w8PnfRrPnhN0dGvP_-ZJiSmDQORpXT2gyaHvXDGvNoOzAfTzP34tytKjPcx8ZjUsCx-joMoVKMBV1OtaY2pFRBQLIe38tLtTkr8/QQ20140627-2.png?psid=1)
