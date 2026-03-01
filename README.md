data-science-project 1
==============================

## 📌 Project Overview

This project explores clustering and data visualization techniques applied to social media sentiment analysis during the COVID-19 pandemic. The dataset contains five numerical emotional features extracted from Twitter comments — valence, fear, anger, happiness, and sadness — along with associated sentiment labels (negative, neutral, positive).

The objective is to investigate whether unsupervised learning methods can naturally recover the three sentiment trends using only the emotional features (without using the labels during clustering).

The project includes:

Exploratory data analysis through pairwise visualizations of feature distributions to understand relationships and antagonistic patterns between emotions.

K-Means clustering with model selection using Overlap and Silhouette scores to determine the optimal number of clusters.

Cluster evaluation using Precision, Recall, and F1-score by comparing discovered clusters to actual sentiment labels.

Hierarchical clustering (agglomerative or divisive) using Euclidean distance, dendrogram analysis, and different cut thresholds to analyze grouping behavior.

This project demonstrates practical implementation of clustering validation, performance evaluation, and visual interpretation of high-dimensional emotional data.

How to run the project
------------
Install the project dependencies by running the following command:
```bash
pip install -r requirements.txt
```

Project Organization
------------
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `visual_analyse.ipynb`.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │   └── distance.py
    │   │
    │   ├── features       <- Scripts to turn raw data into new features 
    │   │   └── features_selection.py
    │   │
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                              generated with `pip freeze > requirements.txt`


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
