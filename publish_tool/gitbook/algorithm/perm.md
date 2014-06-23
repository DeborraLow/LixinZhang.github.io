# Permutation

##求所有的全排列
[https://oj.leetcode.com/problems/permutations/](https://oj.leetcode.com/problems/permutations/)

最基本的solution：

```cpp
class Solution {
public:
//Note:Compute all perms of a global array by exchanging each element to the end, then recursively permuting the others
    vector<vector<int> > permute(vector<int> &num) {
        vector<vector<int> > finalres;
        dfs(finalres, num, num.size());
        return finalres;
    }
    void dfs(vector<vector<int> > &finalres, vector<int> &num, int N){
        if (N==0) {
            finalres.push_back(num);
            return;
        }
        for(int i=0; i<N; i++){
            swap(num[i], num[N-1]);
            dfs(finalres, num, N-1);
            swap(num[i], num[N-1]);
        }

    }
};
```

##求某一排列的下一个排列next_permutation
[https://oj.leetcode.com/problems/next-permutation/](https://oj.leetcode.com/problems/next-permutation/)

STL中有标准函数调用接口，有标准的解决方法：
STL next_perm 标准算法？

1. 从右往左找第一个破坏递增循序的位置i
2. 从右往左找第一个比位置i大的位置j
3. swap(s[i],s[j])
4. reverse(i+1,n)

同理可求prev_permutation。

```cpp
class Solution {
public:
    void reverse(int start, vector<int> &num){
        int end = num.size() - 1;
        while(start<end){
            swap(num[start], num[end]);
            start++;
            end--;
        }
    }
    void nextPermutation(vector<int> &num) {
        int tmp = -9999;
        int p = num.size() - 1;
        while(p >= 0 && num[p] >= tmp){
            tmp = num[p];
            p--;
        }
        if(p < 0){
            reverse(0, num);
            return;
        }
        int p2 = num.size()-1;
        while(p2>=0 && num[p2] <= num[p]){
            p2 --;
        }
        swap(num[p2], num[p]);
        reverse(p+1, num);
    }
};

```



##包含重复元素的全排列
[https://oj.leetcode.com/problems/permutations-ii](https://oj.leetcode.com/problems/permutations-ii/)

借用next_permutation的实现。

```cpp
//利用前一道题目中的next_perm方法

class Solution {
public:
    vector<vector<int> > permuteUnique(vector<int> &num) {
        vector<vector<int> > res;
        sort(num.begin(), num.end());
        res.push_back(num);
        while(nextPermutation(num)){
            res.push_back(num);
        }
        return res;
    }

   void reverse(int start, vector<int> &num){
        int end = num.size() - 1;
        while(start<end){
            swap(num[start], num[end]);
            start++;
            end--;
        }
    }
    bool nextPermutation(vector<int> &num) {
        int tmp = -9999;
        int p = num.size() - 1;
        while(p >= 0 && num[p] >= tmp){
            tmp = num[p];
            p--;
        }
        if(p < 0){
            //reverse(0, num);
            return false;
        }
        int p2 = num.size()-1;
        while(p2>=0 && num[p2] <= num[p]){
            p2 --;
        }
        swap(num[p2], num[p]);
        reverse(p+1, num);
        return true;
    }
};
```

##求第k个permutation
[https://oj.leetcode.com/problems/permutation-sequence/](https://oj.leetcode.com/problems/permutation-sequence/)

```cpp

//不能有传统的perm方法解，找规律，可以不断缩小规模，更新起始index

class Solution {
public:
	string getPermutation( int n, int k )
	{
		string	s( n, '0' );
		string	result;
		for ( int i = 0; i < n; ++i )
			s[i] += i + 1;
		return(kth_permutation( s, k ) );
	}


private:
	int factorial( int n )
	{
		int result = 1;
		for ( int i = 1; i <= n; ++i )
			result *= i;
		return(result);
	}


	string kth_permutation( const string &seq, int k )
	{
		const int	n = seq.size();
		string		S( seq );
		string		result;
		int		base = factorial( n - 1 ); --k; /* 康托编码从 0 开始 */
		for ( int i = n - 1; i > 0; k %= base, base /= i, --i )
		{
			auto a = next( S.begin(), k / base );
			result.push_back( *a );
			S.erase( a );
		}
		result.push_back( S[0] );                       /* 最后一个 */
		return(result);
	}
};

```

