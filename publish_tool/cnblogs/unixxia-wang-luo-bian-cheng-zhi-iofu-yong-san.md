Title: unix下网络编程之I/O复用（三）
Date: 2012-03-01 05:27
Author: 糖拌咸鱼
Slug: unixxia-wang-luo-bian-cheng-zhi-iofu-yong-san

**<font size="5">poll函数</font>**

   
在上文[unix下网络编程之I/O复用（二）][]中已经介绍了select函数的相关使用，本文将介绍另一个常用的I/O复用函数poll。poll提供的功能与select类似，不过在处理流设备时，它能够提供额外的信息。

**poll函数原型：**

``` {.brush: .cpp; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
#include<poll.h>   int poll (struct pollfd * fdarray , unsigned long nfds , int timeout);   //返回：就需描述字的个数，0——超时，-1——出错
```

</p>

** **第一个参数是指向一个结构数组第一个元素的指针，每个数组元素都是一个pollfd结构。如下：

</p>

<p>
``` {.brush: .cpp; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
struct pollfd {  int fd; //descriptor to check    short events; //events of interest on fd`    short revents; //events tha occurred on fd}
```

</p>

要测试的条件由events成员指定，函数在相应的revents成语中返回该描述字的状态。（每个描述字都有两个变量，一个为调用值，另一个为返回结果，从而避免使用值-结果参数，这与select函数是不同的）。下图列出了用于指定events标志以及测试revents标志的一些常值。

</p>

[![image][]][]

</p>

上图需要注意的是，POLLERR,POLLHUP,POLLNVAL是处理错误的描述字，因此它们也就不可以出现在input事件中，即events。poll识别三类数据：普通（normal），优先级带（priority
band）和高优先级（high priority）。

</p>

**对TCP和UPD而言，以下条件引起poll返回特定的revents。**

</p>

<em>1、 All regular TCP data and all UDP data is considered normal.

  
2、 TCP's out-of-band data (Chapter 24) is considered priority band.

  
3、 When the read half of a TCP connection is closed (e.g., a FIN is
received), this is also considered normal data and a subsequent read
operation will return 0.

  
4、 The presence of an error for a TCP connection can be considered
either normal data or an error (POLLERR). In either case, a subsequent
read will return –1 with errno set to the appropriate value. This
handles conditions such as the receipt of an RST or a timeout.

  
5、 The availability of a new connection on a listening socket can be
considered either normal data or priority data. Most implementations
consider this normal data.

  
6、 The completion of a nonblocking connect is considered to make a
socket writable.</em>

</p>

                                                                                   
——《unix网络编程》第三版

</p>

**参数nfds，指示结构数组中元素的个数。**

</p>

**参数timeout：**

</p>

与select中的timeout不同，poll函数的timeout参数是一int值，表示poll函数返回前等待多长时间，它是毫秒级别的。它有三种情况的取值：1、INFTIM（一个负数值），表示永远等待，即一直阻塞。2、0，表示立即返回，非阻塞。3、\>0，表示正待指定数目的毫秒数。

</p>

**poll函数的返回值：**

</p>

当poll发生错误时，poll函数的返回值-1，若定时器时间到之前没有任何描述字就绪，则返回0，否则返回就绪描述字的个数，即其revents成员值非0的描述字个数。

</p>

如果我们不再关心某个特定描述字，那么可以把与他对应的pollfd结构的fd成员设置成一个负值。poll函数将忽略这样的pollfd结构的events成员，返回时将它的revents成员的值置为0。

</p>

 

</p>

**poll函数的通信列子：一个简单的TCP回射服务器程序**

</p>

**pollServer.c:使用select机制的服务器程序**

</p>

<p>
``` {.brush: .cpp; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
#include <stdio.h>#include <string.h>#include <arpa/inet.h>#include <netinet/in.h>#include <sys/socket.h>#include <poll.h>/*环境为ubuntu10.04自带c环境，无法自动引入下列宏，所以自己写在前面了*/#define INFTIM -1#define POLLRDNORM    0x040       /* Normal data may be read.  */#define POLLRDBAND    0x080       /* Priority data may be read.  */#define POLLWRNORM  0x100       /* Writing now will not block.  */#define POLLWRBAND 0x200       /* Priority data may be written.  */#define MAXLINE  1024#define OPEN_MAX  16 //一些系统会定义这些宏#define SERV_PORT  10001int main(){   int i , maxi ,listenfd , connfd , sockfd ;   int nready;  int n;   char buf[MAXLINE];   socklen_t clilen;    struct pollfd client[OPEN_MAX];   struct sockaddr_in cliaddr , servaddr;   listenfd = socket(AF_INET , SOCK_STREAM , 0);    memset(&servaddr,0,sizeof(servaddr));    servaddr.sin_family = AF_INET;   servaddr.sin_port = htons(SERV_PORT);    servaddr.sin_addr.s_addr = htonl(INADDR_ANY); bind(listenfd , (struct sockaddr *) & servaddr, sizeof(servaddr));   listen(listenfd,10); client[0].fd = listenfd; client[0].events = POLLRDNORM;   for(i=1;i<OPEN_MAX;i++)   {        client[i].fd = -1;   }    maxi = 0; for(;;)  {        nready = poll(client,maxi+1,INFTIM);     if (client[0].revents & POLLRDNORM)      {            clilen = sizeof(cliaddr);            connfd = accept(listenfd , (struct sockaddr *)&cliaddr, &clilen);            for(i=1;i<OPEN_MAX;i++)           {                if(client[i].fd<0)                {                    client[i].fd = connfd;                   client[i].events = POLLRDNORM;                   break;               }            }            if(i==OPEN_MAX)          {                printf("too many clients! \n");            }            if(i>maxi) maxi = i;          nready--;            if(nready<=0) continue;       }     for(i=1;i<=maxi;i++)      {            if(client[i].fd<0) continue;          sockfd = client[i].fd;           if(client[i].revents & (POLLRDNORM|POLLERR))         {                n = read(client[i].fd,buf,MAXLINE);              if(n<=0)              {                    close(client[i].fd);                 client[i].fd = -1;               }                else             {                    buf[n]='\0';                 printf("Socket %d said : %s\n",sockfd,buf);                    write(sockfd,buf,n); //Write back to client              }                nready--;                if(nready<=0) break; //no more readable descriptors           }        }    }    return 0;}
```

</p>

客户端程序参考上一篇文章。

</p>

**总结：**

</p>

  
本文介绍了poll函数的原型，参数说明，注意事项以及一个简单的代码例子。在unix后续版本中，加入了epoll函数I/O复用机制，它在一定条件下更加高效，在以后的文章中，会对epoll机制再进行详细的描述。之前在学习python的时候，也接触了select和poll，但是当时了解的比较浅显，希望通过最近的学习可以对unix下I/O复用有更深入的认识。

</p>

  [unix下网络编程之I/O复用（二）]: http://www.cnblogs.com/coser/archive/2012/02/29/2373478.html
  [image]: http://images.cnblogs.com/cnblogs_com/coser/201203/201203011326419251.png
    "image"
  [![image][]]: http://images.cnblogs.com/cnblogs_com/coser/201203/201203011326413777.png
