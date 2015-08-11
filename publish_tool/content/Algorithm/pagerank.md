Title: Pagerank及简单的map-reduce实现
Date: 2015-08-11 21:53
Category: Algorithm

> <code>Pagerank</code>家喻户晓，网上的介绍性文章很多，这里就不在多说了，主要记录下map-reduce实现方法。

##Pagerank 简单介绍

Pagerank将每个页面抽象表达为一个结点，如果有一个页面$$$a$$$包含有一个或多个链接指向另一个页面$$$b$$$，那么表示页面$$$a$$$对页面$$$b$$$的重要性进行了认可，为其投了一票。这种关系，可以抽象为图结构中的一条有向边。然后通过能力传递的观点，每个结点会将自己的权重分发给其指向的结点，经过多轮的迭代，完成最后的收敛，最后得到各自的pagerank分值。

Pagerank的一般形式表达为：
$$PR(u) = (1-d) + d \cdot \sum\_{v \in B(u)} PR(v)$$

其中，$$$PR(u)$$$表示结点u的pagerank分数，$$$B(u)$$$表示指向u的结点集合。参数$$$d$$$用来解决当没有结点指向$$$u$$$时的情况，如果不设置，则会出现最终结点收敛为0的情况，一般设置$$$d=0.85$$$。

这里假设的是在Pagerank图结构里，每条边的权重是一样的，然而在现实问题当中并非如此，比如一个页面a中存在10条链接，9条指向b，1条指向c，那么a应该分配比a更多的权重给b。因此，一个稍微改进的版本如下：
$$PR(u) = (1-d) + d \cdot \sum\_{v \in B(u)} PR(v) * weight\_{v->u}$$
用$$$weight\_{v->u}$$$来衡量边的权重。

##Pagerank的streaming版本的map-reduce实现
###原始输入数据格式
其中，每一行表示
<pre>
a b 0.3
a d 0.4
a c 0.3
d b 0.5
</pre>
###数据预处理
####people_rank_pre_processing_mapper.py
    ::python
    #!/usr/bin/python
    import sys
    for line in sys.stdin :
        uin, to_uin, weight = line.strip().split()
        #key -> uin_peoplerank
        key = "%s_%s" % (uin, "1.0")
        #value -> touin_weight
        value = "%s_%s" % (to_uin, weight)
        print key, value

####people_rank_pre_processing_reducer.py
    ::python
    #!/usr/bin/python
    import sys

    uin2uinlist = {}
    for line in sys.stdin :
        key, value = line.strip().split()
        if key not in uin2uinlist :
            uin2uinlist[key] = []
        uin2uinlist[key].append(value)

    for key in uin2uinlist :
        print key, ",".join(uin2uinlist[key])
       
####输出格式
<pre>
a_1.0 b_0.3,d_0.4,c_0.3
d_1.0 b_0.5
</pre>

###一轮的Pagerank迭代
接预处理的输出为输入。
####people_rank_mapper.py
    ::python
    #!/usr/bin/python
    import sys

    """
    PeopleRank is similar to PageRank
    PeopleRank assign different weight to different edges according to votes count.
    PR(u) = (1-d) + d * sum_{v \in B(u)} PR(v) * weight_{v->u}
    """

    for line in sys.stdin :
        curuin, touinlist = line.strip().split()
        uin, rank = curuin.split("_")
        rank = float(rank)
        touinlist = [item.split("_") for item in touinlist.split(",")]
        #assign uin's score to its point-to-uins by score * weight
        for item in touinlist :
            touin, weight = item[0], float(item[1])
            print "%s\t%s" % (touin, "score:%f" % (rank * weight))
        print "%s\t%s" % (uin, "list:%s" % touinlist)
    
####people_rank_reducer.py
    ::python
    #!/usr/bin/python
    import sys

    uin_to_sum_rank = {}
    line_to_be_updated = {}

    d = 0.85

    for line in sys.stdin :
        uin, value = line.strip().split("\t")
        tag, val = value.split(":")
        if tag == "list" :
            line_to_be_updated[uin] = val
        elif tag == "score" :
            if uin not in uin_to_sum_rank :
                uin_to_sum_rank[uin] = 0.0
            uin_to_sum_rank[uin] += float(val)
        else :
            pass

    #update PeopleRank score
    for uin in line_to_be_updated :
        if uin not in uin_to_sum_rank :
            newRank = (1-d)
        else:
            newRank = (1-d) + uin_to_sum_rank[uin] * d
        print "%s_%f" % (uin, newRank), line_to_be_updated[uin]
    
####输出格式
<pre>
a_0.150000 [['b', '0.3'], ['d', '0.4'], ['c', '0.3']]
d_0.490000 [['b', '0.5']]
</pre>

###Controller
由于pagerank算法是一个多轮迭代的过程，因此
