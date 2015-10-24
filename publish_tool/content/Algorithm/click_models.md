Title: Notes on Click Model
Date: 2015-10-24 21:44
Category: Algorithm

> 在做click model，进行了一些简单的调研。主要参考一些相关的survey和paper，参考文章已在reference中列出。

##  Introduction

### What is Click Model 

*  Click models aim at modeling user clicks on a SERP(search engine result page) based on **Search Log**.
*  Calculate the probability of a click on a given document, $$$P(C_u=1)$$$.
*  Calculate the probability of a click on that document given previously observed clicks in the same session, $$$P(C_u=1|C_{<r_u})$$$.
*  Help **understand users**, **simulate users**, **evaluate search**, **improve search**.

##  Basic Click Models

###Basic Models
* Random Click Model (RCM)
* Click-through Rate Models (CTR)
    * Rank-based CTR Model (RCTR)
    * Document-based CTR Model (DCTR)
* Position-based Model (PBM)
* Cascade Model (CM)
* User Browsing Model (UBM)
* Dependent Click Model (DCM)
* Click Chain Model (CCM)
* Dynamic Bayesian Network Model (DBN)
    * Simplified DBN Model (SDBN)

###Notation
**Expression** & **Meaning**

| Expression | Meaning|
| ------------ | ------------- |
|$$$SERP$$$ | search engine result page |
|$$$u$$$ | A document  |
|$$$q$$$ | A user's query  |
|$$$r$$$ | The rank of a document |
|$$$u\_r$$$ | A document at rank r  |
|$$$r\_u$$$ | The rank of a document u |

**Event** & **Meaning**

| Event | Meaning|
| ------------ | ------------- |
|$$$E$$$ | a user examines an object on a $$$SERP$$$ |
|$$$A$$$ | a user is attracted by the object's representation|
|$$$C$$$ | an object is clicked |
|$$$S$$$ | a user's information need is satisified |

### Random Click Model (RCM)
$$P(C\_u = 1) = \rho$$

### Click-through Rate Models (CTR)

* Rank-based CTR Model (RCTR)
$$P(C\_r = 1) = \rho\_r$$

* Document-based CTR Model (DCTR)
$$P(C\_{u} = 1) = \rho\_{uq}$$


###Position-based Model (PBM)
<img src='http://lixinzhang.github.io/image/PBM.png'></img>

**Examination hypothesis**. The probability of a user examining a document depends heavily on its rank or position. PBM introduces a set of examination parameters $$$\gamma\_{r}$$$, one for each rank. PBM does not depend on the events at previous ranks.

$$P(C\_u=1) = P(E\_u=1) \cdot P(A\_u=1)$$
$$P(A\_u=1) = \alpha\_{uq}$$
$$P(E\_u=1) = \gamma\_{uq}$$

###Cascade Model (CM)
<img src='http://lixinzhang.github.io/image/CM.png'></img>

Cascade model assumes that a user scans documents on a SERP from top to bottom until they find a relevant document. It can only describe sessions with one click.

$$E\_r = 1 \quad and \quad A\_r = 1 \Leftrightarrow C\_r = 1 $$
$$P(A\_r=1) = \alpha\_{u\_r q} $$
$$P(E\_1=1) = 1 $$
$$P(E\_r=1|E\_{r-1}=0) = 0 $$
$$P(E\_r=1|C\_{r-1}=1) = 0 $$
$$P(E\_r=1|E\_{r-1}=1, C\_{r-1}=0) = 1$$

###User Browsing Model (UBM)
<img src='http://lixinzhang.github.io/image/UBM.png'></img>

