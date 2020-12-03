# Data Acquisition

## Introduction
In this folder resides a collection of scripts to facilitate the process of data acquisition. 
The idea is to first use the `dump_issues` script to scrape GitHub for issues and get a json file.
In order to translate this json dump into a fasttext data format, use the `json2fasttext` script. 
If you need to split this dataset into a binary dataset, translate any multi-label fasttext data with the help of the `create_binary_datasets` script.

## Usage

 ### [Github Scraper](dump_issues.py)

 >Make Sure to edit the variables `username` and `token` in the script to match your GitHub API credentials before using the script, as it will not work otherwise.
        
    python dump_issues.py <OWNER_NAME> <REPO_NAME>

### [Fasttext Converter](json2fasttext.py)

    python json2fasttext.py <INPUT.json> <OUTPUT.txt>

        
### [Binary Data Set Splitter](create_binary_datasets.py)

    python create_binary_datasets.py <INPUT.json> <OUTPUT.txt>

