Title: N—grams Notes
Date: 2014-04-21 10:20
Category: Note
Tags: NLP

##N-gram
###Goal
Assign a probability to a sentence. Compute the probability of a sentence or sequence of words:
$$P(W)=P(w_1,w_2,...w_N)$$

The Chain Rule applied to compute joint probability of words in sentence 
  
  $$P(w_1w_2w_3...w_n) = \prod_{i=1}^{n} P(w_i|w_1w_2...w\_{i-1})$$

###Markov Assumption
$$P(w_1w_2...w_n) \thickapprox \prod\_{i=1}^{n} P(w_i|w_{i-k}...w\_{i_1})$$
In other words, we approximate each component in the product :
$$P(w_i|w_1w_2...w\_{i-1}) \thickapprox P(w_i|w\_{i-k}...w\_{i_1})$$

###Ngram
####Model
* <code>Unigram</code>:simplest case
$$P(w_1w_2...w_n) \thickapprox \prod\_{i=1}^{n} P(w_i)$$
* <code>Bigram model</code> : Condition on the previous word:
$$P(w_i|w\_{i-k}...w\_{i_1}) \thickapprox P(w_i|w_{i-1})$$
* Extend to trigrams,4-grams,5-grams

####Estimating bigram probabilities
* The Maximum Likelihood Estimate(最大释然估计)
$$P(w_i|w_{i-1}) = \frac{count(w\_{i-1}, w_i)}{count(w\_{i-1})}$$
* It would be $$$zero$$$ when $$$count(w\_{i-1}, w_i)=0$$$. So, in order to avoid underflow, we do everything in <code>log</code> space, also adding is faster than multiplying.
* $$log(p_1p_2p_3p_4) = log(p_1)+log(p_2)+log(p_3)+log(p_4)$$

####Evaluation
#####Perplexity
> In information theory, perplexity is a measurement of how well a probability distribution or probability model predicts a sample. It may be used to compare probability models.

The best language model is one that best predicts an unseen test set. Give the highest <code>P(sentence)</code>.
Perplexity is the inverse probability of the test set, normalised by the number of words. Minimizing perplexity is the same as maximising probability.
$$PP(W)=P(w_1w_2...w_N)^{-\frac{1}{N}}$$

Lower perplexity = better model

####The perils(危险) of overfitting
* N-grams only work well for word prediction if the test corpus looks like the training corpus.
    * In real life, it often doesn't
    * We need to train robust models that generalise!
    * One kind of generalization:zeros
        * Things that don't ever occur in the training set, but occur in the test set.  
    * Zero probability bigrams
        * mean that we will assign 0 probability to the test set!
        * can not compute <code>perplexity</code>(can't divide by 0)
        
###Smoothing
####Add-one(Laplace) smoothing(拉普拉斯平滑)
* Pretend we saw each word one more time than we did.（比实际多一次）
* MLE estimate
  $$P\_{MLE}(w_i|w_{i-1})=\frac{c(w\_{i-1},w_i)}{c(w\_{i-1})}$$

* MLE Add-1 estimate
  $$P\_{MLE}(w_i|w_{i-1})=\frac{c(w\_{i-1},w_i)+1}{c(w\_{i-1})+V}$$
  where $$$V=len(sentence)$$$
* Reconstituted(重组) counts
  
  $$c(w_{n-1}w_n)=\frac{[C(w\_{n-1}w_n)+1] \times C(w\_{n-1})}{C(w\_{n-1}+V)}$$
  
* Add-1estimation is not so good, and there are better methods for <code>N-grams</code>,<code>add-1</code> performs well in domains where the number of zeros isn't so huge.

###Backoff(回退) and Interpolation（插值）
Sometimes it helps to use less context, condition on less context for contexts you have not learned much about.
####Backoff
* use trigram if you have good evidence, otherwise bigram, otherwise unigram. (当trigram置信度较低时考虑回退到bigram，还可以再回退到unigram)
####Interpolation
* mix unigram, bigram, trigram, works better than back off
* Linear Interpolation
$$\overline{P}(w_n|w_{n-2}w\_{n-1}) = \lambda_1 P(w_n|w\_{n-2}w\_{n-1}) + \lambda_2 P(w_n|w\_{n-1}) + \lambda_3 P(w_n)$$
* How to set lambdas?

###Unknown words
Instead: create an unknown word token _rare_, any training word not in L(a fixed lexicon L of size V) changed to _rare_, now we train its probabilities like a normal word.

###Huge web-scale n-gram
####Pruning(修剪)
* Only store <code>N-grams</code> with count > threshold, remove singletons of higher-order n-grams
* Entropy-based pruning

####Efficiency
* Efficient data structures like tries
* Bloom filters: approximate language models
* store words as indexes, not strings
* Smoothing for web-scale N-grams ("stupid back off" Brants et al.2007)

###Good turing Smoothing
* Use the count of things we've seen once to help estimate the count of things we've never seen.Notation:$$$N_c = Frequence of frequency of c$$$, the count of things we've seen c times.
* Calculations:
    * $$$P_{GT}(unseen) = \frac{N_1}{N}$$$
    * $$$c^{*}=\frac{(c+1)N_{c+1}}{N_c}$$$
    * $$$P_{GT}(seen>1) = \frac{c^{*}}{N}$$$
* Good_Turing complications(问题)
    *$$$N_c$$$中才并不一定连续，为防止出现跳跃的情况，出现$$$N_c=0$$$，在不可信区间，fit一条直线。 


