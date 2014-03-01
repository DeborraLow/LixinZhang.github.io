Title: 基于iptables实现NAT的分析与应用
Date: 2012-07-18 15:22
Author: 糖拌咸鱼
Slug: ji-yu-iptablesshi-xian-natde-fen-xi-yu-ying-yong

<span style="font-size: large;">**关于iptables**</span>

</p>

参考：[Iptables 指南 1.1.19][]

</p>

<span style="font-size: large;">**iptables提供的NAT的分析与应用**</span>

</p>

    
为什么要进行NAT？一个很好的例子：假设我们只有一台服务器具有外网IP，其他服务器都只具有内网IP，那么这些内网服务器外网无法访问到。那么我们可以将具有外网IP的那台服务器作为一个路由中转，将请求转发到内网的机器上来。如何转发呢？大家都知道IP报文中有两个重要的地址属性：源地址与目的地址。IP报文传递过程中需要经过哪台机器，是由这两个地址所决定的。

</p>

    
首先有个问题要明确。首先，客户端对某台服务器访问时，可能会需要多个路由的转发才能到达，但是这样的转发并**没有改变IP报文的源地址和目的地址**，路由器是通过改变目的MAC地址来决定下一个转发的位置的。NAT（Network
Address
Translation）包含DNAT和SNAT，即目的地址转换与源地址转换。DNAT可以实现当IP报文到达某台主机时，通过改变目的地址，将该IP报文再转发到其他主机上。当遇到第一个IP报文被转发后，后面的数据流会自动转发。而SNAT与DNAT相似，只是改变的是源地址。下图展示了iptables的结构流程图。

</p>

[![tables\_traverse][]][]

</p>

ip报文在通过iptables过程中，首先要经过PREROUTING阶段，然后通过过滤、处理、判断该报文是否需要被转发或是在本机进行处理，之后会到达POSTROUTING阶段，进而完成iptables的处理（其他阶段的处理细节可以参考上一节给出的链接）。因此，DNAT需要在PREROUTING阶段进行而SNAT必须在POSTROUTING阶段进行。

</p>

**命令格式：**

</p>

**DNAT**：**iptables -t nat -A PREROUTING --dst \$INET\_IP -p tcp
--dport 80 -j DNAT \\ --to-destination \$HTTP\_IP**

</p>

将匹配\$INET\_IP:80的IP报文的目的地址更改为\$HTTP\_IP

</p>

**SNAT：**iptables -t nat -A POSTROUTING -p tcp --dst \$HTTP\_IP --dport
80 -j SNAT \\ --to-source \$LAN\_IP****

</p>

将匹配\$HTTP\_IP:80的IP报文源地址更改为\$LAN\_IP

</p>

     
接下来重点提及一下de-DNAT（反向目的地址转换）以及de-SNAT（反向源地址转换），网上的信息比较少，本人通过参考[Where
the de-SNAT actually takes
place?][]了解到，de-DNAT和de-SNAT发生的位置与DNAT和SNAT正好相反。也就是说DNAT发生在PREROUTING阶段，而de-DNAT发生在POSTROUTING阶段，都是是将地址进行对换的过程，前者改变的目的地址，而后者其实改变的是源地址（该源地址是DNAT操作前的目的地址）。这就解释了为什么客户端发出的IP报文通过iptables改变目的地址后，还可以得到正确的回复。

</p>

     举一个例子：

</p>

[![图片1][]][]

</p>

 

</p>

   
在上图的模型中。client为外网的一个客户端，Router具有外网IP-Router\_WAN\_IP和内网Router\_LAN\_IP，一系列Server与Router在同一个内网，但是只有内网IP。我们用Router机器做地址转换，将client发送的请求转发到具有Server\_IP的内网机器上。

</p>

    1、client发出对Router的请求，IP报文的地址\<Client\_IP ,
Router\_WAN\_IP\>，
当该报文到达Router上的iptables，首先进入PREROUTING阶段，如果配置了DNAT且地址匹配成功，会将该报文的目的地址进行更改为内网Server\_IP，报文地址格式\<Client\_IP
, Server\_IP\>。   
***DNAT命令：**iptables -t nat -A PREROUTING --dst **Router\_WAN\_IP**
-p tcp --dport 80 -j DNAT \\ --to-destination **Server\_IP***   
   
2、经过PREROUTING阶段后，进行route，由于目的地址改变了，将会把该报文转发到Server\_IP上。
  
   
3、当Server处理完请求后，会进行回复，此时新的报文地址\<Server\_IP,Client\_IP\>，由于Client\_IP对于Server来说并不是直接可达的，并且会将Router看出一个网关。因此IP报文再通过Router，进行反向DNAT，将Server\_IP转换为Router\_WAN\_IP，在经过多个路由的转发返回给Client\_IP。

</p>

   
在以上步骤中，我们似乎没有进行SNAT的操作，也实现了基本设想。但是如果Client也处于与其他机器一起的内网环境的话，就出现了问题。因为在上面的步骤3中，新的报文Client\_IP是可以直接到达的，那么该报文就不会经过Router，而直接转发给了Client。但是，这时候Client接受到报文之后，发现与其请求的目的地址不一致（因为Client最初请求的是Router的地址），因此Client会把这个报文丢掉。因此，我们就必须要让从Server回来的报文首先经过Router，我们需要改变从Router出来的IP报文的源地址。使用SNAT可以实现源地址的转换。这样就把从Router出来的报文转换为\<Router\_LAN\_IP
，Server\_IP\>，再经过Server回复，产生新的报文地址\<Server\_IP ,
Router\_LAN\_IP\>。该报文会发送到Router，iptables会进行反向DNAT和反向SNAT，将报文地址改为\<Router\_WAN\_IP
，Client\_IP\>，最后返回到Client。   
***SNAT命令：**iptables -t nat -A POSTROUTING -p tcp –dst **Server\_IP**
--dport 80 -j SNAT \\ --to-source **Router\_LAN\_IP***

</p>

   
但是上面会产生一个问题，就是Server接收到的报文的源地址都是Router，而无法得知最初的Client地址，对于某些功能需求，这是很不好的。在参考链接中，有相关的解决办法讲述，这里不做赘述。

</p>

**<span style="font-size: large;">总结：</span>**

</p>

 
最近在做一个东西，所以学习了iptables，个人觉得iptables是非常强大的。本文是个人对用iptables进行NAT的一些思考与理解，由于对iptables了解尚浅且个人能力有限，本文内容仅供参考，还请批评指正。

</p>

  [Iptables 指南 1.1.19]: http://www.frozentux.net/iptables-tutorial/cn/iptables-tutorial-cn-1.1.19.html
  [tables\_traverse]: http://images.cnblogs.com/cnblogs_com/coser/201207/201207182321141071.jpg
    "tables_traverse"
  [![tables\_traverse][]]: http://images.cnblogs.com/cnblogs_com/coser/201207/201207182320402162.jpg
  [Where the de-SNAT actually takes place?]: http://lists.netfilter.org/pipermail/netfilter/2006-August/066503.html
  [图片1]: http://images.cnblogs.com/cnblogs_com/coser/201207/201207182321496260.png
    "图片1"
  [![图片1][]]: http://images.cnblogs.com/cnblogs_com/coser/201207/201207182321345959.png
