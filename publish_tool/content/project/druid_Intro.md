Title: Druid Introduction and usage in S&D Analytic Tool
Date: 2014-05-23 12:53
Category: opensource
Tags: Druid


Druid is an open-source <strong>analytics</strong> data store designed for <strong>real-time</strong> exploratory queries on <strong>large-scale</strong> data sets (100’s of Billions entries, 100’s TB data). 

##Key Features

1. Columnar storage format for partially nested data structures
2. Hierarchical query distribution with intermediate pruning
3. Indexing for quick filtering
4. Realtime and batch ingestion (ingested data is immediately available for querying)
5. Fault-tolerant distributed architecture that doesn’t lose data


##When Druid
1. Need analytics, not a key-value store
2. Large amounts of data
3. Real-time

##Why Druid

| timestamp |  advertiser | gender | country | impressions | clicks | revenue
| ------------ | ------------- | ------------ | ------------ | ------------- | ------------ |------------ |
| 2011-01-01T01:00:00Z | yahoo.com | Male |  USA  |  1800   |     25   |  15.70|

To Answer: <strong>How many impressions from males in USA were on yahoo.com?</strong>

####RDBMS ?
1. Full table scans were slow, regardless of the storage engine used.
2. Maintaining proper dimension tables, indexes and aggregate tables was painful

####Massive NOSQL With Pre-Computation ?
1. Supporting high dimensional OLAP requires pre-computing an exponentially large amount of data.


####Druid
Contains three key parts: <strong>Metrics, Dimensions, timestamp</strong>

1. Partial Aggregates + In-Memory + Indexes => Fast Queries

2. Distributed Data + Parallelizable Queries => Horizontal Scalability
    * Queries against the Druid cluster are perfectly horizonta

3. Real-Time Analytics: Immutable Past, Append-Only Future
    * memory mapping strategy 
    * past events happen once and never change
    * an event stream that flows into a set of real-time indexers

##Design

