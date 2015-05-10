Title: Python MySQLdb 学习总结
Date: 2012-01-12 08:51
Author: 糖拌咸鱼
Slug: python-mysqldb-xue-xi-zong-jie

  
 任何应用都离不开数据，所以在学习python的时候，当然也要学习一个如何用python操作数据库了。MySQLdb就是python对mysql数据库操作的模块。官方Introduction
: MySQLdb is an thread-compatible interface to the popular
MySQL database server that provides the Python database API.
它其实相当于翻译了对应C的接口。

</p>

  
使用这种数据库接口大多是就是执行连接数据库-\>执行query-\>提取数据-\>关闭连接
这几个步骤。MySQLdb提供比较关键的对象，分别是Connection、Cursor、Result。具体使用步骤很简单先不写了，先写一些个人认为比较重要、值得注意的地方。

</p>

 1、虽然在MySQLdb.Connect(host ,user , passw ,
db)函数中，我们经常使用的只是这几个参数，但是其实里面还有很多比如字符集、线程安全、ssl等也都是很重要的参数，使用时要身份注意。

</p>

 2、当使用Connection.query()函数进行query后，connection
对象可以返回两种result，分别是store\_result和use\_result，store\_result
将结果集存回client端，而use\_result则是结果集保存在server端，并且维护了一个连接，会占用server资源。此时，不可以进行任何其他的查询。建议使用store\_result，除非返回结果集（result
set）过大或是无法使用limit的情形。

</p>

 3、提取（fetch）数据的返回形式大多有三种情形。 as a tuple(how=0) ；as
dictionaries, key=column or table.column if duplicated(how=1)；as
dictionaries, key=table.column (how=2)

</p>

 4、每次fetch，在result内部都会产生数据位置的移动，也就是说假如有10行数据，执行result.fetch\_row(3,0)，会得到前三行，再执行result.fetch\_row(3,0)，则会得到中间的三行，所以说fetch会导致position的移动。另外值得注意的是，如果使用use\_result，也就是数据存储在server时，在fetch所有的条目之前，不能进行任何的query操作。

</p>

 5、mysql本身不支持游标（Cursor），但是MySQLdb对Cursor进行了仿真。重要的执行query方法有execute
和 executemany
。execute方法，执行单条sql语句，调用executemany方法很好用，数据库性能瓶颈很大一部分就在于网络IO和磁盘IO将多个insert放在一起，只执行一次IO，可以有效的提升数据库性能。游标cursor具有fetchone、fetchmany、fetchall三个方法提取数据，每个方法都会导致游标游动，所以必须关注游标的位置。游标的scroll(value,
mode)方法可以使得游标进行卷动，mode参数指定相对当前位置(relative)还是以绝对位置(absolute)进行移动。

</p>

 6、MySQLdb提供了很多函数方法，在官方指南里没有完全罗列，使用者可以用help去看看，里面提供了很多方便的东西。

</p>

 7、对于mysql来说，如果使用支持事务的存储引擎，那么每次操作后，commit是必须的，否则不会真正写入数据库，对应rollback可以进行相应的回滚，但是commit后是无法再rollback的。commit()
可以在执行很多sql指令后再一次调用，这样可以适当提升性能。

</p>

 8、executemany处理过多的命令也不见得一定好，因为数据一起传入到server端，可能会造成server端的buffer溢出，而一次数据量过大，也有可能产生一些意想不到的麻烦。合理，分批次executemany是个不错的办法。

</p>

  最后，我自己写了个pyMysql模块，主要是对MySQLdb提供的常用方法进行了简单的再次封装，也借此机会好好学习下MySQLdb，以及练习python的编码。**该程序使用的数据库表，采用myisam引擎，所以没加上commit()，一般最好还是要加上的。**

</p>

