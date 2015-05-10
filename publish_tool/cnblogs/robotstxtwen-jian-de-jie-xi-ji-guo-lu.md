Title: robots.txt文件的解析及过滤
Date: 2012-04-03 06:33
Author: 糖拌咸鱼
Slug: robotstxtwen-jian-de-jie-xi-ji-guo-lu

**什么是robots.txt文件?**

</p>

       
robots.txt（统一小写）是一种存放于[网站][]根目录下的[ASCII][]编码的[文本文件][]，它通常告诉网络[搜索引擎][]的漫游器（又称[网络蜘蛛][]），此网站中的哪些内容是不能被搜索引擎的漫游器获取的，哪些是可以被（漫游器）获取的。
因为一些系统中的URL是大小写敏感的，所以robots.txt的文件名应统一为小写。robots.txt应放置于网站的根目录下。如果想单独定义搜索引擎的漫游器访问子目录时的行为，那么可以将自定的设置合并到根目录下的robots.txt，或者使用robots[元数据][]。Robots.txt协议并不是一个规范，而只是约定俗成的，所以并不能保证网站的隐私。 ——维基百科（<http://zh.wikipedia.org/wiki/Robots.txt>）

</p>

**基本属性：**

</p>

User-agent: 定义搜索引擎的类型  
Disallow: 定义禁止搜索引擎收录的地址  
Allow: 定义允许搜索引擎收录的地址  
Crawl-delay:支持Crawl-delay参数，设置为多少秒，以等待同服务器之间连续请求(网络爬虫的礼貌策略)  
\#:一些robots.txt 会有注释，\#后面都是注释内容，需要过滤掉 

</p>

**一些例子；**

</p>

User-agent: \* 这里的\*代表的所有的搜索引擎种类，\*是一个通配符  
Disallow: /admin/ 这里定义是禁止爬寻admin目录下面的目录  
Disallow: /require/ 这里定义是禁止爬寻require目录下面的目录  
Disallow: /ABC/ 这里定义是禁止爬寻ABC目录下面的目录  
Disallow: /cgi-bin/\*.htm
禁止访问/cgi-bin/目录下的所有以".htm"为后缀的URL(包含子目录)。  
Disallow: /\*?\* 禁止访问网站中所有的动态页面  
Disallow: /jpg\$ 禁止抓取网页所有的.jpg格式的图片  
Disallow:/ab/adc.html 禁止爬去ab文件夹下面的adc.html文件。  
Allow: /cgi-bin/　这里定义是允许爬寻cgi-bin目录下面的目录  
Allow: /tmp 这里定义是允许爬寻tmp的整个目录  
Allow: .htm\$ 仅允许访问以".htm"为后缀的URL。  
Allow: .gif\$ 允许抓取网页和gif格式图片  
Crawl-delay: 10 

</p>

**C++实现解析robots.txt，并对url进行过滤：**

</p>

robotsFilter.h

</p>

<div class="cnblogs_code">

</p>
<p>
    /* * urlFilter.h * *  Created on: 2012-3-26 *      Author: xiaojay */#ifndef URLFILTER_H_#define URLFILTER_H_#include "../urlFrontier/url.h"#include<string.h>#include<assert.h>#include <iostream>using namespace std;#define MAXDISALLOW 100//接口class urlFilter{public:    // 当u合法时，返回true，否则返回false    virtual bool filter(url * u) = 0;    virtual bool filter(const char * url_text) = 0;};//robots.txt过滤class robotsFilter : public urlFilter{public:    robotsFilter(const char * host_name , const char * robots_txt);    ~robotsFilter();    virtual bool filter(url * u);    virtual bool filter(const char * url_text);    void parseRobots();    void printDisallow();    bool robotsMatch(char * match , char * file);private:    char * strlwr(char *); //辅助函数，大写转小写    char * disallow [MAXDISALLOW];    int disallow_size;    char * allow[MAXDISALLOW];    int allow_size;    char * hostname;    char * robotstxt;    int crawldelay ;};#endif /* URLFILTER_H_ */

</p>
<p>

</div>

</p>

robotsFilter.cpp

</p>

<div class="cnblogs_code">

