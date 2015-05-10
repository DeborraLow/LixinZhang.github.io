Title: 三种常见的聚类算法的python实现 kmeans、Hierarchical clustering、kmedoids
Date: 2013-04-10 12:08
Author: 糖拌咸鱼
Slug: san-chong-chang-jian-de-ju-lei-suan-fa-de-pythonshi-xian-kmeans-hierarchical-clustering-kmedoids

   
聚类是机器学习、数据挖掘相关的一类很常见的问题。关于聚类算法的介绍这里就不多写了，因为无论是教科书还是网络上都有太多的资料了。这里，用一个《Programming
Collective
Intelligence》中的聚类例子，写几个经典聚类算法的实现，分别是hierachiclaCluster、kmeans、kmedoids。

</p>

  
另外，最近一直在看数据挖掘、自然语言处理相关的东西，通过看资料发现有些东西很好理解，但是长时间不用的话，过一段时间就忘记得差不多了。其实换个角度想，也是自己对这些东西理解得不深刻。我觉得踏踏实实的实现这些算法是必要的，因为在实现过程中，我们可以发现哪些地方是算法的核心思想，哪些地方是性能瓶颈，这也为进一步优化提供了基础。

</p>

 

</p>

<span style="font-size: x-large;">问题背景及数据集：</span>

</p>

    
blog的聚类。如何判断两个blog是相似的呢？由于相关的博客的主题内容应该是相同的，即会出现很多相同的词。于是我们为每个blog定义一个向量，该向量的维度为数据集中所有出现的不同词的个数，向量的值为对应词出现的次数。判断两个向量间的相似性，我们使用[pearson相似性度量][]算法。

</p>

   
测试数据集描述：[blogdata.txt][]数据集，该数据集第一行包含所有数据集中出现的不同词，共有m个，剩下所有行，每一行对应一篇blog，共m+1列，用tab分开。第一列为博客名，接下来m列为一个向量，代码每个词出现的次数。接下来就聚类吧\~

</p>

<span style="font-size: x-large;">Hierachical clustering :</span>

</p>

维基百科：<http://en.wikipedia.org/wiki/Hierarchical_clustering>

</p>

<span style="font-size: x-large;">kmeans clustering :</span>

</p>

维基百科：<http://en.wikipedia.org/wiki/Kmeans>

</p>

<span style="font-size: x-large;">kmedoids clustering :</span>

</p>

维基百科：<http://en.wikipedia.org/wiki/K-medoids>

</p>

虽然上面三种算法都很好理解，但是这都是基础算法，要想深入，还有很多很多相关问题需要解决，比如k如何设置；随机选取初始点的问题等等，而且如何选取好用的聚类算法也值得商榷。

</p>

github代码位置：<https://github.com/LixinZhang/bookreviews/tree/master/Programming_Collective_Intelligence/chapter3>

</p>

