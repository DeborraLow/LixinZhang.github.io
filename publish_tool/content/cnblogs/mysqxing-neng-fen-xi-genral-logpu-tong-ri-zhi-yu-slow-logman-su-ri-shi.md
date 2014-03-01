Title: Mysq性能分析 —— Genral log（普通日志）与 Slow log（慢速日式）
Date: 2011-11-08 13:06
Author: 糖拌咸鱼
Slug: mysqxing-neng-fen-xi-genral-logpu-tong-ri-zhi-yu-slow-logman-su-ri-shi

      
 对Mysql进行深入的分析对于发现mysql性能瓶颈和寻找优化策略是十分必要的。
我们可以从不同的粒度上对Mysql进行分析：可以整体分析服务器，或者检查单个查询或批查询。  
通过分析，我们得到的如下信息：  
1、Mysql访问得最多的数据  
2、Mysql执行得最多的查询的种类  
3、Mysql停留时间最长的状态  
4、Mysql用来执行查询的使用得最频繁的子系统  
5、Mysql查询过程中访问的数据种类  
6、Mysql执行了多少种不同类型的活动，比如索引扫描。

</p>

Mysql提供了两种查询日志，它们可以为我们获取以上信息提供帮助。
这两种查询日志为**普通日志（general log）**和**慢速日志（slow log）**。

</p>

  
**<span style="font-size: 16px;">General log：</span>**  
Geleral
log记录了服务器接收到的每一个查询或是命令，无论这些查询或是命令是否正确甚至是否包含语法错误，general
log 都会将其记录下来 ，记录的格式为 {Time ，Id ，Command，Argument
}。也正因为mysql服务器需要不断地记录日志，开启General
log会产生不小的系统开销。 因此，Mysql默认是把General log关闭的。
我们可以通过修改Mysql全局变量来开启General log功能或是更改日志存放路径。
  
<span
style="color: #ff0000;">**注意：**</span>mysql5.0版本，如果要开启slow
log、general log，需要重启，从MySQL5.1.6版开始，general query log和slow
query
log开始支持写到文件或者数据库表两种方式，并且日志的开启，输出方式的修改，都可以在Global级别动态修改。

</p>

1、首先查看log\_output，确认日志输出到文件还是数据库。  
<span style="color: #000080;">mysql\> show variables like
'log\_output';</span>  
<span style="color: #000080;">+-------------------+-------+</span>  
<span style="color: #000080;">| Variable\_name | Value |</span>  
<span style="color: #000080;">+-------------------+-------+</span>  
<span style="color: #000080;">| log\_output       |  FILE |</span>  
<span style="color: #000080;">+-------------------+-------+</span>  
<span style="color: #000080;">1 row in set (0.00 sec)</span>  
通过以上结果可以发现，log\_output的值为FILE,证明是输出到日志文件，如果为TABLE则输出到默认‘mysql’数据库中的相应日志表，该表的默认引擎为CSV。

</p>

2、接下来通过如下命令可以查看 mysql默认的 General log 配置。  
<span style="color: #000080;">mysql\> show global variables like
'%general%';</span>  
<span
style="color: #000080;">+------------------+---------------------------+</span>  
<span style="color: #000080;">| Variable\_name | Value |</span>  
<span
style="color: #000080;">+------------------+---------------------------+</span>  
<span style="color: #000080;">| general\_log | OFF |</span>  
<span style="color: #000080;">| general\_log\_file |
/var/lib/mysql/ubuntu.log |</span>  
<span
style="color: #000080;">+------------------+---------------------------+</span>  
<span style="color: #000080;">2 rows in set (0.00 sec)</span>  
general\_log的值为OFF,所以当前general\_log是关闭的。general\_log\_file变量的值是日志文件的路径。  
3、通过 set global general\_log = on; 命令开启General log。  
4、最后我们可以从/var/lib/mysql/ubuntu.log文件中查看相应日志信息。

</p>

<span style="font-size: 16px;">**Slow log：**</span>  
General
log日志内容比较简单，不包含执行时间或其他只有在查询结束之后才能得到的信息，相反，slow
log 记录了这些内容。  
1、我们首先来看一下与慢日志相关的全局变量。  
<span style="color: #000080;">mysql\> show global variables like
'%slow%';</span>  
<span
style="color: #000080;">+---------------------+--------------------------------+</span>  
<span style="color: #000080;">| Variable\_name | Value |</span>  
<span
style="color: #000080;">+---------------------+--------------------------------+</span>  
<span style="color: #000080;">| log\_slow\_queries | ON |</span>  
<span style="color: #000080;">| slow\_launch\_time | 2 |</span>  
<span style="color: #000080;">| slow\_query\_log | ON |</span>  
<span style="color: #000080;">| slow\_query\_log\_file |
/var/lib/mysql/ubuntu-slow.log |</span>  
<span
style="color: #000080;">+---------------------+--------------------------------+</span>  
<span style="color: #000080;">4 rows in set (0.00 sec)</span>  
笔者的mysql已经开启了慢日志选项。变量slow\_launch\_time的值代表着捕获所有执行时间超过2秒的查询。slow
log可以记录没有使用索引的查询，它也能记录执行速度比较慢的管理命令。  
开启log\_queries\_not\_using\_indexes，将会记录没有使用索引的查询到slow日志里。  
<span style="color: #000080;">mysql\> show global variables like
'%not\_using%';</span>  
<span
style="color: #000080;">+-------------------------------+-------+</span>  
<span style="color: #000080;">| Variable\_name | Value |</span>  
<span
style="color: #000080;">+-------------------------------+-------+</span>  
<span style="color: #000080;">| log\_queries\_not\_using\_indexes | OFF
|</span>  
<span
style="color: #000080;">+-------------------------------+-------+</span>  
<span style="color: #000080;">1 row in set (0.00 sec)</span>

</p>

slow log 的日志格式为：  
\# Time: 111108 19:38:00  
\# User@Host: root[root] @ localhost []  
\# Query\_time: 15.268541 Lock\_time: 0.000237 Rows\_sent: 1
Rows\_examined: 102  
use mytest;  
SET timestamp=1320752280;  
select count(a.b) from mytable a ,mytable b ,mytable c ,mytable d;

</p>

慢速日志的确提供了很多有用的信息，但是不代表出现的查询一定一直都是慢的。如果同样的查询在慢速日志里出现了多次，那么它的确需要优化，但是如果只是出现了偶尔一两次，则有可能是其他客观原因造成的，比如某些锁，I/O磁盘物理性问题，网络问题等等。  
慢速日志的slow\_launch\_time的时间单位为秒，可以通过网上第三方补丁将其更改为毫秒级，用于更加精细的日志记录和分析，但是这需要重新编译mysql。

</p>

我们通常在日志中查找下面几个信息：长查询、影响比较大的查询和新查询。这可能需要我们自己写一下脚本或是借助某些第三方工具进行日志分析。
  
General log 系统开销比较大，一般不建议开启。

</p>

 

</p>

