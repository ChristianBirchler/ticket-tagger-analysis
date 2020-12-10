# Machine Learning Model Evaluations for GitHub Issue Classification

## Abstract
Issue labeling on large software projects is a time-consuming task. With classification models, it is feasible to automate this process. Ticket Tagger is a tool that enables issue labeling on GitHub with a fasttext classifier. In our project, we assess the evaluation of Ticket Tagger and compare it with other machine learning models. We collect issues of the pandas' open-source repository on GitHub and predict the labels. Different preprocessing techniques are applied and evaluated. Our results show that the preprocessing will affect the variability in the scores. With the right preprocessing technique it is possible to improve the current implementation of Ticket Tagger.

## Introduction
The maintenance of a software project depends on issues. Large projects get a high number of new issues every day. The developers need proper labeling of issues to treat them efficiently. Many projects still rely on manual labeling of issues. This circumstance is challenging in popular projects with few developers since the resources of manual labeling are limited. With machine learning techniques it is possible to automate this process. 

[Ticket Tagger](https://github.com/rafaelkallis/ticket-tagger/tree/master/src) is a machine learning-driven issue classification bot. It was written by [Rafael Kallis](https://github.com/rafaelkallis) in the scope of a project similar to this one. Once installed in a GitHub repository, Ticket Tagger offers the benefit of automatic issue classification. Small repositories may not gain much value from it, but larger ones do since they receive more issues per time unit.

In this project, we perform an empirical investigation of machine learning prediction strategies for issue types classification on GitHub. First, the data is extended with the data set from the pandas' repository. Then various preprocessing strategies (like stemming and stopword removal) are used on the pandas' data set to explore the possibilities of Ticket Tagger. And finally, all preprocessed and not preprocessed data sets are also evaluated in the [WEKA](https://www.cs.waikato.ac.nz/ml/weka/) and [MEKA](https://waikato.github.io/meka/) GUI, such that the results from the Ticket Tagger software can be referenced and compared to the results of similar software. All results represent the evaluation metrics 
of a 10-Fold [cross validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics)). More specifically, the F-Score is the main metric that is compared in this project.

## Study Methodology
Since our goal was to improve the performance of Ticket Tagger, the following research questions guided our project to reach that goal:

>*RQ1*: To what extent can we increase performance?

>*RQ2*: Which tools and changes have the biggest positive impact?

We provided separate README files with a detailed explanation of how we collected the data and performed the analysis. Below we provided an overview of tasks that are performed in our project.

Tasks Overview:

* Extend the original study
    * Extend the original data set with another balanced real world data set
        * [Extract Issues Data](./scripts/README.md)
        * [Pandas Data Set](./datasets/README.md)
    * Extend the original ML pipeline
        * Compare our approach to other baseline approaches
            * [Convert our Data Sets to arff format for WEKA / MEKA](./scripts/README.md)
            * [arff data sets](./datasets/README.md)
        * Preprocessing with Ticket Tagger
            * [Preprocessing](./scripts/README.md)
            * [Preprocessed Data Sets](./datasets/README.md)
        * Multi binary label classification
            * [Multi Binary Scripts](./scripts/README.md)
            * [Multi Binary Data Sets](./datasets/README.md)


## Results / Discussion
The results are listed below. Also, an additional [readme](../results/README.md) discussing some of the results can
be found in the results directory.


## Conclusion

