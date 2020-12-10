# Data

## [WEKA Data Set](./weka_data_set)

Located in the WEKA_Data_Set directory.
The data sets have their origin in the data sets that were used for
fasttext. First the data sets in fasttext format were converted to 
arff format with our converter script (LINK MULTILABEL CONVERTER). Then
a StringToWordVector filter (provided from WEKA GUI) was applied. 


## [MEKA Data Set](./meka_data_set)

Located in the MEKA_Data_Set_BinaryRelevance directory.
The data sets have their origin in the data sets that were used for
fasttext. First the data sets in fasttext format were converted to 
arff format with our converter script (LINK BR CONVERTER). Then
a StringToWordVector filter (provided from MEKA GUI) was applied. 

Note:   The MEKA data sets are different compared to the WEKA data sets in this case, because 
the MEKA GUI will only return the correct evaluation metrics if the data set corresponds to the
binary relevance strategy.

## [Pandas](./data_set-pandas.txt)
The formatted data sets of the issues on the pandas' GitHub repository can be found here. One version is a [balanced](./data_set-pandas-balanced.txt) data set which is mainly used for our further usage.

#### **As of 12.10.2020 classified labels from pandas issues:**
- questions (33 - Question): 105
- enhancement (01 - Enhancement, 23 - Wish List): 1625
- bug (00 - Bug, 06 - Regression): 5170
- total: 6900
