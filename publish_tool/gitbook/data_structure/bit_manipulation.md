# Bit manipulation


##Basic operation

1. 得到某个位置是否为1
2. 设置一个num的第i个位置的值1
3. 将num的第i个位置清0
4. 将从最高有效位的到位置i，均清0
5. 将从位置i到位置0，均清0



```cpp
bool getBit(int num, int i){
    return (num & (1<<i)) != 0;
}

int setBit(int num, int i){
    return num | (i<<i);
}

int clearBit(int num, int i){
    return num & (~(1<<i));
}

int clearBitMSBThroughI(int num, int i){
    int mask = (1<<i) - 1;
    return num & mask;
}

int clearBitsIthrough0(int num, int i){
    int mask = ~((1<<(i+1)) - 1);
    return num & mask;
}
```
