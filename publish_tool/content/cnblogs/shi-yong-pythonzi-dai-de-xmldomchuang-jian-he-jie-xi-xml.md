Title: 使用python自带的xml.dom创建和解析xml
Date: 2012-01-10 09:08
Author: 糖拌咸鱼
Slug: shi-yong-pythonzi-dai-de-xmldomchuang-jian-he-jie-xi-xml

  
 python中的xml.dom模块使用的就是传统的dom解析api和方法。所以也就不写什么了，主要就是练习敲敲代码，继续熟悉python。本文通过xml.dom.minidom创建一个xml文档，然后再解析出来，用以熟悉相关接口方法的使用。

</p>

**创建一个xml文档：**

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:python;gutter:false;}
'''Created on 2012-1-10Create a xml document@author: xiaojay'''from xml.dom import minidomdoc = minidom.Document()doc.appendChild(doc.createComment("This is a simple xml."))booklist = doc.createElement("booklist")doc.appendChild(booklist)def addBook(newbook):    book = doc.createElement("book")    book.setAttribute("id", newbook["id"])        title = doc.createElement("title")    title.appendChild(doc.createTextNode(newbook["title"]))    book.appendChild(title)        author = doc.createElement("author")    name = doc.createElement("name")    firstname = doc.createElement("firstname")    firstname.appendChild(doc.createTextNode(newbook["firstname"]))    lastname = doc.createElement("lastname")    lastname.appendChild(doc.createTextNode(newbook["lastname"]))    name.appendChild(firstname)    name.appendChild(lastname)    author.appendChild(name)    book.appendChild(author)        pubdate = doc.createElement("pubdate")    pubdate.appendChild(doc.createTextNode(newbook["pubdate"]))    book.appendChild(pubdate)        booklist.appendChild(book)addBook({"id":"1001","title":"An apple","firstname":"Peter","lastname":"Zhang","pubdate":"2012-1-12"})addBook({"id":"1002","title":"Love","firstname":"Mike","lastname":"Li","pubdate":"2012-1-10"})addBook({"id":"1003","title":"Steve.Jobs","firstname":"Tom","lastname":"Wang","pubdate":"2012-1-19"})addBook({"id":"1004","title":"Harry Potter","firstname":"Peter","lastname":"Chen","pubdate":"2012-11-11"})f = file("book.xml","w")doc.writexml(f)f.close()
```

</p>
<p>

</div>

</p>

　　通过doc.toprettyxml(indent, newl,
encoding)方法可以优雅显示xml文档，但是要避免直接写入文本，否则会给解析带来麻烦，尽量使用自带的writexml方法。

</p>

生成的文档内容：

</p>
<p>
> </p>
>
> \<?xml version="1.0" ?\>  
> \<!--This is a simple xml.--\>  
> \<booklist\>  
>  　　\<book id="1001"\>  
>  　　　　\<title\>  
>  　　　　An apple  
>  　　　　\</title\>  
>  　　\<author\>  
>  　　　　\<name\>  
>  　　　　　　\<firstname\>  
>  　　　　　　Peter  
>  　　　　　　\</firstname\>  
>  　　　　　　\<lastname\>  
>  　　　　　　Zhang  
>  　　　　　　\</lastname\>  
>  　　　　\</name\>  
>  　　\</author\>  
>  　　\<pubdate\>  
>  　　2012-1-12  
>  　　\</pubdate\>  
>  　　\</book\>
>
> </p>
>
>  .................  
> \</booklist\>
>
> </p>
>
>  
>
> </p>
> <p>

</p>

**解析该xml文档：**

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:python;gutter:false;}
'''Created on 2012-1-10Scan a xml doc@author: xiaojay'''from xml.dom import minidom , Nodeclass bookscanner:    def __init__(self,doc):        for child in doc.childNodes :            if child.nodeType == Node.ELEMENT_NODE \            and child.tagName == "book" :                bookid = child.getAttribute("id")                print "*"*20                print "Book id : " , bookid                self.handle_book(child)                    def handle_book(self,node):        for child in node.childNodes :            if child.nodeType == Node.ELEMENT_NODE :                if child.tagName == "title":                    print "Title : " , self.getText(child.firstChild)                if child.tagName == "author":                    self.handle_author(child)                if child.tagName == "pubdate":                    print "Pubdate : " , self.getText(child.firstChild)                def getText(self,node):        if node.nodeType == Node.TEXT_NODE :            return node.nodeValue        else: return ""            def handle_author(self,node):        author = node.firstChild        for child in author.childNodes:            if child.nodeType == Node.ELEMENT_NODE:                if child.tagName == "firstname" :                    print "Firstname : ", self.getText(child.firstChild)                if child.tagName == "lastname" :                    print "Lastname : " , self.getText(child.firstChild)        doc = minidom.parse("book.xml")for child in doc.childNodes :    if child.nodeType == Node.COMMENT_NODE:        print "Conment : " , child.nodeValue    if child.nodeType == Node.ELEMENT_NODE:        bookscanner(child)
```

</p>
<p>

</div>

</p>

　　

</p>

输出结果：

</p>
<p>
> </p>
>
> Conment : This is a simple xml.  
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
> Book id : 1001  
> Title : An apple  
> Firstname : Peter  
> Lastname : Zhang  
> Pubdate : 2012-1-12  
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
> Book id : 1002  
> Title : Love  
> Firstname : Mike  
> Lastname : Li  
> Pubdate : 2012-1-10  
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
> Book id : 1003  
> Title : Steve.Jobs  
> Firstname : Tom  
> Lastname : Wang  
> Pubdate : 2012-1-19  
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
> Book id : 1004  
> Title : Harry Potter  
> Firstname : Peter  
> Lastname : Chen  
> Pubdate : 2012-11-11
>
> </p>
> <p>

</p>

