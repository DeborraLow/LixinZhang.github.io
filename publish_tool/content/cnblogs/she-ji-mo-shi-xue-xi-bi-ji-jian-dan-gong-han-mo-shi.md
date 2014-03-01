Title: 设计模式学习笔记——简单工厂模式
Date: 2011-04-15 08:27
Author: 糖拌咸鱼
Slug: she-ji-mo-shi-xue-xi-bi-ji-jian-dan-gong-han-mo-shi

  **<span size="4" style="font-size: medium;">简单工厂模式：</span>**

</p>

<span size="4" style="font-size: medium;">** **<span size="3"
style="font-size: small;">**定义：**专门定义一个类来负责创建其他类的实例，被创建的实例通常都具有共同的父类。简单工厂模式又被称为静态工厂模式，属于类的创建型模式。其实质是
由一个工厂类根据传入的参量，动态决定应该创建出哪一个产品类的实例，但简单工厂模式并不是23种设计模式。</span></span>

</p>

<span size="3"
style="font-size: small;"> **参与者：**简单工厂模式主要设计三个参与者（工厂角色，抽象产品角色，具体产品角色）</span>

</p>

<span size="3" style="font-size: small;"> **一个实例：**</span>

</p>

<span size="3" style="font-size: small;">** **
在校园里，无论是老师还是学生，一般都会有一个id号码，用于登录校园内的各种门户系统。所以，经常会遇到用用户的id号码来区别用户身份，并创建用户对象的问题。</span>

</p>

<span size="3"
style="font-size: small;">1、首先建立一个抽象类SchoolUser，用做学生和教师的父类。</span>

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
package SimpleFacotryTest;public abstract class SchoolUser {    public String UserName="";   public String UserType="";   public abstract void Describe();}
```

</p>

<span size="3" style="font-size: small;"> </span>

</p>

<span size="3"
style="font-size: small;">2、创建具体类Teacher和Student，两个具体类的构造函数是通过传递id值来获取用户的详细信息的。</span>

</p>

<span size="3" style="font-size: small;">Student:</span>

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
package SimpleFacotryTest;public class Student extends SchoolUser{   public Student(String id)    {        //通过id查询详细信息     this.UserName="Tom";     this.UserType="Student"; }    public void Describe()   {        System.out.println("User "+this.UserName+" is "+this.UserType);  }}
```

</p>

<span size="3" style="font-size: small;">Teacher：</span>

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
package SimpleFacotryTest;public class Teacher extends SchoolUser{  public Teacher(String id )   {        //通过id查询详细信息     this.UserName="Peter";       this.UserType="Teacher"; }    public void Describe()   {        System.out.println("User "+this.UserName+" is a "+this.UserType);    }}
```

</p>

<span size="3"
style="font-size: small;">3、接下来就要开始实现我们的工厂了。正如我们前面在定义里所说的一样，简单工厂是通过传进的参数来动态决定应该创建出哪一个产品类的实例。那么他就需要一个逻辑判断的过程，具体问题具体分析。</span>

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
package SimpleFacotryTest;public class Factory { public static SchoolUser createUser(String id){      //假设id为11111的为学生号码，id为00000的为老师的号码       //编写逻辑判断     if(id.equals("11111")){          return new Student(id);      }else if (id.equals("00000")){           return new Teacher(id);      }else {          return null;     }    }}
```

</p>

<span size="3"
style="font-size: small;">4、以上三步已经实现了简单工厂模式的设计原理。接下来，我们来创建一个客户端去使用该工厂。</span>

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
package SimpleFacotryTest;import java.util.Scanner;;public class Client {   public static void main(String[] args) {     Scanner scanner = new Scanner(System.in);        String id="";        while(true){         id = scanner.next();         SchoolUser user = Factory.createUser(id);            if(user==null) {             System.out.println("不存在该号码的用户");         }else{               user.Describe();         }        }    }}
```

</p>

5、看一下运行结果：

</p>

[![QQ截图未命名][]][]

</p>

6、最后总结一下：

</p>

     
通过上面这个简单的例子，可以看得出来，在简单工厂模式中。工厂类是整个模式的关键所在，它包含必要的判断逻辑，能够根据外界给定的信息，决定究竟应该创建哪个具体类的对象。通过使用工厂类，外界可以从直接创建具体产品对象的尴尬局面中摆脱出来，仅仅需要负责“消费”对象就可以了，而不必管这些对象究竟是如何创建的具体细节，这样就明确区分了各自的职责和权力，有利于整个软件体系结构的优化。

</p>

<span size="3" style="font-size: small;">    
但是由于工厂类集中了所有实例的创建逻辑，很容易违反GRASPR的高内聚的责任分配原则。将全部创建逻辑都集中在了一起，使得逻辑变得十分负责，而且当有新产品加入时，会进行大量代码的修改工作，对系统的扩展和维护也非常不利。</span>

</p>

  [QQ截图未命名]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104151627038211.jpg
    "QQ截图未命名"
  [![QQ截图未命名][]]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104151627031243.jpg
