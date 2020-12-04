# Results

### Overview

The content of this directory:

- Comparison_models_weka.xlsx
    - The results of comparing various models in WEKA with the balanced pandas data set.
- Comparing_preprocessing_weka.xlsx
    - The results of comparing various models in WEKA with mutliple differently preprocessed data sets (balanced pandas data set)
- MBL_pandas_benchmark.csv
    - {insert description}
- MBL_pandas_benchmark.txt
    - {insert description}
- ML_pandas_benchmark.txt
    - {insert description}
- original_vs_pandas.txt
    - Here the ticket tagger results with data sets from two different repositories are compared
- Preprocessing_boxplot.png
    - Boxplot that shows F-Scores depending on the results of 'Comparing_preprocessing_weka.xlsx'
- Preprocessing_boxplot_wobayes.png
    - Boxplot that shows F-Scores depending on the results of 'Comparing_preprocessing_weka.xlsx' without the NaiveBayes model
- WEKA&MEKA_F-Scores.xlsx
    - The results of comparing different models in WEKA/MEKA with different data sets (and different repositories)

### Title 1



### Title 2


### Title 3 




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





