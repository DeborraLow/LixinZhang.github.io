Title: gtest 安装
Date: 2013-07-24 13:23
Author: 糖拌咸鱼
Slug: gtest-an-zhuang

<span style="line-height: 1.5;">1、下载，</span><span
style="line-height: 1.5;">https://code.google.com/p/googletest/。</span><span
style="line-height: 1.5;">解压，进入该目录，按REAME说明</span>

</p>

<span style="line-height: 1.5;">安装：1.5之前 make
install可以安装，1.6之后不可以。。。安装可按README里的提示进行安装：</span>

</p>

a、g++ -I./include -I./ -c ./src/gtest-all.cc
（注意，-I后没有空格，直接加./）

</p>

b、ar -rv libgtest.a gtest-all.o

</p>

这步之后会生成两个文件，libgtest.a和gtest-all.o

</p>

4、g++ -I./include mytest.cpp libgtest.a -o mytest -lpthread

</p>

（注意mytest为自己写的简单测试代码，编译时注意加-lpthread,因为gtest是多线程的，不然编译会报错：undefined
reference to ...）

</p>