**<span style="font-size: large;">clusterBase.py 用来导入数据</span>**

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
from math import sqrtdef importData(FIFE = 'blogdata.txt') :    blogwords = []    blognames = []    f = open(FIFE, 'r')     words = f.readline().split()    #//remove '\r\n'    for line in f:            blog = line[:-2].split('\t')        blognames.append(blog[0])                blogwords.append([int(word_c) for word_c in blog[1:]]       )     return blogwords,blognamesdef pearson_distance(vector1, vector2) :    """    Calculate distance between two vectors using pearson method    See more : http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient    """    sum1 = sum(vector1)    sum2 = sum(vector2)    sum1Sq = sum([pow(v,2) for v in vector1])    sum2Sq = sum([pow(v,2) for v in vector2])    pSum = sum([vector1[i] * vector2[i] for i in range(len(vector1))])    num = pSum - (sum1*sum2/len(vector1))    den = sqrt((sum1Sq - pow(sum1,2)/len(vector1)) * (sum2Sq - pow(sum2,2)/len(vector1)))    if den == 0 : return 0.0    return 1.0 - num/den
```

</p>

**<span style="font-size: large;">hierachiclaCluster.py</span>**

</p>

<span
style="font-size: medium;">注意distances字典的使用，可以减少大量重复的计算</span>

</p>

<span
style="font-size: medium;">另外这个聚类算法，最终生成的是一颗树形结构。因此打印结果，需要递归的进行</span>

</p>

<span
style="font-size: medium;">在集体智慧编程书里，给出了一个利用PIL模块画树形图的算法，挺有参考价值的。</span>

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
#/usr/bin/pythonfrom clusterBase import importData,pearson_distanceclass bicluster:    def __init__(self, vec, left=None,right=None,distance=0.0,id=None) :        self.left = left        self.right = right        self.vec = vec        self.id = id        self.distance = distancedef hcluster(blogwords,blognames) :    biclusters = [ bicluster(vec = blogwords[i], id = i ) for i in range(len(blogwords)) ]    distances = {}    flag = None;    currentclusted = -1    while(len(biclusters) > 1) :        min_val = 2;        biclusters_len = len(biclusters)        for i in range(biclusters_len-1) :            for j in range(i + 1, biclusters_len) :                if distances.get((biclusters[i].id,biclusters[j].id)) == None:                    distances[(biclusters[i].id,biclusters[j].id)] = pearson_distance(biclusters[i].vec,biclusters[j].vec)                d = distances[(biclusters[i].id,biclusters[j].id)]                 if d < min_val :                    min_val = d                    flag = (i,j)        bic1,bic2 = flag        newvec = [(biclusters[bic1].vec[i] + biclusters[bic2].vec[i])/2 for i in range(len(biclusters[bic1].vec))]        newbic = bicluster(newvec, left=biclusters[bic1], right=biclusters[bic2], distance=min_val, id = currentclusted)        currentclusted -= 1        del biclusters[bic2]        del biclusters[bic1]        biclusters.append(newbic)    return biclusters[0]'''Print the tree structure, save as a jpeg image file.'''from PIL import Image, ImageDrawdef getheight (clust) :    if clust.left == None and clust.right == None :return 1    return getheight(clust.left) + getheight(clust.right)def getdepth(clust) :    if clust.left == None and clust.right == None :return 0    return max(getdepth(clust.left),getdepth(clust.right)) + clust.distancedef drawdendrogram(clust,labels,jpeg='clusters.jpg') :    h = getheight(clust) * 20    w = 1200    depth = getdepth(clust)    scaling = float(w-150) / depth        img = Image.new('RGB',(w,h),(255,255,255))    draw = ImageDraw.Draw(img)    draw.line((0,h/2,10,h/2),fill=(255,0,0))    drawnode(draw,clust,10,(h/2),scaling,labels)    img.save(jpeg,'JPEG')def drawnode(draw, clust, x, y, scaling, labels) :    if clust.id < 0 :        h1 = getheight(clust.left) * 20        h2 = getheight(clust.right) * 20        top = y - (h1+h2)/2        bottom = y + (h1+h2)/2        #line length        ll = clust.distance * scaling        draw.line((x,top+h1/2,x,bottom-h2/2),fill=(255,0,0))        draw.line((x,top+h1/2,x+ll,top+h1/2),fill=(255,0,0))        draw.line((x,bottom-h2/2,x+ll,bottom-h2/2),fill=(255,0,0))        drawnode(draw,clust.left, x+ll, top+h1/2,scaling, labels)        drawnode(draw,clust.right,x+ll, bottom-h2/2,scaling,labels)    else :        draw.text((x+5,y-7),labels[clust.id],(0,0,0))if __name__ == '__main__' :    #pearson_distance    blogwords,blognames = importData()    clust = hcluster(blogwords,blognames)    print clust    #drawdendrogram(clust,blognames,jpeg='blogclust.jpg')
```

</p>

 

</p>

