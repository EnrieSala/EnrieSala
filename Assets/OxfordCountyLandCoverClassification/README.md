# Oxford County Land Cover Classification
## Overview
This project focuses on unsupervised land cover classification to determine the types of land cover present in Oxford County, Nova Scotia.

## Features
- Area of Interest (AOI) selection (20 km²)
- Sentinel 2 imagery processing (10m RGBN bands)
- CCRS land cover dataset clipping
- Schema creation based on CCRS land cover classes
- Reference point generation (200 stratified random points)
- Object-Based Image Analysis (OBIA) classification
- Accuracy assessment and comparison

## Requirements
- ArcGIS Pro software (Training Samples Manager tool Classification Wizard tool) 
- Access to Copernicus Browser for Sentinel 2 imagery download
- CCRS 2020 Land Cover of Canada dataset

## Output
The OBIA classification results will produce a land cover map of the 20 km² Area of Interest, categorizing the landscape into various classes such as:
- Temperate or sub-polar needleleaf forest
- Sub-polar taiga needleleaf forest
- Temperate or sub-polar broadleaf deciduous forest
- Wetland
- Cropland
- Urban areas
- Water bodies
- Snow and ice

## Project Drawbacks
Some drawbacks of this classification include it's limitation to a 20 km² area (may not be representative of larger regions). It also relies on the most recent Sentinel 2 image, which might not capture seasonal variations. Additionally, the accuracy is dependent on the quality of the reference points and visual interpretation.

## Improvements
- Explore additional Sentinel 2 bands to enhance classification accuracy
- Increase the number of reference points to improve reliability 
- Experiment with different segmentation parameters for optimal classification results 
- Utilize cross-validation for more robust accuracy assessment
- Create a semi-automated workflow to improve data processing
