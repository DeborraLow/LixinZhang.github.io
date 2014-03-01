Title: 设计模式学习笔记——适配器(Adapter)模式
Date: 2011-04-16 06:11
Author: 糖拌咸鱼
Slug: she-ji-mo-shi-xue-xi-bi-ji-gua-pei-qi-adaptermo-shi

**定义：**通常，客户类（clients of
class）通过类的接口访问它提供的服务。有时，现有的类（existing
class）可以提供客户类的功能需要，但是它所提供的接口不一定是客户类所期望的。这是由于现有的接口太详细或者缺乏详细或接口的名称与客户类所查找的不同等诸多不同原因导致的。在这种情况下，现有的接口需要转化（convert）为客户类期望的接口，这样保证了对现有类的重用。如果不进行这样的转化，客户类就不能利用现有类所提供的功能。适配器模式（Adapter
Pattern）可以完成这样的转化。适配器模式建议定义一个包装类，包装有不兼容接口的对象。这个包装类指的就是适配器（Adapter），它包装的对象就是适配者(Adaptee)。适配器提供客户类需要的接口，适配器接口的实现是把客户类的请求转化为对适配者的相应接口的调用。换句话说：当客户类调用适配器的方法时，在适配器类的内部调用适配者类的方法，这个过程对客户类是透明的，客户类并不直接访问适配者类。因此，适配器可以使由于借口不兼容而不能交互的类可以一起工作（work
together）。

</p>

**现实中的例子：**电脑电源连接电源线，再连接插座取得电能。电脑电源作为客户调用电源线接口，电源线作为适配器连接口形接口插座取得电能。

</p>

**分类：**适配器可以分为两类，分别为类适配器和对象适配器。

</p>

**类适配器：**类适配器是通过继承类适配者类（Adaptee
Class）实现的，另外类适配器实现客户类所需要的接口。当客户对象调用适配器类方法的时候，适配器内部调用它所继承的适配者的方法。（基于继承的概念）

</p>

**对象适配器：**对象适配器包含一个适配器者的引用（reference），与类适配器相同，对象适配器也实现了客户类需要的接口。当客户对象调用对象适配器的方法的时候，对象适配器调它所包含的适配器者实例的适当方法。（利用对象的合成）

</p>

**引用一个”深入浅出java设计模式“的一个例子：**

</p>

建立一个验证给定客户填写地址是否合法的应用。这个应用是作为大的客户数据管理应用的一部分。

</p>

1、首先定义一个地址验证的接口

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
public interface AddressValidator { public boolean isValidAddress(String address);}
```

</p>

2、定义一个USAddress的验证类，用来验证地址是否符合US标准

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
public class USAddress implements AddressValidator{   public boolean isValidAddress(String address){       //对address逻辑逻辑验证     return true; }}
```

</p>

3、USAddress类实现AddressValidator接口，因此使用USAddress实例作为验证客户地址过程的一部分是没有任何问题的。

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
public class Customer {   String CustomerType; String Address;  public Customer(String type,String address){     this.CustomerType=type;      this.Address=address;    }    public boolean isValidAddress(){     AddressValidator validator;      validator=getValidator(CustomerType);        return validator.isValidAddress(Address);    }    private AddressValidator getValidator(String type){      AddressValidator validator = null;       if(type.equals("US")){           validator=new USAddress();       }        return validator;    }}
```

</p>

4、接下来问题来了，如果现在要添加一个加拿大地址的验证类的话，该怎么办呢？可以自己定义一个CAAddress类然后实现AddressValidator接口，再去编辑逻辑的验证代码。但是如果现在的情况是，已经有一个写好的工具类，但是它提供的接口不能直接用于Customer类的使用，例如下面的类：

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
public class CAAddress {  public boolean isValidCanadianAddr(String address){      //对address进行逻辑验证     return true; }}
```

</p>

这时候，我们只有两种解决方法，一种方法是改变CAAdress类的接口，但是可能会有其他的应用正在使用CAAdress类的这种形式。改变CAAdress类接口会影响现在使用CAAdress类的客户。另一种方法是应用适配器模式，类适配器CAAdressAdapter可以继承CAAdress类实现AddressValidator接口。

</p>

我们建立一个适配器类，用于将CAAdress的接口转换为Customer所期望的接口。

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
public class CAAddressAdapter extends CAAddress implements AddressValidator{   @Override    public boolean isValidAddress(String address) {      //调用父类CAAddress中的验证方法        return isValidCanadianAddr(address); }   }
```

</p>

5、我们再修改一下Customer类中getValidator的方法，应用CAAddressAdapter设计和对AddressValidator（声明期望的接口）对象的多态调用使Customer可以利用接口不兼容CAAddress类提供的服务。

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
private AddressValidator getValidator(String type){    AddressValidator validator = null;   if(type.equals("US")){       validator=new USAddress();   }else if(type.equals("Canada")){     validator= new CAAddressAdapter();   }    return validator;}
```

</p>

6、上面讨论的都是类适配器，也就是说是通过继承的方式进行接口转换的。接下来，我们来看看对象适配器。

</p>

首先将AddressValidator
定义为抽象类，然后定义CAAddressAdapter类extends该抽象类，由于java并不支持多继承，所以Adapter不能再继承CAAdress类了，那么就利用对象组合的这个概念，将CAAdresss类作为Adapter的一个成员，在类内部进行方法的调用。

</p>
<p>
``` {.brush: .java; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
class CAAddressAdapter extends AddressValidator {   private CAAddress objCAAddress;   public CAAddressAdapter(CAAddress address) {     objCAAddress = address;   }   public boolean isValidAddress(String address) {     return objCAAddress.isValidCanadianAddr(address);   } }
```

</p>

这样也会使得Customer使用相同类型的接口了。

</p>

**总结一下：**适配器可以将一个类的接口和另一个类的接口匹配起来，使用的前提是你不能或不想修改原来的适配器的母接口。适配器模式可以避免修改接口不同的代码，而进行代码的高效复用。

</p>

