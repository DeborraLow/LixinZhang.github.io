Title: 信息检索中的评价指标MAP和NDCG
Date: 2015-12-06
Category: search
Tags: search

> 简单记录一下信息检索中MAP和NDCG两个关键的评价指标。

##MAP
###MAP计算
<code>MAP</code>全称Mean Average Precision，表示平均正确率。其中<code>AP</code>的计算方法如下：
$$AveP=\frac{\sum_{k=1}^{n}(P(k) \times rel(k))}{相关文档数量}$$
其中，$$$k$$$为检索结果队列中的排序位置，$$$P(k)$$$为前$$$k$$$个结果的准确率，即$$$P(k)=\frac{相关文档数量}{总文档数量}$$$，$$$rel(k)$$$表示位置$$$k$$$的文档是否相关，相关为1，不相关为0。

MAP即是将多个query对应的AP求平均。
$$MAP=\frac{\sum_{q=1}^{Q} AveP(q)}{Q}$$
Q为query的数量。

###举例
假设有两个主题，主题1有4个相关网页，主题2有5个相关网页。某系统对于主题1检索出4个相关网页，其rank分别为1, 2, 4, 7；对于主题2检索出3个相关网页，其rank分别为1,3,5。对于主题1，平均准确率为(1/1+2/2+3/4+4/7)/4=0.83。对于主题2，平均准确率为(1/1+2/3+3/5+0+0)/5=0.45。则MAP= (0.83+0.45)/2=0.64。” ——[例子来源](http://www.cnblogs.com/ywl925/archive/2013/08/16/3262209.html)

##NDCG
###NDCG定义
> Discounted cumulative gain (DCG) is a measure of ranking quality. In information retrieval, it is often used to measure effectiveness of web search engine algorithms or related applications. Using a graded relevance scale of documents in a search engine result set, DCG measures the usefulness, or gain, of a document based on its position in the result list. The gain is accumulated from the top of the result list to the bottom with the gain of each result discounted at lower ranks.


###NDCG假设
> Two assumptions are made in using DCG and its related measures.</br>
1. Highly relevant documents are more useful when appearing earlier in a search engine result list (have higher ranks)</br>
2. Highly relevant documents are more useful than marginally relevant documents, which are in turn more useful than irrelevant documents.</br>
DCG originates from an earlier, more primitive, measure called Cumulative Gain.

###NDCG计算

先说CG（Cumulative Gain，累计增益），
$$CG\_{p} = \sum\_{i=1}^{p}rel_i$$
其中，$$$p$$$为文档在搜索结果列表中的排序位置，$$$rel_i$$$为处在该位置文档的等级相关性（graded relevance）。

CG的劣势是等级相关性与位置无关，但这样并不合理，将一个相关性更高的结果替换排在前面相关性较弱的结果，应该更佳，但是CG的表现是两者无差异。因此，引入了DCG（Discounted Cumulative Gain）。
$$DCG\_{p}=\sum_{i=1}^{P} \frac{2^{rel\_i} - 1}{log\_{2}^{i+1}}$$
DCG考虑了位置的影响，表示结果位置越靠前的文档，其相关性表现对整体排序质量的影响越大。

然而，DCG仍有一个缺点，不同query返回的搜索结果数量不同，其DCG的值相差很大，是不可比的。因此，需要对DCG做一定的归一化，于是有了NDCG（Normalized DCG）。
$$NDCG_p=\frac{DCG_p}{IDCG_p}$$
其中，$$$IDCG_p$$$为搜索结果按相关性排序之后能得到的最大DCG值。

###举例
[维基百科](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)上的例子：
搜索结果为文档D1,D2,D3,D4,D5,D6，相关性分数分别为3，2，3，0，1，2，则：
$$CG_6 = 3 + 2 + 3 + 0 + 1 + 2=11$$
$$DCG_6 = \sum_{i=1}^{6} \frac{rel_i}{log_2^{i+1}}=8.10$$
按相关性排序可以得到最优结果，即最大DCG为文档按照{3，3，2，2，1，0}排序：
$$IDCG_6=8.69$$ 
$$NDCG_6 = \frac{DCG_6}{IDCG_6}=0.932$$