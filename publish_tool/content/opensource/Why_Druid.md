Title: Why Druid?
Date: 2014-09-07 10:20
Category: opensource
Tags: Druid

##Druid

由于在Yahoo!作了很多关于Druid的工作，这里总结一下我对Druid的理解。

Druid是神马？

> An open-source, real-time data store designed to power interactive applications at scale.

可以查下官网，或者参考我之前写过的一些内容。

官网：[http://druid.io/](http://druid.io/)

之前写过的：[Druid Introduction and usage in S&D Analytic Tool](http://lixinzhang.github.io/druid-introduction-and-usage-in-sd-analytic-tool.html)

![222](http://lixinzhang.github.io/image/o_Druid.jpg)

###我对Druid的理解

* 主要用于数据分析，而非查询，因此如果想拿到某条具体的instance，Druid是不合适的。虽然可以通过GroupBy的操作拿到这样的结果。

* 如果有需求是，通过某些字段作为filter，还有很多的metrics需要统计，如广告的impression，click，serve等，Druid就太合适，天生就是支持这些东西的。

* Deep Storage， Druid提出了<code>Deep Storage</code>的概念，就是说存储这活放到更独立的地方去，冗余复制、访问控制等机制交给更成熟的分布式文件系统（如S3，HDFS）去管理，而不必担心数据会丢失。

* 容错性与扩展性非常好，只需要简单配置Zookeeper与coordinator地址，然后直接启动即可加入集群，开始负载。而且节点挂了，由于<code>Deep Storage</code>的存在，不必担心数据的丢失。

* 实时ingest。这个也是Druid最大卖点，因为很多数据仓库等开源工具貌似对实时的数据导入的支持并不理想，而Druid可以做到实时的导入，而且查询结果会merge realtime node与historical node进行准确的数据统计。这也是很多工具做不到的。

* Bitmap index + compression algorithm。 位图索引与位图压缩算法，使其存储空间变小，而且由于统计服务中字段的候选集实例个数一般较少，采用位图索引可以极大加快查询速度。举个例子，如果想统计男或女的数量，传统数据库中的B-tree索引，大概只能减少一般的查询量，而位图索引通过高效的位操作，可以更加快速。

* 面向列式的存储，这个不言而喻，因为Druid的前提假设是数据一旦导入，你不会再更改，且不会存在大量查询某一行instance的请求。因此，采用面向列式的存储，可以很大程度上减少I/O。

* Real-time导入数据，是通过<code>Kafka</code>，这使得导入数据变得非常方便，因为只要任何客户端能写进kafka就能写进Druid。
