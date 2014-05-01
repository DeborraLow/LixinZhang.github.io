Title: Linked List Cycle 循环链表环问题
Date: 2014-05-01 9:23
Category: Algorithm
Tags: 面试题

##Linked List Cycle 循环链表环问题

循环链表环问题，非常非常经典的题目，应该已经被问烂了，面试的时候如果5分钟之内写不出来，绝对说不过去的。我主要想写一下这个问题的证明思路。

####Leetcode链接
[linked-list-cycle](http://oj.leetcode.com/problems/linked-list-cycle/)

[linked-list-cycle-ii](http://oj.leetcode.com/problems/linked-list-cycle-ii/)

####解法
1. 最好的方法是时间复杂度 O(n),空间复杂度 O(1) 的。设置两个指针,一个快一个慢,快的指针每次走两步,慢的指针每次走一步,如果快指针和慢指针相遇,则说明有环。

2. 从1中的相遇点与起点同时这是两个指针，每次前进一步，相遇点即为环的入口点。

###证明
![pic](https://sdfpaw.dm2303.livefilestore.com/y2pITGzfyaJwtYVgaA9Q78xmJdFTkc46JHO2zcn4yQs_b_8Iz3mKmJ0L9uoTuYhSa6wtdh6Z9bjV6Lvej-hwixDx00KpUfD7SXaw_GHkUh_lys/%E6%97%A0%E6%A0%87%E9%A2%98.png?psid=1)

不妨设慢的指针为p1, 快的指针为p2。 则当p1与p2同时进入环时，进行k次移动两个指针相遇则有$$$2k-k<(L2+L3)$$$，即p1肯定走不完一圈，便与p2相遇在meetnode节点。于是，p2所走步数$$$S_2$$$及p1所走步数$$$S_1$$$有
$$S_2 = L1+m(L2+L3)+L2$$
$$S_1 = L1+L2$$
$$S_2 = 2 * S_1$$
化简后，可以得到如下式子：
$$L1=(m-1)(L2+L3) + L3$$
从上式可以看出L1比L3多了一些环，于是我们可以从meetcode以及起始点设置指针，然后每次走一步，保证两者会环的入口处相遇。


