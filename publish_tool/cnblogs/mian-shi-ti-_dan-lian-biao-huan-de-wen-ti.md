Title: 面试题_单链表环的问题
Date: 2011-04-03 06:06
Author: 糖拌咸鱼
Slug: mian-shi-ti-_dan-lian-biao-huan-de-wen-ti

**<span
style="font-size: 16px;">问题：有一个单链表，其中可能有一个环，也就是某个节点的next指向的是链表中在它之前的节点，这样的链表的尾部形成一环。</span>**

</p>

**<span
style="font-size: 16px;">1、如何判断一个链表是否存在环？</span>**

</p>

**<span
style="font-size: 16px;">2、如果链表存在环，如何找到环的入口点？</span>**

</p>

**问题1分析：**设置两个指针fast和slow，初始值都指向头指针，slow每次前进一步，fast每次前进两步。如果存在环，则fast必先进入环，而slow后进入环，两个指针必定相遇，当然，fast先到达尾部为NULL，则为无环链表。

</p>

**证明：**两个指针fast和slow，fast一次递增两步，slow一次递增一步。如果有环的话两者必然重合，反之亦然。因为fast每次走2步，而slow每次走一步，所以它们之间的差距是一步一步缩小的。当slow进入环入口点后，fast和slow之间的差距将会一步步缩小，如4,3,2,1,0。到0的时候就重合了。根据此方式，可以证明，fast每次走三步以上，并不总能加快检测速度，反而有可能判别不出环。

</p>

**问题2分析：**如果fast和slow相遇，那么在相遇时，slow肯定没有遍历完链表，而fast已经在环内循环了n圈（n\>=1）。

</p>

假设slow走了s步，则fast走了2s步（fast的步数还等于s加上在环上多转的n圈），设环长为r，则：

</p>

2s=s+nr

</p>

s=nr

</p>

设整个链表长L，入口环与相遇点距离为x，起点到环入口点的距离为a，则

</p>

a+x=s=nr

</p>

a+x=(n-1)r+r=(n-1)r+L-a

</p>

a=(n-1)r+(L-a-x)

</p>

(L-a-x)为相遇点到环入口点的距离。由此可知，从链表头到环入口点等于(n-1)循环内环+相遇点到环入口点。于是可以从链表头和相遇点分别设一个指针，每次各走一步，两个指针必定相遇，且相遇第一点为环入口点。

</p>

<div class="cnblogs_code">

</p>

<div>

<span style="color: #000000;">\#include</span><span
style="color: #000000;">\<</span><span
style="color: #000000;">iostream</span><span
style="color: #000000;">\></span><span style="color: #000000;">  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"></span><span
style="color: #0000ff;">namespace</span><span style="color: #000000;">
std;  
</span><span style="color: #0000ff;">struct</span><span
style="color: #000000;"> Node  
{  
Node</span><span style="color: #000000;">\*</span><span
style="color: #000000;"> next;  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> value;  
Node(</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> v)  
{  
value</span><span style="color: #000000;">=</span><span
style="color: #000000;">v;  
next</span><span style="color: #000000;">=</span><span
style="color: #000000;">NULL;  
}  
};  
  
Node</span><span style="color: #000000;">\*</span><span
style="color: #000000;"> isExistLoop(Node</span><span
style="color: #000000;">\*</span><span style="color: #000000;"> head)  
{  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">slow一次走一步，fast一次走两步</span><span
style="color: #008000;">  
</span><span style="color: #000000;"> Node</span><span
style="color: #000000;">\*</span><span style="color: #000000;">
slow</span><span style="color: #000000;">=</span><span
style="color: #000000;">head,</span><span
style="color: #000000;">\*</span><span
style="color: #000000;">fast</span><span
style="color: #000000;">=</span><span style="color: #000000;">head;  
</span><span style="color: #0000ff;">while</span><span
style="color: #000000;">(fast</span><span
style="color: #000000;">!=</span><span
style="color: #000000;">NULL</span><span
style="color: #000000;">&&</span><span
style="color: #000000;">fast</span><span
style="color: #000000;">-\></span><span
style="color: #000000;">next</span><span
style="color: #000000;">!=</span><span style="color: #000000;">NULL)  
{  
slow</span><span style="color: #000000;">=</span><span
style="color: #000000;">slow</span><span
style="color: #000000;">-\></span><span style="color: #000000;">next;  
fast</span><span style="color: #000000;">=</span><span
style="color: #000000;">fast</span><span
style="color: #000000;">-\></span><span
style="color: #000000;">next</span><span
style="color: #000000;">-\></span><span style="color: #000000;">next;  
</span><span style="color: #0000ff;">if</span><span
style="color: #000000;">(slow</span><span
style="color: #000000;">==</span><span
style="color: #000000;">fast)</span><span
style="color: #0000ff;">return</span><span style="color: #000000;">
slow;  
}  
</span><span style="color: #0000ff;">return</span><span
style="color: #000000;"> NULL;  
}  
  
