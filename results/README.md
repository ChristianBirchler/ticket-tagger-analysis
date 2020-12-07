# Results

### Overview

Comparison_models_weka.xlsx 
- The results of comparing various models in WEKA with the balanced pandas data set.
    
Comparing_preprocessing_weka.xlsx 
- The results of comparing various models in WEKA with mutliple differently preprocessed data sets (balanced pa

MBL_pandas_benchmark.csv
- {insert description}

MBL_pandas_benchmark.txt
- {insert description}

ML_pandas_benchmark.txt
- {insert description}

original_vs_pandas.txt
- Here the ticket tagger results with data sets from two different repositories are compared

Preprocessing_boxplot.png
- Boxplot that shows F-Scores depending on the results of 'Comparing_preprocessing_weka.xlsx'

Preprocessing_boxplot_wobayes.png
- Boxplot that shows F-Scores depending on the results of 'Comparing_preprocessing_weka.xlsx' without the NaiveBayes model

WEKA&MEKA_F-Scores.xlsx
- The results of comparing different models in WEKA/MEKA with different data sets (and different repositories)


## WEKA

WEKA (Waikato Environment for Knowledge Analysis) is a software developed by the University of Waikato in New Zealand.
It is a free software licensed under the GNU General Public License, and the companion to the book 'Data Mining: Practical Machine Learning Tools and Techniques'.
WEKA supports several data mining tasks, such as data preprocessing and classification. In the scope of this project,
WEKA is used for multilabel classification by using various models (J48, RandomForest, NaivaBayes and more). Finally the evaluation 
with Boost Models (AdaBoost, LogitBoost) is also taken into account when comparing the TicketTagger results with WEKA results.

For every evaluation, the WEKA default configuration for 10-fold Cross Validation was used.

#### J48 

Classification Configuration: 
```
J48 -C 0.25 -M 2
```

#### RandomForest

Classification Configuration: 
```
RandomeForest -P 100 -I 100 -num-slots 1 -K 0 -M 1.0 -V 0.001 -S 1
```

#### NaiveBayes

Classification Configuration: none


#### AdaBoost (with J48)

Classification Configuration: 
```
AdaBoostM1 -P 100 -S1 -I 10- weka.classifiers.trees.J48 --C 0.25 -M 2
```

#### LogitBoost (with DecisionStump)

Classification Configuration: 
```
LogitBoost -P 100 -L-1.797…E308 -H 1.0 -Z3.0 -O1 -E1 -S1 -I 10 -W weka.classifiers.trees.DecisionStump
```







## MEKA (Binary Relevance)

The MEKA project provides an open source implementation of methods for multi-label learning and evaluation.
In multi-label classification, we want to predict multiple output variables for each input instance. 
This different from the 'standard' case (binary, or multi-class classification) which involves only a
single target variable. MEKA is based on the WEKA Machine Learning Toolkit; it includes dozens of multi-label
methods from the scientific literature, as well as a wrapper to the related MULAN framework. In this project,
we compare the multibinary results from fasttext and the binary relevance results from MEKA.

For every evaluation, the MEKA default configuration for 10-fold Cross Validation was used.

#### J48 

Classification Configuration: 
```
BR – W weka.classifier.trees.J48 -- -C 0.25 -M 2
```

#### RandomForest

Classification Configuration: 
```
BR – W weka.classifier.trees.RandomForest -- -I 100 -K 0 -S 1 -num-slots 1
```


#### NaiveBayes

Classification Configuration: none



## Comparison TicketTagger to WEKA and MEKA

We decided to compare the different models based on their F scores. In [this file](WEKA&MEKA_F-Scores.xlsx) we compared the three models J48, RandomForest and Naïve Bayes for three different datasets. We took the original dataset used for Ticket Tagger, an only English version of this dataset and a completely different dataset. 
 [Ticket Tagger](https://github.com/rafaelkallis/ticket-tagger) has an average F-Score of 0.826. Out of all the models we tested not one reached the 0.8 mark for this dataset. For the pandas dataset we tested we got better results, With Weka J48 and RandomForest as well as the Booster models AdaBoost and LogitBoost passed the 0.8 mark. With Binary Relevance in MEKA only RandomForest passed the 0.8 mark but J48 came close with up to 0.793. 
The best result with Rafaels original dataset we achieved with RandomForest in WEKA. 
The highest F-Score overall we got by using AdaBoost with  J48 on the Pandasdataset, this got us an F Score of 0.825. 
We tried if we would get better results by using preprocessed datasets: 
![Boxplot](Preprocessing_boxplot.png)
In this plot we can see the distribution of F-scores for each model if Preprocessing techniques are used. We used 12 different combinations of Preprocessing and ran them all for each model. In the above plot it can be observed that some of the models where more affected then others. The largest distribution happens while using J48. There we can see that with some Preprocessing the F-score can be pushed up to the same level as logitboost. If we look at our resulttable [this file](Comparison_preprocessing_weka.xlsx), the preprocessing method J48 performed the best with  is stopword.  For Logitboost preprocessing actually lowered the F-Score.  With Hoeffdingtree all Preprocessing did improve the F-Score, but here again the stopword preprocessing did the best. For the Naïve Bayes it was actually the PTB Preprocessing that improved the F-Score the most and some of the other methods even lowered the F-Score. 
Overall AdaBoost and Logitboost did produce the best F-Scores but they are also by far the slowest models. 




