# Project Introduction


Ticket Tagger is a machine learning driven issue classification bot. It was written by Rafael Kallis
in the scope of a project similar to this one. Once installed in your github repository, Ticket Tagger can
be used to gain the benefit of autmatic issue classification. Small repositories may not gain much value from it, but
once the repository grows to a point, where you get thousands of issues per day, an automatic issue classification bot
will become very helpful. 

This project focusses on improving and validating the effectiveness of the Ticket Tagger software. First, the data is
extended with the data set from the pandas repository. Then various preprocessing strategies (like stemming and stopword
removal) are used on the pandas data set in order to explore the possibilities of Ticket Tagger. And finally all preprocessed and 
unpreprocessed data sets are also evaluated in the WEKA and MEKA GUI, such that the results from the Ticket Tagger
software can be referenced and compared to the results of similar software. All results represent the evaluatlion metrics 
of a 10-Fold cross validation. More specifically, the F-Score is the main metric that is compared in this project.


## Data Sets



## Preprocessing



## Comparison WEKA/MEKA