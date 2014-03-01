Title: 使用python pylab库 画线
Date: 2013-06-20 07:06
Author: 糖拌咸鱼
Slug: shi-yong-python-pylabku-hua-xian

pylab
提供了比较强大的画图功能，但是函数和参数都比较多，很容易搞混。我们平常使用最多的应该是画线了。下面，简单的对一些常用的划线函数进行了封装，方便使用。

</p>

<div class="cnblogs_code">

</p>
<p>
      1 # -*- coding: utf-8 -*-  2 import pylab  3 import random  4   5 class MiniPlotTool :  6     '''  7     A mini tool to draw lines using pylab  8     '''  9     basecolors = ['red','green','yellow','blue','black','cyan','magenta'] 10  11     def __init__(self, baseConfig) : 12         self.figsize = baseConfig.get('figsize',None) 13         self.axis = baseConfig.get('axis',None) 14         self.title = baseConfig.get('title','NoName') 15         self.ylabel = baseConfig.get('ylabel','NoName') 16         self.grid = baseConfig.get('grid',False) 17         self.xaxis_locator = baseConfig.get('xaxis_locator',None) 18         self.yaxis_locator = baseConfig.get('yaxis_locator',None) 19         self.legend_loc = baseConfig.get('legend_loc',0) 20          21         if self.figsize != None : 22             pylab.figure(figsize = self.figsize) 23         if self.axis != None : 24             pylab.axis(self.axis) 25          26         pylab.title(self.title) 27         pylab.ylabel(self.ylabel) 28         ax = pylab.gca() 29         pylab.grid(self.grid) 30         if self.xaxis_locator != None : 31             ax.xaxis.set_major_locator( pylab.MultipleLocator(self.xaxis_locator) ) 32         if self.yaxis_locator != None : 33             ax.yaxis.set_major_locator( pylab.MultipleLocator(self.yaxis_locator) ) 34         self.lineList = [] 35         self.id = 1 36  37     def addline(self, lineConf) : 38         self.lineList.append((self.id, lineConf)) 39         self.id += 1 40         return {'id' : self.id - 1} 41  42     def removeline(self, lineId) : 43         for i in range(len(self.lineList)) : 44             id, conf = self.lineList[i] 45             if id == lineId : 46                 del self.lineList[i] 47                 break 48         else : 49             return {'status' : -1} 50         print len(self.lineList) 51         return {'status' : 0} 52  53     def __parselineConf(self, lineConf) : 54         X = lineConf['X'] 55         Y = lineConf['Y'] 56         marker = lineConf.get('marker',None) 57         color = lineConf.get('color', random.choice(MiniPlotTool.basecolors)) 58         markerfacecolor = lineConf.get('markerfacecolor',color) 59         label = lineConf.get('label','NoName') 60         linewidth = lineConf.get('linewidth',1) 61         linestyle = lineConf.get('linestyle','-') 62         return X, Y, marker, color, markerfacecolor, label, linewidth, linestyle 63  64     def plotSingleLine(self, lineConf): 65         X, Y, marker, color, markerfacecolor, label, linewidth, linestyle = self.__parselineConf(lineConf) 66         pylab.plot(X, Y, marker = marker, color = color, markerfacecolor = markerfacecolor, label=label, linewidth = linewidth, linestyle = linestyle) 67         pylab.legend(loc = self.legend_loc) 68  69     def plot(self) : 70         colors = [MiniPlotTool.basecolors[i % len(MiniPlotTool.basecolors)] for i in range(len(self.lineList))] 71         for i in range(len(self.lineList)) : 72             id, conf = self.lineList[i] 73             if conf.get('color',None) : 74                 conf['color'] = colors[i] 75             X, Y, marker, color, markerfacecolor, label, linewidth, linestyle = self.__parselineConf(conf) 76             pylab.plot(X, Y, marker = marker, color = color, markerfacecolor = markerfacecolor, label=label, linewidth = linewidth, linestyle = linestyle) 77         pylab.legend(loc = self.legend_loc) 78  79     def show(self) : 80         pylab.show() 81  82          83 if __name__ == '__main__' : 84     #test 85     baseConfig = { 86         #'figsize' : (6,8), 87         #'axis': [0,10,0,10], 88         #'title' : 'hello title', 89         #'ylabel' : 'hello ylabel', 90         'grid' : True, 91         #'xaxis_locator' : 0.5, 92         #'yaxis_locator' : 1, 93         #'legend_loc' : 'upper right' 94     } 95     tool = MiniPlotTool(baseConfig) 96     X = [ i for i in range(10)] 97     Y = [random.randint(1,10) for i in range(10)] 98     Y2 = [random.randint(1,10) for i in range(10)] 99     lineConf = {100         'X' : X,101         'Y' : Y102         #'marker' : 'x',103         #'color' : 'b',104         #'markerfacecolor' : 'r',105         #'label' : '222',106         #'linewidth' : 3,107         #'linestyle' : '--'108     }109     lineConf2 = {110         'X' : X,111         'Y' : Y2,112         'marker' : 'o',113         'color' : 'b',114         'markerfacecolor' : 'r',115         'label' : '222',116         'linewidth' : 3,117         'linestyle' : '--'118     }119     #tool.plotSingleLine(lineConf)120     print tool.addline(lineConf)121     print tool.addline(lineConf2)122 123     #print tool.removeline(1)124     tool.plot()125     tool.show()

