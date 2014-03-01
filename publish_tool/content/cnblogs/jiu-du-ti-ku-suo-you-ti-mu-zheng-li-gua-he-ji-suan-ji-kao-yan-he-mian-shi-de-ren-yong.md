Title: 九度题库（所有题目整理，适合计算机考研和面试的人用）
Date: 2013-10-20 01:12
Author: 糖拌咸鱼
Slug: jiu-du-ti-ku-suo-you-ti-mu-zheng-li-gua-he-ji-suan-ji-kao-yan-he-mian-shi-de-ren-yong

本来搜一道面试题，找到叫九度题库的地方，发现里面的题目都比较基础，很适合当面试题来练习。

</p>

于是，闲得蛋疼，把所有题目给爬下来了，并整理成markdown格式，然后export成pdf，方便大家离线阅读。

</p>

写下抓下来的方法：

</p>

1、把列表页先wget下，然后抽取链接（用grep处理就好了，如cat problemset\*
| grep 'problem.php?pid=' | egrep -v 'obj'\> urls.txt）

</p>

2、然后...(毫无技术可言，纯属娱乐）

</p>

<div class="cnblogs_Highlighter">

</p>
<p>
``` {.brush:python;gutter:true;}
# -*- coding:utf-8 -*-import sysimport osdown_cnt = 0for line in file(sys.argv[1]) :    try:        down_cnt += 1        idx = line.find('problem')        idx_a = line.find('</a')        url = 'http://ac.jobdu.com/'+line[idx:idx+20]        p_name = ('%04d_' % down_cnt) + line[idx+22:idx_a] + '.html'        p_name = p_name.replace(' ','_')        print p_name, url        os.system('wget %s -O %s' % (url, p_name))        total_lines = len(file(p_name).readlines())        filter_text = '"dd|dt|dl"'        print '*' * 20, total_lines        content = os.popen('sed -n "132, %dp" %s | egrep -v %s ' % (total_lines-20, p_name, filter_text,))        fout = file(p_name[:-5] + '.md', 'w')        for l in content :            l = l.strip()            if (len(l) < 1) :continue            l = l.replace('题目1','###题目1').replace('<b>','####').replace('</b>','####').replace('<div>','').replace('</div>','').replace('<o:p>','').replace('</o:p>','')            fout.write(l)            fout.write('\n')        fout.close()        print 'No.%5d, %s done.' % (down_cnt, p_name[:-5] + '.md')    except :        print 'error'
```

</p>
<p>

</div>

</p>

3、pdf下载（有些文字不全，还请见谅）：[九都题库][]

</p>

  [九都题库]: http://ishare.iask.sina.com.cn/f/62856915.html