</p>
<p>
    /* * robotFilter.cpp * *  Created on: Mar 31, 2012 *      Author: mayday */#include "urlFilter.h"// 初始化相关参数robotsFilter::robotsFilter(const char * host_name , const char * robots_txt){    assert(host_name!=NULL && robots_txt!=NULL);    int len = strlen(host_name);    hostname = new char [len + 1];    strcpy(hostname,host_name);    len = strlen(robots_txt);    robotstxt = new char [len + 1];    strcpy(robotstxt,robots_txt);    disallow_size = 0;    allow_size = 0;    crawldelay = 0;}robotsFilter::~robotsFilter(){    delete [] hostname;    delete [] robotstxt;    for(int i=0;i<disallow_size;i++)    {        delete [] disallow[i];    }    for(int i=0;i<allow_size;i++)    {        delete [] allow[i];    }}char* robotsFilter::strlwr( char* str ){    char* orig = str;    // process the string    for (;*str != '\0'; str++ )        *str = tolower(*str);    return orig;}//解析robots文本void robotsFilter::parseRobots(){    //cout<<robotstxt<<endl;    //key:value     char key [32];    char value [100];    int i,j;    int posl = 0, posm = 0 ,posr =0;    int len = strlen(robotstxt);    bool hasAgent = false;    //总体思路，确定三个标志的位置，然后分割字符串. ——>posl( key )posm( value )posr    while(posl<len && posm<len && posr<len)    {        //找到第一个不为空格和换行符的字符位置，确定posl        while(posl<len && (robotstxt[posl]==' '                || robotstxt[posl]=='\n' || robotstxt[posl]=='\r')) posl++;        //以#开头的，直接过滤掉该行        if(robotstxt[posl]=='#')        {            while(posl<len && robotstxt[posl]!='\n') posl++;            continue;        }        //找‘：’,确定posm        posm = posl+1;        while(posm<len && robotstxt[posm]!=':') posm++;        //找换行符位置，确定posr        posr = posm+1;        while(posr<len && robotstxt[posr]!='\n') posr++;        for(j=0,i=posl;i<posm;i++)        {            if(robotstxt[i]!=' '&&robotstxt[i]!='\t'&&robotstxt[i]!='\r'&&robotstxt[i]!='\n')                key[j++] = robotstxt[i];        }        key[j] = '\0';        for(j=0,i=posm+1;i<posr;i++)        {            if(robotstxt[i]!=' '&&robotstxt[i]!='\t'&&robotstxt[i]!='\r'&&robotstxt[i]!='\n')                value[j++] = robotstxt[i];        }        value[j]='\0';        posl = posr;        //cout<<key<<"\t"<<value<<endl;        //确定user-agent，是否针对本爬虫        if(strcmp(strlwr(key),"user-agent")==0){            if(strcmp(value,"*")==0||strcmp(value,"webcrawler")==0)            {                hasAgent = true;            }            else hasAgent = false;        }        if(hasAgent)        {            int len_val = strlen(value);            if(len_val<=0) continue;            if(strcmp(strlwr(key),"disallow")==0 && disallow_size<MAXDISALLOW)            {                disallow[disallow_size] = new char [len_val+1];                strcpy(disallow[disallow_size],strlwr(value));                disallow_size++;            }            else if (strcmp(strlwr(key),"allow")==0 && allow_size<MAXDISALLOW)            {                allow[allow_size] = new char [len_val+1];                strcpy(allow[allow_size],strlwr(value));                allow_size++;            }            else if(strcmp(strlwr(key),"craw-delay")==0)            {                crawldelay = 0;                int len_val = strlen(value);                for(int i=0;i<len_val;i++)                {                    crawldelay = crawldelay * 10 + value[i]-'0';                }            }        }    }}void robotsFilter::printDisallow(){    for(int i=0;i<disallow_size;i++)    {        cout<<disallow[i]<<endl;    }}

