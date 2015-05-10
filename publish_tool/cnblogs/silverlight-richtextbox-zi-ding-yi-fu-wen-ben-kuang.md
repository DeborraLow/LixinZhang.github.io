Title: Silverlight RichTextBox 自定义富文本框
Date: 2010-09-06 12:56
Author: 糖拌咸鱼
Slug: silverlight-richtextbox-zi-ding-yi-fu-wen-ben-kuang

**核心代码：**

</p>

<div class="cnblogs_code">

</p>

<div>

<span style="color: #0000ff;">using</span><span style="color: #000000;">
System;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Collections.Generic;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Linq;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Net;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Windows;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Windows.Controls;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Windows.Documents;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Windows.Input;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Windows.Media;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Windows.Media.Animation;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Windows.Shapes;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Windows.Navigation;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Windows.Media.Imaging;  
</span><span style="color: #0000ff;">using</span><span
style="color: #000000;"> System.Collections.ObjectModel;  
</span><span style="color: #0000ff;">namespace</span><span
style="color: #000000;"> RichTextBoxDemo  
{  
</span><span style="color: #0000ff;">public</span><span
style="color: #0000ff;">partial</span><span
style="color: #0000ff;">class</span><span style="color: #000000;">
MainPage : UserControl   
{  
</span><span style="color: #0000ff;">private</span><span
style="color: #000000;"> List</span><span
style="color: #000000;">\<</span><span
style="color: #000000;">String</span><span
style="color: #000000;">\></span><span style="color: #000000;">
list</span><span style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
List</span><span style="color: #000000;">\<</span><span
style="color: #0000ff;">string</span><span
style="color: #000000;">\></span><span style="color: #000000;">();  
</span><span style="color: #0000ff;">private</span><span
style="color: #000000;"> Image selectedImage</span><span
style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
Image();  
</span><span style="color: #0000ff;">private</span><span
style="color: #000000;"> CwChoosePic childW;  
</span><span style="color: #0000ff;">private</span><span
style="color: #000000;"> CwChooseLink cl;  
</span><span style="color: #0000ff;">public</span><span
style="color: #000000;"> MainPage()  
{  
InitializeComponent();  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">绑定字体样式数据</span><span
style="color: #008000;">  
</span><span style="color: #000000;"> ObservableCollection</span><span
style="color: #000000;">\<</span><span
style="color: #000000;">FontFamily</span><span
style="color: #000000;">\></span><span style="color: #000000;">
fonts</span><span style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
ObservableCollection</span><span style="color: #000000;">\<</span><span
style="color: #000000;">FontFamily</span><span
style="color: #000000;">\></span><span style="color: #000000;">();  
fonts.Add(</span><span style="color: #0000ff;">new</span><span
style="color: #000000;"> FontFamily(</span><span
style="color: #800000;">"</span><span
style="color: #800000;">Arial</span><span
style="color: #800000;">"</span><span style="color: #000000;">));  
fonts.Add(</span><span style="color: #0000ff;">new</span><span
style="color: #000000;"> FontFamily(</span><span
style="color: #800000;">"</span><span style="color: #800000;">Courier
New</span><span style="color: #800000;">"</span><span
style="color: #000000;">));  
fonts.Add(</span><span style="color: #0000ff;">new</span><span
style="color: #000000;"> FontFamily(</span><span
style="color: #800000;">"</span><span style="color: #800000;">Times New
Roman</span><span style="color: #800000;">"</span><span
style="color: #000000;">));  
fonts.Add(</span><span style="color: #0000ff;">new</span><span
style="color: #000000;"> FontFamily(</span><span
style="color: #800000;">"</span><span
style="color: #800000;">宋体</span><span
style="color: #800000;">"</span><span style="color: #000000;">));  
MyComboBox.DataContext</span><span
style="color: #000000;">=</span><span style="color: #000000;"> fonts;  
MyComboBox.SelectedIndex</span><span
style="color: #000000;">=</span><span
style="color: #800080;">0</span><span style="color: #000000;">;  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">绑定字体大小</span><span
style="color: #008000;">  
</span><span style="color: #000000;"> ObservableCollection</span><span
style="color: #000000;">\<</span><span
style="color: #000000;">Double</span><span
style="color: #000000;">\></span><span style="color: #000000;">
fontsize</span><span style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
ObservableCollection</span><span style="color: #000000;">\<</span><span
style="color: #0000ff;">double</span><span
style="color: #000000;">\></span><span style="color: #000000;">();  
</span><span style="color: #0000ff;">for</span><span
style="color: #000000;"> (</span><span
style="color: #0000ff;">int</span><span style="color: #000000;">
i</span><span style="color: #000000;">=</span><span
style="color: #800080;">8</span><span style="color: #000000;">;
i</span><span style="color: #000000;">\<=</span><span
style="color: #800080;">50</span><span style="color: #000000;">;
i</span><span style="color: #000000;">+=</span><span
style="color: #800080;">2</span><span style="color: #000000;">)  
{  
fontsize.Add(i);  
}  
SizeComboBox.DataContext</span><span
style="color: #000000;">=</span><span style="color: #000000;">
fontsize;  
SizeComboBox.SelectedIndex</span><span
style="color: #000000;">=</span><span
style="color: #800080;">0</span><span style="color: #000000;">;  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">为ComboBox绑定颜色画刷</span><span
style="color: #008000;">  
</span><span style="color: #000000;"> ObservableCollection</span><span
style="color: #000000;">\<</span><span
style="color: #000000;">SolidColorBrush</span><span
style="color: #000000;">\></span><span style="color: #000000;">
brush</span><span style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
ObservableCollection</span><span style="color: #000000;">\<</span><span
style="color: #000000;">SolidColorBrush</span><span
style="color: #000000;">\></span><span style="color: #000000;">();  
brush.Add(</span><span style="color: #0000ff;">new</span><span
style="color: #000000;"> SolidColorBrush(Colors.Red));  
brush.Add(</span><span style="color: #0000ff;">new</span><span
style="color: #000000;"> SolidColorBrush(Colors.Blue));  
brush.Add(</span><span style="color: #0000ff;">new</span><span
style="color: #000000;"> SolidColorBrush(Colors.Green));  
</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.ColorComboBox.ItemsSource</span><span
style="color: #000000;">=</span><span style="color: #000000;"> brush;  
</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.ColorComboBox.SelectedIndex</span><span
style="color: #000000;">=</span><span
style="color: #800080;">0</span><span style="color: #000000;">;  
}  
</span><span style="color: #0000ff;">private</span><span
style="color: #0000ff;">void</span><span style="color: #000000;">
btn\_Blod\_Click(</span><span style="color: #0000ff;">object</span><span
style="color: #000000;"> sender, RoutedEventArgs e)  
{  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">字体加粗</span><span style="color: #008000;">  
</span><span style="color: #000000;"> FontWeight fw</span><span
style="color: #000000;">=</span><span style="color: #000000;">
(FontWeight)</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.richTextBox.Selection.GetPropertyValue(TextElement.FontWeightProperty);  
</span><span style="color: #0000ff;">if</span><span
style="color: #000000;"> (fw</span><span
style="color: #000000;">==</span><span style="color: #000000;">
FontWeights.Bold)  
{  
</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.richTextBox.Selection.ApplyPropertyValue(TextElement.FontWeightProperty,
FontWeights.Normal);  
}  
</span><span style="color: #0000ff;">else</span><span
style="color: #000000;">  
{  
</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.richTextBox.Selection.ApplyPropertyValue(TextElement.FontWeightProperty,
FontWeights.Bold);  
}  
}  
</span><span style="color: #0000ff;">private</span><span
style="color: #0000ff;">void</span><span style="color: #000000;">
btn\_Italic\_Click(</span><span
style="color: #0000ff;">object</span><span style="color: #000000;">
sender, RoutedEventArgs e)  
{  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">字体加倾斜</span><span style="color: #008000;">  
</span><span style="color: #000000;"> FontStyle fs</span><span
style="color: #000000;">=</span><span style="color: #000000;">
(FontStyle)</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.richTextBox.Selection.GetPropertyValue(TextElement.FontStyleProperty);  
</span><span style="color: #0000ff;">if</span><span
style="color: #000000;"> (fs</span><span
style="color: #000000;">==</span><span style="color: #000000;">
FontStyles.Italic)  
{  
</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.richTextBox.Selection.ApplyPropertyValue(TextElement.FontStyleProperty,
FontStyles.Normal);  
}  
</span><span style="color: #0000ff;">else</span><span
style="color: #000000;">  
{  
</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.richTextBox.Selection.ApplyPropertyValue(TextElement.FontStyleProperty,
FontStyles.Italic);  
}  
}  
</span><span style="color: #0000ff;">private</span><span
style="color: #0000ff;">void</span><span style="color: #000000;">
MyComboBox\_SelectionChanged(</span><span
style="color: #0000ff;">object</span><span style="color: #000000;">
sender, SelectionChangedEventArgs e)  
{  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">更改字体样式</span><span
style="color: #008000;">  
</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.richTextBox.Selection.ApplyPropertyValue(TextElement.FontFamilyProperty,
(FontFamily)MyComboBox.SelectedItem);  
}  
</span><span style="color: #0000ff;">private</span><span
style="color: #0000ff;">void</span><span style="color: #000000;">
SizeComboBox\_SelectionChanged(</span><span
style="color: #0000ff;">object</span><span style="color: #000000;">
sender, SelectionChangedEventArgs e)  
{  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">更改字体大小</span><span
style="color: #008000;">  
</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.richTextBox.Selection.ApplyPropertyValue(TextElement.FontSizeProperty,</span><span
style="color: #0000ff;">this</span><span
style="color: #000000;">.SizeComboBox.SelectedItem);  
}  
</span><span style="color: #0000ff;">private</span><span
style="color: #0000ff;">void</span><span style="color: #000000;">
ColorComboBox\_SelectionChanged(</span><span
style="color: #0000ff;">object</span><span style="color: #000000;">
sender, SelectionChangedEventArgs e)  
{  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">更改字体颜色</span><span
style="color: #008000;">  
</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.richTextBox.Selection.ApplyPropertyValue(TextElement.ForegroundProperty,
(SolidColorBrush)</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.ColorComboBox.SelectedItem);  
}  
</span><span style="color: #0000ff;">private</span><span
style="color: #0000ff;">void</span><span style="color: #000000;">
btn\_AddImage\_Click(</span><span
style="color: #0000ff;">object</span><span style="color: #000000;">
sender, RoutedEventArgs e)  
{  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">从ChildWindow控件中获取图片，从而添加到编辑框</span><span
style="color: #008000;">  
</span><span style="color: #000000;"> childW</span><span
style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
CwChoosePic();  
childW.Show();  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">在关闭时出发事件</span><span
style="color: #008000;">  
</span><span style="color: #000000;"> childW.Closed</span><span
style="color: #000000;">+=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
EventHandler(childW\_Closed);  
}  
</span><span style="color: #0000ff;">void</span><span
style="color: #000000;"> childW\_Closed(</span><span
style="color: #0000ff;">object</span><span style="color: #000000;">
sender, EventArgs e)  
{  
Paragraph pg</span><span style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
Paragraph();  
InlineUIContainer container</span><span
style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
InlineUIContainer();  
container.Child</span><span style="color: #000000;">=</span><span
style="color: #000000;"> childW.GetSelectImage();  
pg.Inlines.Add(container);  
</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.richTextBox.Blocks.Add(pg);  
}  
</span><span style="color: #0000ff;">private</span><span
style="color: #0000ff;">void</span><span style="color: #000000;">
btn\_AddLink\_Click(</span><span
style="color: #0000ff;">object</span><span style="color: #000000;">
sender, RoutedEventArgs e)  
{  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">从ChildWindow控件中获取链接信息，从而添加到编辑框</span><span
style="color: #008000;">  
</span><span style="color: #000000;"> cl</span><span
style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
CwChooseLink();  
cl.Show();  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">在关闭时出发事件</span><span
style="color: #008000;">  
</span><span style="color: #000000;"> cl.Closed</span><span
style="color: #000000;">+=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
EventHandler(cl\_Closed);  
}  
</span><span style="color: #0000ff;">void</span><span
style="color: #000000;"> cl\_Closed(</span><span
style="color: #0000ff;">object</span><span style="color: #000000;">
sender, EventArgs e)  
{  
</span><span style="color: #008000;">//</span><span
style="color: #008000;">增加段落</span><span style="color: #008000;">  
</span><span style="color: #000000;"> Paragraph pg</span><span
style="color: #000000;">=</span><span
style="color: #0000ff;">new</span><span style="color: #000000;">
Paragraph();  
pg.Inlines.Add( cl.GetHyperlink());  
</span><span style="color: #0000ff;">this</span><span
style="color: #000000;">.richTextBox.Blocks.Add(pg);  
}  
}  
}</span>

</div>

</p>
<p>

</div>

</p>

<span style="font-family: monospace; font-size: x-small;"><span style="line-height: normal; white-space: pre-wrap;">

  
</span></span>

</p>

**<span style="font-family: mceinline;">效果截图：</span>**

</p>

**<span style="font-family: mceinline;">  
</span>**

</p>

![][]

</p>

 

</p>

![][1]

</p>

  []: http://pic002.cnblogs.com/images/2011/146443/2011110620321010.png
  [1]: http://pic002.cnblogs.com/images/2011/146443/2011110620321953.png
