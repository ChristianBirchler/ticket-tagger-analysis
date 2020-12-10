# Machine Learning Model Evaluations for GitHub Issue Classification



## Collaborators




<table style="width:100%; border-collapse:collapse; border: 0;">
  <tr>
    <td>
        <h3 align="center"><a href="https://github.com/TimDeanMoser">Tim Moser</a></h3>
    </td>
    <td>
        <h3 align="center"><a href="https://github.com/LeguDave">David Steiger</a></h3>
    </td>
    <td>
        <h3 align="center"><a href="https://github.com/ChristianBirchler">Christian Birchler</a></h3>
    </td>
    <td>
        <h3 align="center"><a href="https://github.com/LaraFr">Lara Fried</a></h3>
    </td>
    <td>
        <h3 align="center"><a href="https://github.com/spanichella">Sebastiano Panichella</a></h3>
    </td>
    <td>
        <h3 align="center"><a href="https://github.com/rafaelkallis">Rafael Kallis</a></h3>
    </td>
  </tr>
  <tr>
    <td>
        <a href="https://github.com/TimDeanMoser">
            <img src="https://avatars0.githubusercontent.com/u/56076095?s=460&u=b18b975c4570628eee4fa5d24439c384f1f70c6c&v=4" width="100%" />
        </a>
    </td>
    <td>
        <a href="https://github.com/LeguDave">
            <img src="https://avatars2.githubusercontent.com/u/55451472?s=460&u=0728bfc37d68f34357ac2825ae14a4af715c6ebd&v=4" width="100%" />
        </a>
    </td>
    <td>
        <a href="https://github.com/ChristianBirchler">
            <img src="https://avatars0.githubusercontent.com/u/33133633?s=460&u=0c04c3ba77c1a999f0d087646c38b4902a1c665a&v=4" width="100%" />
        </a>
    </td>
    <td>
        <a href="https://github.com/LaraFr">
            <img src="https://avatars3.githubusercontent.com/u/34027454?s=460&v=4" width="100%" />
        </a>
    </td>
    <td>
        <a href="https://github.com/spanichella">
            <img src="https://avatars1.githubusercontent.com/u/5339914?s=460&u=ea140c59718ae85b6b33fa97cabb4232a084f30a&v=4" width="100%" />
        </a>
    </td>
    <td>
        <a href="https://github.com/rafaelkallis">
            <img src="https://avatars3.githubusercontent.com/u/9661903?s=460&u=ae6e33f486ad0fed762cb7d8f1e07d4540130b27&v=4" width="100%" />
        </a>
    </td>
  </tr>
</table>


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



