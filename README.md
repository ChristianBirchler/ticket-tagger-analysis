# Introduction
This script crawls all issues (open and closed) of the provided user and repo. The data will be dumped to a text file in the same format as you reveive the data from the GitHub REST API.
# Usage
First you have to put your GitHub access token into the source code. Otherwise you have a bigger limitation for receiving the data.
```
python crawler.py <repo_owner> <repo>
python crawler.py numpy numpy
```
