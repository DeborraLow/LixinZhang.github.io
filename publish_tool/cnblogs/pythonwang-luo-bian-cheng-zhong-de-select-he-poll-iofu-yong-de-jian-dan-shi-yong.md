Title: Python网络编程中的select 和 poll I/O复用的简单使用
Date: 2012-01-06 14:12
Author: 糖拌咸鱼
Slug: pythonwang-luo-bian-cheng-zhong-de-select-he-poll-iofu-yong-de-jian-dan-shi-yong

**<span
style="font-size: large;">首先列一下，sellect、poll、epoll三者的区别</span>**
  
**select**   
select最早于1983年出现在4.2BSD中，它通过一个select()系统调用来监视多个文件描述符的数组，当select()返回后，该数组中就绪的文件描述符便会被内核修改标志位，使得进程可以获得这些文件描述符从而进行后续的读写操作。

</p>

select目前几乎在所有的平台上支持，其良好跨平台支持也是它的一个优点，事实上从现在看来，这也是它所剩不多的优点之一。

</p>

select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024，不过可以通过修改宏定义甚至重新编译内核的方式提升这一限制。

</p>

另外，select()所维护的存储大量文件描述符的数据结构，随着文件描述符数量的增大，其复制的开销也线性增长。同时，由于网络响应时间的延迟使得大量TCP连接处于非活跃状态，但调用select()会对所有socket进行一次线性扫描，所以这也浪费了一定的开销。

</p>

**poll**   
poll在1986年诞生于System V Release
3，它和select在本质上没有多大差别，但是poll没有最大文件描述符数量的限制。

</p>

poll和select同样存在一个缺点就是，包含大量文件描述符的数组被整体复制于用户态和内核的地址空间之间，而不论这些文件描述符是否就绪，它的开销随着文件描述符数量的增加而线性增大。

</p>

另外，select()和poll()将就绪的文件描述符告诉进程后，如果进程没有对其进行IO操作，那么下次调用select()和poll()的时候将再次报告这些文件描述符，所以它们一般不会丢失就绪的消息，这种方式称为水平触发（Level
Triggered）。

</p>

**epoll**   
直到Linux2.6才出现了由内核直接支持的实现方法，那就是epoll，它几乎具备了之前所说的一切优点，被公认为Linux2.6下性能最好的多路I/O就绪通知方法。

</p>

epoll可以同时支持水平触发和边缘触发（Edge
Triggered，只告诉进程哪些文件描述符刚刚变为就绪状态，它只说一遍，如果我们没有采取行动，那么它将不会再次告知，这种方式称为边缘触发），理论上边缘触发的性能要更高一些，但是代码实现相当复杂。

</p>

epoll同样只告知那些就绪的文件描述符，而且当我们调用epoll\_wait()获得就绪文件描述符时，返回的不是实际的描述符，而是一个代表就绪描述符数量的值，你只需要去epoll指定的一个数组中依次取得相应数量的文件描述符即可，这里也使用了内存映射（mmap）技术，这样便彻底省掉了这些文件描述符在系统调用时复制的开销。

</p>

另一个本质的改进在于epoll采用基于事件的就绪通知方式。在select/poll中，进程只有在调用一定的方法后，内核才对所有监视的文件描述符进行扫描，而epoll事先通过epoll\_ctl()来注册一个文件描述符，一旦基于某个文件描述符就绪时，内核会采用类似callback的回调机制，迅速激活这个文件描述符，当进程调用epoll\_wait()时便得到通知。

</p>

**<span style="font-size: large;">使用 select ：</span>**   
在python中，select函数是一个对底层操作系统的直接访问的接口。它用来监控sockets、files和pipes，等待IO完成（Waiting
for I/O
completion）。当有可读、可写或是异常事件产生时，select可以很容易的监控到。
  
select.select（rlist, wlist, xlist[, timeout]）
传递三个参数，一个为输入而观察的文件对象列表，一个为输出而观察的文件对象列表和一个观察错误异常的文件列表。第四个是一个可选参数，表示超时秒数。其返回3个tuple，每个tuple都是一个准备好的对象列表，它和前边的参数是一样的顺序。下面，主要结合代码，简单说说select的使用。
  
**Server端程序:**   
1、该程序主要是利用socket进行通信，接收客户端发送过来的数据，然后再发还给客户端。
  
2、首先建立一个TCP/IP socket，并将其设为非阻塞，然后进行bind和listen。   
3、通过select函数获取到三种文件列表，分别对每个列表的每个元素进行轮询，对不同socket进行不同的处理，最外层循环直到inputs列表为空为止
  