**代码如下**：PyMysql.py

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:python;gutter:false;}
#-*- encoding:gb2312 -*-_'''Created on 2012-1-12@author: xiaojay'''import MySQLdbimport MySQLdb.cursorsSTORE_RESULT_MODE = 0USE_RESULT_MODE = 1CURSOR_MODE = 0DICTCURSOR_MODE = 1SSCURSOR_MODE = 2SSDICTCURSOR_MODE = 3FETCH_ONE = 0FETCH_MANY = 1FETCH_ALL = 2class PyMysql:    def __init__(self):        self.conn = None        pass     def newConnection(self,host,user,passwd,defaultdb):        """        建立一个新连接，指定host、用户名、密码、默认数据库        """        self.conn = MySQLdb.Connect(host,user,passwd,defaultdb)        if self.conn.open == False:            raise None    def closeConnnection(self):        """        关闭当前连接        """        self.conn.close()        def query(self,sqltext,mode=STORE_RESULT_MODE):        """        作用：使用connection对象的query方法，并返回一个元组(影响行数(int),结果集(result))        参数：sqltext：sql语句             mode=STORE_RESULT_MODE（0） 表示返回store_result，mode=USESTORE_RESULT_MODE（1） 表示返回use_result        返回：元组(影响行数(int),结果集(result)        """        if self.conn==None or self.conn.open==False :            return -1        self.conn.query(sqltext)        if mode == 0 :            result = self.conn.store_result()         elif mode == 1 :            result = self.conn.use_result()        else :            raise Exception("mode value is wrong.")        return (self.conn.affected_rows(),result)        def fetch_queryresult(self,result,maxrows=1,how=0,moreinfo=False):        """        参数:result： query后的结果集合            maxrows： 返回的最大行数            how： 以何种方式存储结果             (0：tuple,1：dictionaries with columnname,2：dictionaries with table.columnname)            moreinfo 表示是否获取更多额外信息（num_fields，num_rows,num_fields）        返回：元组（数据集，附加信息（当moreinfo=False）或单一数据集（当moreinfo=True）        """        if result == None : return None        dataset =  result.fetch_row(maxrows,how)        if moreinfo is False :            return dataset        else :            num_fields = result.num_fields()            num_rows = result.num_rows()            field_flags = result.field_flags()            info = (num_fields,num_rows,field_flags)            return (dataset,info)            def execute(self,sqltext,args=None,mode=CURSOR_MODE,many=False):        """        作用：使用游标（cursor）的execute 执行query        参数：sqltext： 表示sql语句             args： sqltext的参数             mode：以何种方式返回数据集                CURSOR_MODE = 0 ：store_result , tuple                DICTCURSOR_MODE = 1 ： store_result , dict                SSCURSOR_MODE = 2 : use_result , tuple                SSDICTCURSOR_MODE = 3 : use_result , dict              many：是否执行多行操作（executemany）        返回：元组（影响行数（int），游标（Cursor））        """        if mode == CURSOR_MODE :            curclass = MySQLdb.cursors.Cursor        elif mode == DICTCURSOR_MODE :            curclass = MySQLdb.cursors.DictCursor        elif mode == SSCURSOR_MODE :            curclass = MySQLdb.cursors.SSCursor        elif mode == SSDICTCURSOR_MODE :            curclass = MySQLdb.cursors.SSDictCursor        else :            raise Exception("mode value is wrong")                cur = self.conn.cursor(cursorclass=curclass)        line = 0        if many == False :            if args == None :                 line = cur.execute(sqltext)            else :                line = cur.execute(sqltext,args)        else :            if args == None :                line = cur.executemany(sqltext)            else :                line = cur.executemany(sqltext,args)        return (line , cur )        def fetch_executeresult(self,cursor,mode=FETCH_ONE,rows=1):        """        作用：提取cursor获取的数据集        参数：cursor：游标             mode：执行提取模式              FETCH_ONE: 提取一个； FETCH_MANY :提取rows个 ；FETCH_ALL : 提取所有             rows：提取行数        返回：fetch数据集        """        if cursor == None :             return         if mode == FETCH_ONE :            return cursor.fetchone()        elif mode == FETCH_MANY :            return cursor.fetchmany(rows)        elif mode == FETCH_ALL :            return cursor.fetchall()        if __name__=="__main__" :    print help (PyMysql)
```

</p>
<p>

</div>

</p>

　　

</p>

**测试代码：**

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:python;gutter:false;}
#-*- encoding:gb2312 -*-import PyMysql"""authors 这张表很简单。+--------------+-------------+------+-----+---------+----------------+| Field        | Type        | Null | Key | Default | Extra          |+--------------+-------------+------+-----+---------+----------------+| author_id    | int(11)     | NO   | PRI | NULL    | auto_increment || author_last  | varchar(50) | YES  |     | NULL    |                || author_first | varchar(50) | YES  | MUL | NULL    |                || country      | varchar(50) | YES  |     | NULL    |                |+--------------+-------------+------+-----+---------+----------------+本文主要的所有操作都针对该表。"""def printAuthors(res,mode=0,lines=0):    """    格式化输出    """    print "*"*20, " lines: ",lines ," ","*"*20    if mode==0  :        for author_id , author_last , author_first , country in res :            print "ID : %s , Author_last : %s , Author_First : %s , Country : %s" \            % (author_id , author_last , author_first , country )    else :        for item in res :            print "-----------"                            for key in item.keys():                print key ," : ",item[key]#建立连接mysql = PyMysql.PyMysql()mysql.newConnection(        host="localhost",         user="root",         passwd="peterbbs",         defaultdb="bookstore")""#定义sql语句sqltext = "select * from authors order by author_id "#调用query方法,得到resultlines , res = mysql.query(sqltext, mode=PyMysql.STORE_RESULT_MODE)#提取数据data = mysql.fetch_queryresult(res, maxrows=20, how=0, moreinfo=False)#打印printAuthors(data,0,lines)#演示多行插入sqltext = "insert into authors (author_last,author_first,country) values (%s,%s,%s)"args = [('aaaaaa','bbbbbb','cccccc'),('dddddd','eeeeee','ffffff'),('gggggg','hhhhhh','iiiiii')]lines ,cur = mysql.execute(sqltext,args,mode=PyMysql.DICTCURSOR_MODE,many=True)print "*"*20, lines ,"行被插入 ","*"*20sqltext = "select * from authors order by author_id "#调用cursor.execute方法,得到resultlines ,cur = mysql.execute(sqltext,mode=PyMysql.DICTCURSOR_MODE)#提取数据data = mysql.fetch_executeresult(cur, mode=PyMysql.FETCH_MANY, rows=20)#打印printAuthors(data,1,lines)#关闭连接mysql.closeConnnection()
```