###Architecture
![pic](https://sdfpaw.dm2301.livefilestore.com/y2pHe7KzpgAdMOMQQlel-Q4VrKoSLP2ejxwNdW_U6TZgK9UvD1Cu-JvhoqEgkeeSjS_q8SkCqq9QGWBVeGZR4wZucgbnm3QB2XSWn9wLKf61j0/QQ20140621-1.png?psid=1)

###Key features
####Data Storage
* Converted to columnar format
* Indexed with bitmap indexes
* Compressed using various algorithms
    * LZF (switching to Snappy is on the roadmap, not yet implemented)
    * Dictionary encoding w/ id storage minimization
    * Bitmap compression
    * RLE (on the roadmap, but not yet implemented)
    
####Index tasks
1. Index Task, local model
2. Index Hadoop Task
3. Realtime Index Task
4. Segment Merging Tasks
    * Append Task
    * Merge Task
5. Segment Destroying Tasks
    
####Querying
1. Filters: 
    * Selector
    * Regular expression filter
    * Logical expression filters(And Or Not)
    * JavaScript filter
2. Aggregations：
    * Count aggregator
    * longSum, doubleSum
    * Min / Max aggregators
    * JavaScript aggregator
3. group by, orderly, having
4. Search
5. top N
    
##Usage in S&D Analytic Tool

###Setup
1. Mysql
2. Zookeeper
3. Historical Node
4. Coordinator Node
5. Broker Node
6. Real-time Node
7. Indexer node(load batch and real-time data into the system)

###Data schema
####Dimensions

| age |  gender | country | state | city | DMA | device | cookie | user_segments 
| ------------ | ------------- | ------------ | ------------ | ------------- | ------------ |------------ |------------ |------------ |
| 30 | 1 | 123 |  456  |  789   |   25   |  15 | 2213133| [1, 3, 56, 2323]|

####Metrics(imps_in_bidrange)

| b1 |  b2 | b3 | b4 | b5 | b6 | b7 | b8 | b9 | b10 | b11
| ------------ | ------------- | ------------ | ------------ | ------------- | ------------ |------------ |------------ |------------ |------------ |------------ |
| 2 |  12 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0


###Ingest raw data into druid through indexing service
####0. Data format(Json or csv)
<pre>
{"rt": 16202, "gr": 0, "di": 24701058, "timestamp": "2014-04-16T07:00:00.000Z", "age": 34, "b3": 0, "b2": 0, "si": 2347587, "us": [1, 12, 22, 63, 68, 70, 89, 91, 113, 122, 129, 135, 149, 150, 155, 187, 195954, 735956, 735959, 735960, 735963, 735964, 735965, 735971, 735972, 735977, 735982, 735985, 735991, 735992, 735996, 735997, 736004, 736011, 736018, 736022, 736033, 736038, 736042, 736045, 736046, 736067, 736070, 748039, 808330, 809665, 812679, 812714, 812725, 812727, 812982, 813028, 813368, 813385, 20020861, 20020920, 20020940, 20020992, 20020999, 20021036, 20021039, 20021110, 200211 20023587, 20023591, 20023624, 20023625], "b4": 0, "b5": 0, "cy": 2436704, "b7": 0, "b6": 0, "b1": 0, "b10": 0, "b11": 16, "cr": 23424977, "dt": 5199421, "b8": 0, "b9": 4}
</pre>

####1. Build Index( support local model or hadoop model )
<pre>
{
  "type" : "index",
  "dataSource" : "sdafullTesting",
  "granularitySpec": {
    "type":"uniform",
    "intervals":["2014-04-15T07:00:00.000Z/2014-04-17T07:59:59.000Z"],
    "gran":"DAY"
  },
  "aggregators" : [{ "type": "longSum", "fieldName": "b1", "name": "b1" },
{ "type": "longSum", "fieldName": "b2", "name": "b2" },
{ "type": "longSum", "fieldName": "b3", "name": "b3" },
{ "type": "longSum", "fieldName": "b4", "name": "b4" },
{ "type": "longSum", "fieldName": "b5", "name": "b5" },
{ "type": "longSum", "fieldName": "b6", "name": "b6" },
{ "type": "longSum", "fieldName": "b7", "name": "b7" },
{ "type": "longSum", "fieldName": "b8", "name": "b8" },
{ "type": "longSum", "fieldName": "b9", "name": "b9" },
{ "type": "longSum", "fieldName": "b10", "name": "b10" },
{ "type": "longSum", "fieldName": "b11", "name": "b11" }],
  "firehose" : {
    "type" : "local",
    "baseDir" : "examples/indexing/",
    "filter" : "feed.json.full.total",
    "parser" : {
      "timestampSpec" : {
        "column" : "timestamp",
        "timestampFormat": "iso"
      },
      "data" : {
          "format": "json",
          "dimensions": ["age","cr","cy","di","dt","gr","rt","si","us"]
      }
    }
  }
}
</pre>

####2. Query

<pre>
{
    "aggregations": [
        {"type":"count", "name":"audienceCount"},
        { "fieldName": "b1", "name": "b1", "type": "longSum" },
        { "fieldName": "b2", "name": "b2", "type": "longSum" },
        { "fieldName": "b3", "name": "b3", "type": "longSum" },
        { "fieldName": "b4", "name": "b4", "type": "longSum" },
        { "fieldName": "b5", "name": "b5", "type": "longSum" },
        { "fieldName": "b6", "name": "b6", "type": "longSum" },
        { "fieldName": "b7", "name": "b7", "type": "longSum" },
        { "fieldName": "b8", "name": "b8", "type": "longSum" },
        { "fieldName": "b9", "name": "b9", "type": "longSum" },
        { "fieldName": "b10", "name": "b10", "type": "longSum" },
        { "fieldName": "b11", "name": "b11", "type": "longSum" }
    ],
    "filter": { 
        "type":"and",
        "fields":[
        {"type": "selector", "dimension": "dt", "value": 5199421},
        {"type": "selector", "dimension": "gr", "value": 1},
        {"type":"or",
            "fields":[
            {"type": "selector", "dimension": "us", "value": 113},
            {"type": "selector", "dimension": "us", "value": 122},
            {"type": "selector", "dimension": "us", "value": 129},
            {"type": "selector", "dimension": "us", "value": 135}
            ]
        },
        {"type": "javascript", "dimension": "age", "function" : "function(x) { return x> 30 && x<60}"}
        ]
        },
    "dataSource": "sdafullTesting",
    "granularity": "all",
    "queryType": "timeseries",
    "intervals": [
        "2010-04-10T16:00:00.000+08:00/2024-04-19T16:00:00.000+08:00"
    ]
}
</pre>

####3. Result
<pre>
{
  "timestamp" : "2014-04-16T07:00:00.000Z",
  "result" : {
    "audienceCount" : 21790,
    "b1" : 15613,
    "b11" : 75409,
    "b3" : 5387,
    "b2" : 8356,
    "b5" : 7823,
    "b10" : 6333,
    "b4" : 9033,
    "b7" : 5279,
    "b6" : 6313,
    "b9" : 6296,
    "b8" : 5756
  }
}
</pre>

###Vespa VS Druid

Data from pig job's output, one part, contains <code>221784</code> instances.

| Metrics |  vespa  | Druid | 
| ------------ | ------------- | ------------ | 
|Data size | xml-large | <strong>json-small</strong> |
|Import data and build index cost time | 4min06s | <strong>3min02s</strong> |
| Avg(100 Queries cost time) | 0.074922 | <strong>0.048718</strong>|
| Full scan query cost time | 0.161210 | <strong>0.077793</strong>|

###Next...
1. set a large mount of data
2. setup a druid cluster in multiple machines
3. change schema, don't set bidranges column, to support queries for any bidprice range

###References
1. [Druid Design Document](http://druid.io/docs/0.6.105/Design.html)
2. [Druid: White Paper(Sigmod 2014)](http://static.druid.io/docs/druid.pdf)
3. [Introducing Druid: Real-Time Analytics at a Billion Rows Per Second April 30, 2011 · ERIC TSCHETTER](http://druid.io/blog/2011/04/30/introducing-druid.html)
4. [Druid, Part Deux: Three Principles for Fast, Distributed OLAP May 20, 2011 · ERIC TSCHETTER](http://druid.io/blog/2011/05/20/druid-part-deux.html)
4. [Querying Your Data November 4, 2013 · RUSSELL JURNEY](http://druid.io/blog/2013/11/04/querying-your-data.html)
5. [Vespa Tutorial](http://vespa.trondheim.corp.yahoo.com/5/documentation/tutorial.html)



