Title: Mysql不同存储引擎的表转换方法
Date: 2011-11-05 10:39
Author: 糖拌咸鱼
Slug: mysqlbu-tong-cun-chu-yin-qing-de-biao-zhuan-huan-fang-fa

<span style="font-size: 18pt;">**Mysql不同存储引擎的表转换方法**</span>

</p>

**1、Alter table**  

直接修改表的存储引擎，但是这样会导致大量的系统开销，Mysql为此要执行一个就表向新表的逐行复制。在此期间，转换操作可能会占用服务器的所有I/O处理能力。转换表之后，原先引擎的特殊性质都会丢失，无法复原。  
**2、转储和导入方法**  

用提供的mysqldump工具，可以将原有的表转换为一个文本文件，然后修改该文件，将里面的create
table语句的引擎选项修改为需要更改后的引擎。  
**3、创建一个新的表，并把旧表中的数据导入新的表**

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:sql;gutter:false;}
  create table innodb_table like myisam_table ;   alter table innodb_table engine=innodb;  insert into innodb_table select * from myisam_table;  drop myisam_table;
```

</p>
<p>

</div>

</p>

　　  以上方法适合数据量不大的情况，如果数据量很大的话，可能会产生大量的
undo log 日志，为了避免undo log过于庞大，可以逐段进行复制;

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:sql;gutter:false;}
  start transaction;  insert into innodb_table select * from myisam_table where id between x and y; #逐次增大x和y的值  commit; 
```

</p>
<p>

</div>

</p>

　　

</p>

参考书籍：《高性能mysql》

</p>

**  
**

</p>