</p>
<p>

</div>

</p>

　　

</p>

**测试输出：**

</p>
<p>
> </p>
>
>  \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* lines: 5
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
>
> </p>
>
> ID : 1 , Author\_last : Greene , Author\_First : Graham , Country :
> United Kingdom  
> ID : 4 , Author\_last : Peter , Author\_First : David , Country :
> China  
> ID : 5 , Author\_last : mayday , Author\_First : Feng , Country :
> France  
> ID : 6 , Author\_last : zhang , Author\_First : lixin , Country :
> France  
> ID : 9 , Author\_last : zhang111 , Author\_First : lixin , Country :
> France  
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 3 行被插入
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* lines: 8
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
> -----------  
> country : United Kingdom  
> author\_id : 1  
> author\_first : Graham  
> author\_last : Greene  
> -----------  
> country : China  
> author\_id : 4  
> author\_first : David  
> author\_last : Peter  
> -----------  
> country : France  
> author\_id : 5  
> author\_first : Feng  
> author\_last : mayday  
> -----------  
> country : France  
> author\_id : 6  
> author\_first : lixin  
> author\_last : zhang  
> -----------  
> country : France  
> author\_id : 9  
> author\_first : lixin  
> author\_last : zhang111  
> -----------  
> country : cccccc  
> author\_id : 53  
> author\_first : bbbbbb  
> author\_last : aaaaaa  
> -----------  
> country : ffffff  
> author\_id : 54  
> author\_first : eeeeee  
> author\_last : dddddd  
> -----------  
> country : iiiiii  
> author\_id : 55  
> author\_first : hhhhhh  
> author\_last : gggggg
>
> </p>
> <p>

</p>