**<span style="font-size: large;">kmeans.py</span>**

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
from clusterBase import importData, pearson_distanceimport randomdef print_matchs(matchs) :    for i in range(len(matchs)) :        print i , '---->',        for item in matchs[i] :            print item,        print     print '-'*20def kmeans(blogwords, k) :    min_max_per_word = [ [min([row[i] for row in blogwords]), max([row[i] for row in blogwords])]  for i in range(len(blogwords[0]))]    # generate k clusters randomly    clusters = []    for i in range(k) :        cluster = []        for min_, max_ in min_max_per_word :            cluster.append(random.random() * (max_ - min_) + min_)        clusters.append(cluster)    lables = []    matchs = [ [] for i in range(k)]    lastmatchs = [ [] for i in range(k)]    rounds = 100    while rounds > 0 :        matchs = [ [] for i in range(k)]        print 'round \t',rounds        for i in range(len(blogwords)) :            bestmatch_cluster = None            min_distance = 2.1            for j in range(k) :                dis = pearson_distance(clusters[j], blogwords[i])                if dis < min_distance :                    min_distance = dis                    bestmatch_cluster = j            matchs[bestmatch_cluster].append(i)        print_matchs(matchs)        print_matchs(lastmatchs)        if matchs == lastmatchs : break        lastmatchs = [[ item for item in matchs[i] ] for i in range(k)]        #move the centroids to the average of their members        for j in range(k) :            avg = [0.0 for i in range(len(blogwords[0])) ]            for m in matchs[j] :                vec = blogwords[m]                for i in range(len(blogwords[0])) :                    avg[i] += vec[i]            avg = [ item / len(matchs[j]) for item in avg]            clusters[j] = avg        rounds -= 1        if __name__ == '__main__' :    blogwords,blognames = importData()    kmeans(blogwords,5)
```

</p>

k-medoids.py

</p>
<p>
``` {.brush: .py; .auto-links: .true; .collapse: .false; .first-line: .1; .gutter: .true; .html-script: .false; .light: .false; .ruler: .false; .smart-tabs: .true; .tab-size: .4; .toolbar: .true;}
'''Another clusting method , k-medoids.See more : http://en.wikipedia.org/wiki/K-medoidsThe most common realisation of k-medoid clustering is the Partitioning Around Medoids (PAM) algorithm and is as follows:[2]1. Initialize: randomly select k of the n data points as the medoids2. Associate each data point to the closest medoid. ("closest" here is defined using any valid distance metric, most commonly Euclidean distance, Manhattan distance or Minkowski distance)3. For each medoid m     For each non-medoid data point o         Swap m and o and compute the total cost of the configuration4. Select the configuration with the lowest cost.5. repeat steps 2 to 4 until there is no change in the medoid.'''from clusterBase import importData, pearson_distanceimport randomdistances_cache = {}def totalcost(blogwords, costf, medoids_idx) :    size = len(blogwords)    total_cost = 0.0    medoids = {}    for idx in medoids_idx :        medoids[idx] = []    for i in range(size) :        choice = None        min_cost = 2.1        for m in medoids :            tmp = distances_cache.get((m,i),None)            if tmp == None :                tmp = pearson_distance(blogwords[m],blogwords[i])                distances_cache[(m,i)] = tmp            if tmp < min_cost :                choice = m                min_cost = tmp        medoids[choice].append(i)        total_cost += min_cost    return total_cost, medoids    def kmedoids(blogwords, k) :    size = len(blogwords)    medoids_idx = random.sample([i for i in range(size)], k)    pre_cost, medoids = totalcost(blogwords,pearson_distance,medoids_idx)    print pre_cost    current_cost = 2.1 * size # maxmum of pearson_distances is 2.        best_choice = []    best_res = {}    iter_count = 0    while 1 :        for m in medoids :            for item in medoids[m] :                if item != m :                    idx = medoids_idx.index(m)                    swap_temp = medoids_idx[idx]                    medoids_idx[idx] = item                    tmp,medoids_ = totalcost(blogwords,pearson_distance,medoids_idx)                    #print tmp,'-------->',medoids_.keys()                    if tmp < current_cost :                        best_choice = list(medoids_idx)                        best_res = dict(medoids_)                        current_cost = tmp                    medoids_idx[idx] = swap_temp        iter_count += 1        print current_cost,iter_count        if best_choice == medoids_idx : break        if current_cost <= pre_cost :            pre_cost = current_cost            medoids = best_res            medoids_idx = best_choice                return current_cost, best_choice, best_resdef print_match(best_medoids, blognames) :    for medoid in best_medoids :        print blognames[medoid],'----->',        for m in best_medoids[medoid] :            print '(',m,blognames[m],')',        print        print '---------' * 20 if __name__ == '__main__' :    blogwords, blognames = importData()    best_cost,best_choice,best_medoids = kmedoids(blogwords,8)    print_match(best_medoids,blognames)
```

</p>

 

</p>

<span style="font-size: x-large;"> </span>

</p>

  [pearson相似性度量]: http://zh.wikipedia.org/wiki/%E7%9A%AE%E5%B0%94%E9%80%8A%E7%A7%AF%E7%9F%A9%E7%9B%B8%E5%85%B3%E7%B3%BB%E6%95%B0
  [blogdata.txt]: http://kiwitobes.com/clusters/blogdata.txt
