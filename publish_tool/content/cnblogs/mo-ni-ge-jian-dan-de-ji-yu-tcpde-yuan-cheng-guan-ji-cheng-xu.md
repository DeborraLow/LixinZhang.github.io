Title: 模拟一个简单的基于tcp的远程关机程序
Date: 2010-12-05 13:07
Author: 糖拌咸鱼
Slug: mo-ni-ge-jian-dan-de-ji-yu-tcpde-yuan-cheng-guan-ji-cheng-xu

<span
style="white-space: pre;"></span>最近在学习unix网络编程，现在正在学习tcp的通信。其实，只要建立起了tcp通信，操作远端的计算机就不是什么问题了。正向telnet一样，也是基于tcp/IP协议的。所以这个实验，也算是对telnet功能的一种简单的模拟。

</p>

<span
style="white-space: pre;"></span>但是，值得注意的问题是关机涉及到系统权限，所以要给运行在Server端的程序以足够的权限，这样才可以在接收到Client端的关机请求时，执行关机。

</p>

将会模拟如下执行过程：

</p>

1．<span></span>执行 mytelnet 跟上参数telnet服务器 IP地址 127.0.0.1

</p>

2．<span></span>输入login 向服务器请求登录，随之服务器会要求输入密码

</p>

3．<span></span>输入一个错误的登录密码 123 

</p>

4．<span></span>服务器验证不通过，所以返回Fail to login ,please check
your password

</p>

5．<span></span>再次输入密码，这次输入正确的密码123456

</p>

6．<span></span>服务器验证通过，此时客户端可以执行基于telnet的远程操控

</p>

7．<span></span>输入操控命令，例如关机命令shutdown 

</p>

8．<span></span>服务器将会执行shutdown 操作。

</p>

**在编译时使用如下的命令：**

</p>

**Server:**

</p>

**<span face="monospace" size="2"
style="font-family: monospace; font-size: 15px;"><span
style="line-height: normal; white-space: pre-wrap;">sudo gcc server.c -o
server //足够的权限</span></span>**

</p>

**<span face="monospace" size="2"
style="font-family: monospace; font-size: 15px;"><span
style="line-height: normal; white-space: pre-wrap;">sudo chmod u+s
server </span></span>**

</p>

**<span face="monospace" size="2"
style="font-family: monospace; font-size: x-small;"><span
style="line-height: normal; white-space: pre-wrap;"><span
style="font-size: 15px;">./server</span></span></span>**

</p>

**<span face="monospace" style="font-family: monospace;"><span
style="font-size: 15px; line-height: normal; white-space: pre-wrap;">Client:</span></span>**

</p>

**<span face="monospace" size="2"
style="font-family: monospace; font-size: 15px;"><span
style="line-height: normal; white-space: pre-wrap;">gcc client.c -o
mytelnet</span></span>**

</p>

<span face="monospace" size="2"
style="font-family: monospace; font-size: x-small;"><span
style="line-height: normal; white-space: pre-wrap;">**<span
style="font-size: 15px;">./mytelnet 10.3.1.210</span>**  
</span></span>

</p>

**Client端：**

</p>

<span face="monospace" size="2" style="font-family: monospace; font-size: x-small;"><span style="line-height: normal; white-space: pre-wrap;">

<div class="cnblogs_code">

</p>
<p>
    #include <stdio.h>#include <string.h>#include <arpa/inet.h>#include <netinet/in.h>#include <sys/socket.h>#define MAXLINE 4096void clientWork(FILE* fp , int sockfd){    char sendline[MAXLINE],receiveline[MAXLINE];    int n;    while(fgets(sendline,MAXLINE,fp)!=NULL)    {        write(sockfd,sendline,strlen(sendline));        n=read(sockfd,receiveline,MAXLINE);        receiveline[n]='\0';        fputs(receiveline,stdout);        if(strcmp(receiveline,"bye\n")==0) break;    }}int main( int argc , char * * argv ){    int sockfd , n ;    char recvline[ MAXLINE + 1];    struct sockaddr_in servaddr;    if( ( sockfd = socket( AF_INET , SOCK_STREAM , 0 ) ) < 0 ) {        printf( "socket error\n" );        exit( 1 );    }    memset( &servaddr , 0 , sizeof( servaddr ) );    servaddr.sin_family = AF_INET;    servaddr.sin_port = htons( 2000 );//指定Server端的端口号    char * serverAddress=argv[1];    //判断指定的ip地址是否有错误    if( inet_pton( AF_INET ,serverAddress , &servaddr.sin_addr ) <= 0 )  {        printf( "inet_pton error for %s\n" , serverAddress );        exit( 1 );     }    if( connect( sockfd , (struct sockaddr *)&servaddr , sizeof( servaddr ) ) < 0 )  {        printf( "connect error\n" );        exit( 1 );    }    //从Terminal中读取用户输入的指令    clientWork(stdin,sockfd);    close(sockfd);    return 0;}

