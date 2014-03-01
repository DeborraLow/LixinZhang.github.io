Title: 两道动态规划的作业题
Date: 2012-11-27 03:03
Author: 糖拌咸鱼
Slug: liang-dao-dong-tai-gui-hua-de-zuo-ye-ti

#### <span style="font-weight: bold;">Question1</span>

</p>

用动态规划方法手工求解下面的问题：

</p>

某工厂调查了解市场情况，估计在今后四个月内，市场对其产品的需求量如下表所示。

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
<td valign="top" width="284">
</p>

时期（月）

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="284">
</p>

需要量（产品单位）

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="284">
</p>

1

</p>

2

</p>

3

</p>

4

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="284">
</p>

2

</p>

3

</p>

2

</p>

4

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

已知：对每个月来讲，生产一批产品的固定成本费为 3
(千元)，若不生产，则为零。每生产单位产品的成本费为 1
（千元)。同时，在任何一个月内，生产能力所允许的最大生产批量为不超过6个单位。又知每单位产品的库存费用为每月
0.5 （千元），同时要求在第一个月开始之初，
及在第四个月末，均无产品库存。
问：在满足上述条件下，该厂应如何安排各个时期的生产与库存，使所花的总成本费用最低？

</p>

要求：写出各种变量、状态转移方程、递推关系式、和详细计算步骤。

</p>

**Solution：**

</p>

**阶段：**按月份时间进行阶段划分，i表示第i月

</p>

**状态：**月初时的库存量S

</p>

**决策集合：**第i月生产单位产品的数量k~i~，且0\<=k~i~\<=6

</p>

不妨设第i月的产品需求量为a~i~，则**状态间的转移关系**为S~i+1~ = S~i~ +
k~i~ – a~i~。我们设F[i ,
s]为从第i月到第n（n=4）月的最低总成本费用，则不难得出如下状态转移方程的**递推关系式**：

</p>

[![image][]][]

</p>

其中：w=0 (k==0) 或 w=3 + 1\*k (1\<=k\<=6)

</p>

边界条件：F[5,0] = 0；s + k –a[i] \>=0；

</p>

目标结果状态：F[1,0]即所求最低成本费用

</p>

手工求解计算详细计算步骤如下：

</p>

<table border="1" cellpadding="0" cellspacing="0">
</p>
<p>
<tbody>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="100">
</p>

i=4

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

**状态**

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

k=0

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

k=1

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=2

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=3

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=4

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=6

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

**Min**

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

**决策**

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>
<p>
    F[4,0]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    7

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    8

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    9

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    7

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    4

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>
<p>
    F[4,1]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    6.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    7.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    8.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    9.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    6.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    3

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>
<p>
    F[4,2]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    6

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    7

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    8

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    9

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    10

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    6

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    2

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>
<p>
    F[4,3]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    5.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    6.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    7.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    8.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    9.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    10.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    5.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    1

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>
<p>
    F[4,4]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    2

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    6

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    7

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    8

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    9

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    10

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    11

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    2

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    0

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="100">
</p>

i=3

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

**状态**

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

k=0

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

k=1

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=2

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=3

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=4

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=6

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

**Min**

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

**决策**

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[3 , 0]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

12

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

12.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

13

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

13.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

11

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

11

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

6

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[3 , 1]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

11.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

12

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

12.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

13

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

10.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

10.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

5

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[3 , 2]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

8

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

11.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

12

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

12.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

10

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

8

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

0

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[3 , 3]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

8

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

11.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

12

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

9.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

8

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

0

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[3 , 4]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

8

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

11.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

9

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

8

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

0

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[3 , 5]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

8

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

8.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

8

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

0

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[3 , 6]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

0

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="100">
</p>

i=2

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

**状态**

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

k=0

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

k=1

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=2

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=3

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=4

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=6

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

**Min**

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

**决策**

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[2 , 0]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

17

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

17.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

16

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

17

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

16

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

5

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[2 , 1]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

16.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

17

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

15.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

16.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

