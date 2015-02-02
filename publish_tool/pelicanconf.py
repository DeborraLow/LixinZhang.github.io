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
<p>I am now a FTE working for Yahoo!(Beijing R&D). 
I graduated from Beihang University(BUAA, Beijing) with master degree in Computer Science, 
and got bachelor degree in Software Engineering from Southeast University(SEU, Nanjing).
<p>
You could find me in <a href="https://github.com/LixinZhang" title="Github">Github</a>,
 <a href="https://www.facebook.com/zhanglixin.peter" title="Facebook">Facebook</a>,
 <a href="http://www.linkedin.com/pub/lixin-zhang/72/bb/66a" title="Linkedin">Linkedin</a>,
 <a href="http://weibo.com/zhanglixin5566" title="新浪微博">新浪微博</a> and <a href="http://www.cnblogs.com/coser" title="博客园">博客园</a> 
or reach me via <a href="mailto:zhanglixinseu@gmail.com" title="My email address" itemprop="email">Gmail</a>.
</p>

<p>
I mostly work in Python, C++/C on Mac OS, UNIX-style OS and I have rich intern experience 
in many companies on my school-days, like Yahoo(one year), Alibaba(one year) 
and Innovation Works(two month). 
Now I am focusing on Computational Advertising, Recommender System, Data Mining which are now very pupular in industry and academia. 
I am also familiar with Web Development, Distributed System and Network Programming.
</p>

<p>
My hobbies are Winning Eleven computer game and music of Linkin Park, Taylor Swift, Avril Lavigne, Taiwan Mayday and 逃跑计划. 
English as my second language is very poor to me. So I try to write some blogs and notes in English to improve my language skill.
</p>

 '''}

PROJECTS = [{
     'name': 'L2R for BT',
     'url': 'https://github.com/LixinZhang/advertisingLab',
     'description': 'Audience Ranking : an algorithm helps longtail'
     ' advertisers to select top-ranked audience according to their relevance with advertisements.'},
     {'name': 'miniCrowler',
     'url': 'https://github.com/LixinZhang/miniCrowler',
     'description': 'MiniCrawler is a simple web crawler implemented by Python.'},
     {'name':'ServerClusterManageTool',
     'url':'https://github.com/LixinZhang/ServerClusterManageTool',
     'description': 'A tool help users to manage machines on PaaS in web clients.'},
     {'name':'DistributedCrawler',
     'url':'https://github.com/LixinZhang/DistributedCrawler',
     'description': 'This is a Distributed Web Crawler Project using C++ on Linux platform.'}]
