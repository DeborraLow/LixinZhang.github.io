Title: ubuntu下mysql-python模块的安装
Date: 2012-01-11 04:56
Author: 糖拌咸鱼
Slug: ubuntuxia-mysql-pythonmo-kuai-de-an-zhuang

**安装步骤：**

</p>

1、sudo apt-get install python-setuptools

</p>

2、sudo apt-get install libmysqld-dev

</p>

3、sudo apt-get install libmysqlclient-dev

</p>

4、sudo apt-get install python-dev

</p>

5、sudo easy\_install mysql-python

</p>

 

</p>

**测试下：**

</p>

在python交互式窗口，import MySQLdb 试试，不报错的话，就证明安装好了。

</p>

 

</p>

**eclipse 检测出错：**

</p>

如果平常是在eclipse pydev
下进行python开发的话，那么直接在eclipse环境下使用MySQLdb还会存在问题的，一般会提示有语法错误，原因是模块插件未导入eclipse的问题。解决方法就是将其导入就ok了。

</p>

首先查看下文件路径 print MySQLdb.\_\_file\_\_

</p>

然后Window -\> Preferences -\> Pydev -\> Interpreter-Python -\> new
Folder

</p>

最后把第一步获取的路径加上去，点ok就可以了。 

</p>

 

</p>

