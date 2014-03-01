Title: Python 多线程抓取网页
Date: 2012-03-16 15:53
Author: 糖拌咸鱼
Slug: python-duo-xian-cheng-zhua-qu-wang-ye

   最近，一直在做网络爬虫相关的东西。
看了一下开源C++写的larbin爬虫，仔细阅读了里面的设计思想和一些关键技术的实现。

</p>

1、larbin的URL去重用的很高效的bloom filter算法；   
2、DNS处理，使用的adns异步的开源组件；   
3、对于url队列的处理，则是用部分缓存到内存，部分写入文件的策略。   
4、larbin对文件的相关操作做了很多工作   
5、在larbin里有连接池，通过创建套接字，向目标站点发送HTTP协议中GET方法，获取内容，再解析header之类的东西
  
6、大量描述字，通过poll方法进行I/O复用，很高效   
7、larbin可配置性很强   
8、作者所使用的大量数据结构都是自己从最底层写起的，基本没用STL之类的东西
  
......   
还有很多，以后有时间在好好写篇文章，总结下。

</p>

  
这两天，用python写了个多线程下载页面的程序，对于I/O密集的应用而言，多线程显然是个很好的解决方案。刚刚写过的线程池，也正好可以利用上了。其实用python爬取页面非常简单，有个urllib2的模块，使用起来很方便，基本两三行代码就可以搞定。虽然使用第三方模块，可以很方便的解决问题，但是对个人的技术积累而言没有什么好处，因为关键的算法都是别人实现的，而不是你自己实现的，很多细节的东西，你根本就无法了解。
我们做技术的，不能一味的只是用别人写好的模块或是api，要自己动手实现，才能让自己学习得更多。

</p>

 
我决定从socket写起，也是去封装GET协议，解析header，而且还可以把DNS的解析过程单独处理，例如DNS缓存一下，所以这样自己写的话，可控性更强，更有利于扩展。对于timeout的处理，我用的全局的5秒钟的超时处理，对于重定位（301or302）的处理是，最多重定位3次，因为之前测试过程中，发现很多站点的重定位又定位到自己，这样就无限循环了，所以设置了上限。具体原理，比较简单，直接看代码就好了。

</p>

  
自己写完之后，与urllib2进行了下性能对比，自己写的效率还是比较高的，而且urllib2的错误率稍高一些，不知道为什么。网上有人说urllib2在多线程背景下有些小问题，具体我也不是特别清楚。

</p>

**先贴代码：**

</p>

**fetchPage.py**  使用Http协议的Get方法，进行页面下载，并存储为文件

</p>
<p>

    :::python
