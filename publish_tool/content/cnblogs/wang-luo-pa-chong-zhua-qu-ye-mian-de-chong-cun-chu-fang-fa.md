Title: 网络爬虫抓取页面的一种存储方法
Date: 2012-04-02 09:38
Author: 糖拌咸鱼
Slug: wang-luo-pa-chong-zhua-qu-ye-mian-de-chong-cun-chu-fang-fa

   **前言：**

</p>

   网络爬虫抓取下来的页面，都是大文本，应该如何存储呢？
我觉得，如果存储在mysql 或是
sqlserver这种关系型数据库当中，应该不是很恰当的。首先，页面相对独立，基本没什么关系型可言，只有url或是描文本-\>页面这种简单的关系，而关系型数据库系统为了支持关系以及高效查询会增加很多额外的开销，这样得不偿失。不仅如此，爬虫在抓取页面工程中，效率应该很高，如果用关系型数据库存页面的华，短时间内会有大量的数据插入I/O，插入肯定会是一个瓶颈问题，这对数据库维护网络以及物理磁盘来说，压力也是比较大的。因此，我觉得直接存储为数据文本比较合适，开源的larbin爬虫，也采用的是文本方式的存储，但是它默认是为每个页面存储一个物理文件，我个人觉得这样的话，频繁的文件创建、写入、flush、关闭，系统开销也比较大的。
综合考虑我设计了一个方案，即一个物理文件存储多个页面，为了支持适当的查找和分割、合并操作，数据文件会对应一个索引文件。这样的话，在操作工程中，可以再索引文件中进行，索引文件相对数据文件要小得多，遍历或是查询会非常快。不仅如果，当进行数据合并的时候，只需要合并索引文件即可，这样会方便得多。

</p>

    **设计方案：**

</p>

![][]

</p>

**索引项的格式：**
页面号码，页面大小，URL文本大小，时间文本大小，URL文本 ，时间文本
(之间以空格分割，当然也可以添加其他多种数据属性)。  
**例子：**60 14328 56 25
http://www.cnblogs.com:80//coser/archive/2012/02/23.html Fri Mar 30
08:31:34 2012 ；
该记录就表示，页面号码为60，页面数据大小为14328字节，URL文本大小：56，时间文本大小：25（这两个文本大小主要用于解析后面的真实文本的时候，截取比较方便而已）,URL： http://www.cnblogs.com:80//coser/archive/2012/02/23.html，抓取时间：Fri
Mar 30 08:31:34 2012

</p>

 
 对于数据文件，多少个页面存储为一个物理文件是可以自定义的，也就是说每个数据文件的最多页面数是有一个阀值的。索引文件会根据这个阀值自动确定到页面文件。爬虫抓取下来的页面，没有任何的格式修饰，直接以Append的方式存入到文本中，只不过再存储之前需要确定该页面的大小和相关属性。对于页面的大小无须重计算，因为在网络爬取过程中的read函数会自动返回字节的大小。接下来讨论的就是，如果根据索引文件，比较高效的定位或是分割出指定的页面数据。
在linux系统编程中，存在几个重要的文件操作函数open、read、write、lseek等等。前三个函数都比较常见就不解释了，最后一个lseek说一下，lseek()是用来控制文件的读写位置的，其原型为off\_t
lseek(int fildes,off\_t offset ,int whence);
使用该函数，就可以通过索引文件中的页面文件大小的属性，来控制数据文件指针的移动，从而高效的定位到要查找的指定文件位置，根据页面size再通过read函数便可以将其读取出来。

</p>

**总结：**

</p>

 
这是我目前毕业设计（分布式网络爬虫）中的一部分内容，由于自己能力有限，之前也没过多接触这方面的内容，所以不敢保证以上内容是完全正确且合理的。写在这里，只是想记录一下自己遇到的一些问题，以及因此产生的一些想法和解决方案，大家可以一起来探讨，欢迎批评指正。

</p>

最后，贴一些关键代码（C++），感兴趣的朋友，可以参考下：

</p>

indexFile.h

</p>

<div class="cnblogs_code">

</p>
<p>
    /* * indexFile.h * *  Created on: Mar 30, 2012 *      Author: mayday */#ifndef INDEXFILE_H_#define INDEXFILE_H_#include<iostream>#include<sys/stat.h>#include<fcntl.h>#include<stdio.h>#include<string.h>#include<assert.h>#include<time.h>#include<stdlib.h>#include<vector>#define MAXFILELIMIT 10using namespace std;//索引项struct indexer{    int num; //存储号码    char url [150]; //url文本    char timep [36]; //抓取时间文本    int size; //存储页面的大小};/* * 索引文件工具类 */class indexFile{public:    //构造函数，file_name指定索引文件名， pflag指定文件读写属性    indexFile(const char * file_name , int pflag);    //设置索引参数    void set(const int size_text , const int num_text ,const char * url_text , const char * time_text);    //根据指定格式，对索引文件记录text进行解析    void parse (const char * text , int & pnum , int & psize , char * purl, char * ptime);    //迭代遍历利索引项    bool next (indexer & index);    //写文件    void writef();    //读文件，按行读    void readnextline();    //关闭文件    void closef();    //读写属性    const static int R = 0;    const static int W = 1;    const static int A = 2;private:    int flag;    char filename [30];    char array [150 + 20 + 36];    indexer idx;    mode_t mode;    FILE * fp;};/* * 根据索引文件遍历对应页面储存文件 */class scanFile{public:    //构造函数，初始化相关参数 ，basename指定页面存储文件名字 ，index_name指定索引文件名字    scanFile(const char * base_name , const char * index_name);    ~scanFile();    //根据索引文件中的页面记录号，定位页面，返回页面数据    char * locate(const int page_num);private:    //初始化offset，【agesize    void init();    //重新定位文件    void setnewfile(const int file_num);    indexFile * index;    int filefd;    char * basename;    char currentfilename [32];    int currentfilenumber;    vector<int> offset;    vector<int> pagesize;    char * page_content;};#endif /* INDEXFILE_H_ */

