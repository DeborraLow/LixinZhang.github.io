Title: TCP连接的建立以及利用tcpdump分析连接建立的过程
Date: 2010-12-05 12:49
Author: 糖拌咸鱼
Slug: tcplian-jie-de-jian-li-yi-ji-li-yong-tcpdumpfen-xi-lian-jie-jian-li-de-guo-cheng

TCP连接的建立以及利用tcpdump分析连接建立的过程
==============================================

</p>

<span>一、实验目的</span>
=========================

</p>

**<span>实验</span><span lang="EN-US">1\_1</span><span>：</span>**

</p>

<span>使用</span><span
lang="EN-US">Freebsd/Linux</span><span>操作系统下的</span><span
lang="EN-US">C</span><span>编译器和网络程序的调试方法，掌握</span><span
lang="EN-US">TCP</span><span>连接建立和终止以及调整缓冲区大小的方法。</span>

</p>

<span lang="EN-US"> </span>

</p>

**<span>实验</span><span lang="EN-US">1\_2</span><span>：</span>**

</p>

<span>使用<span
lang="EN-US">ethereal/TCPDump</span>等抓包工具，截取<span
lang="EN-US">TCP</span>建立过程中产生的数据包，分析连接建立过程。</span>

</p>

<span>二、实验环境</span>
=========================

</p>

<span>操作系统：</span><span lang="EN-US">Ubuntu
10.04</span><span>系统</span>

</p>

<span>编辑器：</span><span lang="EN-US">vim</span>

</p>

<span>网络环境：</span><span lang="EN-US">PC1</span><span>：</span><span
lang="EN-US">Ipv4</span><span>地址</span><span
lang="EN-US">10.3.1.210</span>

</p>

<span lang="EN-US"><span>             </span><span> 

</span>PC2</span><span>：</span><span
lang="EN-US">Ipv4</span><span>地址</span><span lang="EN-US">

10.3.1.211</span>

</p>

<span lang="EN-US"><span>             </span><span> 

</span></span><span>两台电脑在同一个网段，可以互相通信，能</span><span
lang="EN-US">ping</span><span>通。</span>

</p>

<span>代码语言：</span><span lang="EN-US">c</span><span>语言</span>

</p>

<span>代码编译器：</span><span
lang="EN-US">gcc</span><span>编译器</span>

</p>

<span>三、实验内容</span>
=========================

</p>

<!--[if !supportLists]--><strong><span lang="EN-US"><span>1.<span>      

</span></span></span></strong><!--[endif]-->**<span>设计思路</span> **

</p>

<span>该实验分为两部分：</span><span
lang="EN-US">Tcp</span><span>通信的连接以及利用</span><span
lang="EN-US">tcpdump</span><span>进行抓包，从抓包的内容分析</span><span
lang="EN-US">Tcp</span><span>进行连接的过程。</span>

</p>

**<span>第一部分：</span><span
lang="EN-US">Tcp</span><span>连接的建立</span> **

</p>

<span lang="EN-US">Server</span><span>端：</span>

</p>

<span
lang="EN-US"><span>      </span></span><span>思路：需要定义两个</span><span
lang="EN-US">socket</span><span>，一个用于监听，一个用于接受客户端传来的</span><span
lang="EN-US">socket</span><span>。定义</span><span
lang="EN-US">ipv4</span><span>地址参数，指定</span><span
lang="EN-US">Ip</span><span>地址和端口号。然后进行</span><span
lang="EN-US">bind</span><span>，</span><span
lang="EN-US">bind</span><span>成功后进行对指定</span><span
lang="EN-US">socket</span><span>的监听。当有客户端进行连接请求时，</span><span
lang="EN-US">accept</span><span>函数会接收到来自</span><span
lang="EN-US">Client</span><span>端的</span><span
lang="EN-US">socket</span><span>。然后</span><span
lang="EN-US">Server</span><span>将输出</span><span
lang="EN-US">Client</span><span>端相关信息，例如</span><span
lang="EN-US">Ip</span><span>地址或是端口号等，在向客户端</span><span
lang="EN-US">buffer</span><span>流写入欢迎信息。最后关闭连接。</span>

