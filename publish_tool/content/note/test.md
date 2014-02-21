Title: Python中的模块与包
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: python_module_package
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

###标准库的安装路径
在<code>import</code>模块的时候，python是通过系统路径找到这些模块的，我们可以将这些路径打印出来：
<pre>
 pprint.pprint(sys.path)
['',
 '/Library/Python/2.7/site-packages/pip-1.4.1-py2.7.egg',
 '/Library/Python/2.7/site-packages/python_recsys-0.2-py2.7.egg',
 '/Users/zhanglixin/opensource/ipython',
 '/Library/Python/2.7/site-packages/pexpect-3.0-py2.7.egg',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC',
 '/Library/Python/2.7/site-packages']
</pre>

那么，我们放进这些路径里的模块或包，就可以不需指定路径，直接使用<code>import</code>导入了。特别的，<code>/Library/Python/2.7/site-packages</code>，我们常用的应该放在这里。

##常见问题：

* 引入某一特定路径下的模块
  * 使用<code>sys.path.append(your_module_path)</code>

* 将一个路径加入到python系统路径下，避免每次通过代码指定路径
  * 利用系统环境变量 <code>export PYTHONPATH=$PYTHONPATH:your_module_path</code>，
  * 直接将这个路径链接到类似<code>/Library/Python/2.7/site-packages</code>目录下

* 好的建议
  * 经常使用<code>if \_\_name\__ == '\_\_main__'</code>，保证你写包既可以import又可以独立运行，用于test。
  * 多次import不会多次执行模块，只会执行一次。可以使用<code>reload</code>来强制运行模块，但不提倡。
  
###包（package）
为了组织好模块，将多个模块分为一个包。包是python模块文件所在的目录，且该目录下必须存在<code>\_\_init__.py</code>文件。常见的包结构如下：
<pre>
package_a
├── __init__.py
├── module_a1.py
└── module_a2.py
package_b
├── __init__.py
├── module_b1.py
└── module_b2.py
main.py
</pre>

* 如果<code>main.py</code>想要引用<code>package_a</code>中的模块<code>module_a1</code>，可以使用:
<pre>
from package_a import module_a1
import package_a.module_a1
</pre>

* 如果<code>package_a</code>中的<code>module_a1</code>需要引用<code>package_b</code>，那么默认情况下，python是找不到<code>package_b</code>。我们可以使用<code>sys.path.append('../')</code>,可以在<code>package_a</code>中的<code>\_\_init\_\_.py</code>添加这句话，然后该包下得所有module都添加* <code>import \_\_init__</code>即可。