Node</span><span style="color: #000000;">\*</span><span
style="color: #000000;"> findLoopNode(Node</span><span
style="color: #000000;">\*</span><span style="color: #000000;"> head)  
{  
Node</span><span style="color: #000000;">\*</span><span
style="color: #000000;"> second</span><span
style="color: #000000;">=</span><span
style="color: #000000;">isExistLoop(head);</span>

</div>

</p>

<div>

<span style="color: #000000;">second = second-\>next;  
</span><span style="color: #0000ff;">if</span><span
style="color: #000000;">(second</span><span
style="color: #000000;">==</span><span
style="color: #000000;">NULL)</span><span
style="color: #0000ff;">return</span><span style="color: #000000;">
NULL;  
Node</span><span style="color: #000000;">\*</span><span
style="color: #000000;"> first</span><span
style="color: #000000;">=</span><span style="color: #000000;"> head;  
  
</span><span style="color: #0000ff;">while</span><span
style="color: #000000;">(second</span><span
style="color: #000000;">!=</span><span style="color: #000000;">first)  
{  
second</span><span style="color: #000000;">=</span><span
style="color: #000000;">second</span><span
style="color: #000000;">-\></span><span style="color: #000000;">next;  
first</span><span style="color: #000000;">=</span><span
style="color: #000000;">first</span><span
style="color: #000000;">-\></span><span style="color: #000000;">next;  
}  
</span><span style="color: #0000ff;">return</span><span
style="color: #000000;"> first;  
}  
  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> main()  
{  
</span><span style="color: #0000ff;">const</span><span
style="color: #000000;"></span><span
style="color: #0000ff;">int</span><span style="color: #000000;">
LENGTH</span><span style="color: #000000;">=</span><span
style="color: #800080;">20</span><span style="color: #000000;">;  
Node</span><span style="color: #000000;">\*</span><span
style="color: #000000;"> nodelist[LENGTH];  
nodelist[</span><span style="color: #800080;">0</span><span
style="color: #000000;">]</span><span
style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
Node(</span><span style="color: #800080;">0</span><span
style="color: #000000;">);  
Node</span><span style="color: #000000;">\*</span><span
style="color: #000000;"> head</span><span
style="color: #000000;">=</span><span
style="color: #000000;">nodelist[</span><span
style="color: #800080;">0</span><span style="color: #000000;">];  
Node</span><span style="color: #000000;">\*</span><span
style="color: #000000;"> pre</span><span
style="color: #000000;">=</span><span style="color: #000000;">head;  
</span><span style="color: #0000ff;">for</span><span
style="color: #000000;">(</span><span
style="color: #0000ff;">int</span><span style="color: #000000;">
i</span><span style="color: #000000;">=</span><span
style="color: #800080;">1</span><span
style="color: #000000;">;i</span><span
style="color: #000000;">\<</span><span
style="color: #000000;">LENGTH;i</span><span
style="color: #000000;">++</span><span style="color: #000000;">)  
{  
nodelist[i]</span><span style="color: #000000;">=</span><span
style="color: #000000;"></span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
Node(i);  
pre</span><span style="color: #000000;">-\></span><span
style="color: #000000;">next</span><span
style="color: #000000;">=</span><span
style="color: #000000;">nodelist[i];  
pre</span><span style="color: #000000;">=</span><span
style="color: #000000;">nodelist[i];  
}  
pre</span><span style="color: #000000;">-\></span><span
style="color: #000000;">next</span><span
style="color: #000000;">=</span><span
style="color: #000000;">nodelist[</span><span
style="color: #800080;">14</span><span style="color: #000000;">];  
  
</span><span style="color: #0000ff;">if</span><span
style="color: #000000;">(isExistLoop(head))  
{  
cout</span><span style="color: #000000;">\<\<</span><span
style="color: #800000;">"</span><span
style="color: #800000;">存在环</span><span
style="color: #800000;">"</span><span
style="color: #000000;">\<\<</span><span style="color: #000000;">endl;  
}  
</span><span style="color: #0000ff;">else</span><span
style="color: #000000;"> cout</span><span
style="color: #000000;">\<\<</span><span
style="color: #800000;">"</span><span
style="color: #800000;">不存在环</span><span
style="color: #800000;">"</span><span
style="color: #000000;">\<\<</span><span style="color: #000000;">endl;  
  
cout</span><span style="color: #000000;">\<\<</span><span
style="color: #000000;">findLoopNode(head)</span><span
style="color: #000000;">-\></span><span
style="color: #000000;">value</span><span
style="color: #000000;">\<\<</span><span style="color: #000000;">endl;  
  
</span><span style="color: #0000ff;">for</span><span
style="color: #000000;">(</span><span
style="color: #0000ff;">int</span><span style="color: #000000;">
j</span><span style="color: #000000;">=</span><span
style="color: #800080;">0</span><span
style="color: #000000;">;j</span><span
style="color: #000000;">\<</span><span
style="color: #000000;">LENGTH;j</span><span
style="color: #000000;">++</span><span style="color: #000000;">)  
{  
delete nodelist[j];  
}  
</span><span style="color: #0000ff;">return</span><span
style="color: #000000;"></span><span
style="color: #800080;">0</span><span style="color: #000000;">;  
}</span>

</div>

</p>
<p>

</div>

</p>

