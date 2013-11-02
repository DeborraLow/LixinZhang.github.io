#minHash算法原理


## 相关资源
[[http://www.cnblogs.com/bourneli/archive/2013/04/04/2999767.html|利用minHash与LSH寻找相似的集合]] \\ 
[[http://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E5%93%88%E5%B8%8C|最小hash]]

##算法原理
###比较集合间的相似度
两个集合的相似度可以近似等价于，这两个集合中每个元素经过N个hash函数后取得N个最小hash值的集合的相似度
###可以理解为降维
将集合中的元素通过N个hash函数取最小hash值，相当于将含有M个值的集合S降维到N。

假设，有K个集合，每个集合有M个元素，那么传统比较两两集合的相似度需要K*(K-1)*M*M 。

如果采用minHash，假设hash函数为N个，则比较两两集合只需要K*(K-1)*N*N，而N要比M小得多，从而降低了计算复杂度