'''Created on 2012-3-13Get Page using GET methodDefault using HTTP Protocol , http port 80@author: xiaojay'''import socketimport statisticsimport datetimeimport threadingsocket.setdefaulttimeout(statistics.timeout)class Error404(Exception):    '''Can not find the page.'''    passclass ErrorOther(Exception):    '''Some other exception'''    def __init__(self,code):        #print 'Code :',code        passclass ErrorTryTooManyTimes(Exception):    '''try too many times'''    passdef downPage(hostname ,filename , trytimes=0):    try :        #To avoid too many tries .Try times can not be more than max_try_times        if trytimes >= statistics.max_try_times :             raise ErrorTryTooManyTimes    except ErrorTryTooManyTimes :        return statistics.RESULTTRYTOOMANY,hostname+filename    try:        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         #DNS cache        if statistics.DNSCache.has_key(hostname):            addr = statistics.DNSCache[hostname]        else:            addr = socket.gethostbyname(hostname)            statistics.DNSCache[hostname] = addr        #connect to http server ,default port 80        s.connect((addr,80))        msg  = 'GET '+filename+' HTTP/1.0\r\n'        msg += 'Host: '+hostname+'\r\n'        msg += 'User-Agent:xiaojay\r\n\r\n'        code = ''         f = None        s.sendall(msg)        first = True        while True:            msg = s.recv(40960)            if not len(msg):                if f!=None:                    f.flush()                    f.close()                break            # Head information must be in the first recv buffer            if first:                first = False                                headpos = msg.index("\r\n\r\n")                code,other = dealwithHead(msg[:headpos])                if code=='200':                    #statistics.fetched_url += 1                    f = open('pages/'+str(abs(hash(hostname+filename))),'w')                    f.writelines(msg[headpos+4:])                elif code=='301' or code=='302':                    #if code is 301 or 302 , try down again using redirect location                    if other.startswith("http") :                                        hname, fname = parse(other)                        downPage(hname,fname,trytimes+1)#try again                    else :                        downPage(hostname,other,trytimes+1)                elif code=='404':                    raise Error404                else :                     raise ErrorOther(code)            else:                if f!=None :f.writelines(msg)        s.shutdown(socket.SHUT_RDWR)        s.close()        return statistics.RESULTFETCHED,hostname+filename    except Error404 :        return statistics.RESULTCANNOTFIND,hostname+filename    except ErrorOther:        return statistics.RESULTOTHER,hostname+filename    except socket.timeout:        return statistics.RESULTTIMEOUT,hostname+filename    except Exception, e:        return statistics.RESULTOTHER,hostname+filenamedef dealwithHead(head):    '''deal with HTTP HEAD'''    lines = head.splitlines()    fstline = lines[0]    code =fstline.split()[1]    if code == '404' : return (code,None)    if code == '200' : return (code,None)    if code == '301' or code == '302' :         for line in lines[1:]:            p = line.index(':')            key = line[:p]            if key=='Location' :                return (code,line[p+2:])    return (code,None)    def parse(url):    '''Parse a url to hostname+filename'''    try:        u = url.strip().strip('\n').strip('\r').strip('\t')        if u.startswith('http://') :            u = u[7:]        elif u.startswith('https://'):            u = u[8:]        if u.find(':80')>0 :            p = u.index(':80')            p2 = p + 3        else:            if u.find('/')>0:                p = u.index('/')                 p2 = p            else:                p = len(u)                p2 = -1        hostname = u[:p]        if p2>0 :            filename = u[p2:]        else : filename = '/'        return hostname, filename    except Exception ,e:        print "Parse wrong : " , url        print edef PrintDNSCache():    '''print DNS dict'''    n = 1    for hostname in statistics.DNSCache.keys():        print n,'\t',hostname, '\t',statistics.DNSCache[hostname]        n+=1def dealwithResult(res,url):    '''Deal with the result of downPage'''    statistics.total_url+=1    if res==statistics.RESULTFETCHED :        statistics.fetched_url+=1        print statistics.total_url , '\t fetched :', url    if res==statistics.RESULTCANNOTFIND :        statistics.failed_url+=1        print "Error 404 at : ", url    if res==statistics.RESULTOTHER :        statistics.other_url +=1        print "Error Undefined at : ", url    if res==statistics.RESULTTIMEOUT :        statistics.timeout_url +=1        print "Timeout ",url    if res==statistics.RESULTTRYTOOMANY:        statistics.trytoomany_url+=1        print e ,"Try too many times at", urlif __name__=='__main__':        print  'Get Page using GET method'    

</p>

