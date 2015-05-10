Title: 设计模式学习笔记——抽象工厂（Abstract Factory）模式
Date: 2011-04-15 12:41
Author: 糖拌咸鱼
Slug: she-ji-mo-shi-xue-xi-bi-ji-chou-xiang-gong-han-abstract-factorymo-shi

本文章转自<http://blog.csdn.net/ipqxiang/archive/2007/12/20/1955677.aspx> 

</p>

感觉讲解得很详细。

</p>

#### <span style="font-weight: bold;">一、 抽象工厂（Abstract Factory）模式</span>

</p>

抽象工厂模式是所有形态的工厂模式中最为抽象和最具一般性的一种形态。

</p>

为了方便引进抽象工厂模式，引进一个新概念：**产品族（Product
Family）。**所谓产品族，是指位于不同产品等级结构，功能相关联的产品组成的家族。如图：

</p>

[![Pic44][]][]

</p>

图中一共有四个产品族，分布于三个不同的产品等级结构中。只要指明一个产品所处的产品族以及它所属的等级结构，就可以唯一的确定这个产品。

</p>

引进抽象工厂模式

</p>

所谓的抽象工厂是指一个工厂等级结构可以创建出分属于不同产品等级结构的一个产品族中的所有对象。如果用图来描述的话，如下图：

</p>

[![Pic45][]][]

</p>

#### <span style="font-weight: bold;"> </span>

</p>

#### <span style="font-weight: bold;">二、 Abstract Factory模式的结构：</span>

</p>

[![Pic46][]][]

</p>

图中描述的东西用产品族描述如下：

</p>

[![Pic47][]][]

</p>

<span color="#c0504d" style="color: #c0504d;">抽象工厂（Abstract
Factory）角色</span>：担任这个角色的是工厂方法模式的核心，它是与应用系统商业逻辑无关的。

</p>

<span color="#c0504d" style="color: #c0504d;">具体工厂（Concrete
Factory）角色</span>：这个角色直接在客户端的调用下创建产品的实例。这个角色含有选择合适的产品对象的逻辑，而这个逻辑是与应用系统的商业逻辑紧密相关的。

</p>

<span color="#c0504d" style="color: #c0504d;">抽象产品（Abstract
Product）角色</span>：担任这个角色的类是工厂方法模式所创建的对象的父类，或它们共同拥有的接口。

</p>

<span color="#c0504d" style="color: #c0504d;">具体产品（Concrete
Product）角色</span>：抽象工厂模式所创建的任何产品对象都是某一个具体产品类的实例。这是客户端最终需要的东西，其内部一定充满了应用系统的商业逻辑。

</p>

#### <span style="font-weight: bold;"> </span>

</p>

#### <span style="font-weight: bold;">三、 程序举例：</span>

</p>

该程序演示了抽象工厂的结构，本身不具有任何实际价值。

</p>
<p>
``` {.brush: .csharp; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
// Abstract Factory pattern -- Structural example  using System;// "AbstractFactory"abstract class AbstractFactory{  // Methods  abstract public AbstractProductA CreateProductA();  abstract public AbstractProductB CreateProductB();}// "ConcreteFactory1"class ConcreteFactory1 : AbstractFactory{  // Methods  override public AbstractProductA CreateProductA()  {    return new ProductA1();  }  override public AbstractProductB CreateProductB()  {    return new ProductB1();  }}// "ConcreteFactory2"class ConcreteFactory2 : AbstractFactory{  // Methods  override public AbstractProductA CreateProductA()  {    return new ProductA2();  }  override public AbstractProductB CreateProductB()  {    return new ProductB2();  }}// "AbstractProductA"abstract class AbstractProductA{}// "AbstractProductB"abstract class AbstractProductB{  // Methods  abstract public void Interact( AbstractProductA a );}// "ProductA1"class ProductA1 : AbstractProductA{}// "ProductB1"class ProductB1 : AbstractProductB{  // Methods  override public void Interact( AbstractProductA a )  {    Console.WriteLine( this + " interacts with " + a );  }}// "ProductA2"class ProductA2 : AbstractProductA{}// "ProductB2"class ProductB2 : AbstractProductB{  // Methods  override public void Interact( AbstractProductA a )  {    Console.WriteLine( this + " interacts with " + a );  }}// "Client" - the interaction environment of the productsclass Environment{  // Fields  private AbstractProductA AbstractProductA;  private AbstractProductB AbstractProductB;  // Constructors  public Environment( AbstractFactory factory )  {    AbstractProductB = factory.CreateProductB();    AbstractProductA = factory.CreateProductA();  }   // Methods  public void Run()  {    AbstractProductB.Interact( AbstractProductA );  }}/// <summary>/// ClientApp test environment/// </summary>class ClientApp{  public static void Main(string[] args)  {    AbstractFactory factory1 = new ConcreteFactory1();    Environment e1 = new Environment( factory1 );    e1.Run();    AbstractFactory factory2 = new ConcreteFactory2();    Environment e2 = new Environment( factory2 );    e2.Run();  }}
```

</p>

#### <span style="font-weight: bold;">四、 在什么情形下使用抽象工厂模式：</span>

</p>

在以下情况下应当考虑使用抽象工厂模式：

</p>

-   一个系统不应当依赖于产品类实例如何被创建、组合和表达的细节，这对于所有形态的工厂模式都是重要的。
-   这个系统有多于一个的产品族，而系统只消费其中某一产品族。
-   同属于同一个产品族的产品是在一起使用的，这一约束必须在系统的设计中体现出来。
-   系统提供一个产品类的库，所有的产品以同样的接口出现，从而使客户端不依赖于实现。

