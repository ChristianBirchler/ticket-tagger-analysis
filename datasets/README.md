# Data

### WEKA Data Set

Located in the WEKA_Data_Set directory.
The data sets have their origin in the data sets that were used for
fasttext. First the data sets in fasttext format were converted to 
arff format with our converter script (LINK MULTILABEL CONVERTER). Then
a StringToWordVector filter (provided from WEKA GUI) was applied. 


### MEKA Data Set

Located in the MEKA_Data_Set_BinaryRelevance directory.
The data sets have their origin in the data sets that were used for
fasttext. First the data sets in fasttext format were converted to 
arff format with our converter script (LINK BR CONVERTER). Then
a StringToWordVector filter (provided from MEKA GUI) was applied. 

Note:   The MEKA data sets are different compared to the WEKA data sets in this case, because 
the MEKA GUI will only return the correct evaluation metrics if the data set corresponds to the
binary relevance strategy.