</p>
<p>

</div>

</p>

indexFile.cpp

</p>

<div class="cnblogs_code">

</p>
<p>
    /* * indexFile.cpp * *  Created on: Mar 30, 2012 *      Author: mayday */#include"indexFile.h"indexFile::indexFile(const char * file_name , int pflag){    assert(file_name!=NULL);    strcpy(filename,file_name);    flag = pflag;    if (pflag == R)        fp = fopen(filename,"r");    else if (pflag == W)        fp = fopen(filename,"w");    else if (pflag == A)        fp = fopen(filename,"a");    assert(fp!=NULL);}void indexFile::set    (const int num_text , const int size_text ,const char * url_text , const char * time_text){    assert(url_text!=NULL&&time_text!=NULL);    idx.size = size_text;    idx.num = num_text;    strcpy(idx.url,url_text);    strcpy(idx.timep,time_text);}void indexFile::parse    (const char * text , int & pnum , int & psize , char * purl, char * ptime){    assert(text!=NULL);    int size_url , size_time;    int len = strlen(text);    sscanf(text,"%d%d%d%d", &pnum, &psize, &size_url, &size_time);    int pos1 = len - size_time - size_url - 1;    int pos2 = pos1 + size_url;    if(purl!=NULL)    {        strncpy(purl,text+pos1,pos2-pos1);        purl[pos2-pos1] = '\0';    }    if(ptime!=NULL)    {        strncpy(ptime,text+pos2+1,len-pos2-1);        ptime[len-pos2-1] = '\0';    }}bool indexFile::next(indexer & index){    assert(flag == R);    char *line = NULL;    size_t len = 0;    getline(&line,&len,fp);    if(strlen(line)<=1) return false;    parse(line,index.num , index.size ,index.url , index.timep);    return true;}void indexFile::writef(){    assert(flag != R);    int size_url = strlen(idx.url);    int size_time = strlen(idx.timep);    sprintf(array,"%d %d %d %d %s %s",idx.num,idx.size,size_url,size_time,idx.url,idx.timep);    fwrite(array,strlen(array),sizeof(char),fp);}void indexFile::closef(){    fflush(fp);    fclose(fp);}///////////////////////////////////////////////////scanFile::scanFile(const char * base_name , const char * index_name){    assert(basename!=NULL && index_name!=NULL);    index = new indexFile(index_name,indexFile::R);    int len = strlen(base_name);    basename = new char [len + 1];    strcpy(basename,base_name);    filefd = 0;    setnewfile(0);    offset.push_back(0);    page_content = new char [96000];    init();}void scanFile::setnewfile(const int page_num){    close(filefd);    //重新命名    char num_str [7];    sprintf(num_str,"%06d",page_num);    strcpy(currentfilename,basename);    strcat(currentfilename,num_str);    currentfilenumber = page_num;    //创建 or 打开新文件    mode_t mode = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH;    filefd = open(currentfilename,O_RDONLY, mode);}scanFile::~scanFile(){    delete [] page_content;    delete [] basename;}void scanFile::init(){    indexer idx;    int counter = 0;    int pre = 0;    //遍历索引文件，记录数据页面偏移量    while(index->next(idx))    {        if(counter%MAXFILELIMIT==0)        {            pre = 0;        }        offset.push_back(pre+idx.size);        pagesize.push_back(idx.size);        pre = offset.back();        counter++;    }}char * scanFile::locate(const int page_num){    int number = page_num / MAXFILELIMIT;    if (number!=currentfilenumber)    {        //update filefd  , currentfilenumber , currentfilenumber        setnewfile(number);    }    int size_offset = offset.at(page_num-1);    int size = pagesize.at(page_num-1);    //找到数据文件的指定序号的开始位置    lseek(filefd,size_offset,SEEK_SET);    //从上面的文件位置，进行读取    read(filefd,page_content,size);    page_content[size] = '\0';    return page_content;}/*//Testint main(){    time_t timep;    time (&timep);    char * t = asctime(gmtime(&timep));    char filename [] = "fife10002.idx";    indexFile index(filename , indexFile::R);    indexer idx;    while(index.next(idx))    {        cout<<"No.\t"<<idx.num<<"\tSize:"<<idx.size<<endl;        cout<<"Fetched Url:\t"<<idx.url<<"Fetched Time:\t"<<idx.timep<<endl;    }    index.closef();    return 0;}*/

</p>
<p>

</div>

</p>

  
  
  

</p>

  []: http://pic002.cnblogs.com/images/2012/146443/2012040216580211.jpg
