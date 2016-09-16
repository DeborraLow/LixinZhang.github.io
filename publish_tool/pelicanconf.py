#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'LixinZhang'
SITENAME = u'Backyard of LixinZhang'
SITEURL = 'http://lixinzhang.github.io'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
#MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight, linenums=True)', 'extra']


# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('weibo', 'http://weibo.com/zhanglixin5566/'),
        ('Facebook', 'https://www.facebook.com/zhanglixin.peter'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './elegant'
GITHUB_URL = 'https://github.com/LixinZhang'
DISQUS_SITENAME = 'zhanglixinseu'
OUTPUT_PATH = './'

LANDING_PAGE_ABOUT = {'title':'Backyard of LixinZhang', 'details':'''
<p>北京，腾讯，微信，基础研究</p>
<p>本科在东南大学，研究生在北京航空航天大学。</p>
</p>
<p>目前的工作方向主要是推荐系统、搜索引擎，关注机器学习、数据挖掘、自然语言处理相关领域。</p>
<p>微信是我毕业第一份正式工作，毕业前实习过Yahoo!、阿里巴巴、创新工场。</p>
</p>
<p>
折腾过好多技术方向，到现在也没折腾明白，还在探索中...
</p>
<p>Balance work and life，希望自己能逐渐成为一个有趣的人。</p>

 '''}

PROJECTS = [
     {'name':'Gmail',
     'url':'mailto:zhanglixinseu@gmail.com',
     'description': 'Feel free to reach me via Email'},
     {'name': 'Github',
     'url': 'https://github.com/LixinZhang',
     'description': '一些代码，放在上面托管'},
     {'name':'Facebook',
     'url':'https://www.facebook.com/zhanglixin.peter',
     'description': '联系在外国朋友的'},
     {'name':'Linkedin',
     'url':'http://www.linkedin.com/pub/lixin-zhang/72/bb/66a',
     'description': '欢迎互相关注'},
     {'name': '新浪微博',
     'url': 'http://weibo.com/zhanglixin5566',
     'description': '扯淡用的'},
     {'name':'知乎',
     'url':'http://www.zhihu.com/people/zhanglixin',
     'description': '学习各种知识'},
     {'name':'博客园',
     'url':'http://www.cnblogs.com/coser',
     'description': '之前的博客，很多是本科时候记录的东西'}
     ]
