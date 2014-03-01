Title: Json概述以及python对json的相关操作
Date: 2011-12-14 08:21
Author: 糖拌咸鱼
Slug: jsongai-shu-yi-ji-pythondui-jsonde-xiang-guan-cao-zuo

<span style="font-size: medium;">**什么是json：**</span>

</p>

JSON(JavaScript Object Notation)
是一种轻量级的数据交换格式。易于人阅读和编写。同时也易于机器解析和生成。它基于JavaScript
Programming Language, Standard ECMA-262 3rd Edition - December
1999的一个子集。JSON采用完全独立于语言的文本格式，但是也使用了类似于C语言家族的习惯（包括C,
C++, C\#, Java, JavaScript, Perl,
Python等）。这些特性使JSON成为理想的数据交换语言。

</p>

JSON建构于两种结构：

</p>

“名称/值”对的集合（A collection of name/value
pairs）。不同的语言中，它被理解为对象（object），纪录（record），结构（struct），字典（dictionary），哈希表（hash
table），有键列表（keyed list），或者关联数组 （associative array）。   
值的有序列表（An ordered list of
values）。在大部分语言中，它被理解为数组（array）。   
这些都是常见的数据结构。事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。

</p>

jso官方说明参见：<http://json.org/>

</p>

Python操作json的标准api库参考：<http://docs.python.org/library/json.html>

</p>

<span style="font-size: medium;">**对简单数据类型的encoding 和
decoding：**</span>

</p>

使用简单的json.dumps方法对简单数据类型进行编码，例如：

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
import jsonobj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]encodedjson = json.dumps(obj)print repr(obj)print encodedjson
```

</p>

输出：

</p>

[[1, 2, 3], 123, 123.123, 'abc', {'key2': (4, 5, 6), 'key1': (1, 2, 3)}]
  
[[1, 2, 3], 123, 123.123, "abc", {"key2": [4, 5, 6], "key1": [1, 2, 3]}]

</p>

通过输出的结果可以看出，简单类型通过encode之后跟其原始的repr()输出结果非常相似，但是有些数据类型进行了改变，例如上例中的元组则转换为了列表。在json的编码过程中，会存在从python原始类型向json类型的转化过程，具体的转化对照如下：

</p>

[![image][]][]

</p>

json.dumps()方法返回了一个str对象encodedjson，我们接下来在对encodedjson进行decode，得到原始数据，需要使用的json.loads()函数：

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
decodejson = json.loads(encodedjson)print type(decodejson)print decodejson[4]['key1']print decodejson
```

</p>

输出：

</p>

\<type 'list'\>   
[1, 2, 3]

</p>

[[1, 2, 3], 123, 123.123, u'abc', {u'key2': [4, 5, 6], u'key1': [1, 2,
3]}]

</p>

loads方法返回了原始的对象，但是仍然发生了一些数据类型的转化。比如，上例中‘abc’转化为了unicode类型。从json到python的类型转化对照如下：

</p>

[![image][1]][]

</p>

json.dumps方法提供了很多好用的参数可供选择，比较常用的有sort\_keys（对dict对象进行排序，我们知道默认dict是无序存放的），separators，indent等参数。

</p>

排序功能使得存储的数据更加有利于观察，也使得对json输出的对象进行比较，例如：

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
data1 = {'b':789,'c':456,'a':123}data2 = {'a':123,'b':789,'c':456}d1 = json.dumps(data1,sort_keys=True)d2 = json.dumps(data2)d3 = json.dumps(data2,sort_keys=True)print d1print d2print d3print d1==d2print d1==d3
```

</p>

输出：

</p>

{"a": 123, "b": 789, "c": 456}   
{"a": 123, "c": 456, "b": 789}   
{"a": 123, "b": 789, "c": 456}   
False   
True

</p>

上例中，本来data1和data2数据应该是一样的，但是由于dict存储的无序特性，造成两者无法比较。因此两者可以通过排序后的结果进行存储就避免了数据比较不一致的情况发生，但是排序后再进行存储，系统必定要多做一些事情，也一定会因此造成一定的性能消耗，所以适当排序是很重要的。

</p>

indent参数是缩进的意思，它可以使得数据存储的格式变得更加优雅。

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
data1 = {'b':789,'c':456,'a':123}d1 = json.dumps(data1,sort_keys=True,indent=4)print d1
```

</p>

输出：

</p>

{   
    "a": 123,   
    "b": 789,   
    "c": 456   
}

</p>

