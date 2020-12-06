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

* Extend the the original study
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
            
            
The [results](./results/README.md) are collected in the results directory.
