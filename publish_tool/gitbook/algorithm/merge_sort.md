# merge sort
###Basic
####source code
```cpp
#include<iostream>
using namespace std;

void merge(int arr[], int tmp[], int low, int mid, int high){
    int i = low, j = mid+1;
    int idx = low;
    while(i<=mid && j<=high){
        if (arr[i] < arr[j]){
            tmp[idx++] = arr[i++];
        }else{
            tmp[idx++] = arr[j++];
        }
    }
    while(i<=mid) tmp[idx++] = arr[i++];
    while(j<=high) tmp[idx++] = arr[j++];
    for(int i=low; i<=high; i++) arr[i] = tmp[i];
}

void merge_sort(int arr[], int tmp[], int low, int high){
    if (low >= high) return;
    int mid = (low + high) / 2;
    merge_sort(arr, tmp, low, mid);
    merge_sort(arr, tmp, mid+1, high);
    merge(arr, tmp, low, mid, high);
}

int main(){
    int arr[] = {2,1,3,0,8,1,6,9,7};
    int tmp[1000];
    merge_sort(arr, tmp, 0, sizeof(arr) / sizeof(int) -1);
    for(int i=0; i<sizeof(arr)/sizeof(int); i++){
        cout<<arr[i]<<endl;
    }
    return 0;
}
```
