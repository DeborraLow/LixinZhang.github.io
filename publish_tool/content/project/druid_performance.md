Title: Druid Cluster Performance Report
Date: 2014-06-03 12:53
Category: opensource
Tags: Druid

##Background

Druid has five key components: <strong>Historical Node</strong>, <strong>Realtime Node</strong>, <strong>Coordinator Node</strong>, <strong>Broker Node</strong>, and <strong>Indexer Node</strong>. In this report, we didn't setup Realtime nodes and  builded index only through batch way.

Aside from these nodes, there are 3 external dependencies to the system : <strong>ZooKeeper</strong>, <strong>MySQL instance</strong>, <strong>"deep storage"</strong>. We used HDFS as "deep storage".

Get more detailed description of these components, please visit the official website: [Design of Druid](http://druid.io/docs/0.6.105/Design.html) or the [White paper](http://static.druid.io/docs/druid.pdf).

This performance report is based on the application of [D&A Analytic Tool](https://docs.google.com/a/yahoo-inc.com/document/d/1O46sJhNWI-B5ToXY96BGPTNZZNCAXH633PHKz2b3GaM/edit?usp=drive_web).

###Data Set
<strong>89G</strong> data containing 59837541 instances with Json format. We imported the data into HDFS, and build index through a Hadoop job.

Size of the data is too large to build index in local model. We tried to setup a standalone Hadoop cluster to build index, it failed due to out of memory of JVM. We also tried to optimize the setting of JVM memory and count of MR tasks, it still could't work. So a distributed Hadoop cluster is needed. 


##Cluster Setup

####Machine Summary
<pre>
Summary:    HP DL160 G6, 2 x Xeon X5650 2.67GHz, 15.7GB / 16GB 1333MHz DDR3, 1 x 500GB SATA
System:     HP ProLiant DL160 G6, C-2P/16/500, ySPEC 39.5
Processors: 2 x Xeon X5650 2.67GHz (HT enabled, 12 cores, 24 threads) - Gulftown B1, 64-bit, six-core, 32nm, L3: 12MB
Memory:     15.7GB / 16GB 1333MHz DDR3 == 4 x 4GB - 4GB PC3-10600 Hynix DDR3-1333 ECC Registered CL9 2Rx4
                                      14 x empty
Disk:       sda (ahci0): 500GB (33%) JBOD == 1 x 500GB 7.2K SATA/300 HP/Seagate Constellation ES 32MB
Disk-Control:   ahci0: HP/Intel ICH10 82801J 6 Port SATA/300 AHCI
Chipset:    Intel 5520 IOH-36D B3 (Tylersburg), 82801JIR A0 (ICH10R)
Network:    eth0 (igb): HP NC362i/Intel 82576 Gigabit, 1Gb/s <full-duplex>
Network:    eth1 (igb): HP NC362i/Intel 82576 Gigabit, no carrier
OS:     YLinux 6.5.0_84, RHEL Server 6.5, Linux 2.6.32-431.3.1.el6.YAHOO.20140110.x86_64 x86_64, 64-bit
BIOS:       HP O33 08/16/2010, rev 8.15
Hostname:   raptorsim0017.rm.bf1.yahoo.com
</pre>

####Druid Service Cluster

* 10 Historical Nodes; 
* 1 Zookeeper Node; 
* 1 Broker Node;
* 1 Mysql;
* 1 Coodinator Node; 
* 1 index Node 
* Deep Storage(HDFS)

No.|Nodes Hostname | Role | Dependencies|
:----------- :| :-----------: | :-----------:| :-----------:
1 |raptorsim0008.rm.bf1.yahoo.com | Coodinator, Historical | Hadoop Client, Mysql, Zookeeper
2 |raptorsim0009.rm.bf1.yahoo.com | Mysql, Historical     | Hadoop Client, Zookeeper
3 |raptorsim0010.rm.bf1.yahoo.com | Zookeeper, Historical  |Hadoop Client, Zookeeper
4 |raptorsim0011.rm.bf1.yahoo.com | Broker     |Mysql, Zookeeper
5 |raptorsim0012.rm.bf1.yahoo.com | Historical |Hadoop Client, Zookeeper
6 |raptorsim0013.rm.bf1.yahoo.com | Historical |Hadoop Client, Zookeeper
7 |raptorsim0014.rm.bf1.yahoo.com | Historical |Hadoop Client, Zookeeper
8 |raptorsim0015.rm.bf1.yahoo.com | Historical |Hadoop Client, Zookeeper
9 |raptorsim0016.rm.bf1.yahoo.com | index, Hadoop Master |Hadoop, Mysql, Zookeeper
10|raptorsim0017.rm.bf1.yahoo.com | Historical |Hadoop Client, Zookeeper
11|raptorsim0018.rm.bf1.yahoo.com | Historical |Hadoop Client, Zookeeper
12|raptorsim0019.rm.bf1.yahoo.com | Historical |Hadoop Client, Zookeeper


####Hadoop[yarn] Index Builder Cluster
No.|Nodes Hostname | Role | 
:----------- :| :-----------: | :-----------:
1 |raptorsim0012.rm.bf1.yahoo.com | Slave 
2 |raptorsim0013.rm.bf1.yahoo.com | Slave 
3 |raptorsim0014.rm.bf1.yahoo.com | Slave 
4 |raptorsim0015.rm.bf1.yahoo.com | Slave 
5 |raptorsim0016.rm.bf1.yahoo.com | Master, Druid Indexer 
6 |raptorsim0017.rm.bf1.yahoo.com | Slave 
7 |raptorsim0018.rm.bf1.yahoo.com | Slave 
8 |raptorsim0019.rm.bf1.yahoo.com | Slave 


####Hadoop(yarn) Setting

MIN_CONTAINER_SIZE should be 1024 MB if total RAM per Node is between 8 GB and 24 GB.

containers = min (2\*CORES, 1.8\*DISKS, (Total available RAM) / MIN_CONTAINER_SIZE) = 5

RAM-per-container = max(MIN_CONTAINER_SIZE, (Total Available RAM) / containers)) = 2048m


No.|Configuration File | Configuration Setting | Value|
:----------- :| :-----------: | :-----------:| :-----------:
1 |yarn-site.xml    | yarn.nodemanager.resource.memory-mb    | containers * RAM-per-container = 6 * 2048 = 12288
2 |yarn-site.xml    | yarn.scheduler.minimum-allocation-mb   | RAM-per-container = 2048
3 |yarn-site.xml     | yarn.scheduler.maximum-allocation-mb  | containers * RAM-per-container = 6 * 2048 = 12288
4 |mapred-site.xml  | mapreduce.map.memory.mb    | RAM-per-container = 2048 * 0.25 = 512
5 |mapred-site.xml  | mapreduce.reduce.memory.mb     | 2 * RAM-per-container = 2 * 2048 * 1.5 = 6144
6 |mapred-site.xml  | mapreduce.map.java.opts    | -Xmx512m * 0.8 = 384
7 |mapred-site.xml  | mapreduce.reduce.java.opts     | -Xmx6144m * 0.8 = 5120
8 |hadoop-env.sh|HADOOP_DATANODE_OPTS|-Xmx12g

####Property setting to make Druid faster

#####JVM Heap
Broker nodes can use the JVM heap as a query cache and thus, the size of the heap will affect on the number of results that can be cached. 

Historical nodes use off-heap memory to store intermediate results, and by default, all segments are memory mapped before they can be queried. The more off-heap memory is available, the more segments can be served without the possibility of data being paged onto disk. 

Coordinator nodes do not require off-heap memory and the heap is used for loading information about all segments to determine what segments need to be loaded, dropped, moved, or replicated.

No.|Node | Setting|
:----------- :| :-----------: | :-----------:
1 | Broker nodes | -Xmx8192m
2 | Historical nodes | -Xmx4096m
3 | Coordinator nodes | -Xmx4096m


#####Historical Nodes

No.|Property | Description | Setting|
:----------- :| :-----------: | :-----------:| :-----------:
1 |druid.processing.buffer.sizeBytes|This specifies a buffer size for the storage of intermediate results. The computation engine in both the Historical and Realtime nodes will use a scratch buffer of this size to do all of their intermediate computations off-heap. Larger values allow for more aggregations in a single pass over the data while smaller values can require more passes depending on the query that is being executed.|<strong>2147483648(2GB)</strong>
2 |druid.processing.numThreads|The number of processing threads to have available for parallel processing of segments.| <strong>5</strong>
3 |druid.segmentCache.locations|Segments assigned to a Historical node are first stored on the local file system (in a disk cache) and then served by the Historical node. These locations define where that local cache resides.| <strong>40000000000(40GB)</strong>

##Performance 

###Query Latency
####Queries Construction

Druid has its own query languages and accepts queries as POST requests. The body of the POST request is a JSON object containing key-value pairs specifying various query parameters.

We developed a tool to construct 100 queries with random filters. 

####Latency

Metrics | Cost Time
:---------:|:---------:|
Average(100 random queries)| 1.708s
Full table scan, no filters | 3.799s
Query with hundreds of segment id. | 4.843s

###Building index

Druid would run three Hadoop Jobs for finishing index building.

####Cost Time

It took about <strong>1hour 47mins</strong> to finish index building.

####CPU and I/O
Building index should be an <strong>IO bound</strong> task through analysing the CPU and I/O status during Map and Reduce. I/O writing and reading during both map and reduce tasks is almost 100%. Map tasks occupied more CPU resource than Reduce tasks and Reduce tasks cost more memory.

The number of Reduce tasks depends on the Granularity setting in Druid index task configuration. For instance, it would be 24 reduce tasks if we set granularity as HOUR.

###Disk and Memory Usage by Druid

Raw data in HDFS could be removed after finishing index building.

No.|Nodes Hostname | Disk usage| Memory Usage |
:----------- :| :-----------: | :-----------:| :-----------:
1 |raptorsim0012.rm.bf1.yahoo.com | 9.2G | 10G 
2 |raptorsim0013.rm.bf1.yahoo.com | 8.6G | 10G  
3 |raptorsim0014.rm.bf1.yahoo.com | 8.5G | 10G 
4 |raptorsim0015.rm.bf1.yahoo.com | 8.5G | 10G  
5 |raptorsim0017.rm.bf1.yahoo.com | 8.3G | 10G 
6 |raptorsim0018.rm.bf1.yahoo.com | 8.8G | 10G  
7 |raptorsim0019.rm.bf1.yahoo.com | 8.4G | 10G 
8 |raptorsim0008.rm.bf1.yahoo.com | 8.7G | 10G 
9 |raptorsim0009.rm.bf1.yahoo.com | 8.5G | 10G 
10 |raptorsim0010.rm.bf1.yahoo.com | 8.3G | 10G 
11 |Deep Storage (hdfs)|28.8G(segments data) | --
Total|--|114.6G|100G 


##Conclusion
###Strengths of Druid performance

1. Advantage of Hadoop makes ingest data into Druid faster. 
2. Deep storage (HDFS) makes service highly available. When a historical node fails, others can pull missed data from HDFS to keep serving. Do not lose data.
3. Support timeseries query. We can get result given any time interval quickly.
4. The size of processed data after index building is about 3~4 times smaller than raw data due to some compression algorithm. So, we could store more data, and provided services for more days.
5. Cost less memory. Druid take advantage of memory-mapping technology to make memory usage effective. 

###Weaknesses of Druid performance
1. Less documents or instructions could be found.
2. Druid is memory-based and not so stable. A lot of exceptions occurred due to out of memory error.
3. There is no monitoring methods to help monitor running status of Druid cluster. We can't guarantee the correctness of querying result.
4. Consistency and correctness are weak. Historical nodes need pull data from deep storage, so the latency during data transmission and loading to memory causes the problem.

##Appendix
<strong>iostat -x 1 10 </strong> during map and reduce.
#####Map: 
<pre>
Linux 2.6.32-431.3.1.el6.YAHOO.20140110.x86_64 (raptorsim0017.rm.bf1.yahoo.com)     05/22/14    _x86_64_    (24 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          17.32    0.00    1.38    7.76    0.00   73.54

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda              16.00   604.00  263.00   64.00 69440.00  5352.00   228.72    16.80   51.97   2.68  87.50
          
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          23.94    0.00    2.47    0.00    0.00   73.58

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               0.00     0.00   50.00    0.00 11672.00     0.00   233.44     0.06    1.28   1.24   6.20
          
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          52.01    0.00    1.22    0.34    0.00   46.44

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               1.00     0.00  123.00    0.00 29952.00     0.00   243.51     0.27    2.18   1.40  17.20

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          37.32    0.00    3.65    1.05    0.00   57.99

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               6.00    10.00  252.00    6.00 62264.00   120.00   241.80     0.73    2.84   1.83  47.30

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          39.50    0.00    3.40    0.67    0.00   56.44

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               5.00     0.00  149.00    0.00 36480.00     0.00   244.83     0.77    5.19   2.36  35.20

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          62.70    0.00    1.93    1.72    0.00   33.65

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               2.00  2256.00    6.00  193.00  2048.00 19656.00   109.07     8.66   43.51   2.83  56.40

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          46.50    0.00    1.93    0.21    0.00   51.36

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               0.00     0.00   24.00    0.00  4416.00     0.00   184.00     0.12    5.17   3.83   9.20

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          49.77    0.00    2.01    0.42    0.00   47.80

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               2.00     6.00  109.00    3.00 24720.00    72.00   221.36     0.48    4.28   2.95  33.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          46.52    0.00    1.63    3.81    0.00   48.03

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda              28.00     0.00  211.00    1.00 56704.00     0.00   267.47     2.82   11.64   4.65  98.60

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          55.95    0.00    1.17    6.78    0.00   36.10

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda              35.00     0.00  331.00    0.00 87520.00     0.00   264.41     5.18   15.02   3.02 100.00
</pre>

#####Reduce
<pre>
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           1.73    0.00    0.53    0.85    0.00   96.89

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               1.04   195.55   10.18   10.99  1578.37  2062.87   171.95     0.18    8.46   5.29  11.20

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          10.29    0.00    1.00   13.26    0.00   75.44

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               6.00   394.00   61.00   75.00  5400.00 48096.00   393.35   233.44  905.21   7.35 100.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          11.84    0.00    0.59    9.75    0.00   77.82

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda              15.00     0.00  200.00   69.00 13776.00 54464.00   253.68   167.97 1064.57   3.72 100.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          11.44    0.00    1.68   13.74    0.00   73.15

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda              17.00  7326.00  225.00   51.00 22816.00 37640.00   219.04   158.86 1649.70   3.63 100.10

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           9.50    0.00    1.21    7.92    0.00   81.37

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda              32.00  3680.00  427.00   34.00 48880.00 29336.00   169.67   160.18  671.39   2.17  99.90

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           4.15    0.00    0.75   11.36    0.00   83.73

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda              12.00 27454.00  133.00  166.00 15688.00 130352.00   488.43   225.93  643.60   3.34 100.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.50    0.00    0.38    9.25    0.00   89.87

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               0.00 15968.00   26.00  165.00  3424.00 140464.00   753.34   264.42 1360.66   5.24 100.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.63    0.00    0.21   11.55    0.00   87.61

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               0.00 13316.00   29.00  153.00  4984.00 115752.00   663.38   244.47 1513.18   5.49 100.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.80    0.00    0.42   13.66    0.00   85.13

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               0.00 15027.00   22.00  174.00  3752.00 134056.00   703.10   223.53  956.06   5.11 100.10

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           1.17    0.00    0.29   11.56    0.00   86.97

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await  svctm  %util
sda               1.00 13681.00   30.00  129.00  4760.00 106760.00   701.38   216.07 1236.13   6.29 100.00
</pre>








