Title: K-nearest Neighbors 算法
Date: 2012-11-06 08:27
Author: 糖拌咸鱼
Slug: k-nearest-neighbors-suan-fa

     机器学习初学者，超级小白，不对的地方尽请批评指正。欢迎一起探讨。

     K-nearest Neighbors
学习方法是基于实例的，可用于逼近实值或离散目标函数，概念简明。对于基于实例的算法，学习过程只是简单地存储已知的训练数据，当遇到新的查询实例时，一系列相似的实例被从存储器中取出，并用来分类新的查询实例。因此，基于实例的算法的最大不足也就在于分类新实例的开销特别大。

     关于该算法的基本介绍可以参考下教材或是维基百科[k-nearest neighbor
algorithm][]。这里主要写一下比较重要的问题。

     对于K-nearest
Neighbors算法而言，其距离是根据标准欧式距离定义的。可以把实例看做为一个多维向量，其距离就是求向量间的距离。

    1NN：预测值或类别，仅根据训练集中离待预测实例最近的参考实例决定

   
KNN：首先找到与待测实例最近的k个点，然后根据这k个点决定。进行分类：选择这k个实例中最普遍的类别值（majority
vote）；进行回归（求值）：加权平均值（average weighted by inverse
distance）。

基本过程：

> 1 Calculate distances of all training vectors to test vector   
> 2 Pick k closest vectors   
> 3 Calculate average/majority

虽然，KNN算法的原理很简单，但是其中很多问题需要解决。比如k值如何选择（k值过小，比较局限不稳定；k值过大，很多噪点影响），如何选择维度（实例中可能有很多维度属性与分类无关，而这些维度却很大程度影响了距离的计算结果），如何规格化参数（比如一个实例向量\<1,1000,5\>，该向量的第二个属性影响因子太大，因为我们一般认为所有属性是同等重要的，因此需要规格化样本数据），如何建立高效的索引（避免每次分类计算开销过大）。。。其实，需要研究的问题很多，也很困难。

 

**一个使用K-nearest Neighbors 算法进行分类的应用实例：**

**进行手写数字的分类**

[![image][]][]

**数据集：**Training
dataset：<http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra>

               Test
dataset：<http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tes>

**说明：**

这是一个分类的问题，手写识别数字，类别为数字0\~9。

每个训练实例，本应该是一个32\*32大小的0、1矩阵，但是由于维数过大，有人对此进行了优化，即按4\*4大小将其分块，然后化简为8\*8大小的矩阵，并用一个32维的向量进行表示。

**代码如下：**

<div class="cnblogs_code"
style="border-bottom: #cccccc 1px solid; border-left: #cccccc 1px solid; padding-bottom: 5px; background-color: #f5f5f5; padding-left: 5px; padding-right: 5px; border-top: #cccccc 1px solid; border-right: #cccccc 1px solid; padding-top: 5px;">

    from numpy import *import operatordef file2matrix (dataset_filename) :    dataset = open(dataset_filename , 'r')    items = dataset.readlines()    dimension = len(items[0].split(',')) - 1    train_items_lines = len(items)    returnMat = zeros((train_items_lines , dimension))    index = 0    classLabelVector = []    for item in items :        item = item.strip()        split_item_list = item.split(',')        split_item_list = map(lambda x:int(x) , split_item_list)        returnMat[index,:] = split_item_list[:dimension]        classLabelVector.append(int(split_item_list[-1]))        index += 1    dataset.close()    return returnMat , classLabelVectordef classify(inX , dataset , labels , k) :    datasetSize = dataset.shape[0]    #Compute distance using matrix    #inX repeats datasetSize rows to be a matrix with the same size of dataset    diffMat = tile(inX , (datasetSize,1)) - dataset    sqDiffMat = diffMat**2    sqDistance = sqDiffMat.sum(axis=1)    distance = sqDistance**0.5    sortedDistIndicies = distance.argsort()    classCount = {}    for i in range(k) :        label = labels[sortedDistIndicies[i]]        classCount[label] = classCount.get(label,0) + 1        sortedClassCount = sorted(classCount.iteritems() , key=operator.itemgetter(1) , reverse=True)    return sortedClassCount[0][0]def test_classify ( k ) :    dataset , labels =  file2matrix('dataset/optdigits.tra')    test_dataset = open('dataset/optdigits.tes' , 'r')    test_items = test_dataset.readlines()    success = 0    error = 0    for item in test_items :        item = item.strip()        split_item_list = item.split(',')        split_item_list = map(lambda x:int(x) , split_item_list)        classify_res = classify(split_item_list[:-1] , dataset , labels , k)        real_res = split_item_list[-1]        if classify_res == real_res :            success += 1        else :            error += 1    print '*'*10 , k ,'*'*10    print 'success\t' , success    print 'error\t' , error    return float(error)/float((error+success))if __name__ == '__main__' :    print test_classify(1)    print test_classify(5)    print test_classify(10)    print test_classify(15)    print test_classify(20)    print test_classify(30)

</p>
<p>

</div>

</p>

</p>

**运行结果：不同k值得影响**

</p>

[![image][1]][]

</p>

不难看出，k值并非越大越好，对于该问题而言，k在5的范围之内似乎是最佳的。

</p>

  [k-nearest neighbor algorithm]: http://en.wikipedia.org/wiki/K-nearest_neighbor_algorithm
  [image]: http://images.cnblogs.com/cnblogs_com/coser/201211/201211061626479454.png
    "image"
  [![image][]]: http://images.cnblogs.com/cnblogs_com/coser/201211/201211061626454885.png
  [1]: http://images.cnblogs.com/cnblogs_com/coser/201211/20121106162649552.png
    "image"
  [![image][1]]: http://images.cnblogs.com/cnblogs_com/coser/201211/201211061626485701.png
