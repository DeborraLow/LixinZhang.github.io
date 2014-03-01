Title: 使用Python中HTTPParser模块进行简单的html解析
Date: 2012-01-09 06:17
Author: 糖拌咸鱼
Slug: shi-yong-pythonzhong-httpparsermo-kuai-jin-xing-jian-dan-de-htmljie-xi

      
很早之前，在.net平台下写过一个分析html代码的程序，那时候的思想是将html代码解析成一棵类似树的结构，然后在分析其中的标签。Python中，HTTPParser模块，更像是在过程中进行解析，模拟遇到开始标签怎样开始，怎样处理属性和值，又当遇到结束标签该怎样结束等等过程。对于格式规范、代码简洁的html容易解析，如果复杂、不规范的html解析会很繁琐。

</p>

**<span style="font-size: 16px;">HTTPParser：</span>**

</p>

HTMLParser是python用来解析html的模块。它可以分析出html里面的标签、数据等等，是一种处理html的简便途径。
  
HTMLParser采用的是一种事件驱动的模式，当HTMLParser找到一个特定的标记时，它会去调用一个用户定义的函数，以此来通知程序处理。  
它主要的用户回调函数的命名都是以handler\_开头的，都是HTMLParser的成员函数。  
当我们使用时，就从HTMLParser派生出新的类，然后重新定义这几个以handler\_开头的函数即可。

</p>

**<span style="font-size: 16px;">例子：</span>**

</p>

写了小例子，用于分析获取到我们东南大学教务处网站的信息公告栏，内容比较简单。

</p>

![][]

</p>

打开jwc网站。

</p>

查看源代码，可以发现信息公告栏里有这样格式的html片段：

</p>

\<td width="314" height="20"\>\<a href="/admin/disp.asp?id=5323"
target="newwin"\>关于申请2012年德国乌尔姆大学本科交流项目的报...\</a\>\<img
src="imagess/new.gif" width="26" height="10"\>\</td\>   
\<td width="76" height="20"\>2012-1-9\</td\>

</p>

于是，可以简单的提取包含href="/admin/disp.asp?"属性的\<a\>标签获取文本和链接，以及紧接着的\<td\>标签获取日期值。

</p>

具体python实现代码如下：

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:python;gutter:false;}
#-*- encoding:gb2312 -*-'''Created on 2012-1-9@author: xiaojay'''from HTMLParser import HTMLParserfrom htmlentitydefs import entitydefsimport urllib2url = "http://jwc.seu.edu.cn"class NewsParser(HTMLParser):    def __init__(self):        HTMLParser.__init__(self)        self.link = ""        self.text = ""        self.items = [] #保存提取结果        self.flag = False        self.parse_date = False        self.date_start = False    def handle_starttag(self,tag,attrs):        #处理开始标签        if tag=='a' and attrs:            for key ,value in attrs:                if key=='href':                    index = value.find("?")                    if index>0 and value[0:index]=="/admin/disp.asp":                        self.flag = True                        self.parse_date = True                                     self.link = value        if tag == "td" and self.parse_date == True :            self.date_start = True                            def handle_data(self,data):        #处理数据        if self.flag == True :            self.text = data        if self.date_start == True :            self.items.append((self.text,self.link,data))    def handle_entityref(self , name):        #处理实体引用        if entitydefs.has_key(name):            self.handle_data(name)        else :            self.handle_data("&"+name )    def handle_endtag(self,tag):        #处理结束标签        if tag == 'a' and self.flag== True :            self.flag = False        if tag == 'td' and self.parse_date and self.date_start :            self.parse_date = False            self.date_start = False    def getItems(self):        return self.items    req = urllib2.Request(url)fd = urllib2.urlopen(req)newsparser = NewsParser()#调用feed方法，开始处理newsparser.feed(fd.read())items = newsparser.getItems()for text , link , date in items :    print text , link , date                                                    
```

</p>
<p>

</div>

</p>

运行结果：

</p>
<p>
> </p>
>
> 关于申请2012年德国乌尔姆大学本科交流项目的报...
> /admin/disp.asp?id=5323 2012-1-9  
> 关于公布“东南大学第五届PLD设计竞赛”结果的通知 /admin/disp.asp?id=5322
> 2012-1-6  
> 关于公布“2011年国家大学生创新性实验计划项目... /admin/disp.asp?id=5321
> 2012-1-6  
> 关于公布2011年“国家大学生创新性实验计划项目... /admin/disp.asp?id=5320
> 2012-1-6  
> 关于申请暑假东南大学与台湾中原大学交换生的报名通知
> /admin/disp.asp?id=5319 2012-1-5  
> 本科生申报2012年SRTP项目的预通知 /admin/disp.asp?id=5318 2012-1-5  
> 关于申请2012年法国巴黎电子信息学院本科交流项...
> /admin/disp.asp?id=5317 2012-1-5  
> 关于申请2012年日本北海道大学本科交流项目的报...
> /admin/disp.asp?id=5316 2012-1-4
>
> </p>
> <p>

</p>

  []: http://pic002.cnblogs.com/images/2012/146443/2012010914154791.png