</p>
<p>

</div>

</p>

 

</p>

 

</p>

![][] 

</p>

#### 附：引用自：https://sites.google.com/site/guyingbo/matplotlib%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0

</p>

#### 线属性:

</p>

颜色（color 简写为 c）：

</p>

-   蓝色： 'b' (blue)
-   绿色： 'g' (green)
-   红色： 'r' (red)
-   蓝绿色(墨绿色)： 'c' (cyan)
-   红紫色(洋红)： 'm' (magenta)
-   黄色： 'y' (yellow)
-   黑色： 'k' (black)
-   白色： 'w' (white)
-   灰度表示： e.g. 0.75 ([0,1]内任意浮点数)
-   RGB表示法： e.g. '\#2F4F4F' 或 (0.18, 0.31, 0.31)
-   任意合法的html中的颜色表示： e.g. 'red', 'darkslategray'

</p>

线型（linestyle 简写为 ls）：

</p>

-   实线： '-'
-   虚线： '--'
-   虚点线： '-.'
-   点线： ':'
-   点： '.' 

</p>

点型（标记marker）：

</p>

-   像素： ','
-   圆形： 'o'
-   上三角： '\^'
-   下三角： 'v'
-   左三角： '\<'
-   右三角： '\>'
-   方形： 's'
-   加号： '+' 
-   叉形： 'x'
-   棱形： 'D'
-   细棱形： 'd'
-   三脚架朝下： '1'（就是丫）
-   三脚架朝上： '2'
-   三脚架朝左： '3'
-   三脚架朝右： '4'
-   六角形： 'h'
-   旋转六角形： 'H'
-   五角形： 'p'
-   垂直线： '|'
-   水平线： '\_'
-   gnuplot 中的steps： 'steps' （只能用于kwarg中）

</p>

标记大小（markersize 简写为 ms）： 

</p>

-   markersize： 实数 

</p>

标记边缘宽度（markeredgewidth 简写为 mew）：

</p>

-   markeredgewidth：实数

</p>

标记边缘颜色（markeredgecolor 简写为 mec）：

</p>

-   markeredgecolor：颜色选项中的任意值

</p>

标记表面颜色（markerfacecolor 简写为 mfc）：

</p>

-   markerfacecolor：颜色选项中的任意值

</p>

透明度（alpha）：

</p>

-   alpha： [0,1]之间的浮点数

</p>

线宽（linewidth）：

</p>

-   linewidth： 实数

</p>

  []: http://images.cnitblog.com/blog/146443/201306/20150727-438e0f45f5b0455e82691c9e5fe11e2d.png
