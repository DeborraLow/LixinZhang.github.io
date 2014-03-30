Title: Computing AUC using sklearn
Date: 2014-03-23 12:53
Category: MachineLearning
Tags: Python

##What is AUC?
>When using normalized units, the area under the curve (often referred to as simply the AUC, or AUROC) is equal to the probability that a classifier will rank a randomly chosen positive instance higher than a randomly chosen negative one (assuming 'positive' ranks higher than 'negative').

A ROC curve plots Ture positive versus false positives for different classification thresholds. The <code>Area Under Curve(AUC)</code>for a ROC curve is the probability that the algorithm assigns a higher score to a random positive example than a random negative example.

Instead, using AUC since it combines the prediction performance over all ranks into a single number.

## Computing AUC using sklearn
    :::python
    import numpy as np
    from sklearn import metrics
    y = np.array([1, 1, 2, 2])
    pred = np.array([0.1, 0.4, 0.35, 0.8])
    #Label considered as positive and others are considered negative.
    fpr, tpr, thresholds = metrics.roc_curve(y, pred, pos_label=2)
    metrics.auc(fpr, tpr)

##Computing ROC using sklearn
    :::python
    import numpy as np
    from sklearn import metrics
    y = np.array([1, 1, 2, 2])
    scores = np.array([0.1, 0.4, 0.35, 0.8])
    fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)

##Reference
1. [ROC wikipedia](http://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve)
2. [Computing ROC using sklearn](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html)
3. [Computing AUC using sklearn](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html)
