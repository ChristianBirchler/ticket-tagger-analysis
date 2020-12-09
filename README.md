# Machine Learning Model Evaluations for GitHub Issue Classification



## Collaborators
> Insert some Pictures PLS

`Tim Moser` | `David Steiger` | `Christian Birchler` | `Lara Fried` | Sebastiano Panichella | Rafael Kallis
--- | --- | --- | --- | --- | --- 
 | pic / link | pic / link | pic / link | pic / link | pic / link | pic / link

## Table of Contents
[Code Pipeline & Usage](./code-pipeline)  
[Data](./datasets)  
[Results & Discussion](./results)  
[Study Information](./study)

## Goal of Repository
Issue labeling on GitHub is usually done manually by the developers. In order to automate this process a tool name Ticket Tagger was developed. It classifies the issues on GitHub by a fasttest classifier. [Ticket Tagger](https://github.com/rafaelkallis/ticket-tagger/tree/master/src) is a machine learning-driven issue classification bot. It was written by [Rafael Kallis](https://github.com/rafaelkallis) in the scope of a project similar to this one. Once installed in a GitHub repository, Ticket Tagger offers the benefit of automatic issue classification. Small repositories may not gain much value from it, but larger ones do since they receive more issues per time unit.

[The paper by R. Kallis et al. (2019)](https://doi.org/10.1109/ICSME.2019.00070)   

### The main limitations of [Ticket Tagger](https://github.com/rafaelkallis/ticket-tagger/tree/master/src)
- It uses only the fasttext classifier developed by facebook
- The evaluation was done on issues of different repositories
- No preprocessing of the data was done
- The data sets used for training come from lots of different repositories by fetching data using [Google Big Query GitHub Archive](https://codelabs.developers.google.com/codelabs/bigquery-github#0)

### The main problems or questions we address in this repository 
>Can we increase the classification performance with different classifiers?

>What changes in the data have an impact on the classifications?

>Does using a single repository for machine learning increase prediction performance (We use [Pandas](https://github.com/pandas-dev/pandas) in our case)?

This repository contains all data, scripts and evaluations to explore those problems and questions.

## Extension Points  
### Extend the original data set with another balanced real world data set  
* [Extract Issues Data](./code-pipeline/README.md)
* [Pandas Data Set](./datasets/README.md)
### Extend the original ML pipeline
* Compare our approach to other baseline approaches
    * [Convert our Data Sets to arff format for WEKA / MEKA](./code-pipeline/README.md)
    * [arff data sets](./datasets/README.md)
* Preprocessing with Ticket Tagger
    * [Preprocessing](./code-pipeline/README.md)
    * [Preprocessed Data Sets](./datasets/README.md)
* Multi binary label classification
    * [Multi Binary Script](./code-pipeline/README.md)
    * [Multi Binary Data Sets](./datasets/README.md)

## Summary of Findings

- [Preprocessing](./code-pipeline/stemming) affects the performance considerably but introduced variance depending on method used
- Using the [Pandas](https://pandas.pydata.org/) repository for training and testing leads to higher performance when cross validating
- [Fasttext](https://fasttext.cc/) may not generate the best performing model when it comes to issue classification

> A more detailed description and discussion can be found in the [results folder](./results)



## References

 
- [Ticket Tagger: Machine Learning Driven Issue Classification](https://doi.org/10.1109/ICSME.2019.00070)  
- [Fasttext](https://fasttext.cc/)  
- [WEKA](https://www.cs.waikato.ac.nz/ml/weka/) & [MEKA](https://waikato.github.io/meka/)  
- [Pandas](https://pandas.pydata.org/)  

*A Project in the Context of the University of Zurich Course [Software Maintenance & Evolution](https://www.ifi.uzh.ch/en/seal/teaching/courses/sme.html)*

![UZH](https://www.uzh.ch/cmsssl/terrific/modules/Logo/img/uzh_logo_e_pos_web_main.jpg)



