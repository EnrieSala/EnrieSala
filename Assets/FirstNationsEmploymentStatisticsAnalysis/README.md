# Indigenous Labour Force Analysis Project
## Overview
This project contains two R Markdown (RMD) files that analyze labour force statistics and population data for Indigenous communities across Canada. The files are part of a two stage analysis project that includes data extraction, transformation, loading (ETL), and exploratory data analysis (EDA). It combines geographical data from First Nations' Locations with labour force statistics and gender-based population data to provide insights into employment patterns and demographic distributions within Indigenous communities.

1. `Project1ETLPipelinewithGender.Rmd`: This file contains the ETL process for preparing the dataset.
2. `Project2SalaEnrie.Rmd`: This file contains the exploratory data analysis of the prepared dataset.

## Features
- Data extraction and transformation from multiple CSV sources
- Geospatial component integration (Indigenous Band Locations)
- Gender-based labour force and population analysis
- Data cleaning and imputation techniques
- Exploratory Data Analysis (EDA) with visualizations

## Requirements
- R (version 4.0.0 or higher)
- Required R packages: (tidyverse,ggplot2,GGally,pheatmap,DMwR2)

## Usage
1. Clone the repository
2. Set up the R environment with required packages
3. Update file paths in the R scripts to match your local directory structure
4. Run the ETL pipeline script (Project1ETLPipelinewithGender.Rmd)
5. Run the EDA script (Project2SalaEnrie.Rmd)

## Data Processing Steps
Data Extraction
Load CSV files for First Nations' locations and labour force statistics
Filter and clean raw data
Data Transformation
Perform data type adjustments
Handle missing values using mode and KNN imputation
Create bins for rate variables
Merge datasets using left join
Data Loading
Create tidy datasets for analysis
Export processed data for EDA
Exploratory Data Analysis
Single Variable Numerical Analysis
Labour Count distribution
Population distribution by gender and location
Correlation Analysis
Examine relationships between Labour Count, Rate, and Population
Categorical Variable Analysis
Employment rate distributions
Gender and on/off reserve population proportions
Multiple Categorical Variable Analysis
Heatmap of population distribution by band and type

## Output
Processed datasets: 'indigenousbandsgender.csv' and 'indigenousbandsgender2.csv'
Visualizations:
Distribution plots
Correlation matrices
Boxplots
Stacked and proportional bar charts
Population distribution heatmap
Project Drawbacks
Limited to a 20 km² area of interest
Reliance on most recent available data, which may not capture seasonal variations
Potential for data quality issues in source datasets
## To Do
Implement automated cloud detection for Sentinel 2 image selection
Explore additional Sentinel 2 bands to enhance classification accuracy
Increase the number of reference points for improved statistical robustness
Develop an interactive web map to complement static visualizations
Implement version control for code and data products