</p>

**<span lang="EN-US"> </span>**

</p>

<span lang="EN-US">Client</span><span>端：</span>

</p>

<span>思路：定义一个</span><span
lang="EN-US">char</span><span>字符数组，用于接受服务器端，传来的信息。定义一个</span><span
lang="EN-US">socket</span><span>，然后定义指定服务器端</span><span
lang="EN-US">Ipv4</span><span>地址以及端口号。然后</span><span
lang="EN-US">client</span><span>端主动进行</span><span
lang="EN-US">connect</span><span>连接。连接成功后，接受</span><span
lang="EN-US">Server</span><span>端写入的信息，然后逐一读出，并打印在屏幕上。</span>

</p>

<span lang="EN-US"> </span>

</p>

**<span>第二部分：抓包</span> **

</p>

<span>利用</span><span
lang="EN-US">tcpdump</span><span>抓包工具，进行抓包，然后查看抓包内容。通过</span><span>截取<span
lang="EN-US">TCP</span>建立过程中产生的数据包，分析连接建立过程。</span>

</p>

 

</p>

 

</p>

 

</p>

<span>四、相关代码</span>
=========================

</p>

**server:**

</p>

<span face="monospace" size="2" style="font-family: monospace; font-size: x-small;"><span style="line-height: normal; white-space: pre-wrap;">

<div class="cnblogs_code">

</p>
<p>
    #include <stdio.h>#include <string.h>#include <arpa/inet.h>#include <netinet/in.h>#include <sys/socket.h>#define MAXSIZE 1024int main(int argc , char * * argv ){    char buffer[MAXSIZE];    int listenfd=socket(AF_INET,SOCK_STREAM,0);//定义socket，指向ipv4地址的字节流套接口        struct sockaddr_in serverAddr;    memset(&serverAddr,0,sizeof(serverAddr));//sockAddr_in 进行初始化    serverAddr.sin_family=AF_INET;    serverAddr.sin_addr.s_addr=htonl(INADDR_ANY);    serverAddr.sin_port=htons(2000);    if(bind(listenfd,(struct sockaddr *) &serverAddr,sizeof(serverAddr))==-1)    {        printf("There is an error during binding\n");        return -1;    }    else    {        printf("Bind successfully!!!\n");    }    //对listenfd进行监听，从最初建立时的主动套接口（用于进行connect的套接口）转化为被动套接口（接受连接）    listen(listenfd,100);//第二个参数为套接口排队的最大连接个数    int connectfd;    socklen_t addrlen;    struct sockaddr_in connectAddr;    memset(&connectAddr,0,sizeof(connectAddr));    printf("Be ready to accept a connection!\n");    while(1)    {        connectfd=accept(listenfd,(struct sockAddr * )&connectAddr,&addrlen);//接受client端一个请求的socket        char * clientAddress=inet_ntop(AF_INET,&connectAddr.sin_addr,buffer,sizeof(buffer));//获取客户端的ip地址        int clientPort=connectAddr.sin_port;//获取客户端的端口号        //打印出客户端的ip地址以及端口号        printf("Connect from %s , port %d \n",clientAddress,clientPort);        snprintf(buffer,sizeof(buffer),"%s","Welcome to server!\n");                write(connectfd,buffer,sizeof(buffer));        close(connectfd);    }    close(listenfd); //虽然因为上面有while（true），这行永远都执行不了，但是时刻注意关闭socket连接应该是个好习惯。             return 0;}

</p>
<p>

</div>

</p>
  
</span></span>

</p>

**client:**

</p>

**  
**

</p>

<span face="monospace" size="2" style="font-family: monospace; font-size: x-small;"><span style="line-height: normal; white-space: pre-wrap;">

<div class="cnblogs_code">

