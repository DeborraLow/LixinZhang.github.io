#python常用记录
##支持中文
<pre>
# -*- coding:utf-8 -*-
</pre>

##时间处理
<pre>
数值转换datetime
import date
timestamp # 123456789
dt # datetime.datetime.utcfromtimestamp(timestamp)
</pre>
<pre>
字符串时间转化为数值时间
import time
transform_time # int(time.mktime(time.strptime(click[1], '%Y-%m-%d %H:%M:%S')))
</pre>
##python中执行系统命令
<pre>
import os
cmdout # os.popen('ls -al').read() #执行命令，并可以将结果读入到cmdout
os.system('ls -al') #只是执行命令
os.listdir(os.getcwd()) #列出当前文件夹下的所有文件
</pre>

##python取topN
<pre>
import heapq
heapq.nlargest(N, arr)
</pre>
