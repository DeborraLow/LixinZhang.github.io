# Priority Queue

##Basic

###基本概念

为方便是实现，假设数组从1开始索引。

堆，又叫做优先级队列

这里是最大堆的实现，参考的是《Algorithm》中priority queue章节

注意一下堆排序，包含建堆与调整堆的过程

其实跟堆没太大关系，只是借用了堆的思想，全程无需swim函数，只需至上而下的调整即可。

###Source Code

```cpp
#include<iostream>
using namespace std;

class MaxPQ {
public:
    MaxPQ(int maxN);
    ~MaxPQ();
    bool isEmpty();
    int size();
    void insert(int value);
    int delMax();
private:
    int * pq;
    int N;
    void exch(int i, int j);
    void swim(int k);
    void sink(int k);
};

MaxPQ::MaxPQ(int maxN):pq(NULL),N(0){
    this->pq = new int [maxN+1];
    this->N = 0;
}

MaxPQ::~MaxPQ(){
    if(pq != NULL) delete [] pq;
}

void MaxPQ::exch(int i, int j){
    swap(this->pq[i], this->pq[j]);
}

int MaxPQ::size(){
    return N;
}

bool MaxPQ::isEmpty(){
    return !(this->size()>0);
}

void MaxPQ::swim(int k){
    while(k/2>0 && this->pq[k]>this->pq[k/2]){
        this->exch(k, k/2);
        k = k/2;
    }
}

void MaxPQ::sink(int k){
    while(2*k <= N){
        int curmax = 2*k;
        if(2*k+1 <=N && this->pq[2*k] < this->pq[2*k+1]){
            curmax = 2*k+1;
        }
        if (this->pq[k] > this->pq[curmax]) break;
        this->exch(k, curmax);
        k = curmax;
    }
}

void MaxPQ::insert(int value){
    this->pq[++N] = value;
    swim(N);
}

int MaxPQ::delMax(){
    if (this->isEmpty()) return -1;
    int curmaxval = pq[1];
    this->exch(1, N--);
    sink(1);
    return curmaxval;
}


class HeapSort{
public:
    static void heapsort(int array[], int len){
        for(int i=len/2; i>=1; i--){
            sink(array, i, len);
        }
        while(len>0){
            swap(array[1], array[len]);
            len--;
            sink(array, 1, len);
        }
    }
    static void sink(int array[], int k, int N){
        while(2*k <= N){
            int curmax = 2*k;
            if(2*k+1 <=N && array[2*k] < array[2*k+1]){
                curmax = 2*k+1;
            }
            if (array[k] > array[curmax]) break;
            swap(array[k], array[curmax]);
            k = curmax;
        }
    }
};


int main(){
    MaxPQ mpq(100);
    int arr[] = {2,1,3,0,8,1,6,9,7};
    int len = sizeof(arr) / sizeof(int);
    for(int i=0; i<len; i++){
        mpq.insert(arr[i]);
    }

    while(!mpq.isEmpty()){
        cout<<mpq.delMax()<<endl;
    }
    len --;
    HeapSort::heapsort(arr, len);
    for(int i=1; i<=len; i++){
        cout<<arr[i]<<endl;
    }
    return 0;
}
```

