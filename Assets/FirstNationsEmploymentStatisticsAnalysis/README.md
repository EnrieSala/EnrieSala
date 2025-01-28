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

## Database Structure
The projects use two main datasets:
genderbands: Contains labor force statistics and geographical data
genderpop: Contains population data broken down by gender and residence status

## Installation and Setup
### Requirements
- R (version 4.0.0 or higher)
- Required R packages: (tidyverse,ggplot2,GGally,pheatmap,DMwR2)

### Instructions
1. Clone the repository
2. Set up the R environment with required packages
3. Update file paths in the R scripts to match your local directory structure
4. Run the ETL pipeline script (Project1ETLPipelinewithGender.Rmd)
5. Run the EDA script (Project2SalaEnrie.Rmd)


## Output
Processed datasets 'indigenousbandsgender.csv' and 'indigenousbandsgender2.csv' to ensure optimal join results for complete data handling 

### Visualizations:
The visualizations produced by the analysis include: 
- Distribution and box plots, histograms 
- Correlation matrices of numeric variables 
- Stacked and proportional bar charts
- Population distribution by band and employment status heatmap
  
## Project Drawbacks
- Limited to a 20 km² area of interest
- Reliance on most recent available data, which may not capture seasonal variations
- Potential for data quality issues in source datasets

## To Do
- Expand the dataset to include more recent years
- Implement advanced statistical modeling techniques
- Create interactive visualizations using Shiny
- Perform comparative analysis with non-Indigenous population data
