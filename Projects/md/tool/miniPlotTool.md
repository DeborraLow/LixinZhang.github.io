#迷你画线（pylab）小工具
pylab 提供了比较强大的画图功能，但是函数和参数都比较多，很容易搞混。我们平常使用最多的应该是画线了。下面，简单的对一些常用的划线函数进行了封装，方便使用。

<a href="https://gist.github.com/LixinZhang/5796875">Download</a>


##如何使用
<pre>
lineConf = {
         'X' : X,
         'Y' : Y,
         'marker' : 'o',
         'color' : 'b',
         'markerfacecolor' : 'r',
         'label' : '222',
         'linewidth' : 3,
         'linestyle' : '--'
     }
</pre>

以上为所花线的主要配置，X表示X坐标值数组，Y表示Y坐标值数组，两者维数应该相同，<code>marker</code>表示坐标节点的形状，<code>color</code>表示线的颜色，<code>label</code>表示所画线的标号，<code>linewidth</code>表示线宽，<code>linestyle</code>线的形状，具体配置选项可以参考后面的内容。

你可以：

1.	画单根线<code>tool.plotSingleLine(lineConf)</code>
2.	画多条线
	<pre>
	tool.addline(lineConf)
	tool.plot()
	tool.show()
	</pre>	



##常用配置选项
###颜色（color 简写为 c）：

*	蓝色： 'b' (blue)
*	绿色： 'g' (green)
*	红色： 'r' (red)
*	蓝绿色(墨绿色)： 'c' (cyan)
*	红紫色(洋红)： 'm' (magenta)
*	黄色： 'y' (yellow)
*	黑色： 'k' (black)
*	白色： 'w' (white)
*	灰度表示： e.g. 0.75 ([0,1]内任意浮点数)
*	RGB表示法： e.g. '#2F4F4F' 或 (0.18, 0.31, 0.31)
*	任意合法的html中的颜色表示： e.g. 'red', 'darkslategray'



###线型（linestyle 简写为 ls）：

*	实线： '-'
*	虚线： '--'
*	虚点线： '-.'
*	点线： ':'
*	点： '.' 



###点型（标记marker）：

*	像素： ','
*	圆形： 'o'
*	上三角： '^'
*	下三角： 'v'
*	左三角： '<'
*	右三角： '>'
*	方形： 's'
*	加号： '+' 
*	叉形： 'x'
*	棱形： 'D'
*	细棱形： 'd'
*	三脚架朝下： '1'（就是丫）
*	三脚架朝上： '2'
*	三脚架朝左： '3'
*	三脚架朝右： '4'
*	六角形： 'h'
*	旋转六角形： 'H'
*	五角形： 'p'
*	垂直线： '|'
*	水平线： '_'
*	gnuplot 中的steps： 'steps' （只能用于kwarg中）


###标记大小（markersize 简写为 ms）： 

*	markersize： 实数 
*	标记边缘宽度（markeredgewidth 简写为 mew）：

*	markeredgewidth：实数
*	标记边缘颜色（markeredgecolor 简写为 mec）：

*	markeredgecolor：颜色选项中的任意值
*	标记表面颜色（markerfacecolor 简写为 mfc）：

*	markerfacecolor：颜色选项中的任意值
*	透明度（alpha）：

*	alpha： [0,1]之间的浮点数
*	线宽（linewidth）：

*	linewidth： 实数

##代码实现
<script src="https://gist.github.com/LixinZhang/5796875.js"></script>
