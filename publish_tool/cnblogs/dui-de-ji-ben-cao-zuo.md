Title: 堆的基本操作
Date: 2011-03-15 05:23
Author: 糖拌咸鱼
Slug: dui-de-ji-ben-cao-zuo

　　我们期望的数据结构能支持插入操作，并能方便地从中取出具有最小或最大关键码的记录，这样的数据结构即为优先级队列。在优先级队列的各种实现中，堆是最高效的一种数据结构。  
　　最小堆：任一结点的关键码均小于或等于它的左右子女的关键码，位于堆顶的结点的关键码是整个元素集合的最小的，所以称它为最小堆。最大堆类似定义。

</p>

　　**创建堆：**采用从下向上逐步调整形成堆得方法来创建堆。为下面的分支结点调用下调算法siftDown，将以它们为根的子树调整为最小堆。从局部到整体，将最小堆逐步扩大，直到将整个树调整为最小堆。

</p>

　　**插入一个元素：**最小堆的插入算法调用了另一种堆得调整方法siftUp，实现自下而上的上滑调整。因为每次新结点总是插在已经建成的最小堆后面，这时必须遵守与sift相反的比较路径，从下向上，与父结点的关键码进行比较，对调。

</p>

　　**删除一个元素：**从最小堆删除具有最小关键码记录的操作时将最小堆的堆顶元素，即其完全二叉树的顺序表示的第0号元素删去，去把这个元素取走后，一般以堆得最后一个结点填补取走的堆顶元素，并将堆的实际元素个数减1.但是用最后一个元素取代堆顶元素将破坏堆，需要调用siftDown算法进行调整堆。

</p>

本文代码均以最小堆的实现为例。

</p>

<div class="cnblogs_code">

</p>

<div>

<span style="color: #000000;">\#include</span><span
style="color: #000000;">\<</span><span
style="color: #000000;">iostream</span><span
style="color: #000000;">\></span><span style="color: #000000;">  
\#include</span><span style="color: #000000;">\<</span><span
style="color: #000000;">assert.h</span><span
style="color: #000000;">\></span><span style="color: #000000;">  
</span><span style="color: #0000ff;">using</span><span
style="color: #0000ff;">namespace</span><span style="color: #000000;">
std;  
  
</span><span style="color: #0000ff;">const</span><span
style="color: #0000ff;">int</span><span style="color: #000000;">
maxheapsize</span><span style="color: #000000;">=</span><span
style="color: #800080;">100</span><span style="color: #000000;">;  
</span><span style="color: #0000ff;">static</span><span
style="color: #0000ff;">int</span><span style="color: #000000;">
currentsize</span><span style="color: #000000;">=</span><span
style="color: #800080;">0</span><span style="color: #000000;">;  
  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">从上到下调整堆</span><span
style="color: #008000;">  
</span><span style="color: #0000ff;">void</span><span
style="color: #000000;"> siftDown(</span><span
style="color: #0000ff;">int</span><span
style="color: #000000;">\*</span><span style="color: #000000;">
heap,</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> currentPos,</span><span
style="color: #0000ff;">int</span><span style="color: #000000;"> m)  
{  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> i</span><span
style="color: #000000;">=</span><span
style="color: #000000;">currentPos;  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> j</span><span
style="color: #000000;">=</span><span
style="color: #000000;">currentPos</span><span
style="color: #000000;">\*</span><span
style="color: #800080;">2</span><span
style="color: #000000;">+</span><span
style="color: #800080;">1</span><span
style="color: #000000;">;</span><span
style="color: #008000;">//</span><span style="color: #008000;">i's
leftChild</span><span style="color: #008000;">  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> temp</span><span
style="color: #000000;">=</span><span style="color: #000000;">heap[i];  
</span><span style="color: #0000ff;">while</span><span
style="color: #000000;">(j</span><span
style="color: #000000;">\<=</span><span style="color: #000000;">m)  
{  
</span><span style="color: #0000ff;">if</span><span
style="color: #000000;">(j</span><span
style="color: #000000;">\<</span><span
style="color: #000000;">m</span><span
style="color: #000000;">&&</span><span
style="color: #000000;">heap[j]</span><span
style="color: #000000;">\></span><span
style="color: #000000;">heap[j</span><span
style="color: #000000;">+</span><span
style="color: #800080;">1</span><span style="color: #000000;">])
j</span><span style="color: #000000;">++</span><span
style="color: #000000;">;</span><span
style="color: #008000;">//</span><span style="color: #008000;"> j points
to minChild</span><span style="color: #008000;">  
</span><span style="color: #0000ff;">if</span><span
style="color: #000000;">(temp</span><span
style="color: #000000;">\<=</span><span
style="color: #000000;">heap[j])</span><span
style="color: #0000ff;">break</span><span style="color: #000000;">;  
</span><span style="color: #0000ff;">else</span><span
style="color: #000000;">   
{  
heap[i]</span><span style="color: #000000;">=</span><span
style="color: #000000;">heap[j];  
i</span><span style="color: #000000;">=</span><span
style="color: #000000;">j;  
j</span><span style="color: #000000;">=</span><span
style="color: #800080;">2</span><span
style="color: #000000;">\*</span><span
style="color: #000000;">i</span><span
style="color: #000000;">+</span><span
style="color: #800080;">1</span><span style="color: #000000;">;  
}  
}  
heap[i]</span><span style="color: #000000;">=</span><span
style="color: #000000;">temp;  
}  
  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">从下向上调整堆</span><span