</p>
<p>
    #include <stdio.h>#include <string.h>#include <arpa/inet.h>#include <netinet/in.h>#include <sys/socket.h>#define MAXLINE 4096int main( int argc , char * * argv ){    int sockfd , n ;    char recvline[ MAXLINE + 1];    struct sockaddr_in servaddr;    if( ( sockfd = socket( AF_INET , SOCK_STREAM , 0 ) ) < 0 ) {        printf( "socket error\n" );        exit( 1 );    }    memset( &servaddr , 0 , sizeof( servaddr ) );    servaddr.sin_family = AF_INET;    servaddr.sin_port = htons( 2000 );//指定Server端的端口号    char * serverAddress="127.0.0.1";    //判断指定的ip地址是否有错误    if( inet_pton( AF_INET ,serverAddress , &servaddr.sin_addr ) <= 0 )  {        printf( "inet_pton error for %s\n" , serverAddress );        exit( 1 );     }    if( connect( sockfd , (struct sockaddr *)&servaddr , sizeof( servaddr ) ) < 0 )  {        printf( "connect error\n" );        exit( 1 );    }    while( ( n = read( sockfd , recvline , MAXLINE ) ) > 0 )  {        recvline[ n ] = 0;        if( fputs( recvline , stdout ) == EOF ) {            printf( "fputs error\n" );            exit( 1 );        }    }    if( n < 0 )  {        printf( "read error\n" );        exit( 1 );    }    exit( 0 );  }

</p>
<p>

</div>

</p>
  
</span></span>

</p>

**<span>编译代码：</span><span lang="EN-US"> </span>**

</p>

<span>

</span>

</p>

<table border="0" cellpadding="0" cellspacing="0">
</p>
<p>
<tbody>
</p>
<p>
<tr>
</p>
<p>
<td bgcolor="white" height="49" width="615">
<!--[endif]--><!--[if !mso]--><span>

</p>

<table border="0" cellpadding="0" cellspacing="0" style="width: 100%;">
</p>
<p>
<tbody>
</p>
<p>
<tr>
</p>
<p>
<td>
<!--[endif]-->

</p>

<div class="shape">

</p>

<span lang="EN-US">Gcc Server.c –o server</span>

</p>

<span lang="EN-US">Gcc Client.c –o client</span>

</p>
<p>

</div>

</p>
<p>
<!--[if !mso]-->

</td>
</p>
<p>
</tr>
</p>
<p>
</tbody>
</p>
<p>
</table>
</p>
<p>
</span><!--[endif]--><!--[if !mso & !vml]--> 

</td>
</p>
<p>
</tr>
</p>
<p>
</tbody>
</p>
<p>
</table>
</p>

<span>

</span>

</p>

**<span>监听抓包代码：</span><span lang="EN-US"> </span>**

</p>

<span><span>

</span></span>

</p>

<table border="0" cellpadding="0" cellspacing="0">
</p>
<p>
<tbody>
</p>
<p>
<tr>
</p>
<p>
<td bgcolor="white" height="33" width="615">
<!--[endif]--><!--[if !mso]--><span>

</p>

<table border="0" cellpadding="0" cellspacing="0" style="width: 100%;">
</p>
<p>
<tbody>
</p>
<p>
<tr>
</p>
<p>
<td>
<!--[endif]-->

</p>

<div class="shape">

</p>

<span lang="EN-US">sudo tcpdump –s 0 –w socketlog host

10.3.1.210 and host 2000</span>

</p>
<p>

</div>

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
</tbody>
</p>
<p>
</table>
</p>
<p>
</span>

</td>
</p>
<p>
</tr>
</p>
<p>
</tbody>
</p>
<p>
</table>
</p>

<span><span>

</span></span>

</p>

<span>

</span>

</p>

<table border="0" cellpadding="0" cellspacing="0">
</p>
<p>
<tbody>
</p>
<p>
<tr>
</p>
<p>
<td bgcolor="white" height="48" width="614">
**<span>读取抓包文件代码：</span>**

</td>
</p>
<p>
</tr>
</p>
<p>
</tbody>
</p>
<p>
</table>
</p>

<span>

</span>

</p>

**<span lang="EN-US"> s</span>**udo tcpdump –r socketlog –A \>\> log