17.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

15.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

4

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[2 , 2]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

16

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

16.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

15

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

16

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

17

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

18

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

15

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

3

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[2 , 3]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

12.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

16

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

14.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

15.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

16.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

17.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

15.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

12.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

0

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[2 , 4]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

12.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

14

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

15

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

16

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

17

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

15

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

12.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

0

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[2 , 5]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

10.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

14.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

15.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

16.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

14.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

10.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

0

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

F[2 , 6]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

11

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

15

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

16

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

14

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

11

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

0

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top">
</p>

i=1

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>

**状态**

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

k=0

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

k=1

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=2

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=3

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=4

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>

k=6

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

**Min**

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>

**决策**

</p>
<p>
</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="top" width="62">
</p>
<p>
    F[1,0]

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    N/A

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    21

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    21.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    22

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    20.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="57">
</p>
<p>
    21.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    20.5

</p>
<p>
</td>
</p>
<p>
<td valign="top" width="56">
</p>
<p>
    5

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

由上表不难得出，所花的总成本费用最低为20.5（千元），该情况下的由递推公式逆推可得决策安排如下：第一个月生产5个单位产品，第二个月生产0个，第三个月生产0个，第四个月生产6个，该方案可使总成本最低，即20.5（千元）。

</p>

**源代码：**

</p>

<div class="cnblogs_code"
style="background-color: #f5f5f5; border: #cccccc 1px solid; padding: 5px;">

</p>
<p>
    #include<iostream>using namespace std;double f[5][7] = {0};int a[5] = {0,2,3,2,4};int main(){    for(int i=0;i<5;i++)        for(int j=0;j<=7;j++)            f[i][j] = 1000;    f[5][0] = 0;    for (int i=4;i>=1;i--){        for(int s=0;s<=6;s++) {            int temp = 0;            for(int k=i;k<=4;k++) temp+= a[k];            if (s>temp) continue;            double min = 10000;            int u = -1;            for(int j=0;j<=6;j++){                int w = 3 + j;                if (j==0) w = 0;                if (s + j - a[i] >= 0 && s + j - a[i] <=6) {                    if (min>f[i+1][s+j-a[i]] + w + 0.5*s) {                        min = f[i+1][s+j-a[i]] + w + 0.5*s;                        u = j;                    }                }            }            f[i][s] = min;        }    }    cout<<"Answer:"<<f[1][0]<<endl;    return 0;}

</p>
<p>

</div>

</p>

<span style="font-weight: bold;">Question2：</span>

</p>

用动态规划方法编程求解下面的问题：

</p>

某推销员要从城市 v~1~出发，访问其它城市
v~2~，v~3~，…，v~6~各一次且仅一次，最后返回 v~1~。D
为各城市间的距离矩阵。

</p>

问：该推销员应如何选择路线，才能使总的行程最短？

</p>

[![clip\_image002][]][]

</p>

要求：写出递推关系式、伪代码和程序相关说明，并分析时间复杂性。（请遵守第一节课提出的有关
assignment 的要求）

</p>

**Solution：**

</p>

设F[i,s]表示当前所在节点为i，已经走过的节点集合为s的最短路程。决策为选择下一个**节点**k，因此，的状态转移方程的递推关系式：

</p>

[![image][1]][]

</p>

其中，d[i,k]表示i节点到k节点的距离

</p>

**源代码：**

</p>

**一些说明：**有几个关键问题需要说明

</p>

1、集合如何表示，表示集合有个很好的方法，就是使用二进制模型。例如：11101表示含有1、3、4、5元素的集合。这一一个十进制的数字就可以代表一个集合。

</p>

2、那么如何进行对集合的操作呢？对于位运算，我们可以利用1的左右移（\<\<
or \>\>）来判断是否包含某个元素。S-{k}也就是方便的表示为：S**[**j**]**
**&** **(**length**-(**1**\<\<(**k**-**1**)))，其中length=**(**1
**\<\<** **(**n**-**1**))** **-** 1**;****