4、当设置timeout参数时，如果发生了超时，select函数会返回三个空列表。   
**代码如下（代码中已经有很详细的注释，这里就不过多解释了）：**

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
'''Created on 2012-1-6The echo server example from the socket section can be extanded to watche for more thanone connection at a time by using select() .The new version starts out by creating a nonblockingTCP/IP socket and configuring it to listen on an address@author: xiaojay'''import selectimport socketimport Queue#create a socketserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)server.setblocking(False)#set option reusedserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR  , 1)server_address= ('192.168.1.102',10001)server.bind(server_address)server.listen(10)#sockets from which we except to readinputs = [server]#sockets from which we expect to writeoutputs = []#Outgoing message queues (socket:Queue)message_queues = {}#A optional parameter for select is TIMEOUTtimeout = 20while inputs:    print "waiting for next event"    readable , writable , exceptional = select.select(inputs, outputs, inputs, timeout)    # When timeout reached , select return three empty lists    if not (readable or writable or exceptional) :        print "Time out ! "        break;        for s in readable :        if s is server:            # A "readable" socket is ready to accept a connection            connection, client_address = s.accept()            print "    connection from ", client_address            connection.setblocking(0)            inputs.append(connection)            message_queues[connection] = Queue.Queue()        else:            data = s.recv(1024)            if data :                print " received " , data , "from ",s.getpeername()                message_queues[s].put(data)                # Add output channel for response                    if s not in outputs:                    outputs.append(s)            else:                #Interpret empty result as closed connection                print "  closing", client_address                if s in outputs :                    outputs.remove(s)                inputs.remove(s)                s.close()                #remove message queue                 del message_queues[s]    for s in writable:        try:            next_msg = message_queues[s].get_nowait()        except Queue.Empty:            print " " , s.getpeername() , 'queue empty'            outputs.remove(s)        else:            print " sending " , next_msg , " to ", s.getpeername()            s.send(next_msg)        for s in exceptional:        print " exception condition on ", s.getpeername()        #stop listening for input on the connection        inputs.remove(s)        if s in outputs:            outputs.remove(s)        s.close()        #Remove message queue        del message_queues[s]                            
```

</p>

**Client端程序：**   
Client端创建多个socket进行server链接，用于观察使用select函数的server端如何进行处理。

  
**代码如下**（代码中已经有很详细的注释，这里就不过多解释了）**：**

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
'''Created on 2012-1-5The example client program uses some sockets to demonstrate how the serverwith select() manages multiple connections at the same time . The clientstarts by connecting each TCP/IP socket to the server@author: peter'''import socketmessages = ["This is the message" ,            "It will be sent" ,            "in parts "]print "Connect to the server"server_address = ("192.168.1.102",10001)#Create a TCP/IP socksocks = []for i in range(10):    socks.append(socket.socket(socket.AF_INET,socket.SOCK_STREAM))for s in socks:    s.connect(server_address)counter = 0for message in messages :    #Sending message from different sockets    for s in socks:        counter+=1        print "  %s sending %s" % (s.getpeername(),message+" version "+str(counter))        s.send(message+" version "+str(counter))    #Read responses on both sockets    for s in socks:        data = s.recv(1024)        print " %s received %s" % (s.getpeername(),data)        if not data:            print "closing socket ",s.getpeername()            s.close()        
```

</p>

 

</p>

**<span style="font-size: large;">使用Poll：</span>**

</p>

Server端：

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .highlight: .[头文件]; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
'''Created on 2012-1-6The poll function provides similar features to select() , but the underlying implementation is more efficient.But poll() is not supported under windows .@author: xiaojay'''import socketimport select import Queue# Create a TCP/IP socket, and then bind and listenserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)server.setblocking(False)server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)server_address = ("192.168.1.102", 10001)print  "Starting up on %s port %s" % server_addressserver.bind(server_address)server.listen(5)message_queues = {}#The timeout value is represented in milliseconds, instead of seconds.timeout = 1000# Create a limit for the eventREAD_ONLY = ( select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)READ_WRITE = (READ_ONLY|select.POLLOUT)# Set up the pollerpoller = select.poll()poller.register(server,READ_ONLY)#Map file descriptors to socket objectsfd_to_socket = {server.fileno():server,}while True:    print "Waiting for the next event"    events = poller.poll(timeout)    print "*"*20    print len(events)    print events    print "*"*20    for fd ,flag in  events:        s = fd_to_socket[fd]        if flag & (select.POLLIN | select.POLLPRI) :            if s is server :                # A readable socket is ready to accept a connection                connection , client_address = s.accept()                print " Connection " , client_address                connection.setblocking(False)                                fd_to_socket[connection.fileno()] = connection                poller.register(connection,READ_ONLY)                                #Give the connection a queue to send data                message_queues[connection]  = Queue.Queue()            else :                data = s.recv(1024)                if data:                    # A readable client socket has data                    print "  received %s from %s " % (data, s.getpeername())                    message_queues[s].put(data)                    poller.modify(s,READ_WRITE)                else :                    # Close the connection                    print "  closing" , s.getpeername()                    # Stop listening for input on the connection                    poller.unregister(s)                    s.close()                    del message_queues[s]        elif flag & select.POLLHUP :            #A client that "hang up" , to be closed.            print " Closing ", s.getpeername() ,"(HUP)"            poller.unregister(s)            s.close()        elif flag & select.POLLOUT :            #Socket is ready to send data , if there is any to send            try:                next_msg = message_queues[s].get_nowait()            except Queue.Empty:                # No messages waiting so stop checking                print s.getpeername() , " queue empty"                poller.modify(s,READ_ONLY)            else :                print " sending %s to %s" % (next_msg , s.getpeername())                s.send(next_msg)        elif flag & select.POLLERR:            #Any events with POLLERR cause the server to close the socket            print "  exception on" , s.getpeername()            poller.unregister(s)            s.close()            del message_queues[s]
```

</p>

