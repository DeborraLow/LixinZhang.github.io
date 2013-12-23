#Linux知识点记录
##vim

####mac下iterm2 vim无法复制解决办法####
<pre>在.vimrc文件中设置set mouse#，但是这样会无法使用鼠标上下滑动的功能，
可以考虑在vim命令模式下执行，set mouse# </pre>

####vim替换####
<pre>
:[range]s/pattern/string/[c,e,g,i]

range	指的是範圍，1,7 指從第一行至第七行，1,$ 指從第一行至最後一行，也就是整篇文章，也可以 % 代表。
pattern	就是要被替換掉的字串，可以用 regexp 來表示。
string	將 pattern 由 string 所取代。
c	confirm，每次替換前會詢問。
e	不顯示 error。
g	globe，不詢問，整行替換。
i	ignore 不分大小寫。
样例  :%s/aaaa/bbbb
</pre>

####vim中输入ctrl A####
<pre>
ctrl v + ctrl a
例如替换操作，%s/ /ctrl v ctrl a, 将‘ ’替换为ctrl A，常用于字段分割的时候
</pre>

####vim中sort使用####
<pre>
假设有如下数据，以空格为数据列分割：
1  何维川   124.63     172  0.72
2  张子寅   99.67      172  0.58
3  周广滨   93.34      188  0.50
4  陈兴     41.86      188  0.22
5  薛永成   26.68      188  0.14
6  张永福   18.25      188  0.10
7  李华田   18.25      188  0.10
8  葛祥营   11.89      164  0.07
9  王天民   -16.55     156  -0.11
10 刘峰     -16.19     152  -0.11
11 郭居岗   -86.73     152  -0.57
12 杨军     -213.45    152  -1.40

如果我们想以第4列数据进行排序，可以在vim中如此做：
1，12!sort -r -n -k4.1,5

-r 是降序排序
-n 是按数字大小排序
-k,表示根据那个字段排序，4.1,表示第4列第一个字符开始 ，5表示到第5个字段为结束
-t 后面跟分隔符，缺省是空格
</pre>

##常用命令
###查找
<pre>
egrep : cat a.txt | egrep 'a|b|c' 查找出现a或b或c的行
find : find . -type f  | xargs grep aaa 查找当前目录下包含aaa内容的文件名及所在行信息
</pre>

###后台运行
<pre>
nohup command &
例如，启动一个httpserver用于传送文件之用：
nohup python -m SimpleHTTPServer 5566 &
</pre>
###软连接、硬链接
####软链接
<pre>
软连接又叫符号链接，这个文件包含了另一个文件的路径名，可以是任意文件或目录，可以链接不同文件系统的文件。
链接文件甚至可以链接不存在的文件，这就产生了一般称之为“断链”的现象，链接文件甚至可以循环链接自己。类似于编程中的递归。
命令：ln -s source_file softlink_file
在对符号文件进行读或写操作的时候，系统会自动把该操作转换为对源文件的操作，
但删除链接文件时，系统仅仅删除链接文件，而不删除源文件本身。
</pre>
####硬连接
<pre>
info ln 命令告诉您，硬链接是已存在文件的另一个名字(A "hard link" is another name for an existing file)，
这多少有些令人困惑。
命令: ln -d existfile newfile
硬链接文件有两个限制
　1)不允许给目录创建硬链接；
　2)、只有在同一文件系统中的文件之间才能创建硬链接。
  对硬链接文件进行读写和删除操作时候，结果和软链接相同。
但如果我们删除硬链接文件的源文件，硬链接文件仍然存在，而且保留了愿有的内容。
  这时，系统就“忘记”了它曾经是硬链接文件。而把他当成一个普通文件。
</pre>

###截取某文件i行到j行的数据
<pre>
 sed -n '1,26p' tanxcatTree.html > cutTree_head.html
</pre>

###grep及egerp使用
<pre>
egrep [正则表达式] 
egrep -v [正则表达式] 取反
充分利用管道机制，即cat file | grep 'aaa' | egrep -v 'b.*\\a?' | egrep 'ccc' | less
grep 含有特殊符号的字符串，如"\t"，可以使用perl style : grep -P "\taaa" 
</pre>

###查看某个文件的绝对路径
<pre>
<code>#!/bin/bash</code>
ls $1 | sed "s:^:`pwd`/: "
</pre>
