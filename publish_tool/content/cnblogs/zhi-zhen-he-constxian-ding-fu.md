Title: 指针和const限定符
Date: 2011-02-23 01:35
Author: 糖拌咸鱼
Slug: zhi-zhen-he-constxian-ding-fu

<div class="cnblogs_code">

</p>
<p>
    #include<iostream> using namespace std; int main() {     const int max=100;     const int min=-100;     //C++语言强制要求指向const对象的指针也必须具有const特性     //指向const对象的指针     //虽然指向的是const的值，但是指针本身并不是const的，所以指针仍然可以改变其值(地址值)，指针所指向的对象则不可以改变     const int * ptr=&max;      ptr=&min;// it is ok     //*ptr=10; it is wrong，指向的是const值，所以不可以改变值          //const指针，说明指针本身的值不可以改变，但是所指向的值如果不是const ，就可以改变     int number=100;     int *const ptr2=&number;      *ptr2=101;      cout<<*ptr2<<endl;     //指向const对象的const指针，一旦这样定义后，既不可以修改该指针的值，也不可以修改指针所指向的值     const int score = 100;     const int *const   ptr3=&score;     return 0; }

</p>
<p>

</div>

</p>

