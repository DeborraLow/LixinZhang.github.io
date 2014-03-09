Title: Issues met when installing software on Mac or PC
Date: 2014-03-04 10:20
Category: Note
Tags: BugFix

###解决Ubuntu下ImportError: libblas.so.3gf

如果你<code>import scipy</code>时出现，类似：
<pre>
import scipy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/dist-packages/scipy/__init__.py", line 78, in <module>
    from numpy import show_config as show_numpy_config
  File "/usr/lib/python2.7/dist-packages/numpy/__init__.py", line 137, in <module>
    import add_newdocs
  File "/usr/lib/python2.7/dist-packages/numpy/add_newdocs.py", line 9, in <module>
    from numpy.lib import add_newdoc
  File "/usr/lib/python2.7/dist-packages/numpy/lib/__init__.py", line 13, in <module>
    from polynomial import *
  File "/usr/lib/python2.7/dist-packages/numpy/lib/polynomial.py", line 17, in <module>
    from numpy.linalg import eigvals, lstsq
  File "/usr/lib/python2.7/dist-packages/numpy/linalg/__init__.py", line 48, in <module>
    from linalg import *
  File "/usr/lib/python2.7/dist-packages/numpy/linalg/linalg.py", line 23, in <module>
    from numpy.linalg import lapack_lite
ImportError: liblapack.so.3gf: cannot open shared object file: No such file or directory
</pre>

那么尝试安装<code>libatlas-base-dev</code>，至少我越到的问题解决了。

>sudo apt-get install libatlas-base-dev

