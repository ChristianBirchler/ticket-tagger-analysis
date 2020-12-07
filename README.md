# Machine Learning Model Evaluations for GitHub Issue Classification

## Abstract
Issue labeling on large software projects is a time-consuming task. With classification models, it is feasible to automate this process. Ticket Tagger is a tool that enables issue labeling on GitHub with a fasttext classifier. In our project, we assess the evaluation of Ticket Tagger and compare it with other machine learning models. We collect issues of the pandas' open-source repository on GitHub and predict the labels. Different preprocessing techniques are applied and evaluated. Our results show that the preprocessing will affect the variability in the scores. With the right preprocessing technique it is possible to improve the current implementation of Ticket Tagger.

## Introduction
The maintenance of a software project depends on issues. Large projects get a high number of new issues every day. The developers need proper labeling of issues to treat them efficiently. Many projects still rely on manual labeling of issues. This circumstance is challenging in popular projects with few developers since the resources of manual labeling are limited. With machine learning techniques it is possible to automate this process. 

[Ticket Tagger](https://github.com/rafaelkallis/ticket-tagger/tree/master/src) is a machine learning-driven issue classification bot. It was written by [Rafael Kallis](https://github.com/rafaelkallis) in the scope of a project similar to this one. Once installed in a GitHub repository, Ticket Tagger offers the benefit of automatic issue classification. Small repositories may not gain much value from it, but larger ones do since they receive more issues per time unit.

In this project, we perform an empirical investigation of machine learning prediction strategies for issue types classification on GitHub. First, the data is extended with the data set from the pandas' repository. Then various preprocessing strategies (like stemming and stopword removal) are used on the pandas' data set to explore the possibilities of Ticket Tagger. And finally, all preprocessed and not preprocessed data sets are also evaluated in the [WEKA](https://www.cs.waikato.ac.nz/ml/weka/) and [MEKA](https://waikato.github.io/meka/) GUI, such that the results from the Ticket Tagger software can be referenced and compared to the results of similar software. All results represent the evaluation metrics 
of a 10-Fold [cross validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics)). More specifically, the F-Score is the main metric that is compared in this project.

## Experimental Design

>*RQ1*: To what extent can we increase Performance?

>*RQ2*: Which tools and changes have the biggest positive impact?

Tasks Overview:

* Extend the original study
    * Extend the original data set with another balanced real world data set
        * [Extract Issues Data](./scripts/README.md)
        * [Pandas Data Set](./datasets/README.md)
    * Extend the original ML pipeline
        * Compare our approach to other baseline approaches
            * [Convert our Data Sets to arff format for WEKA / MEKA](./scripts/README.md)
            * [arff data sets](./datasets/README.md)
        * Preprocessing with Ticket Tagger
            * [Preprocessing](./scripts/README.md)
            * [Preprocessed Data Sets](./datasets/README.md)
        * Multi binary label classification
            * [Multi Binary Scripts](./scripts/README.md)
            * [Multi Binary Data Sets](./datasets/README.md)


## Results
The results are listed below. Also, an additional [readme discussing some of the results](./results/README.md) can
be found in the results directory.

Ticket Tagger Classification Performances:

[*Data Set Comparison (F-Score)*](./results/original_vs_pandas.txt) | Fasttext
--- | ---
Rafael_partial_english_rebalanced | 0.687
Rafael_only_english_rebalanced | 0.550
Pandas_balanced | 0.781		

Ticket Tagger Multi Binary Classication Performances:

[*Multi Binary F-Score*](./results/MBL_pandas_benchmark.txt) | Multi Binary (Fasttext)
--- | ---
Pandas_balanced | 0.745

WEKA Multilabel Classification Performance:

[*Data Set Comparison (F-Score)*](./results/WEKA&MEKA_F-Scores.xlsx) | J48 | RandomForest | NaiveBayer | AdaBoost | LogitBoost
--- | --- | --- | --- | --- | ---
Rafael_partial_english_rebalanced | 0.581 | 0.661 | 0.638 | 0.625 | 0.616
Rafael_only_english_rebalanced | 0.559 | 0.68 | 0.576 | 0.649 | 0.64
Pandas_balanced | 0.817 | 0.816 | 0.551 | 0.825 | 0.824

[*Model Comparison (F-Score)*](./results/Comparison_models_weka.xlsx) | Pandas_Balanced
--- | --- 
RandomTree | 0.661
J48 | 0.817
Hoeffding Tree | 0.714
NaiveBayes | 0.638
lazy Ibk | 0.684
rules.decision table | 0.77
Logit Boost with Decision Stump | 0.824
AdaBoost with J48 | 0.825


MEKA (Binary Relevance Algorithm) with different Data Sets (comparable to multi binary algorithm of Ticket Tagger)

[*F-Score micro averaged*](./results/WEKA&MEKA_F-Scores.xlsx) | J48 | RandomForest | NaiveBayer 
--- | --- | --- | ---
Rafael_partial_english_rebalanced | 0.577 | 0.576 | 0.616
Rafael_only_english_rebalanced | 0.593 | 0.590 | 0.635 
Pandas_balanced | 0.793 | 0.801 | 0.679

[*F-Score macro averaged by example*](./results/WEKA&MEKA_F-Scores.xlsx) | J48 | RandomForest | NaiveBayer 
--- | --- | --- | ---
Rafael_partial_english_rebalanced | 0.505 | 0.465 | 0.607
Rafael_only_english_rebalanced | 0.533 | 0.476 | 0.626 
Pandas_balanced | 0.757 | 0.755 | 0.691

[*F-Score macro averaged by label*](./results/WEKA&MEKA_F-Scores.xlsx) | J48 | RandomForest | NaiveBayer 
--- | --- | --- | ---
Rafael_partial_english_rebalanced | 0.577 | 0.572 | 0.616
Rafael_only_english_rebalanced | 0.593 | 0.587 | 0.635 
Pandas_balanced | 0.793 | 0.800 | 0.681

Preprocessing the pandas data set for Ticket Tagger and WEKA/MEKA

*F-Score* (See: [[1]](./results/ticket-tagger-pandas.txt) [[2]](./results/Comparison_preprocessing_weka.xlsx)) | Fasttext | J48 | Logit Boost | Hoeffding Tree | NaiveBayes
--- | --- | --- | --- | --- | ---
data_set-pandas-balanded | 0.759 | 0.799 | 0.824 | 0.732 | 0.645
data_set-pandas-balanded-porter | 0.732 | 0.748 | 0.810 | 0.759 | 0.643
data_set-pandas-balanded-porter-stopword | 0.779 | 0.790 | 0.810 | 0.755 | 0.635
data_set-pandas-balanded-PTB | 0.660 | 0.798 | 0.817 | 0.75 | 0.654
data_set-pandas-balanded-PTB-stopword | 0.774 | 0.81 | 0.822  | 0.751 | 0.647
data_set-pandas-balanded-PTB-stopword-porter | 0.768 | 0.792 | 0.811 | 0.743 | 0.637
data_set-pandas-balanded-PTB-stopword-snowball | 0.767 | 0.785 | 0.813 | 0.74 | 0.637
data_set-pandas-balanded-snowball | 0.765 | 0.789 | 0.812  | 0.754 | 0.642
data_set-pandas-balanded-snowball-stopword | 0.744 | 0.792 | 0.813 | 0.751 | 0.632
data_set-pandas-balanded-stopword | 0.742 | 0.814 | 0.823 | 0.762 | 0.647
data_set-pandas-balanded-stopword-porter | 0.775 | 0.789 | 0.810  | 0.757 | 0.639
data_set-pandas-balanded-stopword-snowball | 0.787 | 0.784 | 0.813 | 0.758 | 0.638


## Discussion
- interpretations: what do the results mean?
- implications: why do the results matter?
- limitations: what can't the results tell us?
- recommendations: what practical actions or scientific studies should follow?


## Conclusion