</p>
<p>
    //url->file属性与robots.txt匹配串的匹配，如果匹配成功返回true，否则返回falsebool robotsFilter::robotsMatch(char * match ,char * file){    int len_match = strlen(match);    if(len_match<=1) return true;    int len_file =  strlen(file);    if(len_match>len_file) return false;    // ends with '$'    if(match[len_match-1]=='$')    {        int pos_match = 0;        char head [50],tail[20];        pos_match = len_match - 1;        while(pos_match>=0&&match[pos_match]!='*') pos_match --;        strncpy(head,match,pos_match);        head[pos_match] = '\0';        strncpy(tail,match+pos_match+1,len_match-pos_match-2);        tail[len_match-pos_match-2] = '\0';        int lhead = pos_match;        int ltail =    len_match-pos_match-2;        int i = 0;        while(i<lhead && head[i]==file[i]) i++;        if(i!=lhead) return false;        i=0;        while(i<ltail && tail[i]==file[len_file-ltail+i]) i++;        if(i!=ltail) return false;        return true;    }    // 统计 '*'    int starlist [10] , starcount=0;    for(int i=0;i<len_match;i++)        if(match[i]=='*')            starlist[starcount++] = i;    //if have no star    if(starcount==0)    {        int i=0;        while(i<len_match && match[i]==file[i]) i++;        if(i!=len_match) return false;        else return true;    }    // if have star    /*    算法如下，首先按照'*',分割为多给子串    然后各个子串需按序匹配到file文本，且每个子串按首次匹配为准    */        int i=0;    //test head    while(i<starlist[0]&&match[i]==file[i]) i++;    if (i!=starlist[0]) return false;    //test tail    if(match[len_match-1]!='*')    {        int length = len_match - (starlist[starcount-1] + 1);        i = 0;        while(i<length && match[len_match - i -1] == file[len_file - i -1]) i++;        if (i!=length) return false;    }    // match each star    int start_match , end_match , start_file  = starlist[0];    char case_str [50];    for(int i=1;i<starcount;i++)    {        start_match = starlist[i-1]+1;        end_match = starlist[i];        strncpy(case_str,match+start_match,end_match-start_match);        case_str[end_match-start_match] = '\0';        int i = start_file;        int j = 0;        //match case_str , perhaps KMP algorithms is better than mine        while(i<len_file && j<(end_match-start_match))        {            if(file[i]==case_str[j]){                ++i;++j;            }else{                i = i-j+1;                j = 0;            }        }        if(j==(end_match-start_match))        {            start_file = i;        }else return false;    }    return true;}// if u->file matches robots.txt ,return false ; otherwise truebool robotsFilter::filter(url * u){    /*     *robots.txt里面可能有Allow，也可能有Disallow     *其实如果两个都设置的话，会有一点歧义，crawler不知道到底应不应该爬     *这里给出的方法是：两个都进行测试，只要通过一个就ok。     */    if(disallow_size<=0 && allow_size<=0 ) return true;    bool pass_disallow = true;    if(disallow_size>0)    {        if(strcmp(disallow[0],"/")==0 || strcmp(disallow[0],"*")==0                ||strcmp(disallow[0]," ")==0 ||strcmp(disallow[0],"")==0)            pass_disallow = false;        else        {            for(int i=0;i<disallow_size;i++)            {                if (robotsMatch(disallow[i],u->getFile())) {                    pass_disallow = false;                    break;                }            }        }    }    else pass_disallow = false;    if(pass_disallow==true) return true;    bool pass_allow = false;    if (allow_size>0)    {        if(strcmp(allow[0],"/")==0 || strcmp(allow[0],"*")==0) pass_allow = true;        else        {            for(int i=0;i<allow_size;i++)            {                if (robotsMatch(allow[i],u->getFile()))                {                    pass_allow = true;                    break;                }            }        }    }    return pass_allow;}bool robotsFilter::filter(const char * url_text){    char tmp [150];    strcpy(tmp,url_text);    url * u = new url(tmp,0,0);    bool res = filter(u);    delete u;    return res;}

</p>
<p>

</div>

</p>

  
  
  

</p>

  [网站]: http://zh.wikipedia.org/wiki/%E7%BD%91%E7%AB%99 "网站"
  [ASCII]: http://zh.wikipedia.org/wiki/ASCII "ASCII"
  [文本文件]: http://zh.wikipedia.org/wiki/%E6%96%87%E6%9C%AC%E6%96%87%E4%BB%B6
    "文本文件"
  [搜索引擎]: http://zh.wikipedia.org/wiki/%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E
    "搜索引擎"
  [网络蜘蛛]: http://zh.wikipedia.org/wiki/%E7%BD%91%E7%BB%9C%E8%9C%98%E8%9B%9B
    "网络蜘蛛"
  [元数据]: http://zh.wikipedia.org/wiki/%E5%85%83%E6%95%B0%E6%8D%AE
    "元数据"
