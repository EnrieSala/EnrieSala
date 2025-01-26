
# Forest Stand Suitability Script
## Overview
ForestStandSuitability is a Python script designed for QGIS that analyzes and categorizes forest stands based on their suitability as North Mountain Cougar habitat. The script uses data from the Nova Scotia Department of Natural Resources (NSDNR) forestry dataset.
## Features
Analyzes forest stands based on leading species
Calculates habitat suitability using three criteria:
* Average Tree Diameter (AVDI), Forest Stand Average Tree Height (HEIGHT), Cover Type (COVER_TYPE)
* Generates a summary report of low, medium, and high suitability areas
* Allows for multiple analyses with different leading species
## Requirements
QGIS with Python 3.x and NSDNR forestry dataset loaded as the active layer in QGIS
## Usage
1. Load the NSDNR forestry dataset into QGIS and ensure it's the active layer.
2. Run the script from the QGIS Python console.
3. Select a leading species from the provided list.
4. Review the generated suitability report.
5. Choose to run the analysis again with a different species or exit.
## Output
The script generates a formatted report displaying:
-  Number of polygons for each suitability category
- Minimum and maximum area of stands for each category
- Total area and average area of stands for each category
## Script Drawbacks 
- Limited error handling for unexpected inputs or missing data
- Hard-coded values for suitability ratings, which may not be suitable for all forest types
- Lack of visualization features for the results
- Potential performance issues with large datasets due to multiple iterations through features
- The script is designed for a single species at a time
