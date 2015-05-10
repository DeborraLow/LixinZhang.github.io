Title: Synergy 一个bug的解决办法
Date: 2012-12-08 08:01
Author: 糖拌咸鱼
Slug: synergy-ge-bugde-jie-jue-ban-fa

Synergy
，这个工具大家应该都比较熟悉，就是通过网络手段，用一台机器的鼠标和键盘管理多台电脑，相当好用。但是最近，我的这个软件作为Server端时却出现了问题，一直显示“

synergys.exe: no configuration available ”，无论怎么重装都不行。

于是找了好久，终于找到了解决办法，所以在这里记录下。

> synergy -f --config synergy.conf
>
>   
> section: screens   
> hostname1:   
> hostname2:   
> end
>
> section: links   
> hostname1:   
> right = hostname2   
> hostname2:   
> left = hostname1   
> end
>
> save as synergy.conf
>
> run ./synergys -f --config synergy.conf on your mac... then setup the
> windows client.. they should connect.

对于linux而然，建立一个sh脚本，以后用来自动启动就好。

对于windows而言，可以建立一个bat文件，写脚本用来启动Synergy。但是为了让其启动后能够在后台运行，也就是让那个丑陋的控制台图形隐藏掉，可以在代码头部加上这样一句话

> if not "%1"=="wkdxz" mshta
> vbscript:createobject("wscript.shell").run("""%\~f0""
> wkdxz",vbhide)(window.close)&&exit

好了，以后就用.bat启动吧，问题解决了。

</p>

