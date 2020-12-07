# Project Introduction


Ticket Tagger is a machine learning driven issue classification bot. It was written by Rafael Kallis
in the scope of a project similar to this one. Once installed in your github repository, Ticket Tagger can
be used to gain the benefit of autmatic issue classification. Small repositories may not gain much value from it, but
once the repository grows to a point, where you get thousands of issues per day, an automatic issue classification bot
will become very helpful. 

In this project we perform an empirical investigation of machine learning prediction strategies for issue types 
classification on GitHub. First, the data is extended with the data set from the pandas repository. Then various preprocessing strategies (like stemming and stopword
removal) are used on the pandas data set in order to explore the possibilities of Ticket Tagger. And finally all preprocessed and 
unpreprocessed data sets are also evaluated in the WEKA and MEKA GUI, such that the results from the Ticket Tagger
software can be referenced and compared to the results of similar software. All results represent the evaluatlion metrics 
of a 10-Fold cross validation. More specifically, the F-Score is the main metric that is compared in this project.


RQ1: To what extent can we increase Performance?

RQ2: Which tools and changes have the biggest positive impact?

Task Overview:

* Extend the the original studys
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
            
            
[Results](./results/README.md):

Ticket Tagger Classification Performances (F-Score):

*F-Score* | Fasttext
--- | ---
Rafael_partial_english_rebalanced | 0.687
Rafael_only_english_rebalanced | 0.550
Pandas_balanced | 0.781		

Multi Binary Classication Performances (F-Score):

*F-Score* | Multi Binary (Fasttext)
--- | ---
Pandas_balanced | 0.745

WEKA Multilabel Classification Performance:

*Data Set Comparison (F-Score)* | J48 | RandomForest | NaiveBayer | AdaBoost | LogitBoost
--- | --- | --- | --- | --- | ---
Rafael_partial_english_rebalanced | 0.581 | 0.661 | 0.638 | 0.625 | 0.616
Rafael_only_english_rebalanced | 0.559 | 0.68 | 0.576 | 0.649 | 0.64
Rafael_only_english_rebalanced | 0.817 | 0.816 | 0.551 | 0.825 | 0.824

*Model Comparison (F-Score)* | Pandas_Balanced
--- | --- 
RandomTree | 0.661
J48 | 0.817
Hoeffding Tree | 0.714
NaiveBayes | 0.638
lazy Ibk | 0.684
rules.decision table | 0.77
Logit Boost with Decision Stump | 0.824
AdaBoost with J48 | 0.825


MEKA with Binary Releance (BR) 

*F-Score micro averaged* | J48 | RandomForest | NaiveBayer 
--- | --- | --- | ---
Rafael_partial_english_rebalanced | 0.577 | 0.576 | 0.616
Rafael_only_english_rebalanced | 0.593 | 0.590 | 0.635 
Rafael_only_english_rebalanced | 0.793 | 0.801 | 0.679

*F-Score macro averaged by example* | J48 | RandomForest | NaiveBayer 
--- | --- | --- | ---
Rafael_partial_english_rebalanced | 0.505 | 0.465 | 0.607
Rafael_only_english_rebalanced | 0.533 | 0.476 | 0.626 
Rafael_only_english_rebalanced | 0.757 | 0.755 | 0.691

*F-Score macro averaged by label* | J48 | RandomForest | NaiveBayer 
--- | --- | --- | ---
Rafael_partial_english_rebalanced | 0.577 | 0.572 | 0.616
Rafael_only_english_rebalanced | 0.593 | 0.587 | 0.635 
Rafael_only_english_rebalanced | 0.793 | 0.800 | 0.681

Preprocessing

*F-Score* | Fasttext | J48 | Logit Boost | Hoeffding Tree | NaiveBayes
--- | --- | --- | --- | --- | ---
data_set-pandas-balanded | 0.x | 0.799 | 0.824 | 0.732 | 0.645
data_set-pandas-balanded-porter | 0.x | 0.748 | 0.810 | 0.759 | 0.643
data_set-pandas-balanded-porter-stopword | 0.x | 0.790 | 0.810 | 0.755 | 0.635
data_set-pandas-balanded-PTB | 0.x | 0.798 | 0.817 | 0.75 | 0.654
data_set-pandas-balanded-PTB-stopword | 0.x | 0.81 | 0.822  | 0.751 | 0.647
data_set-pandas-balanded-PTB-stopword-porter | 0.x | 0.792 | 0.811 | 0.743 | 0.637
data_set-pandas-balanded-PTB-stopword-snowball | 0.x | 0.785 | 0.813 | 0.74 | 0.637
data_set-pandas-balanded-snowball | 0.x | 0.789 | 0.812  | 0.754 | 0.642
data_set-pandas-balanded-snowball-stopword | 0.x | 0.792 | 0.813 | 0.751 | 0.632
data_set-pandas-balanded-stopword | 0.x | 0.814 | 0.823 | 0.762 | 0.647
data_set-pandas-balanded-stopword-porter | 0.x | 0.789 | 0.810  | 0.757 | 0.639
data_set-pandas-balanded-stopword-snowball | 0.x | 0.784 | 0.813 | 0.758 | 0.638
