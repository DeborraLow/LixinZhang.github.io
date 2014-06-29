# Techniques, Idioms, Patterns
##将constructor和non-member function虚拟化

默认构造函数是不能声明为虚函数的，那么当有根据不同上下文构造新对象的场景时，需要使用到一些技术来替代。

###所谓的virtual constructor
文中提及的这类<code>virtual constructor</code>方法，是根据输入的不同数据产生出不同的类型的对象。
```cpp
class NLComponent; //包含虚函数
class TextBlock : public NLComponent;
class Graphic: public NLComponent;
class NewsLetter{
public:
    list<NLComponent *> components;
    NewsLetter(iostream & str){
        while(str){
            components.push_back(makeComponent(str));
        }
    }
};
```
这里要求NLComponent包含虚函数，以支持多态机制。

###所谓的virtual copy constructor

基类，定义一个纯虚函数<code>clone</code>, 用于继承类产生一个新对象。
这里值得注意的是，基类中的返回类型为<code>NLComponent *</code>，而继承类中的返回类型为各种类指针，由于多态机制才可以这么实现的。<code>pay attention</code>.

```cpp
class NLComponent{
    virtual NLComponent * clone() const = 0;
};
class TextBlock : public NLComponent{
    virtual TextBlock * clone() const {
        return new TextBlock(*this);
    }
};
class Graphic: public NLComponent{
    virtual Graphic * clone() const {
        return new Graphic(*this);
    }
};

class NewsLetter{
public:
    list<NLComponent *> components;
    NewsLetter(iostream & str){
        while(str){
            components.push_back(makeComponent(str));
        }
    }
    NewsLetter(NewsLetter & rhs){
        for component in rhs.components {
            components.push_back(item.clone())
        }
    }
};
```

###将一个非成员函数虚拟化
总体原则是，利用一个虚拟化的非成员函数来实现具体的功能，然后在用非成员函数来调用它，例子如下：

```cpp
class NLComponent{
    virtual ostream& print(ostream &) const = 0;
};
class TextBlock : public NLComponent{
    virtual ostream& print(ostream &) const{};

};
class Graphic: public NLComponent{
    virtual ostream& print(ostream &) const{};
};

inline ostream & operator<<(ostream &, const NLComponent & c);
```