UBM is an extension of PBM model that has some elements of the cascade model. UBM take previous clicks into account.
$$P(E\_r=1|C\_1=c\_1,\cdots,C\_{r-1}=c\_{r-1}) = \gamma\_{rr^{'}} $$
$$r^{'} = max\\{k \in {0,\cdots, r-1},c\_k=1 \\}$$
The probability of user’s examination is related with both the last clicking position and the distance from that position.


###Dependent Click Model (DCM)
<img src='http://lixinzhang.github.io/image/DCM.png'></img>
DCM is an extension of the cascade model that handle sessions with multiple clicks. User has probability $$$\lambda\_{r}$$$ to continue after clicking a result.
$$P(E\_r=1|C\_{r-1} = 1) = \lambda\_{r} $$
$$P(S\_r=1|C\_r=0) = 0 $$
$$P(S\_r=1|C\_r=1) = 1 - \lambda\_r $$
$$P(E\_r=1|S\_{r-1}=1) = 0 $$
$$P(E\_r=1|E\_{r-1}=1, S\_{r-1}=0) = 1$$

###Click Chain Model (CCM)
<img src='http://lixinzhang.github.io/image/CCM.png'></img>

CCM introduces a parameter to handle the situation where a user may abandon the search without clicking on the result. Continuation parameter depends on relevance $$$\alpha\_{uq}$$$. A strong assumption: perceived relevance(感知相关性) equals to actual relevance(实际相关性).

$$P(E\_r=1|E\_{r-1}=1, C\_{r-1}=0) = \tau\_1 $$
$$P(E\_r=1|C\_{c-1}=1) = \tau\_2(1-\alpha\_{u\_{r-1}q}) + \tau\_3\alpha\_{u\_{r-1}q} $$
$$P(S\_r=1|C\_r=0) = 0 $$
$$P(S\_r=1|C\_r=1) = \alpha\_{u\_{rq}} $$
$$P(E\_r=1|E\_{r-1}=1,S\_{r-1}=0) = \tau\_2 $$
$$P(E\_r=1|E\_{r-1}=1,S\_{r-1}=1) = \tau\_3 $$

###Dynamic Bayesian Network Model (DBN)
<img src='http://lixinzhang.github.io/image/DBN.png'></img>

DBN assumes that the user's perseverance after a click depends not on the perceived $$$\alpha\_{uq}$$$ but on the actual relevance $$$\sigma\_{uq}$$$. Parameter $$$\gamma$$$ is the continuation probability for a user that either did not click on a document or clicked but was not satisfied by it.

$$E\_r = 1 \quad and \quad A\_r = 1 \Leftrightarrow C\_r = 1 $$
$$P(A\_r=1) = \alpha\_{u\_r q} $$
$$P(E\_1=1) = 1 $$
$$P(E\_r=1|E\_{r-1}=0) = 0 $$
$$P(S\_r=1|C\_r=1) = \sigma\_{u\_rq} $$
$$P(E\_r=1|S\_{r-1}=1) = 0 $$
$$P(E\_r=1|E\_{r-1}=1, S\_{r-1}=0) = \gamma$$

**Simplified DBN model (SDBN) :  $$$\gamma = 1$$$**

###Evaluation & Comparison

<img src='http://lixinzhang.github.io/image/cmp.png'></img>

**Perplexity** shows how well a click model can predict user clicks in a query session when previous clicks and skips in that session are not known.

**Log-likelihood** is widely used to measure model fitness. It shows how well a model approximates the observed data.

## Click Probabilities

### Click Probabilities
We pay more attention on $$$P(C_u=1)$$$ and $$$P(C_u=1, C\_{<r\_u})$$$.

**RCM, RCTR, DCTR, PBM**
$$P(C_u=1, C_{<r_i}) = P(C_u=1)$$

**PBM**
$$P(C_u=1)=P(A_u=1) \cdot P(E\_{r\_u}=1) = \alpha\_{uq}\gamma\_{r\_u}$$


**CM, DCM, CCM, DBN, SDBN**
$$P(C\_u=1) = P(C\_u=1|E\_{r\_u}=1) \cdot P(E\_{r\_u}=1) = \alpha\_{uq} \epsilon\_{r\_u}$$
$$$P(E\_{r\_u}) = \epsilon\_{r\_u}$$$ is the main difference between different models.

## Parameter Estimation

**Click Model:**

*  Set of events/random variables.
*  Set of dependencies between these events.
*  Set of the model’s parameters.

**Parameter estimation methods:**

*  Maximum likelihood estimation.
*  Expectation maximization.

**Click Model** & **estimation method** & **parameters** 

| Click Model | Estimation method | Parameters |
| ------------ | ------------- | ------------ |
|RCM | MLE | $$$\rho$$$ |
|RCTR | MLE | $$$\rho\_r$$$ |
|DCTR | MLE | $$$\rho\_{uq}$$$ |
|PBM | EM | $$$\alpha\_{uq}$$$,$$$\gamma\_r$$$ |
|CM | MLE | $$$\alpha\_{uq}$$$ |
|UBM | EM | $$$\alpha\_{uq}$$$,$$$\gamma\_{rr^{'}}$$$ |
|SDCM | MLE | $$$\alpha\_{uq}$$$,$$$\lambda\_r$$$  |
|CCM | EM | $$$\alpha\_{uq}$$$, $$$\tau\_1$$$, $$$\tau\_2$$$, $$$\tau\_3$$$ |
|DBN | EM | $$$\alpha\_{uq}$$$, $$$\sigma\_{uq}$$$, $$$\gamma$$$ |
|SDBN | MLE | $$$\alpha\_{uq}$$$ |

##  Advanced Click Models

*  Aggregated search, a SERP aggregates results from multiple sources known as verticals(e.g. News, Image, or video verticals). **Presentaion bias problem**s.
*  Beyond a single query session, from query session to task session.
*  Non-sequential examination problem, a click model incorporating revisiting behaviors.
*  Featured based CTR prediction, similar to ctr prediction for online advertising.

##  Application for search ranking, DBN in Yahoo! 2009

*  Predicting click-through rate, predict CTR at position 1.
*  Predicted relevance as a ranking feature, as a ranking signals.
    $$r\_{uq} = P(S\_i=1|E\_i=1)$$
    $$r\_{uq} = P(S\_i=1|C\_i=1)P(C\_i=1|E\_i=1)$$
    $$r\_{uq} = \alpha\_{uq} \lambda\_{uq}$$
*  Learning a ranking function with predicted relevance. 
*  **Learning to rank**:rank documents based on supervised machine learning.
    *  point-wise
    *  pair-wise
    *  list-wise

##  Reference
* Chuklin, /A/, Markov, /I/, de Rijke, M. Click Models for Web Search[M]// Morgan & Claypool, 2015:115.
* Chapelle O, Zhang Y. A dynamic bayesian network click model for web search ranking[C]// Proceedings of the 18th international conference on World Wide Web ACM, 2009:1-10.
* Guo F, Liu C, Kannan A, et al. Click chain model in web search[J]. Proceedings of WWW, 2009:11-20.
* Code: [PyClick](https://github.com/markovi/PyClick)
