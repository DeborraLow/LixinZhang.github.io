Title: NLP-Spelling Notes
Date: 2014-04-22 13:20
Category: Note
Tags: NLP

##SpellingNotes MOOC Stanford NLP Course
###Spelling Tasks
* Spelling Error Detection
* Spelling Error Correction
    * Auto correct
    * Suggest a correction
    * Suggest lists

###Types of Spelling errors
####Non-word Errors
Is not a word.
#####Detection
* Any word not in a <code>dictionary</code> is an error.
* The larger the dictionary the better.

#####Correction
* Generate candidates: real words that are similar to error.
* Choose the one which is best :
    * Shortest weighted edit distance
    * Highest noisy channel probability
    
####Real word Errors
The word exists, but is used in some wrong way.

* For each word _w_, generate candidate set:
    * Find candidate words with similar <code>pronunciations</code>. Small edit distance.
    * Find candidate words with similar <code>spelling</code>
    * <strong>Include w in candidate set</strong>
* Choose best candidate
    * Noisy Channel
    * Classifier

###Noisy Channel
![Imgur](https://s6yqsa.dm2302.livefilestore.com/y2p8qVaKlvCEsx7dNtxfNHuolfhGMJUzsxsuoEVRhPGsGGvLdLDuuFVbJtE0e_f1NFNPQYUd2d-96MtOSjN7zLSVP9Gm9edeafIohAAxbc5C0g/noisychannel.png?psid=1)
We see an observation x of a misspelled word, and find the correct word w :
$$\widehat{w} = argmax\_{w \in V}P(w|x) = argmax\_{w \in V}\frac{P(x|w)P(w)}{P(x)}=argmax\_{w \in V}P(x|w)P(w)$$

####Damerau-Levenshtein edit distance
* Minimal edit distance between tow strings, where edits are <code>Insertion(插入)</code>, <code>Deletion(删除)</code>, <code>Substitution(替换)</code>, <code>Transposition of two adjacent letters(交换相邻位置)</code>.
* Candidate generation :80% of errors are within edit distance 1, almost all errors within edit distance 2.

####Channel model probability
* Unigram prior probability $$$P(w)$$$
* Given Misspelled word $$$x=x_1,x_2,x_3,...x_m$$$, and correct word $$$w=w_1,w_2,w_3,...w_m$$$, to calculate probability of edit $$$P(x|w)$$$
* Computing error probability : confusion matrix(混淆矩阵)
    * <code>del[x,y]</code> count(xy typed as x)
    * <code>ins[x,y]</code> count(x typed as xy)
    * <code>sub[x,y]</code> count(x typed as y)
    * <code>trans[x,y]</code> count(xy typed as yx)
![img](https://s6xavq.dm2304.livefilestore.com/y2pRxY3vcuwsks7XL72J2tqYli8rKoTDtcM3BT7rGyRST4iYe-1_o_obAGeCc4SDxfjsTe_NorDmhzd4wEAITOfZgZikPzjOViZTRRgnSGKiHM/QQ20140422-1.png?psid=1)    
* Finally, choose one maximum $$$P(x|w)P(w)$$$

####Using a bigram language model
$$P(W_1W_2W_3) = P(W_2|W_1)P(W_3|W_2)$$
where $$$W2$$$ is the word to be corrected.


###Solving real-word spelling errors
* For each word in sentence 
    * Generate candidate set
        * the word itself
        * all single-letter edits that are English words
        * words that are homophones(同音异构词)
* Choose best candidates
    * Noisy channel models
    * Task-specific classifier
   
####Noisy channel for real-world spell correction
* Given a sentence $$$w_1,w_2,w_3,...w_n$$$   
* Generate a set of candidates for each word $$$w_i$$$
  ![](https://sdcf7q.dm2302.livefilestore.com/y2plp808aW2LUETb-u6nWJLf8F5iipqhxUKp4Ofp7eimv-no68FE9psdR7ilZe_oYeJO3S4lGZI95p8CqOn2V7ZQVJx6oXqmVwngTSQRUgkFxs/QQ20140422-2.png?psid=1)
* Choose the sequence W that maximizes $$$P(W)$$$
  ![](https://sdfpaw.dm2302.livefilestore.com/y2pb7_V0YTFYvE-kupXxFdLuix0Ar3TS_fcf6bNGzalxS0qFIJYpJNpS0W-KRuS89GuM-lUnP7u6P0dPBz3VFy6fIvM5APBS-icfpQjDjA6LMM/QQ20140422-4.png?psid=1) 
* <code>two of the</code> should get a higher probability. 

Now, how to calculate $$$P(W)$$$?

* Language model
    * Unigram, Bigram
* Channel model
    * Same as for non-word spelling correction
    * Plus need probability for no error, $$$P(w|w)$$$. That is depends on the application, $$$P(w|w)=0.95$$$ when 1 error in 20 documents.

###Reference:
[Coursera Natural Language Processing](https://class.coursera.org/nlp/lecture)