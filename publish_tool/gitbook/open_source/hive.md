# Hive
##基本操作
DDL:

<pre>
HiveQL DDL statements are documented here, including:
CREATE DATABASE/SCHEMA, TABLE, VIEW, FUNCTION, INDEX
DROP DATABASE/SCHEMA, TABLE, VIEW, INDEX
TRUNCATE TABLE
ALTER DATABASE/SCHEMA, TABLE, VIEW
MSCK REPAIR TABLE (or ALTER TABLE RECOVER PARTITIONS)
SHOW DATABASES/SCHEMAS, TABLES, TBLPROPERTIES, PARTITIONS, FUNCTIONS, INDEX[ES], COLUMNS, CREATE TABLE
DESCRIBE DATABASE, table_name, view_name
</pre>

###基本的创建表
<pre>
CREATE TABLE pokes (foo INT, bar STRING);
</pre>

###使用分区（partition）

####创建包含分区的表
<pre>
CREATE TABLE invites (foo INT, bar STRING) PARTITIONED BY (ds STRING);
</pre>
注意，partition 可以包含多个。

<code>Hive</code>将表组织为“分区”，根据“分区列”的值对表进行粗略的划分，使用分区可以加快数据分片(slice)的查询速度，但并不影响跨多分区的全局遍历。

可以使用<code>show partitions invites;</code>来查看某表中存在哪些分区。

####加载数据
<pre>
LOAD DATA LOCAL INPATH './examples/files/kv2.txt' OVERWRITE INTO TABLE invites PARTITION (ds='2008-08-15');
 LOAD DATA LOCAL INPATH './examples/files/kv3.txt' OVERWRITE INTO TABLE invites PARTITION (ds='2008-08-08');
</pre>

把数据加载到分区表的时候，必须显式指定分区值。 <code>OVERWRITE</code>用于覆盖原有值，如果不加这个关键字的话，会以<code>append</code>的方式添加进去。

<code>./examples/files/kv2.txt</code>数据格式如下：
<pre>
287^Aval_288
246^Aval_247
440^Aval_441
31^Aval_32
373^Aval_374
447^Aval_448
443^Aval_444
</pre>
原始数据中并不包含<code>ds</code>这个partition列，因此这些分区列源于目录名。我们可以check一下hdfs存放数据文件的路径，如下：
<pre>
-bash-4.1$ hadoop fs -ls /user/hive/warehouse/invites
Found 2 items
drwxr-xr-x   - zhanglx supergroup          0 2014-07-03 06:42 /user/hive/warehouse/invites/ds=2008-08-08
drwxr-xr-x   - zhanglx supergroup          0 2014-07-03 05:55 /user/hive/warehouse/invites/ds=2008-08-15
</pre>
发现，分区列(partition column)作为子目录来划分这些数据的。但是在查询过程中，无需关注这些，可以将分区列看做正式的列进行正常的操作，如：
<pre>
SELECT a.foo FROM invites a WHERE a.ds='2008-08-15';
</pre>


###使用桶（bucket）
使用桶的优势：

1. 获得更高的查询处理效率。
2. 使<code>sampling</code>更加有效。在处理大规模数据集时，在开发和修改查询的阶段，如果能自爱数据集的一小部分数据上运行查询，会很方便。


###复杂类型TABLE
创建一个复杂类型的表：
<pre>
create table complex(
    > col1 ARRAY<INT>,
    > col2 MAP<STRING, INT>,
    > col3 STRUCT<a:STRING, b:INT, c:DOUBLE>);
</pre>

对应的文件格式为：
<pre>
1^B2^B3^Aa^C10^Bb^C20^Bc^C30^Aa^B100^B0.1
</pre>

查询结果：
<pre>
[1,2,3]	{"a":10,"b":20,"c":30}	{"a":"a","b":100,"c":0.1}
</pre>

其实在创建表的时候，我们省略了一些内容，默认执行如下：
<pre>
 CREATE TABLE ...
 ROW FORMAT DELIMITED
   FIELDS TERMINATED BY '\001'
   COLLECTION ITEMS TERMINATED BY '\002'
   MAP KEYS TERMINATED BY '\003'
 STORED AS TEXTFILE;
</pre>
我们可以根据具体的数据文件格式，来修改分隔符。STORED AS 也可以改为SequenceFile
其中SequenceFile的意义为：
>对于某些应用而言，需要特殊的数据结构来存储自己的数据。对于基于MapReduce的数据处理，将每个二进制数据的大对象融入自己的文件中并不能实现很高的可扩展性，针对上述情况，Hadoop开发了一组更高层次的容器SequenceFile。

>考虑日志文件，其中每一条日志记录是一行文本。如果想记录二进制类型，纯文本是不合适的。这种情况下，Hadoop的SequenceFile类非常合适，因为上述提供了二进制键/值对的永久存储的数据结构。当作为日志文件的存储格式时，可以自己选择键，比如由LongWritable类型表示的时间戳，以及值可以是Writable类型，用于表示日志记录的数量。SequenceFile同样为可以作为小文件的容器。而HDFS和 MapReduce是针对大文件进行优化的，所以通过SequenceFile类型将小文件包装起来，可以获得更高效率的存储和处理。

另一种是面向列的存储格式<code>RCFile</code>,稍后不一张图：


###导入数据
<pre>
insert overwrite table target
select foo, bar from pokes;
</pre>或
<pre>
from pokes
insert overwrite table target
select foo, bar;
</pre>
这里的<code>overwrite</code>是必须的，如果有分区列，可以这样：
<pre>
insert overwrite table target
partition(dt)
select foo, bar, dt from pokes;
</pre>

如果希望得到append的方式，只能通过load的形式。

还可以在表未定义的情况下，创建表并插入数据：
<pre>
CREATE TABLE target
AS
SELECT col1, col2
FROM source;
</pre>


##查询
###排序与聚集
####使用order by
<pre>
from target
select bar, foo
order by foo asc;
</pre>

order by有个致命的弱点，即最后只使用1个reducer来完成最后的merge操作。这样对于大数据而言，肯定会成为瓶颈。

####使用sort by
如设置：set mapreduce.job.reduces=5;
<pre>
from target
select bar, foo
distribute by bar
sort by foo asc;
</pre>

通过指定distribute by, 可以开启多个reducer并行工作。相当于在每个聚集里，进行排序。但这样只能保证每个reducer里面的有序，不能保证全局有序。
举个例子：



原始文件 | order by结果 | sort by结果
------------ | ------------- | ------------
aa^A12 | aa^A12   | bb^A11
aa^A22 | aa^A22  | aa^A12
bb^A32 | bb^A11 | aa^A22
bb^A11 | bb^A32  | bb^A32