**下面，我将利用上一篇的[线程池][]作为辅助，实现多线程下的并行爬取，并用上面自己写的下载页面的方法和urllib2进行一下性能对比。**

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
'''Created on 2012-3-16@author: xiaojay'''import fetchPageimport threadpoolimport datetimeimport statisticsimport urllib2'''one thread'''def usingOneThread(limit):    urlset = open("input.txt","r")    start = datetime.datetime.now()    for u in urlset:        if limit <= 0 : break        limit-=1        hostname , filename = parse(u)        res= fetchPage.downPage(hostname,filename,0)        fetchPage.dealwithResult(res)    end = datetime.datetime.now()    print "Start at :\t" , start    print "End at :\t" , end    print "Total Cost :\t" , end - start    print 'Total fetched :', statistics.fetched_url    '''threadpoll and GET method'''def callbackfunc(request,result):    fetchPage.dealwithResult(result[0],result[1])def usingThreadpool(limit,num_thread):    urlset = open("input.txt","r")    start = datetime.datetime.now()    main = threadpool.ThreadPool(num_thread)    for url in urlset :        try :            hostname , filename = fetchPage.parse(url)            req = threadpool.WorkRequest(fetchPage.downPage,args=[hostname,filename],kwds={},callback=callbackfunc)            main.putRequest(req)        except Exception:            print Exception.message            while True:        try:            main.poll()            if statistics.total_url >= limit : break        except threadpool.NoResultsPending:            print "no pending results"            break        except Exception ,e:            print e    end = datetime.datetime.now()    print "Start at :\t" , start        print "End at :\t" , end    print "Total Cost :\t" , end - start    print 'Total url :',statistics.total_url    print 'Total fetched :', statistics.fetched_url    print 'Lost url :', statistics.total_url - statistics.fetched_url    print 'Error 404 :' ,statistics.failed_url    print 'Error timeout :',statistics.timeout_url    print 'Error Try too many times ' ,statistics.trytoomany_url    print 'Error Other faults ',statistics.other_url    main.stop()'''threadpool and urllib2 '''def downPageUsingUrlib2(url):    try:        req = urllib2.Request(url)        fd = urllib2.urlopen(req)        f = open("pages3/"+str(abs(hash(url))),'w')        f.write(fd.read())        f.flush()        f.close()        return url ,'success'    except Exception:        return url , None    def writeFile(request,result):    statistics.total_url += 1    if result[1]!=None :        statistics.fetched_url += 1        print statistics.total_url,'\tfetched :', result[0],    else:        statistics.failed_url += 1        print statistics.total_url,'\tLost :',result[0],def usingThreadpoolUrllib2(limit,num_thread):    urlset = open("input.txt","r")    start = datetime.datetime.now()       main = threadpool.ThreadPool(num_thread)            for url in urlset :        try :            req = threadpool.WorkRequest(downPageUsingUrlib2,args=[url],kwds={},callback=writeFile)            main.putRequest(req)        except Exception ,e:            print e            while True:        try:            main.poll()            if statistics.total_url  >= limit : break        except threadpool.NoResultsPending:            print "no pending results"            break        except Exception ,e:            print e     end = datetime.datetime.now()        print "Start at :\t" , start     print "End at :\t" , end    print "Total Cost :\t" , end - start    print 'Total url :',statistics.total_url    print 'Total fetched :', statistics.fetched_url    print 'Lost url :', statistics.total_url - statistics.fetched_url    main.stop()if __name__ =='__main__':    '''too slow'''    #usingOneThread(100)    '''use Get method'''    #usingThreadpool(3000,50)    '''use urllib2'''    usingThreadpoolUrllib2(3000,50)
```

</p>

 

</p>

**<span style="font-size: medium;">实验分析：</span>**

</p>

**实验数据：**larbin抓取下来的3000条url，经过Mercator队列模型（我用c++实现的，以后有机会发个blog）处理后的url集合，具有随机和代表性。使用50个线程的线程池。
  
**实验环境：**ubuntu10.04，网络较好，python2.6   
存储：小文件，每个页面，一个文件进行存储   
PS：由于学校上网是按流量收费的，做网络爬虫，灰常费流量啊！！！过几天，可能会做个大规模url下载的实验，用个几十万的url试试。

</p>

**实验结果：**

</p>

使用**urllib2** ，usingThreadpoolUrllib2(3000,50)

</p>
<p>
> </p>
>
> Start at :    2012-03-16 22:18:20.956054   
> End at :    2012-03-16 22:22:15.203018   
> Total Cost :    0:03:54.246964   
> Total url : 3001   
> Total fetched : 2442   
> Lost url : 559   
> 下载页面的物理存储大小：84088kb
>
> </p>
>
> <p>

</p>

使用自己的**getPageUsingGet** ，usingThreadpool(3000,50)

</p>
<p>
> </p>
>
> Start at :    2012-03-16 22:23:40.206730   
> End at :    2012-03-16 22:26:26.843563   
> Total Cost :    0:02:46.636833   
> Total url : 3002   
> Total fetched : 2484   
> Lost url : 518   
> Error 404 : 94   
> Error timeout : 312   
> Error Try too many times  0   
> Error Other faults  112   
> 下载页面的物理存储大小：87168kb
>
> </p>
>
> <p>

</p>

**小结：**
自己写的下载页面程序，效率还是很不错的，而且丢失的页面也较少。但其实自己考虑一下，还是有很多地方可以优化的，比如文件过于分散，过多的小文件创建和释放定会产生不小的性能开销，而且程序里用的是hash命名，也会产生很多的计算，如果有好的策略，其实这些开销都是可以省略的。另外DNS，也可以不使用python自带的DNS解析，因为默认的DNS解析都是同步的操作，而DNS解析一般比较耗时，可以采取多线程的异步的方式进行，再加以适当的DNS缓存很大程度上可以提高效率。不仅如此，在实际的页面抓取过程中，会有大量的url
，不可能一次性把它们存入内存，而应该按照一定的策略或是算法进行合理的分配。
总之，采集页面要做的东西以及可以优化的东西，还有很多很多。

</p>

**附件下载：[程序代码（水平有限，仅供参考）][]**

</p>

**略改进版：[minicrawler（里面的beautifulSoup需要改成3.x版本的）][]**

</p>

  [线程池]: http://www.cnblogs.com/coser/archive/2012/03/10/2389264.html
  [程序代码（水平有限，仅供参考）]: http://files.cnblogs.com/coser/fetchPages.zip
  [minicrawler（里面的beautifulSoup需要改成3.x版本的）]: http://files.cnblogs.com/coser/miniCrawler-SY1206509-%E5%BC%A0%E7%AB%8B%E9%91%AB.rar
