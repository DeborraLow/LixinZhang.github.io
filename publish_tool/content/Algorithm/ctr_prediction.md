Title: 点击率预估相关笔记
Date: 2016-06-26 12:53
Category: Machine Learning
Tags: ctr prediction

##什么是点击率预估？
* 点击率预估可以形式化为：$$$P(click=1|Item, User, Context)$$$
* 点击行为（点或不点）很容易刻画为一个二分类问题。
* 在计算广告领域更加受到关注，因为与收入（钱）直接挂钩。$$$bidPrice=pCTR * CPC$$$
* 在推荐系统与在线广告应用场景中，点击率预估关注的__目标__不同，在线广告中不仅关注排序性能，也会关注预估值的准确性。而对于推荐系统，我们更关心排序性能，因此$$$AUC$$$作为评估模型效果的指标是合理的。
* 其实也可以看做是一种Learning to rank问题，只不过看要学习的目标是什么。

###点击率预估方法概览
* 特征决定了所有算法效果的上限，而不同的算法只是离这个上限的距离不同而已。
* 广义线性模型 + 人工特征组合(LR + Feature Engineering), 简单，易维护。
* 非线性模型（GBDT，FM，FFM, DNN，MLR）。
* 广义线性模型 + 非线性模型组合特征。
* batch learning -> online learning (Google FTRL) 。

##Logistic Regression + Feature Engineering
> 预估$$$P(Click=1|Item, User, Context)$$$的概率.

###Logistic Regression 逻辑回归
$$L(\omega) = \sum_{i=1}^N{y_i(\omega x_i) - log(1+exp(\omega x_i))} + C \Omega(\omega)
$$

* 优势：模型简单，容易实现，优化算法成熟，模型可解释性强，易维护。
* 劣势：线性模型无法捕捉非线性规律，需要大量人工经验构造非线性的组合特征。

###特征上的一些方法
* categorical feature, ordinal feature, numberical feature，统一one-hot encoding
* 单特征处理：离散化，去冗余特征（Pearson相关性），去无用特征（信息增益），处理极度长尾（覆盖过少）
* 让模型自动进行特征选择，加入L1正则，让模型sparse。
* 人工经验特征组合，控制维数，维数太多，用hash trick进行一定程度的维数压缩。
* 点击反馈特征，用某种特征组合上的过去一段时间（时间窗口）的统计点击率作为特征，也叫做动态特征。让这个特征，随时间动起来，捕捉动态部分，来减少模型的效果衰减。 有人尝试batch + 动态特征的效果比online learning相差不多。

###模型上的一些方法
* Online Learning，Google的FTRL, 2013 KDD，让每个最新的反馈都能更新到模型上。 有人尝试，用batch的方式对模型进行warm up。FTRL-Proximal在L1正则下，稀疏性和精度都比较出色。
* Mixed Logistic Regression，这个是阿里在LR的基础上提出的分片逻辑回归算法，用来解决很多线性不可分的数据。思路，先把数据切片，在每个切片下在回归，不断迭代。
* Coupled Group Lasso，2015 ICML，阿里提出来的，也是自动去刻画user和ad间交叉关系，并且能产生稀疏解，但计算复杂度稍高。 而且貌似对业界没产生什么太大的影响。

##Factorization Machines(FM or FFM)

业界逐渐流行，在数据挖掘类竞赛中表现出色，并在工业界被很多公司证明有效。

* http://www.libfm.org/
* https://github.com/dmlc/difacto 
* https://github.com/zhengruifeng/spark-libFM 

###二阶多项式模型

$$y(X) = \omega\_0 + \sum\_{i=1}^{n} \omega\_i x_i + \sum\_{i=1}^{n} \sum\_{j=i+1}^{n} \omega\_{ij}x\_ix\_j
$$

二次项参数$$$\omega\_{ij}$$$ 可以组成一个对称阵$$$W$$$, 矩阵分解为$$$W=V^TV$$$。参数$$$\omega\_{ij}$$$ 转化为$$$<v\_i, v\_j>$$$

组合二阶特征，刻画特征间的关系，但特征维度过高。

###Factorization Machines
$$y(X) = \omega\_0 + \sum\_{i=1}^{n} \omega\_i x_i + \sum\_{i=1}^{n} \sum\_{j=i+1}^{n} <v_i, v_j> x_ix_j$$

其中，$$$v_i$$$是第i维特征的隐向量，$$$<\cdot,\cdot>$$$代表向量点积。隐向量的长度为k (k < < n)，包含k个描述特征的因子。

$$\sum\_{i=1}^{n} \sum\_{j=i+1}^{n} <v_i, v_j> x_ix_j = \frac{1}{2} \sum\_{f=1}^{k} \left( {\left( \sum\_{i=1}^{n} v\_{i,f} x_i \right)}^2 - \sum\_{i=1}^{n} {v_{i,f}}^2 {x_i}^2 \right)$$

模型参数一共有$$$nk+k+1$$$个，FM参数训练的复杂度也是$$$O(kn)$$$。

###Field-aware Factorization Machines
$$y(X) = \omega\_0 + \sum\_{i=1}^{n} \omega_i x_i + \sum\_{i=1}^{n} \sum\_{j=i+1}^{n} <v\_{i, f_j} , v_{j, f_i}> x_ix_j$$

同一类的特征，应该属于一个field，如country，有美国、中国、日本等，他们属于同一种field。
在FFM中，每一维特征$$$x_i$$$，针对其它特征的每一种"field"$$$f_j$$$，都会学习一个隐向量$$$v_{i,j}$$$。因此，隐向量不仅与特征相关，也与field相关。


##GBDT + LR
###利用GBDT构建新特征
Xinran He et al. Practical Lessons from Predicting Clicks on Ads at Facebook, 2014
<img src='http://lixinzhang.github.io/image/gbdt.png'></img>
对特征做非线性变换后，作为LR的输入。





