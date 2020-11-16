# Stemming
Stem words of issues by using the following scripts (porter and snowball stemming):
```
$ ./porter_stemming.py input_data.txt output_data.txt
$ ./snowball_stemming.py input_data.txt output_data.txt
```

# Create datasets for multilabel classification
If you use the following script:
```
$ ./create_binary_datasets.py input_data.txt
```
It will generate 3 new files with the prefixes `BUG`, `ENHANCEMENT` and `QUESTION`. These files contain only binary labels according to the prefix.