style="color: #008000;">  
</span><span style="color: #0000ff;">void</span><span
style="color: #000000;"> siftUp(</span><span
style="color: #0000ff;">int</span><span
style="color: #000000;">\*</span><span style="color: #000000;">
heap,</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> start)  
{  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> i</span><span
style="color: #000000;">=</span><span
style="color: #000000;">start,j</span><span
style="color: #000000;">=</span><span
style="color: #000000;">(i</span><span
style="color: #000000;">-</span><span
style="color: #800080;">1</span><span
style="color: #000000;">)</span><span
style="color: #000000;">/</span><span
style="color: #800080;">2</span><span style="color: #000000;">;  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> temp</span><span
style="color: #000000;">=</span><span style="color: #000000;">heap[i];  
  
</span><span style="color: #0000ff;">while</span><span
style="color: #000000;">(i</span><span
style="color: #000000;">\></span><span
style="color: #800080;">0</span><span style="color: #000000;">)  
{  
</span><span style="color: #0000ff;">if</span><span
style="color: #000000;">(heap[j]</span><span
style="color: #000000;">\></span><span style="color: #000000;">temp)   
{  
heap[i]</span><span style="color: #000000;">=</span><span
style="color: #000000;">heap[j];  
i</span><span style="color: #000000;">=</span><span
style="color: #000000;">j;  
j</span><span style="color: #000000;">=</span><span
style="color: #000000;">(i</span><span
style="color: #000000;">-</span><span
style="color: #800080;">1</span><span
style="color: #000000;">)</span><span
style="color: #000000;">/</span><span
style="color: #800080;">2</span><span style="color: #000000;">;  
}  
</span><span style="color: #0000ff;">else</span><span
style="color: #0000ff;">break</span><span style="color: #000000;">;  
}  
heap[i]</span><span style="color: #000000;">=</span><span
style="color: #000000;">temp;  
}  
  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">构建堆</span><span style="color: #008000;">  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;">\*</span><span style="color: #000000;">
Heap(</span><span style="color: #0000ff;">int</span><span
style="color: #000000;">\*</span><span
style="color: #000000;">arr,</span><span
style="color: #0000ff;">int</span><span style="color: #000000;"> size)  
{  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> i;  
currentsize</span><span style="color: #000000;">=</span><span
style="color: #000000;">size;  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;">\*</span><span style="color: #000000;">
heap</span><span style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span
style="color: #0000ff;">int</span><span
style="color: #000000;">[maxheapsize];  
assert(heap</span><span style="color: #000000;">!=</span><span
style="color: #000000;">NULL);  
</span><span style="color: #0000ff;">for</span><span
style="color: #000000;">(i</span><span
style="color: #000000;">=</span><span
style="color: #800080;">0</span><span
style="color: #000000;">;i</span><span
style="color: #000000;">\<</span><span
style="color: #000000;">currentsize;i</span><span
style="color: #000000;">++</span><span style="color: #000000;">)
heap[i]</span><span style="color: #000000;">=</span><span
style="color: #000000;">arr[i];  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> currentPos</span><span
style="color: #000000;">=</span><span
style="color: #000000;">(currentsize</span><span
style="color: #000000;">-</span><span
style="color: #800080;">2</span><span
style="color: #000000;">)</span><span
style="color: #000000;">/</span><span
style="color: #800080;">2</span><span style="color: #000000;">;  
</span><span style="color: #0000ff;">while</span><span
style="color: #000000;">(currentPos</span><span
style="color: #000000;">\>=</span><span
style="color: #800080;">0</span><span style="color: #000000;">)  
{  
siftDown(heap,currentPos,currentsize</span><span
style="color: #000000;">-</span><span
style="color: #800080;">1</span><span style="color: #000000;">);  
currentPos</span><span style="color: #000000;">--</span><span
style="color: #000000;">;  
}  
</span><span style="color: #0000ff;">return</span><span
style="color: #000000;"> heap;  
}  
  
  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">增加一个元素</span><span