</p>

#### <span style="font-weight: bold;">五、 抽象工厂的起源</span>

</p>

据说最早的应用是用来创建在不同操作系统的视窗环境下都能够运行的系统。比如在Windows与Unix系统下都有视窗环境的构件，在每一个操作系统中，都有一个视窗构件组成的构件家族。我们可以通过一个抽象角色给出功能描述，而由具体子类给出不同操作系统下的具体实现，如图：

</p>

[![Pic48][]][]

</p>

可以发现上面产品类图有两个产品等级结构，分别是Button与Text；同时有两个产品族：Unix产品族与Windows产品族。

</p>

[![Pic49][]][]

</p>

系统对产品对象的创建要求由一个工厂的等级结构满足。其中有两个具体工厂角色，即UnixFactory和WinFactory。UnixFactory对象负责创建Unix产品族中的产品，而WinFactory负责创建Windows产品族中的产品。

</p>

[![Pic50][]][]

</p>

显然一个系统只能够在某一个操作系统的视窗环境下运行，而不能同时在不同的操作系统上运行。所以，系统实际上只能消费属于同一个产品族的产品。

</p>

在现代的应用中，抽象工厂模式的使用范围已经大大扩大了，不再要求系统只能消费某一个产品族了。

</p>

#### <span style="font-weight: bold;">六、 Abstract Factory模式在实际系统中的实现</span>

</p>

Herbivore：草食动物

  
Carnivore：食肉动物

  
Bison：['baisn]，美洲或欧洲的野牛

</p>

下面实际代码演示了一个电脑游戏中创建不同动物的抽象工厂。尽管在不同大陆下动物物种是不一样的，但动物间的关系仍然保留了下来。

</p>
<p>
``` {.brush: .csharp; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
// Abstract Factory pattern -- Real World example  using System;// "AbstractFactory"abstract class ContinentFactory{  // Methods  abstract public Herbivore CreateHerbivore();  abstract public Carnivore CreateCarnivore();}// "ConcreteFactory1"class AfricaFactory : ContinentFactory{  // Methods  override public Herbivore CreateHerbivore()  { return new Wildebeest(); }  override public Carnivore CreateCarnivore()  { return new Lion(); }}// "ConcreteFactory2"class AmericaFactory : ContinentFactory{  // Methods  override public Herbivore CreateHerbivore()  { return new Bison(); }  override public Carnivore CreateCarnivore()  { return new Wolf(); }}// "AbstractProductA"abstract class Herbivore{}// "AbstractProductB"abstract class Carnivore{  // Methods  abstract public void Eat( Herbivore h );}// "ProductA1"class Wildebeest : Herbivore{}// "ProductB1"class Lion : Carnivore{  // Methods  override public void Eat( Herbivore h )  {    // eat wildebeest    Console.WriteLine( this + " eats " + h );  }}// "ProductA2"class Bison : Herbivore{}// "ProductB2"class Wolf : Carnivore{  // Methods  override public void Eat( Herbivore h )  {    // Eat bison    Console.WriteLine( this + " eats " + h );  }}// "Client"class AnimalWorld{  // Fields  private Herbivore herbivore;  private Carnivore carnivore;  // Constructors  public AnimalWorld( ContinentFactory factory )  {    carnivore = factory.CreateCarnivore();    herbivore = factory.CreateHerbivore();  }  // Methods  public void RunFoodChain()  { carnivore.Eat(herbivore); }}/// <summary>///  GameApp test class/// </summary>class GameApp{  public static void Main( string[] args )  {    // Create and run the Africa animal world    ContinentFactory africa = new AfricaFactory();    AnimalWorld world = new AnimalWorld( africa );    world.RunFoodChain();    // Create and run the America animal world    ContinentFactory america = new AmericaFactory();    world = new AnimalWorld( america );    world.RunFoodChain();  }}
```

</p>

#### <span style="font-weight: bold;">七、 "开放－封闭"原则</span>

</p>

"开放－封闭"原则要求系统对扩展开放，对修改封闭。通过扩展达到增强其功能的目的。对于涉及到多个产品族与多个产品等级结构的系统，其功能增强包括两方面：

</p>

增加产品族：Abstract Factory很好的支持了"开放－封闭"原则。

</p>

增加新产品的等级结构：需要修改所有的工厂角色，没有很好支持"开放－封闭"原则。

</p>

综合起来，抽象工厂模式以一种倾斜的方式支持增加新的产品，它为新产品族的增加提供方便，而不能为新的产品等级结构的增加提供这样的方便。

</p>

  [Pic44]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041125614.gif
    "Pic44"
  [![Pic44][]]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041124185.gif
  [Pic45]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041124218.gif
    "Pic45"
  [![Pic45][]]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041121710.gif
  [Pic46]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041139235.gif
    "Pic46"
  [![Pic46][]]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041126727.gif
  [Pic47]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041136203.gif
    "Pic47"
  [![Pic47][]]: http://images.cnblogs.com/cnblogs_com/coser/201104/20110415204113107.gif
  [Pic48]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041133172.gif
    "Pic48"
  [![Pic48][]]: http://images.cnblogs.com/cnblogs_com/coser/201104/20110415204113663.gif
  [Pic49]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041134284.gif
    "Pic49"
  [![Pic49][]]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041138188.gif
  [Pic50]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041135713.gif
    "Pic50"
  [![Pic50][]]: http://images.cnblogs.com/cnblogs_com/coser/201104/201104152041135157.gif