</p>

<span lang="EN-US"> vi log</span>

</p>

 

</p>

 **操作过程**

</p>

<span lang="EN-US">

</span>

</p>

<span lang="EN-US">1.</span><span>在</span><span
lang="EN-US">Server</span><span>端，启动</span><span
lang="EN-US">tcpdump</span><span>进行抓包。在</span><span
lang="EN-US">Client</span><span>发出一个连接请求，并进行一次实验一的连接。</span>

</p>

<span
lang="EN-US">2.</span><span>读取获取的包，并将其放入一个</span><span
lang="EN-US">log</span><span>文件中，用以分析。</span>

</p>

<span lang="EN-US">3.</span><span>读取</span><span
lang="EN-US">log</span><span>文件。</span>

</p>

<span lang="EN-US"> </span>

</p>

<span lang="EN-US"> </span>

</p>

**<span>分析与结论：</span><span lang="EN-US"> </span>**

</p>

<span
lang="EN-US"><span>      </span></span><span>从抓包的文件可以看出，此次通信，</span><span
lang="EN-US">Server</span><span>端获取到了所有的</span><span
lang="EN-US">package</span><span>。不仅如此，我们也发现了，通信的内容并没有进行加密，而是明文的传送，因为我们成功获取了</span><span
lang="EN-US">Server</span><span>端发给</span><span
lang="EN-US">Client</span><span>的“</span><span lang="EN-US">Welcome to
server</span><span>”的明文信息。</span><span lang="EN-US"> </span>

</p>

<span
lang="EN-US"><span>      </span></span><span>通过包中的内容，我们不难分析出</span><span
lang="EN-US">Tcp</span><span>通信的连接过程。</span><span
lang="EN-US"> </span>

</p>

<!--[if !supportLists]--><span
lang="EN-US"><span>1.<span>     </span></span></span><!--[endif]--><span
lang="EN-US">Client</span><span>端发送</span><span
lang="EN-US">SYN</span><span>，请求进行连接。</span><span
lang="EN-US"> </span>

</p>

<!--[if !supportLists]--><span
lang="EN-US"><span>2.<span>     </span></span></span><!--[endif]--><span
lang="EN-US">Server</span><span>端回复</span><span lang="EN-US">ACK
<span></span></span><span>，</span><span lang="EN-US">MSS=1460</span>

</p>

<!--[if !supportLists]--><span
lang="EN-US"><span>3.<span>     </span></span></span><!--[endif]--><span
lang="EN-US">Client</span><span>端回复</span><span
lang="EN-US">ACK</span><span>，自此</span><span
lang="EN-US">TCP</span><span>连接建立的三次握手完成。</span><span
lang="EN-US"> </span>

</p>

<!--[if !supportLists]--><span
lang="EN-US"><span>4.<span>     </span></span></span><!--[endif]--><span
lang="EN-US">Server</span><span>端发送数据</span><span></span><span>请求</span><span
lang="EN-US">ACK</span>

</p>

<!--[if !supportLists]--><span
lang="EN-US"><span>5.<span>     </span></span></span><!--[endif]--><span
lang="EN-US">Client</span><span>端读取数据，应答</span><span
lang="EN-US">ACK</span>

</p>

<!--[if !supportLists]--><span
lang="EN-US"><span>6.<span>     </span></span></span><!--[endif]--><span
lang="EN-US">Server</span><span>端首先关闭连接，</span><span
lang="EN-US">FIN</span>

</p>

<!--[if !supportLists]--><span
lang="EN-US"><span>7.<span>     </span></span></span><!--[endif]--><span
lang="EN-US">Client</span><span>端回复</span><span
lang="EN-US">ACK</span>

</p>

<!--[if !supportLists]--><span
lang="EN-US"><span>8.<span>     </span></span></span><!--[endif]--><span
lang="EN-US">Server</span><span>端</span><span></span><span>回复</span><span
lang="EN-US">ACK</span><span>连接自此关闭</span><span
lang="EN-US"> </span>

</p>

