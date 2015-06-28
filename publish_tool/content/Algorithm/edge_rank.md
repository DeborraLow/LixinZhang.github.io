Title: Facebook的Feeds排序算法-EdgeRank
Date: 2015-06-28 21:44
Category: Algorithm

> 在做朋友圈互动率的预估，做了一些关于Edgerank的调研工作。

<code>EdgeRank</code>是Facebook早期的Feed Ranking算法，用来解决每个用户的Feeds流中的不同Feed间的排序问题。由于其涉及商业信息，Facebook并为向外公布其具体的排序算法。目前，网络上有的资料大多是根据Facebook某次会议上的演讲内容，推测出的算法过程。

<img src='http://lixinzhang.github.io/image/edge_rank.png'></img>

EdgeRank里的Edge是指好友对某条feed的一个行为（action），具体可以包括创建这条feed，对这条feed进行点赞、评论、点击等。如果好友对某条feed产生了一次action，那么就建立了一条边（edge）。EdgeRank认为影响feed排序的相对位置，主要跟三个因素有关，分别是<code>用户间的亲密度</code>$$$u_e$$$，<code>edge的权重</code>$$$w_e$$$以及这条边产生的<code>时间衰减因子</code>$$$d_e$$$。EdgeRank将$$$u_e$$$，$$$w_e$$$，$$$d_e$$$进行连乘，并按edge累加，得到edgerank分值，如下述公式所示：
$$edgerank = \sum_{e \in edges} u_e \cdot w_e \cdot d_e$$
这三个影响因素都比较容易理解：越亲密的用户，发生Feed的互动可能性越高；不同edge具有不同的权重，如创建>评论>点赞>点击；而时间衰减因素则可以有效反映时间对朋友圈feed重要性影响的程度。

EdgeRank算法中，若只考虑时间因素，那么排序算法就退化为了传统的timeline形式；若只考虑Feed的创建行为，则算法就退化到了根据用户与Feed创建者的亲密度排序。

关于$$$u_e$$$，$$$w_e$$$，$$$d_e$$$这几个参数的计算，$$$w_e$$$可以通过人工经验进行标注，$$$d_e$$$可以考虑采用如下述公式的计算方法

$$d\_e = \frac{1}{1+log(T\_{cur} - T\_{edge})}$$

$$$T\_{cur}$$$ 表示当前时间，$$$T\_{edge}$$$表示edge创建时间。用户亲密度$$$u_e$$$则可以根据用户与用户间的互动情况来估计，不同场景估计方法也不一样，可以考虑挖掘社交网络图结构，比如两个用户之间的路径长度及边权重。此外，这个亲密度应该是又向的，如A对B很重要、很亲密，而B对A则不一定。

###参考资料
EdgeRank参考资料：http://edgerank.net/
