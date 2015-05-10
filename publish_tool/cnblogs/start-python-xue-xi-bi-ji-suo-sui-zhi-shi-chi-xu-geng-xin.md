Title: Start Python 学习笔记（琐碎知识，持续更新。。。）
Date: 2011-12-11 14:21
Author: 糖拌咸鱼
Slug: start-python-xue-xi-bi-ji-suo-sui-zhi-shi-chi-xu-geng-xin

最近比较闲，想学习一门脚本语言，于是选择了python进行学习，之前对脚本语言不是很熟悉，所以不对python好坏做任何评价。希望通过学习python，能让自己对脚本语言有更深刻的认识吧。  
Python的执行过程：当程序执行时，python内部会先将源代码编译成所谓的字节码的形式。字节码是源代码底层的、与平台无关的表现形式。编译字节码的过程中，会生成一个.pyc的文件，这个文件就是编译之后的字节码。Python真正在运行的就是这个字节码文件，如果生成字节码文件之后没有再修改过源代码的话，下次程序运行会跳过编译这个步骤，直接运行pyc文件，这是一种启动速度的优化。字节码文件被发送到python虚拟机（Python
Virtual Machine, PVM）上来执行。PVM是python的运行引擎。  
Python字节码不是机器的二进制代码，只是一种中间表示形式，所以python无法运行的和C/C++一样快。  
Python语言有三种主要的实现方式：CPython、Jython和IronPython。  
Python是动态类型的（自动跟踪你的类型而不是要求声明的代码），但也是强类型的（只能对一个对象进行有效的操作）

</p>

 

</p>

1 、十六进制和八进制表示 0XAF -\> 175  , 010 -\>8   
2、math模块 import math
，使用的时候math.sqrt(100),当确定自己不会导入多个同名函数的情况下，可以使用from
math import sqrt ,以后就可以随时使用sqrt函数了。   
3、对于虚数的处理，使用cmath（complex
math）模块，这样就可以对-1进行sqrt操作了。   
4、input和raw\_input的区别，input会假设用户输入的是合法的Python表达式，使用raw\_input函数，它会把所有的输入当做原始数据（raw
data），然后将其放在字符串中。除非input有特别的需要，否则应该尽可能使用raw\_input函数
  
