Title: kfaka学习笔记
Date: 2014-06-12 10:20
Category: opensource
Tags: kafka

##What is kafka?
> Apache Kafka is publish-subscribe messaging rethought as a distributed commit log.
> Kafka is a distributed, partitioned, replicated commit log service. It provides the functionality of a messaging system, but with a unique design.

![http://kafka.apache.org/images/producer_consumer.png](http://kafka.apache.org/images/producer_consumer.png)

1. <code>Producer</code> 向kafka通过push的方式发送message，这些message会有一个category label 叫做<code>topics</code> ,也就是说Producer通过指定的topic向kafka server发送message。
2. <code>Consumer</code>节点通过订阅对应的topic，来从kafka cluster上pull数据，message，Cosumer节点与kafka cluster之间是通过<code>zookeeper</code>来协调的。
3. <code>kafka cluster</code> 包含多个servers，被叫做<code>broker</code>节点。

##Key Components
####Topics, Logs, partition
在Kafka cluster上，每个Topic会对应多个<code>partitioned logs</code>，partitioned的log很适合多路负载，如下图：

![http://kafka.apache.org/images/log_anatomy.png](http://kafka.apache.org/images/log_anatomy.png)

在kafka server上，每个log会维护一个<code>offset</code>，用来记录数据已经读进的位置，consumer也维护一个<code>offset</code>，用来记录数据consumed的进度。

Kafka cluster会存储一段时间内的（可配置）的所有published的message，不管这些message是否已经被consume了。那么，对于<code>consumer</code>节点的offset不一定只是递增，kafka允许其在任意合法位置进行reprocess。

对于每个partition，会有一个leader server以及零或多个（靠配置，用来做replication）followers server来handle。当leader挂掉，follower会接过处理任务，保证不会有数据丢失

####Producer & Consumer