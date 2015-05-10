Title: unix下网络编程之I/O复用（二）
Date: 2012-02-29 07:04
Author: 糖拌咸鱼
Slug: unixxia-wang-luo-bian-cheng-zhi-iofu-yong-er

<span style="font-size: x-large;">**select函数**</span>

</p>

该函数允许进程指示内核等待多个事件中的任何一个发生，并仅在有一个或是多个事件发生或经历一段指定的时间后才唤醒它。我们调用select告知内核对哪些描述字（就读、写或异常条件）感兴趣以及等待多长时间。我们感兴趣的描述字不局限于套接口，任何描述字都可以使用select来测试。

</p>

**select函数原型：**

</p>

<div class="cnblogs_code">

</p>
<p>
    #include<sys/select.h>#include<sys/time.h>int select (int maxfd , fd_set *readset ,fd_set *writeset, fd_set *exceptionset , const struct timeval * timeout);返回:就绪描述字的正数目，0——超时，-1——出错

</p>
<p>

</div>

</p>

select函数的参数介绍：maxfd表示待测试的描述字**个数**，其值应该为最大的描述字+1，中间的readset,writeset,exceptionset指定我们要让内核测试读、写、异常条件的描述字，最后一个参数告知内核等待所指定描述字中的任何一个就绪可花多长时间。

</p>

**timeval结构：**

</p>

<div class="cnblogs_code">