5、在字符串前面加r，取消转义   
6、列表和元组的主要区别：列表可以修改而元组不能   
7、列表的分片，列表[起始点,终止点之前一点,步长（默认为1）   
8、字符串不能像列表一样被修改，一般转换为列表然后再进行处理   
9、列表a、b，a=a+b的效率要低于a.extend(b)，因为前者是在a+b后生成新的列表然后又赋值给a，而后者是在原a的基础上扩展出b的
  
10、pop方法是唯一一个能够修改列表又返回值的方法。lst.pop() 返回并删除   
11、tuple函数将列表转化为元组 tuple([1,2,3])   
12、模板字符串：string模块提供一种格式化值的方法：模板字符串。它的工作方式类似于很多UnixShell里的变量替换。
from string import Template 。 具体google。   
13、string模块的join方法是split方法的逆方法。EG：seq =
['1','2','3','4','5'];sep = ',';s = sep.join(seq)   
14、字符串的title方法，将字符串转换为标题，也就是所有单词的首字母大写，而其他字母小写。string
= "that's all folks.";string.title()=="That'S All Folks."   
15、strip方法返回去除两侧（不包括内部）空格的字符串。   
16、使用dict的小Demo：   
people = {   
    'Alice':{   
        'phone':1234,   
        'address':'beijing'   
           },   
    'Peter':{   
        'phone':4567,   
        'address':'shanghai'   
            },   
    'Micheal':{   
        'phone':9012,   
        'address':'hangzhou'     
             }   
          }   
name = raw\_input("please input the name : \\n")   
if(people.has\_key(name)==False):   
    print "Not exist"   
else:   
    profile = people[name]   
    \#use dict to format the string   
    print "Phone is : %(phone)s \\nAddress is : %(address)s" % profile   
17、字典的拷贝，字典的普通copy方法是浅拷贝，只是简单的拷贝值，但是如果涉及到应用的拷贝的话，就要考虑使用deepcopy方法进行深拷贝。
  
18、模块的导入：   
   import somemodule   
   from somemodule import somefunction   
   from somemodule import somefunction, anthorfunction,
yetanthorfunction   
   from somemodule import \*   
   使用别名，避免冲突:import math as foobar   
19、交换两个值 x,y = y,x   
20、== 测试相等性，即值是否相等，而 is
用于测试同一性，即是否指向同一个对象   
21、a if b else c ; 如果b为真，则返回a，否则返回c      
22、遍历字典   
d = {'x':1,'y':2,'z':3}   
\#Method1   
for key in d:   
    print key ,'-----\>',d[key]   
\#Method2   
for key in d.keys():   
    print key ,'-----\>',d[key]   
\#Method3   
for (key , value) in d.items() :   
    print key , '-----\>' , value   
23、zip函数可以用来进行并行迭代，可以将多个序列"压缩"在一起，然后返回一个元组的列表
  
names = ['Peter','Rich','Tom']   
ages = [20,23,22]   
d = dict(zip(names,ages))   
for (name,age) in zip(names,ages):   
    print name ,'----', age   
print d['Peter']   
24、在循环中添加else语句，只有在没有调用break语句的时候执行。这样可以方便编写曾经需要flag标记的算法。
  
25、使用del时候，删除的只是名称，而不是列表本身值，事实上，在python中是没有办法删除值的，系统会自动进行垃圾回收。
  
26、求斐波那契数列   
def fibs(num):   
    'a function document'   
    result = [0,1]   
    for i in range(num-2):   
        result.append(result[-2]+result[-1])   
    return result   
27、抽象函数（参数可以缺省，可以通过\*p传递任意数量的参数，传递的是元组；通过\*\*p传递任意数量的参数，传递的是字典）
  
def a(\*p):   
    print p   
def b(\*\*p):   
    print p   
a(1,2,3)   
b(a='1',b='2',c='3')   
"""   
result:   
(1, 2, 3)   
{'a': '1', 'c': '3', 'b': '2'}   
"""   
28、使用globals()函数获取全局变量值，该函数的近亲是vars，它可以返回全局变量的字典（locals返回局部变量的字典）
  
29、随机函数random.choice([1,2,3,4])   
30、关于面向对象   
\#\_\_metaclass\_\_ = type   
class Person:     
    \#private variable   
    \_\_name = ""   
    count = 0   
    def setname(self,name):   
        self.\_\_name = name   
    def getname(self):   
        return self.\_\_name   
    \#private method using '\_\_'   
    def \_\_greet(self):   
        print "Say hello to %s !"%self.\_\_name   
    def greet(self):   
        self.\_\_greet()   
    def inc(self):   
        \# ClassName.variableName means the variable belongs to the
Class   
        \# every instance shares the variable   
        Person.count+=1   
\#create instance   
p = Person()   
p.setname("Peter")   
p.inc()

</p>

p2 = Person()   
p2.setname("Marry")   
p2.inc()

</p>

print "Name : " , p.getname()   
\#private method \_\_Method is converted to public method
\_ClassName\_\_Method   
p.\_Person\_\_greet()   
print "Total count of person :  ", Person.count

</p>

p.count=12 \# change the variable belong to the instance P   
print p.count   
print p2.count

</p>

31、python支持多重继承，如果一个方法从多个超类继承，那么必须要注意一下超类的顺序（在class语句中）：先继承的类中方法会重写后继承的类中的方法，也就是后来将自动忽略同名的继承。
  
32、使用hasattr(tc,'talk') 判断对象tc时候包含talk属性；
使用callable(getattr(tc,'talk',None))
判断对象tc的talk属性是否可以调用，但是在python3.0之后，callable方法已经不再使用了，可以使用hasattr(x,'\_\_call\_\_')代替callable(x)；使用setattr可以动态设置对象的属性，setattr(tc,'talk',speek)
  
33、try：  except： else:    finally:   
可以捕捉多个异常，多个异常用元组进行列出，并且可以捕捉对象，   
def test():   
    while True:   
        try:   
            x = raw\_input("Please input the x: ")   
            y = raw\_input("Please input the y: ")   
            print int(x)//int(y)   
        except ZeroDivisionError as e:   
            print "The second number can not be zero"   
            print e   
        else:   
            print "Nothing exception has happened!"   
        finally:   
            print "Clean up . It will be executed all the time"   
34、异常和函数：在函数内引发异常时，它就会被传播到函数调用的地方(对于方法也是一样)   
  
35、构造方法:def \_\_init\_\_(self , arguments)   
36、子类不会自动调用父类的构造方法   
37、查看模块包含的内容可以使用dir函数，它会将对象（以及模块的所有函数、类、变量等）的所有特性列出.\_\_all\_\_变量定义了模块的共有接口（public
interface）。更准确的说，它告诉解释器：从模块导入所有名字代表什么含义。eg：
form copy import \*
代码你只能访问\_\_all\_\_所定义的接口，而如果想访问其他接口的话，就必须显式地实现，from
copy import PyStringMap

</p>

38、shelve模块的简单使用   
'''   
Created on 2011-12-11   
A demo for shelve   
@author: Peter   
'''   
import shelve

</p>

def store\_person(db):   
    pid = raw\_input("Enter the unique id for the person : ")   
    if pid in db :   
        print "The id exists , please change "   
        return   
    person = {}   
    person['name'] = raw\_input("Enter the name of the person : ")   
    person['age'] = raw\_input("Enter the age of the person : ")   
    person['phone'] = raw\_input("Enter the phone number of the person :
")   
    db[pid] = person   
      
def lookup\_person(db):   
    pid = raw\_input("Enter the id : ")   
    if pid not in db :   
        print "This is no that person"   
        return   
    field = raw\_input("What would you like to know ? (name,age,phone) :
")   
    field = field.strip().lower()   
    print field.capitalize()+":"+db[pid][field]   
      
def enter\_command():   
    cmd = raw\_input("Enter command : ")   
    cmd = cmd.strip().lower()   
    return cmd

</p>

def main():   
    database = shelve.open("database.bat")   
    try:   
        while True:   
            cmd = enter\_command()   
            if cmd == 'store':   
                store\_person(database)   
            elif cmd == 'lookup':   
                lookup\_person(database)   
            elif cmd == 'exit':   
                return   
    finally:   
        database.close()

</p>

if \_\_name\_\_  == '\_\_main\_\_':main()

</p>

* * * * *

</p>

 

</p>

**关于with和contextylib的用法：**

</p>

平常Coding过程中，经常使用到的with场景是（打开文件进行文件处理，然后隐式地执行了文件句柄的关闭）:

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:python;gutter:true;}
    with file('test.py','r') as f :        print f.readline()
```

</p>
<p>

</div>

</p>

　　with的作用，类似try...finally...，提供一种上下文机制，要应用with语句的类，其内部必须提供两个内置函数\_\_enter\_\_以及\_\_exit\_\_。前者在主体代码执行前执行，后则在主体代码执行后执行。as后面的变量，是在\_\_enter\_\_函数中返回的。通过下面这个代码片段以及注释说明，可以清晰明白\_\_enter\_\_与\_\_exit\_\_的用法：

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:python;gutter:false;}
#!encoding:utf-8class echo :    def output(self) :        print 'hello world'    def __enter__(self):        print 'enter'        return self #返回自身实例，当然也可以返回任何希望返回的东西    def __exit__(self, exception_type, exception_value, exception_traceback):        #若发生异常，会在这里捕捉到，可以进行异常处理        print 'exit'        #如果改__exit__可以处理改异常则通过返回True告知该异常不必传播，否则返回False        if exception_type == ValueError :            return True        else:            return Falsewith echo() as e:    e.output()    print 'do something inside'print '-----------'with echo() as e:    raise ValueError('value error')print '-----------'with echo() as e:    raise Exception('can not detect')
```

</p>
<p>

</div>

</p>

运行结果：

</p>

![][]

</p>

　　contextlib是为了加强with语句，提供上下文机制的模块，它是通过Generator实现的。通过定义类以及写\_\_enter\_\_和\_\_exit\_\_来进行上下文管理虽然不难，但是很繁琐。contextlib中的contextmanager作为装饰器来提供一种针对函数级别的上下文管理机制。常用框架如下：

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:python;gutter:false;}
from contextlib import contextmanager@contextmanagerdef make_context() :    print 'enter'    try :        yield {}    except RuntimeError, err :        print 'error' , err    finally :        print 'exit'with make_context() as value :    print value
```

</p>
<p>

</div>

</p>

　　contextlib还有连个重要的东西，一个是nested，一个是closing，前者用于创建嵌套的上下文，后则用于帮你执行定义好的close函数。但是nested已经过时了，因为with已经可以通过多个上下文的直接嵌套了。下面是一个例子：

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:python;gutter:true;}
from contextlib import contextmanagerfrom contextlib import nestedfrom contextlib import closing@contextmanagerdef make_context(name) :    print 'enter', name    yield name    print 'exit', namewith nested(make_context('A'), make_context('B')) as (a, b) :    print a    print bwith make_context('A') as a, make_context('B') as b :    print a    print bclass Door(object) :    def open(self) :        print 'Door is opened'    def close(self) :        print 'Door is closed'with closing(Door()) as door :    door.open()
```

</p>
<p>

</div>

</p>

　　运行结果：

</p>

![][1]

</p>

  []: http://images.cnitblog.com/blog/146443/201301/28171208-485f497abe3240cebdbe6efebf8bc07d.png
  [1]: http://images.cnitblog.com/blog/146443/201301/28174158-0862d4af882d462483c64b2121dcde33.png
