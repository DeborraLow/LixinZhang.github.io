# Online Judge

##Cut the tree
###题目
[https://www.hackerrank.com/challenges/cut-the-tree](https://www.hackerrank.com/challenges/cut-the-tree)

大概意思的一棵树，剪断一个边，分开的两棵树中差值最小为多少。

###Solution
深度遍历，求以各个结点为根时的子树权重和。 然后砍断一个边，即求解min(res, abs(v[i] - abs(v[0]-v[i])));

###Source Code
```cpp
#include<iostream>
#include<vector>
using namespace std;

int abs(int a, int b){
    return max(a,b) - min(a,b);
}

int solution(vector<vector<int> > &tree, vector<int> & root,
              vector<bool> & visited, vector<int> & v, int num){
    if(root.size() == 0 || visited[num] == true) {
        return 0;
    }
    visited[num] = true;
    for(int i=0; i<root.size(); i++){
        v[num] += solution(tree, tree[root[i]], visited, v, root[i]);
    }
    return v[num];
}

int main(){
    int N, tmp, n1, n2;
    cin >> N;
    vector<vector<int> > tree(N);
    vector<int> v;
    vector<bool> visited;
    for(int i=0; i<N; i++){
        cin >> tmp;
        v.push_back(tmp);
        visited.push_back(false);
    }
    for(int i=0; i<N-1; i++){
        cin >> n1 >> n2;
        tree[n1-1].push_back(n2-1);
        tree[n2-1].push_back(n1-1);
    }
    solution(tree, tree[0], visited, v, 0);
    int res = 90000000;
    for(int i=1; i<N; i++){

        res = min(res, abs(v[i] - abs(v[0]-v[i])));
    }
    cout<<res<<endl;
    return 0;
}
```
