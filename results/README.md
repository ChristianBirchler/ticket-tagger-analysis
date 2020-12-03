# Results

### Title 1



### Title 2


### Title 3 




### Comparison WEKA

WEKA (Waikato Environment for Knowledge Analysis) is a software developed by the University of Waikato in New Zealand.
It is a free software licensed under the GNU General Public License, and the companion to the book 'Data Mining: Practical Machine Learning Tools and Techniques'.
WEKA supports several data mining tasks, such as data preprocessing and classification. In the scope of this project,
WEKA is used for multilabel classification by using various models (J48, RandomForest, NaivaBayes). Finally the evaluation 
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







### Comparison MEKA 

The MEKA project provides an open source implementation of methods for multi-label learning and evaluation.
In multi-label classification, we want to predict multiple output variables for each input instance. 
This different from the 'standard' case (binary, or multi-class classification) which involves only a
single target variable. MEKA is based on the WEKA Machine Learning Toolkit; it includes dozens of multi-label
methods from the scientific literature, as well as a wrapper to the related MULAN framework.

For every evaluation, the WEKA default configuration for 10-fold Cross Validation was used.

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
