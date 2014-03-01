Title: 设计模式学习笔记——桥接(Bridge)模式
Date: 2011-04-16 08:44
Author: 糖拌咸鱼
Slug: she-ji-mo-shi-xue-xi-bi-ji-qiao-jie-bridgemo-shi

学习桥接模式时，参考了云飞龙行的“研磨设计模式之桥接模式”一文，感觉作者讲得很好，清晰易懂。

</p>

该文地址：<http://www.cnblogs.com/sjms/archive/2010/09/01/1814718.html>

</p>

桥接模式：

</p>

**定义：**将抽象部分与它的实现部分分离，使它们都可以独立地变化。所谓桥接，通俗点说就是在不同的东西之间搭一个桥，让他们能够连接起来，可以相互通讯和使用。那么在桥接模式中到底是给什么东西来搭桥呢？就是为被分离了的抽象部分和实现部分来搭桥。**在桥接模式中的桥接是单向的**，也就是只能是抽象部分的对象去使用具体实现部分的对象，而不能反过来，也就是个单向桥。

</p>

模式结构和说明：

</p>

[![2010090609125164][]][]

</p>

**说明：**

</p>

**Abstraction：**

</p>

抽象部分的接口。通常在这个对象里面，要维护一个实现部分的对象引用，在抽象对象里面的方法，需要调用实现部分的对象来完成。这个对象里面的方法，通常都是跟具体的业务相关的方法。

</p>

**RefinedAbstraction：**

</p>

扩展抽象部分的接口，通常在这些对象里面，定义跟实际业务相关的方法，这些方法的实现通常会使用Abstraction中定义的方法，也可能需要调用实现部分的对象来完成。

</p>

**Implementor：**

</p>

定义实现部分的接口，这个接口不用和Abstraction里面的方法一致，通常是由Implementor接口提供基本的操作，而Abstraction里面定义的是基于这些基本操作的业务方法，也就是说Abstraction定义了基于这些基本操作的较高层次的操作。

</p>

**ConcreteImplementor：**

</p>

真正实现Implementor接口的对象。

</p>

（1）先看看Implementor接口的定义，示例代码如下：

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
/** * 定义实现部分的接口，可以与抽象部分接口的方法不一样 */public interface Implementor { /**   * 示例方法，实现抽象部分需要的某些具体功能   */  public void operationImpl();}
```

</p>

（2）再看看Abstraction接口的定义，注意一点，虽然说是接口定义，但其实是实现成为抽象类。示例代码如下：

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
/** * 定义抽象部分的接口 */public abstract class Abstraction {    /**   * 持有一个实现部分的对象    */  protected Implementor impl;  /**   * 构造方法，传入实现部分的对象     * @param impl 实现部分的对象    */  public Abstraction(Implementor impl){        this.impl = impl;    }    /**   * 示例操作，实现一定的功能，可能需要转调实现部分的具体实现方法     */  public void operation() {        impl.operationImpl();    }}
```

</p>

（3）该来看看具体的实现了，示例代码如下：

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
/** * 真正的具体实现对象 */public class ConcreteImplementorA implements Implementor {   public void operationImpl() {        //真正的实现  }}
```

</p>
<p>
    另外一个实现，示例代码如下：

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
/** * 真正的具体实现对象 */public class ConcreteImplementorB implements Implementor {  public void operationImpl() {        //真正的实现  }}
```

</p>

（4）最后来看看扩展Abstraction接口的对象实现，示例代码如下：

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
/** * 扩充由Abstraction定义的接口功能 */public class RefinedAbstraction extends Abstraction { public RefinedAbstraction(Implementor impl) {        super(impl); }    /**   * 示例操作，实现一定的功能   */  public void otherOperation(){        //实现一定的功能，可能会使用具体实现部分的实现方法，      //但是本方法更大的可能是使用Abstraction中定义的方法，        //通过组合使用Abstraction中定义的方法来完成更多的功能    }}
```

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
（5）一个测试类：
```

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
public class Test{  public static void main(String [] args){     ConcreteImplementorA implA = new ConcreteImplementorA();     ConcreteImplementorB implB = new ConcreteImplementorB();     RefinedAbstraction client = new RefinedAbstraction(implA);       client.operation();//调用implA方法       client=new RefinedAbstraction(implB);        client.operation();//调用implB方法   }}
```

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
实现了抽象和实现的完美分离。
```

</p>

  [2010090609125164]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104161643328618.gif
    "2010090609125164"
  [![2010090609125164][]]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104161643324473.gif