</p>
<p>
    struct timeval {long tv_sec; //secondslong tv_usec ; //microseconds}

</p>
<p>

</div>

</p>

timeval参数有三种可能值：1、NULL：代表永远等待下去，相当于完全阻塞。2、一个固定的值，代表等待一段固定的时间。3、timeval的属性值为0，表示根本不等待，检查描述字之后立即返回，也就是说事非阻塞的。

</p>

**fd\_set结构：**

</p>

fd\_set结构表示一个描述字集。它典型的应该以一个整数数组来表示，其中每个整数中的每一位对应一个描述字。关于fd\_set有以下四个宏：

</p>
<p>
> </p>
>
> <div class="cnblogs_code">
>
> </p>
> <p>
>     void FD_ZERO(fd_set *fdset); /* clear all bits in fdset */void FD_SET(int fd, fd_set *fdset); /* turn on the bit for fd in fdset */void FD_CLR(int fd, fd_set *fdset); /* turn off the bit for fd in fdset */int FD_ISSET(int fd, fd_set *fdset); /* is the bit for fd on in fdset ? */
>
> </p>
> <p>
>
> </div>
>
> </p>
> <p>

</p>

select函数修改由指针readset，writeset，exceptionset所指向的描述字集，因而这三个参数都是值-结果参数。也就是说，在select函数执行过程中，会修改其中的值。调用该函数时，我们指定关心的描述字的值，该函数返回时，结果指示哪些描述字已就绪。该函数返回后，我们使用FD\_ISSET来测试fd\_set数据类型中的描述字。描述字集中任何与未就绪的描述字对应的位返回时均清为0.为此，每次重新调用select函数中，我们都得再次把所有描述字集合中的所关心的位置为1。这也是在稍候的通信例子里，我们设置resset和allset两个集合的原因所在。

</p>

**select函数返回某个套接口就绪的条件：**

</p>

![][]

</p>

**select函数的通信例子：一个简单的TCP回射服务器程序**

</p>

**SelectServer.c: 使用select机制的服务器端程序**

</p>

 

</p>

<div class="cnblogs_code">

</p>
<p>
      1 #include <stdio.h>  2 #include <string.h>  3 #include <arpa/inet.h>  4 #include <netinet/in.h>  5 #include <sys/socket.h>  6 #include <sys/select.h>  7   8 const static int MAXLINE = 1024;  9 const static int SERV_PORT = 10001; 10  11 int main1() 12 { 13     int i , maxi , maxfd, listenfd , connfd , sockfd ; 14     /*nready 描述字的数量*/ 15     int nready ,client[FD_SETSIZE]; 16     int n ; 17     /*创建描述字集合，由于select函数会把未有事件发生的描述字清零，所以我们设置两个集合*/ 18     fd_set rset , allset; 19     char buf[MAXLINE]; 20     socklen_t clilen; 21     struct sockaddr_in cliaddr , servaddr; 22     /*创建socket*/ 23     listenfd = socket(AF_INET , SOCK_STREAM , 0); 24     /*定义sockaddr_in*/ 25     memset(&servaddr , 0 ,sizeof(servaddr)); 26     servaddr.sin_family = AF_INET; 27     servaddr.sin_port = htons(SERV_PORT); 28     servaddr.sin_addr.s_addr = htonl(INADDR_ANY); 29  30     bind(listenfd, (struct sockaddr *) & servaddr , sizeof(servaddr)); 31     listen(listenfd , 100); 32     /*listenfd 是第一个描述字*/ 33     /*最大的描述字，用于select函数的第一个参数*/ 34     maxfd = listenfd; 35     /*client的数量，用于轮询*/ 36     maxi = -1; 37     /*init*/ 38     for(i=0 ;i<FD_SETSIZE ; i++) 39         client[i] = -1; 40     FD_ZERO(&allset); 41     FD_SET(listenfd, &allset); 42  43     for (;;) 44     { 45         rset = allset; 46         /*只select出用于读的描述字，阻塞无timeout*/ 47         nready = select(maxfd+1 , &rset , NULL , NULL , NULL); 48         if(FD_ISSET(listenfd,&rset)) 49         { 50             clilen = sizeof(cliaddr); 51             connfd = accept(listenfd , (struct sockaddr *) & cliaddr , &clilen); 52             /*寻找第一个能放置新的描述字的位置*/ 53             for (i=0;i<FD_SETSIZE;i++) 54             { 55                 if(client[i]<0) 56                 { 57                     client[i] = connfd; 58                     break; 59                 } 60             } 61             /*找不到，说明client已经满了*/ 62             if(i==FD_SETSIZE) 63             { 64                 printf("Too many clients , over stack .\n"); 65                 return -1; 66             } 67             FD_SET(connfd,&allset);//设置fd 68             /*更新相关参数*/ 69             if(connfd > maxfd) maxfd = connfd; 70             if(i>maxi) maxi = i; 71             if(nready<=1) continue; 72             else nready --; 73         } 74  75         for(i=0 ; i<=maxi ; i++) 76         { 77             if (client[i]<0) continue; 78             sockfd = client[i]; 79             if(FD_ISSET(sockfd,&rset)) 80             { 81                 n = read(sockfd , buf , MAXLINE); 82                 if (n==0) 83                 { 84                     /*当对方关闭的时候，server关闭描述字，并将set的sockfd清空*/ 85                     close(sockfd); 86                     FD_CLR(sockfd,&allset); 87                     client[i] = -1; 88                 } 89                 else 90                 { 91                     buf[n]='\0'; 92                     printf("Socket %d said : %s\n",sockfd,buf); 93                     write(sockfd,buf,n); //Write back to client 94                 } 95                 nready --; 96                 if(nready<=0) break; 97             } 98         } 99 100     }101     return 0;102 }

</p>
<p>

</div>

</p>

<span style="color: #000000; background-color: #fdfdfd;"><span
style="color: #000000; background-color: #fdfdfd;"><span
style="text-decoration: underline;">  
</span></span></span>

</p>

**Client.c: 简单的客户端程序**

</p>

<div class="cnblogs_code">

</p>
<p>
     1 #include <stdio.h> 2 #include <string.h> 3 #include <arpa/inet.h> 4 #include <netinet/in.h> 5 #include <sys/socket.h> 6  7 #define MAXLINE 1024 8 int main() 9 {10     int sockfd ,n;11     char buf [MAXLINE];12     sockfd = socket(AF_INET,SOCK_STREAM ,0);13     struct sockaddr_in servaddr;14     memset(&servaddr, 0 ,sizeof(servaddr));    15     servaddr.sin_family = AF_INET;16     servaddr.sin_port = htons(10001);17     inet_pton( AF_INET ,"127.0.0.1" , &servaddr.sin_addr ) ;18 19     connect(sockfd,(struct sockaddr *)&servaddr , sizeof(servaddr));20     while(1)21     {22         printf("type some words ...\n");23         scanf("%s",buf);24         write(sockfd,buf,sizeof(buf));25         n = read(sockfd,buf,MAXLINE);26         printf("%d bytes received \n ",n);27         buf[n] = '\0';28         printf("%s\n",buf);29     }30     close(sockfd);31     return 0;32 }

</p>
<p>

</div>

</p>

**  
**

</p>

**总结：**

</p>

在本文中，介绍了select函数在I/O复用中相关内容，并给出了一个典型的TCP反射程序的样例，使用select可以处理多个客户端的并发需求。在下一篇文章中，将会重点介绍另一种常见的I/O复用函数poll的使用。

</p>

  []: http://images.cnblogs.com/cnblogs_com/coser/201202/20120229150419828.jpeg
