Title: 设计模式学习笔记——工厂方法模式
Date: 2011-04-15 11:19
Author: 糖拌咸鱼
Slug: she-ji-mo-shi-xue-xi-bi-ji-gong-han-fang-fa-mo-shi

**<span size="4" style="font-size: medium;">工厂方法模式</span>**

</p>

<span size="2"
style="font-size: x-small;">**定义：**工厂方法模式又称为工厂模式，属于类的创建型模式。在工厂方法模式中，父类负责定义创建对象的公共接口，而子类则负责生成具体的对象，这样做的目的是将类的实例化操作延迟到子类中完成，即由子类来决定究竟应该实例化哪一个类。</span>

</p>

<span size="2" style="font-size: x-small;">         
在简单工厂模式中，一个工厂类处于对产品类进行实例化的中心位置，它知道每一个产品类的细节，并决定何时哪一个产品类应当被实例化。但是，简单工厂模式的致命弱点也就是处于核心地位的工厂类。而工厂方法模式，则是创建类多个产品的工厂，从而将产品的创建过程变得分散化，避免简单工厂模式中核心工厂负担过重的问题。</span>

</p>

<span size="2"
style="font-size: x-small;">**参与者：**工厂方法模式主要涉及4个参与者：抽象工厂类、实现抽象工厂类的具体工厂类、抽象产品类和实现抽象产品类的具体产品类</span>

</p>

**<span size="2" style="font-size: x-small;">一个简单例子：</span>**

</p>

<span size="2" style="font-size: x-small;">     
仍引用上一篇简单工厂模式里举的例子。在原有基础上，做适当的修改和添加。</span>

</p>

<span size="2"
style="font-size: x-small;">1、在工厂方法模式里，关于产品部分与简单工厂模式类似，需要一个抽象产品和多个具体产品。定义SchoolUser抽象类，Teacher和Student类继承该父类。</span>

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
//定义抽象产品类，父类public abstract class SchoolUser {   public String UserName="";   public String UserType="";   public abstract void Describe();}//////////////////////////////////////////定义具体产品Studentpublic class Student extends SchoolUser{ public Student(){        this.UserName="Tom";     this.UserType="Student"; }    public void Describe(){      System.out.println("User "+this.UserName+" is "+this.UserType);  }}/////////////////////////////////////////定义具体产品Teacherpublic class Teacher extends SchoolUser{ public Teacher(){        this.UserName="Peter";       this.UserType="Teacher"; }    public void Describe(){      System.out.println("User "+this.UserName+" is a "+this.UserType);    }}
```

</p>

<span size="2"
style="font-size: x-small;">2、接下来就是与简单工厂模式不同的地方了，在简单工厂模式中所有产品的创建都集中在了一个工厂里，而工厂方法模式则是需要创建多个不同类别的工厂实例的。我们首先定义一个抽象工厂接口，其实工厂方法模式的核心</span>

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
public  interface Factory { public SchoolUser createUser();}
```

</p>

<span size="2"
style="font-size: x-small;">3、实现步骤2中的抽象工厂，定义具体的教师工厂和学生工厂</span>

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
public class TeacherFactory implements Factory{  public SchoolUser createUser(){      return new Teacher();    }}////////////////////////////////////////////////public class StudentFactory implements Factory {  public SchoolUser createUser(){      return new Student();    }}
```

</p>

<span size="2"
style="font-size: x-small;">4、最后，创建客户端进行使用测试</span>

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
public class Client {  public static void main(String[] args) {     //创建一个学生工厂，并产生一个学生实例     Factory factory;     factory = new StudentFactory();      SchoolUser student = factory.createUser();       student.Describe();      //创建一个教师工厂，并产生一个教师 实例        factory = new TeacherFactory();      SchoolUser teacher = factory.createUser();       teacher.Describe();  }}
```

</p>

<span size="2" style="font-size: x-small;">5、总结一下：</span>

</p>

<span size="2" style="font-size: x-small;">  
在工厂模式方法中，工厂方法用来创建客户所需要的产品，同时还向客户隐藏了哪种具体产品类被实例化这一细节。工厂方法模式的核心是一个抽象工厂类，各种具体工厂类通过抽象工厂类将工厂方法继承下来。基于工厂角色和产品角色的多态性设计时工厂方法模式的关键。用户只需关心抽象产品和工厂，一旦创建了一个工厂实例，就不用再理会返回的是到底哪一种具体产品，因为产品创建的具体实现细节已经被封装到了具体工厂里。</span>

</p>

<span size="2" style="font-size: x-small;">   工厂模式的另一个优点是在
系统中加入新产品时，无需修改抽象工厂和抽象产品提供的接口，无需更改客户端，也无需更改其他的具体工厂和具体产品，而只需要添加一个具体工厂和具体产品就可以了。这样，系统的可扩展性非常好。</span>

</p>

