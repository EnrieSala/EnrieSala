# First Nations Employment Statistics Analysis Based on Gender 
This repository contains two R Markdown (RMD) files that focus on analyzing indigenous population and labour force data in Canada
including gender as a dimension. The files are part of a two stage analysis project that includes data extraction,
transformation, loading (ETL), and exploratory data analysis (EDA).
1. `Project1ETLPipelinewithGender.Rmd`: This file contains the ETL process for preparing the dataset.
2. `Project2SalaEnrie.Rmd`: This file contains the exploratory data analysis of the prepared dataset.

Both files use R r to process, analyze data and ccreate visuals using data from Statistics Canada.
This analysis perovides insights into Indigenous employment, population distribution, and related socieconomic
factors. 

## Requirements
R and RStudio
Required R packages: tidyverse, ggplot2, GGally, pheatmap, DMwR2
## Usage
Open the .Rmd files in RStudio and run the code chunks sequentially to reproduce the analysis.

# README for Project1ETLPipelineSalaEnrie.Rmd
This R Markdown file contains the Extract, Transform, Load (ETL) process for analyzing Indigenous labor force data in Canada.

## Data Sources
Data sources include: First Nations' Locations CSV and membership in a First Nation or Indian band by labour force status: Canada, provinces and territories CSV. 

## Key Features
Data extraction from CSV files
Data cleaning and transformation
Handling of missing values using mode and KNN imputation
Merging of datasets
Creation of categorical variables through binning
Main Functions
get_mode(): Calculates the mode of a column
Data type adjustments and conversions
Row and column selections
Data joining using left_join()
Output
A cleaned and transformed dataset combining geographical and labor force data for Indigenous communities.

# README for Project2SalaEnrie.Rmd
Exploratory Data Analysis of Indigenous Labor Force and Population Data
This R Markdown file contains the Exploratory Data Analysis (EDA) of the dataset created in Project 1, with additional gender-based labor force statistics.
## Data Sources
Processed data from Project 1
Additional gender-based labor force statistics
## Key Analyses
Single Variable Numerical Analysis
Labor Count Analysis
Population Analysis
Correlation Analysis (Numeric Variables)
Single Categorical Variable Analysis
Multiple Categorical Variable Analysis
Visualizations
Density plots and histograms
Box plots
Scatter plots
Correlation matrices
Heatmaps
## Key Findings
Employment rates and challenges in Indigenous communities
Gender differences in population distribution
On-reserve vs. off-reserve population patterns
Geographical variations in labor force participation
The analysis provides insights into labor force participation and population distribution patterns in Indigenous communities across Canada.