style="color: #008000;">  
</span><span style="color: #0000ff;">void</span><span
style="color: #000000;"> insert(</span><span
style="color: #0000ff;">int</span><span
style="color: #000000;">\*</span><span style="color: #000000;">
heap,</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> value)  
{  
</span><span style="color: #0000ff;">if</span><span
style="color: #000000;">(currentsize</span><span
style="color: #000000;">\>=</span><span
style="color: #000000;">maxheapsize)  
{  
cout</span><span style="color: #000000;">\<\<</span><span
style="color: #800000;">"</span><span style="color: #800000;">Heap is
full!</span><span style="color: #800000;">"</span><span
style="color: #000000;">\<\<</span><span style="color: #000000;">endl;  
</span><span style="color: #0000ff;">return</span><span
style="color: #000000;"> ;  
}  
heap[currentsize]</span><span style="color: #000000;">=</span><span
style="color: #000000;">value;  
siftUp(heap,currentsize);  
currentsize</span><span style="color: #000000;">++</span><span
style="color: #000000;">;  
}  
  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">删除一个元素,并返回删除前的堆顶元素</span><span
style="color: #008000;">  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> removemin(</span><span
style="color: #0000ff;">int</span><span
style="color: #000000;">\*</span><span style="color: #000000;"> heap)  
{  
assert(currentsize</span><span style="color: #000000;">\>=</span><span
style="color: #800080;">0</span><span style="color: #000000;">);  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> removeValue</span><span
style="color: #000000;">=</span><span
style="color: #000000;">heap[</span><span
style="color: #800080;">0</span><span style="color: #000000;">];  
heap[</span><span style="color: #800080;">0</span><span
style="color: #000000;">]</span><span
style="color: #000000;">=</span><span
style="color: #000000;">heap[currentsize</span><span
style="color: #000000;">-</span><span
style="color: #800080;">1</span><span style="color: #000000;">];  
currentsize</span><span style="color: #000000;">--</span><span
style="color: #000000;">;  
siftDown(heap,</span><span style="color: #800080;">0</span><span
style="color: #000000;">,currentsize</span><span
style="color: #000000;">-</span><span
style="color: #800080;">1</span><span style="color: #000000;">);  
</span><span style="color: #0000ff;">return</span><span
style="color: #000000;"> removeValue;  
}  
  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> main()  
{  
</span><span style="color: #0000ff;">const</span><span
style="color: #0000ff;">int</span><span style="color: #000000;">
size</span><span style="color: #000000;">=</span><span
style="color: #800080;">10</span><span style="color: #000000;">;  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;"> arr[size]</span><span
style="color: #000000;">=</span><span
style="color: #000000;">{</span><span
style="color: #800080;">2</span><span
style="color: #000000;">,</span><span
style="color: #800080;">1</span><span
style="color: #000000;">,</span><span
style="color: #800080;">3</span><span
style="color: #000000;">,</span><span
style="color: #800080;">0</span><span
style="color: #000000;">,</span><span
style="color: #800080;">8</span><span
style="color: #000000;">,</span><span
style="color: #800080;">1</span><span
style="color: #000000;">,</span><span
style="color: #800080;">6</span><span
style="color: #000000;">,</span><span
style="color: #800080;">9</span><span
style="color: #000000;">,</span><span
style="color: #800080;">7</span><span
style="color: #000000;">,</span><span
style="color: #800080;">10</span><span style="color: #000000;">};  
</span><span style="color: #0000ff;">int</span><span
style="color: #000000;">\*</span><span style="color: #000000;">
heap</span><span style="color: #000000;">=</span><span
style="color: #000000;">Heap(arr,size);  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">堆排序</span><span style="color: #008000;">  
</span><span style="color: #0000ff;">for</span><span
style="color: #000000;">(</span><span
style="color: #0000ff;">int</span><span style="color: #000000;">
i</span><span style="color: #000000;">=</span><span
style="color: #800080;">0</span><span
style="color: #000000;">;i</span><span
style="color: #000000;">\<</span><span
style="color: #000000;">size;i</span><span
style="color: #000000;">++</span><span style="color: #000000;">)  
{  
arr[i]</span><span style="color: #000000;">=</span><span
style="color: #000000;">removemin(heap);  
cout</span><span style="color: #000000;">\<\<</span><span
style="color: #000000;">arr[i]</span><span
style="color: #000000;">\<\<</span><span style="color: #000000;">endl;  
}  
delete []heap;  
</span><span style="color: #0000ff;">return</span><span
style="color: #800080;">0</span><span style="color: #000000;">;</span>

</div>

</p>

<div>

 

</div>

</p>

<div>

 

</div>

</p>

<div>

 

</div>

</p>

<div>

<span style="color: #000000;"><span style="color: #000000;">  
}</span></span>

* * * * *

面试百度时，遇到的一个面试题：

</div>

</p>

<div>

如何建堆，以及建堆的复杂度是多少？证明之。

</div>

</p>

<div>

复杂度为O(n)，不要凭空想象，因为凭空想象第一感觉是n\*logn的，但是显然是不准确的。

</div>

</p>

<div>

具体证明参考算法导论，第六章 77页。

</div>

</p>

<p>

</div>

</p>

