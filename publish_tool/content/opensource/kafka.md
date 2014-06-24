Title: kafka学习笔记
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
###Topics, Logs, partition
在Kafka cluster上，每个Topic会对应多个<code>partitioned logs</code>，partitioned的log很适合多路负载，如下图：

![http://kafka.apache.org/images/log_anatomy.png](http://kafka.apache.org/images/log_anatomy.png)

在kafka server上，每个log会维护一个<code>offset</code>，用来记录数据已经读进的位置，consumer也维护一个<code>offset</code>，用来记录数据consumed的进度。

Kafka cluster会存储一段时间内的（可配置）的所有published的message，不管这些message是否已经被consume了。那么，对于<code>consumer</code>节点的offset不一定只是递增，kafka允许其在任意合法位置进行reprocess。

对于每个partition，会有一个leader server以及零或多个（靠配置，用来做replication）followers server来handle。当leader挂掉，follower会接过处理任务，保证不会有数据丢失。
###Producer
> The producer is responsible for choosing which message to assign to which partition within the topic.

因此，producer应该在与kafka server通信之后，获取到了server端设置的kafka数量，producer可以决定往哪个partition上发送message。默认，可以通过简单的轮询或者按照语义（based on some key in the message）进行负载均衡。

我觉得之所以producer可以通过制定的partition进行message的发送，是因为同一个partition上的message可以保证是有序的，而多个partition则不可以。对于顺序要求十分严格的需求，这个是必须的。

###Consumer

kafka server与consumer节点间的消息通信有两种方式：<code>Queue</code>以及<code>publish-subscribe</code>。

>  In a queue, a pool of consumers may read from a server and each message goes to one of them; in publish-subscribe the message is broadcast to all consumers. 

在kafka里，每个consumer会有一个<code>group</code>label，同处于一个group里的consumer instance，会通过<code>queue</code>的通信模型进行工作，即只会有一个consumer获取到同一topic上partition log上的message。而如果consumer instance不在一个group里，那么会以<code>publish-subscribe</code>的模式进行message广播，使得订阅同一个topic的不同组的consumer都会收到相同的message。

> Kafka is able to provide both ordering guarantees and load balancing over a pool of consumer processes.

在同一个group里，每个partition只会有一个consumer与其对应，即partition 与 consumer是多对一的关系。这样可以保证同一个partition上的message可以有序的被consume。因此，consumer的数量不应该多余partition的数量，多余的partition就空闲掉了。

另外，要记住多个partition间是无法保证全局有序性的，因此如果有全局有序性的需求，只能指定一个partition，当然也只有个consumer。



##遇到的一些问题
1. 设置partition的数量，当consumer大于partition数量时，多余的consumer不会工作。默认partition为1，所以实际工作中要改一下。
2. 注意log的生命周期设置，默认kafka server会保存一周时间内所有日志文件，因此会占用巨大的磁盘空间，根据自己实际情况，去配置文件中改一下。要不然，很容易磁盘就满了（悲剧过一次）。


##其他引用资料
来自于[Kafka：下一代分布式消息系统](http://blog.ithomer.net/2014/06/kafka-the-next-generation-of-distributed-messaging-systems/)

###Python API for Kafka

1. [https://github.com/getsamsa/samsa](https://github.com/getsamsa/samsa) 
2. [https://github.com/mumrah/kafka-python](https://github.com/mumrah/kafka-python)
		
	:::python
	
    from kazoo.client import KazooClient
    from samsa.cluster import Cluster
    import json
    import time

    zookeeper = KazooClient("budget32.rm.ne1.yahoo.com:2181")
    zookeeper.start()
    cluster = Cluster(zookeeper)
    topic = cluster.topics['demo']
    print cluster.brokers.keys()
    consumer = topic.subscribe('group-name')
    impression = 0
    for message in consumer:
        try:
            obj = json.loads(message)
            t = time.strptime(obj['timestamp'], '%Y-%m-%dT%H:%M:%S')
            if t.tm_min >= 45 & t.tm_min < 50 :
                impression += obj['impression']
            if (impression % 1000 == 0) :
                print impression
            if t.tm_min > 52:
                break
        except :
            print mssage


###kafka存储
Kafka的存储布局非常简单。话题的每个分区对应一个逻辑日志。物理上，一个日志为相同大小的一组分段文件。每次生产者发布消息到一个分区，代理就将消息追加到最后一个段文件中。当发布的消息数量达到设定值或者经过一定的时间后，段文件真正写入磁盘中。写入完成后，消息公开给消费者。

与传统的消息系统不同，Kafka系统中存储的消息没有明确的消息Id。

消息通过日志中的逻辑偏移量来公开。这样就避免了维护配套密集寻址，用于映射消息ID到实际消息地址的随机存取索引结构的开销。消息ID是增量的，但不连续。要计算下一消息的ID，可以在其逻辑偏移的基础上加上当前消息的长度。

消费者始终从特定分区顺序地获取消息，如果消费者知道特定消息的偏移量，也就说明消费者已经消费了之前的所有消息。消费者向代理发出异步拉请求，准备字节缓冲区用于消费。每个异步拉请求都包含要消费的消息偏移量。Kafka利用sendfile API高效地从代理的日志段文件中分发字节给消费者。

###Kafka代理（broker）
与其它消息系统不同，Kafka代理是无状态的。这意味着消费者必须维护已消费的状态信息。这些信息由消费者自己维护，代理完全不管。这种设计非常微妙，它本身包含了创新。

* 从代理删除消息变得很棘手，因为代理并不知道消费者是否已经使用了该消息。Kafka创新性地解决了这个问题，它将一个简单的基于时间的SLA应用于保留策略。当消息在代理中超过一定时间后，将会被自动删除。
* 这种创新设计有很大的好处，消费者可以故意倒回到老的偏移量再次消费数据。这违反了队列的常见约定，但被证明是许多消费者的基本特征。
