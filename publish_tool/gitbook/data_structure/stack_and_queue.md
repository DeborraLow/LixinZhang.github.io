# Stack and Queue

##Sort stack
###Description
用一个辅助栈，来sort一个原始stack，复杂度为O(n^2);
CrackTheInterview 3.6

###Solution
```cpp
void stackSort(stack<int> & sta){
    stack<int> helper;
    while(!sta.empty()){
         if(helper.empty() || helper.top() >= sta.top()){
            helper.push(sta.top());
            sta.pop();
         }else{
             int tmp = sta.top();
             sta.pop();
             while(!helper.empty()){
                 sta.push(helper.top());
                 helper.pop();
             }
             helper.push(tmp);
         }
    }
    while(!helper.empty()){
        sta.push(helper.top());
        helper.pop();
    }
}
```