</p>
<p>

</div>

</p>
  
</span></span>

</p>

**Server端：**

</p>

<span face="monospace" size="2" style="font-family: monospace; font-size: x-small;"><span style="line-height: normal; white-space: pre-wrap;">

<div class="cnblogs_code">

</p>
<p>
    #include <stdio.h>#include <string.h>#include <arpa/inet.h>#include <netinet/in.h>#include <sys/socket.h>#define MAXSIZE 1024#define LOGIN 1    //登录Server#define BYE 2    //离开Server#define PASS 3    //合法登录#define DENY 4 //非法登录#define SHUTDOWN 5 //执行关机#define ERROR -1 //非法信息//记录状态信息static int STATE=0;int getClientChoice(char * clientmsg){    if(strcmp(clientmsg,"login\n")==0) return LOGIN;    if(STATE>0)    {        if(strcmp(clientmsg,"bye\n")==0) return BYE;    }    if(STATE==LOGIN)    {        //Default password is 123456        if(strcmp(clientmsg,"123456\n")==0) return PASS;        else return DENY;    }    if(STATE==PASS)    {        if(strcmp(clientmsg,"shutdown\n")==0) return SHUTDOWN;        else ERROR;        }    return ERROR;};//发送消息void sendMsg(int sockfd,char * buffer,char * msg){    char buffer2[MAXSIZE];    snprintf(buffer2,sizeof(buffer2),"%s",msg);    write(sockfd,buffer2,sizeof(buffer2));}//定义关机函数void myshutdown(){    //系统在一分钟后关机    system("shutdown -t 1");}int main(int argc , char * * argv ){    char buffer[MAXSIZE];    int listenfd=socket(AF_INET,SOCK_STREAM,0);//定义socket，指向ipv4地址的字节流套接口        struct sockaddr_in serverAddr;    memset(&serverAddr,0,sizeof(serverAddr));//sockAddr_in 进行初始化    serverAddr.sin_family=AF_INET;    serverAddr.sin_addr.s_addr=htonl(INADDR_ANY);    serverAddr.sin_port=htons(2000);    if(bind(listenfd,(struct sockaddr *) &serverAddr,sizeof(serverAddr))==-1)    {        printf("There is an error during binding\n");        return -1;    }    else    {        printf("Bind successfully!!!\n");    }    //对listenfd进行监听，从最初建立时的主动套接口（用于进行connect的套接口）转化为被动套接口（接受连接）    listen(listenfd,100);//第二个参数为套接口排队的最大连接个数    int connectfd;    socklen_t addrlen;    struct sockaddr_in connectAddr;    memset(&connectAddr,0,sizeof(connectAddr));    printf("Be ready to accept a connection!\n");    while(1)    {        connectfd=accept(listenfd,(struct sockAddr * )&connectAddr,&addrlen);//接受client端一个请求的socket        char receivebuffer[MAXSIZE];        int revbuflen;        while(1)        {            revbuflen = read(connectfd,receivebuffer,MAXSIZE);            receivebuffer[revbuflen]='\0';            //printf("%s",receivebuffer);            int clientChoice=getClientChoice(receivebuffer);        //    模拟操作过程            if(clientChoice==LOGIN)            {                STATE=LOGIN;                sendMsg(connectfd,buffer,"Please input your password :\n");            }            else if(clientChoice==PASS&&STATE==LOGIN)            {                STATE=PASS;                sendMsg(connectfd,buffer,"Welcome to my Telnet Server...\n");            }            else if(clientChoice==SHUTDOWN&&STATE==PASS)            {                myshutdown();                sendMsg(connectfd,buffer,"Remote computer is going to shutdown...\n");            }            else if (clientChoice==BYE)            {                sendMsg(connectfd,buffer,"bye\n");                break;            }            else if(clientChoice==DENY)            {                sendMsg(connectfd,buffer,"Fail to login ,please check your password\n");            }            else if(clientChoice==ERROR)            {                sendMsg(connectfd,buffer,"wrong,Check your input...\n");            }        }        close(connectfd);    }    close(listenfd); //虽然因为上面有while（true），这行永远都执行不了，但是时刻注意关闭socket连接应该是个好习惯。     return 0;}

</p>
<p>

</div>

</p>
  
</span></span>

</p>

