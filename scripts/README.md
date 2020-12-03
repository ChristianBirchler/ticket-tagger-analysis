# Introduction
This script crawls all issues (open and closed) of the provided user and repo. The data will be dumped to a text file in the same format as you reveive the data from the GitHub REST API.
# Usage
First you have to put your GitHub access token into the source code. Otherwise you have a bigger limitation for receiving the data.
```
python crawler.py <repo_owner> <repo>
python crawler.py numpy numpy
```

# Parser
Reads the 'numpy-numpy.json' file and outputs 'the data_set.txt' file in the format for the ticket tagger

As of 12.10.2020 classified labels:
questions (33 - Question): 105
enhancement (01 - Enhancement, 23 - Wish List): 1625
bug (00 - Bug, 06 - Regression): 5170
total: 6900



# How to aquire arff Data Sets

The script for converting fasttext format data sets into arff data sets can be found in the fastTextToArffConverter
directory. You can choose between multilabel arff data set for WEKA or binary relevance arff data sets for MEKA.
The multilabel converter creates an arff data set, in which exactly one label has to be classified
(either bug,enhancement or question). In the binary relevance converter, the label we used in WEKA is split up, such 
that each possiblity is its own label (0 or 1). Use the commands below in the directory of the converters. Finally, a 
StringToWordVector filter (found in the preprocessing section of the WEKA or MEKA GUI) must be applied to the 
output files, because this preprocessing step is not done automatically.

#### For Multilabel arff data set
```
python arffConverter_Multilabel.py ./inputfile.txt ./outputname.arff
```

#### For Binary Relevance arff data set
```
python arffConverter_BinaryRelevance.py ./inputfile.txt ./outputname.arff
```


