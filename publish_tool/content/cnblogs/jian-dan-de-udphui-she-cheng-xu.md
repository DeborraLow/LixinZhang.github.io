Title: 简单的UDP回射程序
Date: 2010-12-05 13:12
Author: 糖拌咸鱼
Slug: jian-dan-de-udphui-she-cheng-xu

**Server：**

</p>

<span face="monospace" size="2" style="font-family: monospace; font-size: x-small;"><span style="line-height: normal; white-space: pre-wrap;">

<div class="cnblogs_code">

</p>
<p>
    #include <stdio.h>#include <string.h>#include <arpa/inet.h>#include <netinet/in.h>#include <sys/socket.h>#define MAXSIZE 1024#define SERV_PORT 2000void dg_echo(int sockfd, struct sockaddr * pcliaddr, socklen_t clilen){    int n;    socklen_t len;    while(1)    {        char mesg[MAXSIZE];        //回射机制        len=clilen;        n=recvfrom(sockfd,mesg,MAXSIZE,0,pcliaddr,&len);        char servermsg[MAXSIZE]="From Server: ";        int l = strlen(servermsg);        servermsg[l]='\0';        strcat(servermsg,mesg);        sendto(sockfd,servermsg,n+l,0,pcliaddr,len);    }}int main( int args, char ** argv){    int sockfd;    struct sockaddr_in serveraddr, clientaddr;    sockfd=socket(AF_INET,SOCK_DGRAM,0);    bzero(&serveraddr,sizeof(serveraddr));    serveraddr.sin_family=AF_INET;    serveraddr.sin_addr.s_addr=htonl(INADDR_ANY);    serveraddr.sin_port=htons(SERV_PORT);    bind(sockfd,(struct sockaddr *)&serveraddr,sizeof(serveraddr));    dg_echo(sockfd,(struct sockaddr *)&serveraddr,sizeof(clientaddr));    return 0;}

</p>
<p>

</div>

</p>
  
</span></span>

</p>

**Client：**

</p>

<span face="monospace" size="2" style="font-family: monospace; font-size: x-small;"><span style="line-height: normal; white-space: pre-wrap;">

<div class="cnblogs_code">

</p>
<p>
    #include <stdio.h>#include <string.h>#include <arpa/inet.h>#include <netinet/in.h>#include <sys/socket.h>#define MAXSIZE  1024#define SERVER_PORT 2000void dg_client (FILE* fp,int sockfd, const struct sockaddr * pservaddr,socklen_t serverlen){    int n;    char sendline[MAXSIZE],recvline[MAXSIZE+1];    printf("From Client: ");    while(fgets(sendline,MAXSIZE,fp)!=NULL)    {        sendto(sockfd,sendline,strlen(sendline),0,pservaddr,serverlen);        n=recvfrom(sockfd,recvline,MAXSIZE,0,NULL,NULL);        recvline[n]='\0';        fputs(recvline,stdout);        printf("From Client: ");    }}int main (int args, char ** argv ){    int sockfd;    struct sockaddr_in serveraddr;    bzero(&serveraddr,sizeof(serveraddr));        serveraddr.sin_family=AF_INET;    serveraddr.sin_port=htons(SERVER_PORT);    inet_pton(AF_INET,"10.3.1.215",&serveraddr.sin_addr);    sockfd=socket(AF_INET,SOCK_DGRAM,0);    dg_client(stdin,sockfd,(struct sockaddr * )&serveraddr,sizeof(serveraddr));    return 0;        }

</p>
<p>

</div>

</p>
  
</span></span>

</p>

