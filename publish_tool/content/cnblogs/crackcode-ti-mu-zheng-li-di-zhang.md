Title: CrackCode 题目整理 （第一章）
Date: 2013-03-24 11:35
Author: 糖拌咸鱼
Slug: crackcode-ti-mu-zheng-li-di-zhang

[CrackCode Interview 书籍链接地址][]

</p>

/\*  
\* Chapter 1   
\* Question: Implement an algorithm to determine if a string has all
unique characters.   
\* What if you can not use addtional data structures?  
\* 实现一个算法用于判断一个字符串所包含的所有字符是各不相同的。  
\* 尽量不使用额外空间  
\*/

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>using namespace std;/* * 假设为ASCII编码，字符数值范围为0~255，因此开设256大小的bool数据进行记录 */bool solution1(const char * str){    bool exist[256] = {false};    while(*str != '\0'){        if (exist[*str] == true) return false;         exist[*str] = true;        str++;    }    return true;}/* * 上述解法，浪费了空间，因为对应每个字符只有0和1两个状态，可以用bit来记录 * 因此可以开设8*32的bit空间，用位操作解决问题 */struct char_set{    int arr[8]; // 32bit * 8 = 256bit    char_set(){        for(int i=0;i<8;i++) arr[i] = 0;    }};bool solution2(const char * str) {    char_set charset;    int one = 1;    while(*str != '\0'){        int index = (*str) / 32;        int position = (*str) % 32;        if ((charset.arr[index] & (one << position)) > 0) return false;        charset.arr[index] |= (one << position);        str ++;    }    return true;}/* *如果完全不是用额外空间，可以考虑使用排序，然后从头到尾遍历一下即可。时间复杂度O(nlogn) */int main(){    char str [] = "zhangli";    char str2 [] = "zhanglixin";    cout<<solution1(str)<<endl;    cout<<solution2(str)<<endl;    cout<<solution1(str2)<<endl;    cout<<solution2(str2)<<endl;    return 0;}

</p>
<p>

</div>

</p>

/\*  
\* Chapter 1.2  
\* Question:Write code to reverse a c-Style String,  
\* (C-style means that "abcd" is represented as five
characters,including the null character)  
\* 反转字符串  
\*/

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>#include<string.h>using namespace std;/* * 两种考虑，如果可以使用strlen函数，则可以省略找最后一个字符的工作 * 否则，需要自己写 */void solution(char * str){    int len = strlen(str);    int i = 0;    char temp;    while(i < len/2){        temp = str[i];        str[i] = str[len-i-1];        str[len-i-1] = temp;        i++;    }}void solution2(char * str) {    char * end = str;    char temp;    while(*end != '\0'){        end ++;    }    end --;    while(str < end){        temp = *str;        *str = *end;        *end = temp;        str++;        end--;    }}int main(){    char s1[] = "hello world";    char s2[] = "1234567890";    solution(s1);    solution2(s2);    cout<<s1<<endl;    cout<<s2<<endl;    return 0;}

</p>
<p>

</div>

</p>

/\*  
\* Chapter 1.3  
\* Question:Design an algorithm and write code to remove the
duplication characters in a string  
\* without using any addtional buffer. NOTE:One or two addtional
variables are fine.  
\* An extra copy of the array is not.  
\* FOLLOW UP  
\* Write the test cases for this method.  
\*
设计一个算法，用来移除一个字符串中重复的字符，并且不允许使用任何额外的空间（少量变量可以）  
\* 不允许额外的拷贝  
\* 接下来，为这个方法写一些测试用例  
\*/

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>#include<string.h>using namespace std;/* * 由于不允许使用额外空间，导致不能用1.1中类似的方法判断是否重复 * 因此，采用遍历枚举的方式，方法如下： * 对于str[i]，枚举0～tail之间是否已存在该元素，其中0到tail之间字符不重复 * 如果存在，则跳过，否则str[tail]更新为新元素str[i] */void solution(char * str){    if (str == NULL) return ;    int len = strlen(str);    int tail = 1;    int j;    for(int i=1;i<len;i++){        for(j=0;j<tail;j++){            if (str[i] == str[j]) break;        }        if(j == tail) {            str[tail] = str[i];            tail++;        }    }    str[tail] = '\0';}/* * Test Cases: * 1. 不包含任何重复字符 abcd * 2. 所有的字符均重复 aaaa * 3. NULL * 4. 连续重复的字符串，如aaabbb * 5. 非连续重复的字符串 abcabcddeef */int main(){    char s [] = "abcdeagsdgabc";    solution(s);    cout<<s<<endl;    return 0;}

</p>
<p>

</div>

</p>

/\*  
\* Chapter 1.4  
\* Question: Write a method to decide if two strings are anagrams or
not .  
\* 判断两个字符串是否为易位够词，即排序之后相同的两个词  
\* http://en.wikipedia.org/wiki/Anagram  
\*/

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>#include<algorithm>#include<string.h>using namespace std;/* * 通过抽象定义,直接對两个string进行排序，然后判断下就可以了 * 时间复杂度O(nlogn) */bool solution(char * s1, char * s2){    sort(s1,s1+strlen(s1));    sort(s2,s2+strlen(s2));    int cmp = strcmp(s1,s2);    if( cmp == 0) return true;    return false;}/* * 由于方法1具有数据侵入性，即改遍了s1和s2中原有的数据位置，因此不是很好的解决办法。 * 利用空间换时间，用char_count统计s1中每个字符出现的次数 * 然后遍历s2中的每个字符，對char_count进行更新，即对应的char_count减1 * 如果某个字符对应的char_count减为-1,则判定为false * 若字符数不相等也判定为false */bool solution2(char * s1, char * s2){    int char_count[256] = {0};    int len1=0,len2=0;    while(*s1 != '\0') {        char_count[*s1] ++;        s1++;        len1++;    }    while(*s2 != '\0') {        char_count[*s2] --;        if(char_count[*s2] < 0) return false;        s2++;        len2++;    }    if(len1 != len2) return false;    return true;}int main(){    char s1 [] = "hello";    char s2 [] = "lloeh";    cout<<solution(s1,s2);    cout<<solution2(s1,s2);    return 0;}

</p>
<p>

</div>

</p>

/\*  
\* Chapter 1.5  
\* Question:Write a method to replace all spaces in a string with
'%20'  
\* 写一个方法用'%20'替换字符串中的所有空格  
\*/

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>#include<string.h>using namespace std;/* * 这应该算是比较典型的字符串移位的问题 * 首先，如果我们知道了字符串中包含的space数量count，那么替换后的最终长度比原始长度增加了count*2 * 在进行替换过程中，如果从头开始替换，势必在替换过程中，需要對后面的字符进行位置移动，显然这是开销很大的。 * 由于我们已经知道了替换后的最终长度，那么便可以从后往前进行替换，这样不会對前面的字符产生影响。 * 另外，由于字符串的最终长度增加了，那么在原有内存上进行操作，可能会造成字符串的访问越界。 * 因此，最好的方法应该时新建一个string，再返回，这样的话，就无所谓替换的顺序了。 */void solution(char * str){    //我们假设str申请的空间很大，不会产生越界问题    int count = 0;    int len = 0;    char * pstr = str;    while(*pstr != '\0'){        if (*pstr == ' ') count++;        len ++;        pstr++;    }    int final_len = len + 2 * count;    str[final_len] = '\0';    int pos = final_len - 1;    int j = len - 1;    while(j>=0){        if(str[j] != ' ') str[pos--] = str[j];        else{            str[pos - 2] = '%';            str[pos - 1] = '2';            str[pos] = '0';            pos -=3;        }        j--;    }}int main(){    char str [100];    strcpy(str," hello world python ");    solution(str);    cout<<str<<endl;    return 0;}

</p>
<p>

</div>

</p>

/\*  
\* Write an algorithm such that if an element in an M\*N matrix is 0,
its entire row and column is set to 0.  
\*
写一个算法用于实现如果一个M\*N的矩阵中某个元素为0.则将该行和该列所有元素设置为0  
\*/

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>using namespace std;/* * 由于，不能在查找0的时候，进行相应行和列的更新0，因为这样会导致整个矩阵变为0矩阵了 * 那么就需要记录每个0的位置，然后再统一进行行和列的0替换 * 方法1：开两个数组row[i],column[j]，记录第i行与第j列是否为0 * 方法2：建立一个struct，记录row 和 column，用链表形式记录，这样可以最小化存储空间 * 方法3：num = row*MAXCOLUMN + column的方式进行0元素的位置存储 */void solution(int arr[][3], int maxcolumns, int maxrows) {    bool * row = new bool[maxrows];     bool * column = new bool[maxcolumns];    for(int i=0;i<maxrows;i++){        for(int j=0;j<maxcolumns;j++){            if(arr[i][j] == 0){                row[i] = true;                column[i] = true;            }        }    }    for(int i=0;i<maxrows;i++){        for(int j=0;j<maxcolumns;j++){            if(row[i] | column[j]) arr[i][j] = 0;        }    }}int main(){    int arr[3][3] = {{1,2,3},{4,0,6},{7,8,9}};    solution(arr,3,3);    int maxrows = 3;    int maxcolumns = 3;    for(int i=0;i<maxrows;i++){        for(int j=0;j<maxcolumns;j++){            cout<<arr[i][j]<<'\t';        }        cout<<endl;    }       return 0;}

</p>
<p>

</div>

</p>

/\*  
\* Chapter 1.8  
\* Question:Assume you have a method isSubstring which checks if one
word is substring of   
\* another. Given two strings s1 and s2, write code to check if s2 is a
rotation of s1 using  
\* only one call to isSubString(i.e."waterbottle" is a rotation of
"erbottlewat")  
\*
假设你有一个方法可以用来检测一个单词是否为一个另一个的子串。现在给你两个字符串并且只能进行一次substring的调用，判断s2是否为s1的转动形式。  
\*/

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>#include<string.h>#include<assert.h>using namespace std;bool isSubstring(const char * s1, const char * s2){    assert(s1 != NULL && s2 != NULL);    return strstr(s1,s2) == NULL ? false : true;}/* * 首先应该检查s1与s2的长度，如果不想等，则直接判定为false * 对于字符串s1，s1s1则包含了s1转动后的所有形式，因此只要用isSubstring判断s2是否为s1s1的子串即可 */bool solution(const char * s1, const char * s2){    int len1 = strlen(s1);    int len2 = strlen(s2);    if(len1 != len2) return false;    char * temp = new char[len1*2];    strcpy(temp,s1);    strcpy(temp+len1,s1);    bool res = isSubstring(temp,s2);    delete [] temp;    return res;}int main(){    char s1 [] = "waterbottle";    char s2 [] = "erbotdlewat";    cout<<solution(s1,s2)<<endl;}

</p>
<p>

</div>

</p>

 

</p>

 

</p>

 

</p>

  [CrackCode Interview 书籍链接地址]: http://ishare.iask.sina.com.cn/f/21821712.html
