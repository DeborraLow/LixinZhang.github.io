Title: Python中的模块与包
Date: 2014-02-16 05:12
Author: 糖拌咸鱼
Slug: pythonzhong-de-mo-kuai-yu-bao

标准库的安装路径
----------------

</p>

在`import`模块的时候，python是通过系统路径找到这些模块的，我们可以将这些路径打印出来：

</p>

<p>
    >>> pprint.pprint(sys.path)['', '/Library/Python/2.7/site-packages/pip-1.4.1-py2.7.egg', '/Library/Python/2.7/site-packages/python_recsys-0.2-py2.7.egg', '/Users/zhanglixin/opensource/ipython', '/Library/Python/2.7/site-packages/pexpect-3.0-py2.7.egg', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC', '/Library/Python/2.7/site-packages']

</p>

那么，我们放进这些路径里的模块或包，就可以不需指定路径，直接使用`import`导入了。特别的，`/Library/Python/2.7/site-packages`，我们常用的应该放在这里。

</p>

常见问题：
----------

</p>

-   引入某一特定路径下的模块

    </p>

    -   使用`sys.path.append(yourmodulepath)`
-   将一个路径加入到python系统路径下，避免每次通过代码指定路径

    </p>

    -   利用系统环境变量
        `export PYTHONPATH=$PYTHONPATH:yourmodulepath`，
    -   直接将这个路径链接到类似`/Library/Python/2.7/site-packages`目录下
-   好的建议

    </p>

    -   经常使用`if __name__ == '__main__'`，保证你写包既可以import又可以独立运行，用于test。
    -   多次import不会多次执行模块，只会执行一次。可以使用`reload`来强制运行模块，但不提倡。

</p>

包（package）
-------------

</p>

为了组织好模块，将多个模块分为一个包。包是python模块文件所在的目录，且该目录下必须存在`__init__.py`文件。常见的包结构如下：

</p>

<p>
    package_a├── __init__.py├── module_a1.py└── module_a2.pypackage_b├── __init__.py├── module_b1.py└── module_b2.pymain.py

</p>

-   如果`main.py`想要引用`packagea`中的模块`modulea1`，可以使用:

</p>

<p>
    from package_a import module_a1import package_a.module_a1

</p>

-   如果`packagea`中的`modulea1`需要引用`packageb`，那么默认情况下，python是找不到`packageb`。我们可以使用`sys.path.append('../')`,可以在`packagea`中的`__init__.py`添加这句话，然后该包下得所有module都添加\*
    `import __init_`即可。

</p>

