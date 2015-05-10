Title: 【本科毕业设计论文】分布式网络爬虫的研究与实现
Date: 2012-06-29 15:02
Author: 糖拌咸鱼
Slug: ben-ke-bi-ye-she-ji-lun-wen-fen-bu-shi-wang-luo-pa-chong-de-yan-jiu-yu-shi-xian

<span style="font-size: 18pt;">**分布式网络爬虫的研究与实现**</span>

</p>

<span style="font-size: 16px;">摘 要</span> {style="text-align: center;"}
===========================================

</p>

        
随着互联网的高速发展，在互联网搜索服务中，搜索引擎扮演着越来越重要的角色。网络爬虫是搜索引擎系统中十分重要的组成部分，它负责从互联网中搜集网页，这些页面用于建立索引从而为搜索引擎提供支持。面对当前极具膨胀的网络信息，集中式的单机爬虫早已无法适应目前的互联网信息规模，因此高性能的分布式网络爬虫系统成为目前信息采集领域研究的重点。

</p>

        
本文对网络爬虫原理、分布式架构设计以及网络爬虫中的关键模块、瓶颈问题及解决办法进行了相关研究。论文工作主要表现为：

</p>

1、引入一致性哈希算法，用于解决URL任务分发策略、爬虫主机间负载均衡、单机热点问题，确保分布式爬虫系统具有良好的可扩展性、平衡性、容错性。

</p>

2、针对爬虫系统的礼貌性、优先级特性给出了基于Mercator模型的URL队列的设计和实现；

</p>

3、针对大规模URL去重、DNS解析、页面抓取与解析等关键瓶颈问题给出了解决办法；

</p>

4、设计并实现了一种线程池模型，用于多线程并行高效的进行页面采集；

</p>

5、提出一种基于文件方式的页面存储方案，通过建立索引文件与数据文件进行有效的页面存储与管理。

</p>

        
在上述工作的基础上，本文设计实现了一个高性能的分布式网络爬虫原型系统。实验表明，该网络爬虫系统不仅具有高页面抓取效率、高可配置、运行稳定的特点，而且具有良好的可扩展性、容错性、负载平衡性的分布式特性。 

</p>

**关键词：**网络爬虫；分布式；一致性哈希算法；信息采集；线程池

</p>

 

</p>

<span style="font-size: 16px;">**The Research and Implementation of
Distributed Web Crawler**</span>

</p>

<span style="font-size: 16px;">Abstract</span> {style="text-align: center;"}
==============================================

</p>

With the rapid development of Internet, search engines as the main
entrance of the Internet plays a more and more important role. Web
crawler is a very important part of the search engines, which is
responsible to collect web pages from Internet. These pages are used to
build index and provide support for search engines. Because of the great
expansion of Internet Information, a centralized and stand-alone web
crawler has not long been able to adapt to the Internet scale. So
high-performance distributed web crawler system is becoming the focus of
current research in the field of information collection.

</p>

This paper researches and demonstrates some topics about principle,
distributed architecture design, keymodules, the bottleneck problem and
solution in web crawler system. The main work as following :

</p>

​1. This paper introduces a hash algorithm called Consistent Hash, which
is used to solve the strategy of URL partition, hot-spot problem and
load balancing between web crawler nodes and ensure that the distributed
crawler has good scalability, balancing, fault tolerance.

</p>

​2. In order to meet the politeness and priority needs of the web
crawler, this paper designs and implements a URL queue based on Mercator
model.

</p>

​3. The solutions to large-scale URLs deduplication,DNS resolution,page
crawling and parsing and some other key problems are given.

</p>

4.This paper designs and implements a thread pool model for efficient
and  multi-threaded page collection.

</p>

5.A scheme for downloaded page storage is given, which creats indexd
files and data files to manage and store the downloaded data.

</p>

On the basis of the above work, this paper designs and implements a
high-performance distributed web crawler prototype system. The
experiments at the end of this paper show that the Web crawler not only
has the characteristics such as high efficiency page fetching, highly
configurable, stable, but also has good distributed features such as
good scalability, fault tolerance, load balancing and so on.

</p>

**Keywords：**Web Crawler;Distributed;Consistent Hash
 Algorithm;Information Retrieval;Thread Pool

</p>

**毕业设计原文：[分布式网络爬虫的研究与实现][]**

</p>

**PS：本科的毕业设计论文，写的比较浅，但是对网络爬虫的一些概念和功能模块进行了分析与实现。**

</p>

  [分布式网络爬虫的研究与实现]: http://files.cnblogs.com/coser/%E5%88%86%E5%B8%83%E5%BC%8F%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E7%9A%84%E8%AE%BE%E8%AE%A1%E4%B8%8E%E5%AE%9E%E7%8E%B0.pdf
