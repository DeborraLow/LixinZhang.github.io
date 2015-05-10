Title: 利用SimpleHttpServer快速共享文件
Date: 2012-09-28 07:46
Author: 糖拌咸鱼
Slug: li-yong-simplehttpserverkuai-su-gong-xiang-wen-jian

其实这是个小技巧，记录下。

</p>

最近，我一直在windows环境下，用虚拟机进行linux，PuTTY
ssh连接虚拟机进行程序开发的。

</p>

后来，发现两个系统间传递文件实在有点麻烦，本来想搭个ftp或是写个HTTPserver，后来发现SimpleHttpServer十分好用。

</p>

直接python -m SimpleHttpServer 8000 ，就可以在当前目录下直接创建一个http
server。

</p>

在其他机器上，用浏览器就可是访问这个文件夹了，共享文件轻松多了。

</p>

