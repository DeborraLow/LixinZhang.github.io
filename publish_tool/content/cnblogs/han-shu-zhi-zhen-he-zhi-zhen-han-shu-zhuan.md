Title: 函数指针和指针函数（转）
Date: 2011-03-10 07:49
Author: 糖拌咸鱼
Slug: han-shu-zhi-zhen-he-zhi-zhen-han-shu-zhuan

<span size="2" style="font-size: x-small;"><span color="#0000ff"
style="color: #0000ff; font-size: 14pt;">【函数指针】</span>  
  
      
在程序运行中，函数代码是程序的算法指令部分，它们和数组一样也占用存储空间，都有相应的地址。可以使用指针变量指向数组的首地址，也可以使用指针变量指向函数代码的首地址，指向函数代码首地址的指针变量称为函数指针。</span>

</p>

<span size="2" style="font-size: x-small;">1．函数指针定义</span>

</p>

<span size="2" style="font-size: x-small;">函数类型
（\*指针变量名）(形参列表)；</span>

</p>

<span size="2"
style="font-size: x-small;">“函数类型”说明函数的返回类型，由于“()”的优先级高于“\*”,所以指针变量名外的括号必不可少，后面的“形参列表”表示指针变量指向的函数所带的参数列表。</span>

</p>

<span size="2" style="font-size: x-small;">例如：</span>

</p>

<span size="2" style="font-size: x-small;">int (\*f)(int x);</span>

</p>

<span size="2" style="font-size: x-small;">double (\*ptr)(double
x);</span>

</p>

<span size="2" style="font-size: x-small;">在定义函数指针时请注意：  
      
函数指针和它指向的函数的参数个数和类型都应该是—致的；</span>

</p>

<span size="2"
style="font-size: x-small;">函数指针的类型和函数的返回值类型也必须是一致的。</span>

</p>

<span size="2" style="font-size: x-small;">2．函数指针的赋值</span>

</p>

<span size="2"
style="font-size: x-small;">函数名和数组名一样代表了函数代码的首地址，因此在赋值时，直接将函数指针指向函数名就行了。</span>

</p>

<span size="2" style="font-size: x-small;">例如，</span>

</p>

<span size="2" style="font-size: x-small;">int func(int x);   /\*
声明一个函数 \*/</span>

</p>

<span size="2" style="font-size: x-small;">int (\*f) (int x);    /\*
声明一个函数指针 \*/</span>

</p>

<span size="2" style="font-size: x-small;">f=func;            /\*
将func函数的首地址赋给指针f \*/</span>

</p>

<span size="2"
style="font-size: x-small;">赋值时函数func不带括号，也不带参数，由于func代表函数的首地址，因此经过赋值以后，指针f就指向函数func(x)的代码的首地址。</span>

</p>

<span size="2"
style="font-size: x-small;">3．通过函数指针调用函数</span>

</p>

<span size="2"
style="font-size: x-small;">函数指针是通过函数名及有关参数进行调用的。</span>

</p>

<span size="2"
style="font-size: x-small;">与其他指针变量相类似，如果指针变量pi是指向某整型变量i的指针，则\*p等于它所指的变量i；如果pf是指向某浮点型变量f的指针，则\*pf就等价于它所指的变量f。同样地，\*f是指向函数func(x)的指针，则\*f就代表它所指向的函数func。所以在执行了f=func;之后，(\*f)和func代表同一函数。</span>

</p>

<span size="2"
style="font-size: x-small;">由于函数指针指向存储区中的某个函数，因此可以通过函数指针调用相应的函数。现在我们就讨论如何用函数指针调用函数，它应执行下面三步：</span>

</p>

<span size="2"
style="font-size: x-small;">首先，要说明函数指针变量。</span>

</p>

<span size="2" style="font-size: x-small;">例如：int (\*f)(int
x);</span>

</p>

<span size="2"
style="font-size: x-small;">其次，要对函数指针变量赋值。</span>

</p>

<span size="2" style="font-size: x-small;">例如： f=func;   
(func(x)必须先要有定义)</span>

</p>

<span size="2" style="font-size: x-small;">最后，要用
(\*指针变量)(参数表);调用函数。</span>

</p>

<span size="2" style="font-size: x-small;">例如：   
(\*f)(x);(x必须先赋值)</span>

</p>

<span color="#0000ff" size="2"
style="color: #0000ff; font-size: 14pt;">【指针函数】</span>

</p>

<span size="2"
style="font-size: x-small;">一个函数不仅可以带回一个整型数据的值，字符类型值和实型类型的值，还可以带回指针类型的数据，使其指向某个地址单元。</span>

</p>

<span size="2" style="font-size: x-small;">       
返回指针的函数，一般定义格式为：</span>

</p>

<span size="2" style="font-size: x-small;">        类型标识符   
\*函数名(参数表)</span>

</p>

<span size="2" style="font-size: x-small;">int \*f(x，y);</span>

</p>

<span size="2"
style="font-size: x-small;">其中x，y是形式参数，f是函数名，调用后返回一个指向整型数据的地址指针。f(x，y)是函数，其值是指针。</span>

</p>

<span size="2" style="font-size: x-small;">通过分析可得</span>

</p>

<span size="2"
style="font-size: x-small;">函数指针是一个指向函数的指针，而指针函数只是说明他是一个返回值为指针的函数，</span>

</p>

<span size="2"
style="font-size: x-small;">函数指针可以用来指向一个函数。</span>

</p>

<span size="2" style="font-size: x-small;">  
</span>

</p>

