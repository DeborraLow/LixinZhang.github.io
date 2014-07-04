# Linked List
##判断一个链表是不是Palindrome？
```cpp
struct LinkedNode {
    char value;
    LinkedNode * next;
    LinkedNode(char v){
        value = v;
        next = NULL;
    }
    LinkedNode(){next = NULL;}
};

bool isPalindrome(LinkedNode * head, LinkedNode * &cur){
    if (head == NULL) return true;
    bool flag = isPalindrome(head->next, cur);
    if (flag && cur->value == head->value){
        cur = cur->next;
        return true;
    }
    return false;
}

bool isPalindrome(LinkedNode * head){
    LinkedNode * cur = head;
    return isPalindrome(head, cur);
}
```
