Title: explicit作用
Date: 2011-02-25 08:27
Author: 糖拌咸鱼
Slug: explicitzuo-yong

**explicit作用:**  
在C++中，explicit关键字用来修饰类的构造函数，被修饰的构造函数的类，不能发生相应的隐式类型转换，只能以显示的方式进行类型转换。

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<iostream>using namespace std;class Test{public:    explicit Test(int a)//构造函数加explicit修饰，不允许发生隐式类型装换    {        number=a;    }private:    int number;};int main(){    Test test(10);//这样总是对的    Test test2=10;//当构造函数加入explicit修饰时，程序将会编译不通过    return 0;}

</p>
<p>

</div>

</p>

