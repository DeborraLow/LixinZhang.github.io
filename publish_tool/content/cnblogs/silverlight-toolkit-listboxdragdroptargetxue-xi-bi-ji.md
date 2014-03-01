Title: Silverlight Toolkit ListBoxDragDropTarget学习笔记
Date: 2010-09-11 13:07
Author: 糖拌咸鱼
Slug: silverlight-toolkit-listboxdragdroptargetxue-xi-bi-ji

 最近刚接触Silverlight，感觉学习Silverlight还是要先从控件学起。Silverlight
Toolkit
是一个非常不错的控件集，里面具有很多很实用的东西，所以先学习些这些东西还是很有好处的。

</p>

 自己原来通过写鼠标的各种事件，实现鼠标拖动组件的功能，今天学了学Sliverlight
Toolkit 工具，发现有DragDropTarge很好用的东西。废话不多说，直接上代码。

</p>

<span
style="white-space: pre;"></span>首先放上两个ListBox，利用ListBoxDragDropTarget实现拖拽效果。

</p>

<span
style="white-space: pre;"></span>这里需要注意的是，如果想要实现一个ListBox内部的重排序功能，就必须要定义一下ListBox.ItemPanel，否则将无法实现单独ListBox的reorder功能。

</p>

<span face="monospace" size="2" style="font-family: monospace; font-size: x-small;"><span style="line-height: normal; white-space: pre-wrap;">

<div class="cnblogs_code">

</p>
<p>
            <StackPanel Orientation="Horizontal" Margin="20,20,20,20">            <toolkit:ListBoxDragDropTarget AllowDrop="True">                <ListBox Width="100" Height="400" x:Name="FromBox" SelectionMode="Multiple">                    <ListBox.ItemsPanel>                        <ItemsPanelTemplate>                            <StackPanel HorizontalAlignment="Center" />                        </ItemsPanelTemplate>                    </ListBox.ItemsPanel>                    <ListBox.ItemTemplate>                        <DataTemplate>                            <StackPanel>                                <Image Source="{Binding HeadImage}" Height="30" Width="30" HorizontalAlignment="Center"/>                                <TextBlock Width="60" Height="15" Text="{Binding Name}" HorizontalAlignment="Center"/>                            </StackPanel>                        </DataTemplate>                    </ListBox.ItemTemplate>                </ListBox>            </toolkit:ListBoxDragDropTarget>            <toolkit:ListBoxDragDropTarget AllowDrop="True" >                <ListBox Width="100" Height="400" x:Name="ToBox" Margin="50,0,0,0">                    <ListBox.ItemsPanel>                        <ItemsPanelTemplate>                            <StackPanel HorizontalAlignment="Center" />                        </ItemsPanelTemplate>                                   </ListBox.ItemsPanel>                    <ListBox.ItemTemplate>                        <DataTemplate>                            <StackPanel>                                <Image Source="{Binding HeadImage}" Height="30" Width="30" HorizontalAlignment="Center"/>                                <TextBlock Width="60" Height="15" Text="{Binding Name}" HorizontalAlignment="Center"/>                            </StackPanel>                        </DataTemplate>                    </ListBox.ItemTemplate>                </ListBox>            </toolkit:ListBoxDragDropTarget>        </StackPanel>

</p>
<p>

</div>

</p>
  
</span></span>

</p>

<span
style="white-space: pre;"></span>接下来写后台代码，这里预先定义一个Person类，作为数据源。在Person类里，定义name、age、headImage属性，别忘了ListBox可是内容控件哦。这里有一点需要大家注意，我们平常绑定数据，用List\<\>就可以，但是为了实现预期的效果，就必须要使用ObservableCollection\<\>类型，为什么？因为**ObservableCollection表示一个动态数据集合，在添加项、移除项或刷新整个列表时，此集合将提供通知。 **

</p>

<span face="monospace" size="2" style="font-family: monospace; font-size: x-small;"><span style="line-height: normal; white-space: pre-wrap;">

<div class="cnblogs_code">

</p>
<p>
    using System;using System.Collections.Generic;using System.Linq;using System.Net;using System.Windows;using System.Windows.Controls;using System.Windows.Documents;using System.Windows.Input;using System.Windows.Media;using System.Windows.Media.Animation;using System.Windows.Shapes;using System.Windows.Controls.DataVisualization.Charting;using System.Collections.ObjectModel;namespace Demo{    public partial class MainPage : UserControl    {        public MainPage()        {            InitializeComponent();            //集合必须定义为ObservableCollection，因为ObservableCollection            //表示一个动态数据集合，在添加项、移除项或刷新整个列表时，此集合将提供通知。            ObservableCollection<Person> personList = new ObservableCollection<Person>();            personList.Add(new Person {Name="张三" , Age=30 ,HeadImage="image/1.png"});            personList.Add(new Person { Name = "李四", Age = 15, HeadImage = "image/2.png" });            personList.Add(new Person { Name = "王五", Age = 20, HeadImage = "image/3.png" });            ObservableCollection<Person> personList2 = new ObservableCollection<Person>();            personList2.Add(new Person { Name = "赵六", Age = 60 ,HeadImage="image/4.png"});            personList2.Add(new Person { Name = "刘二", Age = 30, HeadImage = "image/5.png" });            personList2.Add(new Person { Name = "赵一", Age = 40, HeadImage = "image/6.png" });            FromBox.ItemsSource = personList;            ToBox.ItemsSource = personList2;        }    }}

</p>
<p>

</div>

</p>
  
</span></span>

</p>

    就这样，利用Silverlight Toolkit很简单就可以实现很强大的功能。

</p>

效果截图：

</p>

<span style="white-space: pre;"></span>![实现左边ListBox向右边拖拽][]  
                               ![单独ListBox内部排序][]

</p>

  [实现左边ListBox向右边拖拽]: http://hi.csdn.net/attachment/201009/11/7475631_12842101881upV.png
  [单独ListBox内部排序]: http://hi.csdn.net/attachment/201009/11/7475631_1284210188mwUb.png
