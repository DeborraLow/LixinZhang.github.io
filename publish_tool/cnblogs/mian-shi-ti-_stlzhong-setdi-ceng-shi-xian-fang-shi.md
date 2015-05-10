Title: 面试题_STL中set底层实现方式
Date: 2013-03-04 14:10
Author: 糖拌咸鱼
Slug: mian-shi-ti-_stlzhong-setdi-ceng-shi-xian-fang-shi

Q：STL中set底层实现方式？ 为什么不用hash？

</p>

A: 第一个问题:set底层实现方式为RB树（即红黑树）。

</p>

    第二个问题:

</p>

   
首先set，不像map那样是key-value对，它的key与value是相同的。关于set有两种说法，第一个是STL中的set，用的是红黑树；第二个是hash\_set，底层用得是hash
table。红黑树与hash table最大的不同是，红黑树是有序结构，而hash
table不是。但不是说set就不能用hash，如果只是判断set中的元素是否存在，那么hash显然更合适，因为set
的访问操作时间复杂度是log(N)的，而使用hash底层实现的hash\_set是近似O(1)的。然而，set应该更加被强调理解为“集合”，而集合所涉及的操作并、交、差等，即STL提供的如交集set\_intersection()、并集set\_union()、差集set\_difference()和对称差集set\_symmetric\_difference()，都需要进行大量的比较工作，那么使用底层是有序结构的红黑树就十分恰当了，这也是其相对hash结构的优势所在。

</p>

 

</p>