</p>

3、![image][2]该图表示一个求解模型树，不难发现含有一个元素的集合要先进行计算，才可以计算还有两个元素状态的解空间，这样就要求不同集合之间是有序的，即含有二进制1的个数少的要排在前面。这样就不会在计算过程中，出现使用未计算结果的情况。实现方法可以使用预排序。因为排序的复杂度相对于整体算法的复杂性而言，是很小的，不会过多影响性能。

</p>

**时间复杂度：**

</p>

由于集合的状态个数为2^n-1^
个，还需要枚举每个结点，以及每个集合中的元素，因此整个算法的近似复杂度为<a name="OLE_LINK9"></a><a name="OLE_LINK8"></a>O(n^2^\*2^n^)。

</p>

**最后给出源代码（水平有限仅供参考）：**

</p>

<div class="cnblogs_code"
style="background-color: #f5f5f5; border: #cccccc 1px solid; padding: 5px;">

</p>
<p>
    #include<iostream>#include<stdio.h>#include<algorithm>using namespace std;const int maxnum = 100001;int Count(int v){    int num = 0;    while(v){        v &= (v-1);        num ++;    }    return num;}bool cmp(int a , int b){    int count1_a = Count(a);    int count1_b = Count(b);    return count1_a < count1_b;}bool existkey( int key , int S) {    int p = 1;    p = p << (key-1);    p = p & S;    if (p>0) return true;    else return false;}void getElements( int S , int * arr , int length , int &return_len) {    int p = 1;    int pos = 0;    for(int i=0;i<length;i++){        if (p == (p&S)){            arr[pos++] = i+1;        }        p = p << 1;    }    return_len = pos;}int main(){    freopen("input.txt","r",stdin);    int n = 0 ;    cin >> n;    int F[10][100];    int S[1000];    int elements [10];    int distance[10][10];    int length_elements = 0;    for(int i=0 ; i<n ; i++ ){        for (int j=0 ; j<n ; j++) {            cin>>distance[i][j];        }    }    for (int i=1 ; i<=n ;i++)        F[i][0] = distance[i][0];        int length = (1 << (n-1)) - 1;    for (int i=1 ; i<=length ; i++){        S[i] = i;    }    sort(S,S+length,cmp);    S[0] = 0;    for (int j=1 ; j<=length ; j++) {        for(int i=1 ; i<n ; i++) {            if (existkey(i , S[j]) != true){                 getElements(S[j] , elements, n , length_elements);                int min = maxnum;                for (int p=0 ; p<length_elements ; p++){                    int k = elements[p];                    int jj = S[j] & (length-(1<<(k-1))) ;                    if (min > ( F[k][jj] + distance[i][k] ) && k!=i )                        min = F[k][jj] + distance[i][k];                }                F[i][S[j]] = min;            }        }    }    int ans = maxnum;    for (int i=1 ; i<n ; i++){        int j = length & (length -(1<<(i-1)));        if (ans > F[i][j] + distance[0][i]) ans = F[i][j] + distance[0][i];    }    cout<<"Answer:\t"<<ans<<endl;    return 0;}

</p>
<p>

</div>

</p>

  [image]: http://images.cnblogs.com/cnblogs_com/coser/201211/201211271102268432.png
    "image"
  [![image][]]: http://images.cnblogs.com/cnblogs_com/coser/201211/201211271102257460.png
  [clip\_image002]: http://images.cnblogs.com/cnblogs_com/coser/201211/201211271102267659.jpg
    "clip_image002"
  [![clip\_image002][]]: http://images.cnblogs.com/cnblogs_com/coser/201211/201211271102265117.jpg
  [1]: http://images.cnblogs.com/cnblogs_com/coser/201211/20121127110230563.png
    "image"
  [![image][1]]: http://images.cnblogs.com/cnblogs_com/coser/201211/201211271102309417.png
  [2]: http://p.blog.csdn.net/images/p_blog_csdn_net/gfaiswl/612517/o_image_thumb_3.gif