输出的数据被格式化之后，变得可读性更强，但是却是通过增加一些冗余的空白格来进行填充的。json主要是作为一种数据通信的格式存在的，而网络通信是很在乎数据的大小的，无用的空格会占据很多通信带宽，所以适当时候也要对数据进行压缩。separator参数可以起到这样的作用，该参数传递是一个元组，包含分割对象的字符串。

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
print 'DATA:', repr(data)print 'repr(data)             :', len(repr(data))print 'dumps(data)            :', len(json.dumps(data))print 'dumps(data, indent=2)  :', len(json.dumps(data, indent=4))print 'dumps(data, separators):', len(json.dumps(data, separators=(',',':')))
```

</p>

输出：

</p>

DATA: {'a': 123, 'c': 456, 'b': 789}   
repr(data)             : 30   
dumps(data)            : 30   
dumps(data, indent=2)  : 46   
dumps(data, separators): 25

</p>

通过移除多余的空白符，达到了压缩数据的目的，而且效果还是比较明显的。

</p>

另一个比较有用的dumps参数是skipkeys，默认为False。
dumps方法存储dict对象时，key必须是str类型，如果出现了其他类型的话，那么会产生TypeError异常，如果开启该参数，设为True的话，则会比较优雅的过度。

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
data = {'b':789,'c':456,(1,2):123}print json.dumps(data,skipkeys=True)
```

</p>

输出：

</p>

{"c": 456, "b": 789}

</p>

 

</p>

<span style="font-size: medium;">**处理自己的数据类型**</span>

</p>

json模块不仅可以处理普通的python内置类型，也可以处理我们自定义的数据类型，而往往处理自定义的对象是很常用的。

</p>

首先，我们定义一个类Person。

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
class Person(object):    def __init__(self,name,age):        self.name = name        self.age = age    def __repr__(self):        return 'Person Object name : %s , age : %d' % (self.name,self.age)if __name__  == '__main__':    p = Person('Peter',22)    print p
```

</p>

如果直接通过json.dumps方法对Person的实例进行处理的话，会报错，因为json无法支持这样的自动转化。通过上面所提到的json和python的类型转化对照表，可以发现，object类型是和dict相关联的，所以我们需要把我们自定义的类型转化为dict，然后再进行处理。这里，有两种方法可以使用。

</p>

**方法一：自己写转化函数**

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
'''Created on 2011-12-14@author: Peter'''import Personimport jsonp = Person.Person('Peter',22)def object2dict(obj):    #convert object to a dict    d = {}    d['__class__'] = obj.__class__.__name__    d['__module__'] = obj.__module__    d.update(obj.__dict__)    return ddef dict2object(d):    #convert dict to object    if'__class__' in d:        class_name = d.pop('__class__')        module_name = d.pop('__module__')        module = __import__(module_name)        class_ = getattr(module,class_name)        args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args        inst = class_(**args) #create new instance    else:        inst = d    return instd = object2dict(p)print d#{'age': 22, '__module__': 'Person', '__class__': 'Person', 'name': 'Peter'}o = dict2object(d)print type(o),o#<class 'Person.Person'> Person Object name : Peter , age : 22dump = json.dumps(p,default=object2dict)print dump#{"age": 22, "__module__": "Person", "__class__": "Person", "name": "Peter"}load = json.loads(dump,object_hook = dict2object)print load#Person Object name : Peter , age : 22
```

</p>

上面代码已经写的很清楚了，实质就是自定义object类型和dict类型进行转化。object2dict函数将对象模块名、类名以及\_\_dict\_\_存储在dict对象里，并返回。dict2object函数则是反解出模块名、类名、参数，创建新的对象并返回。在json.dumps
方法中增加default参数，该参数表示在转化过程中调用指定的函数，同样在decode过程中json.loads方法增加object\_hook,指定转化函数。

</p>

**方法二：继承JSONEncoder和JSONDecoder类，覆写相关方法**

</p>

JSONEncoder类负责编码，主要是通过其default函数进行转化，我们可以override该方法。同理对于JSONDecoder。

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
'''Created on 2011-12-14@author: Peter'''import Personimport jsonp = Person.Person('Peter',22)class MyEncoder(json.JSONEncoder):    def default(self,obj):        #convert object to a dict        d = {}        d['__class__'] = obj.__class__.__name__        d['__module__'] = obj.__module__        d.update(obj.__dict__)        return dclass MyDecoder(json.JSONDecoder):    def __init__(self):        json.JSONDecoder.__init__(self,object_hook=self.dict2object)    def dict2object(self,d):        #convert dict to object        if'__class__' in d:            class_name = d.pop('__class__')            module_name = d.pop('__module__')            module = __import__(module_name)            class_ = getattr(module,class_name)            args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args            inst = class_(**args) #create new instance        else:            inst = d        return instd = MyEncoder().encode(p)o =  MyDecoder().decode(d)print dprint type(o), o
```

</p>

 

</p>

对于JSONDecoder类方法，稍微有点不同，但是改写起来也不是很麻烦。看代码应该就比较清楚了。

</p>

  [image]: http://images.cnblogs.com/cnblogs_com/coser/201112/201112141621131652.png
    "image"
  [![image][]]: http://images.cnblogs.com/cnblogs_com/coser/201112/201112141621136287.png
  [1]: http://images.cnblogs.com/cnblogs_com/coser/201112/201112141621146178.png
    "image"
  [![image][1]]: http://images.cnblogs.com/cnblogs_com/coser/201112/201112141621147225.png
