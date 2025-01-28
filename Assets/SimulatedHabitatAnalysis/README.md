
# Forest Stand Suitability Script

## Overview
ForestStandSuitability is a Python script designed for QGIS that analyzes and categorizes forest stands based on their suitability as North Mountain Cougar habitat. The script uses data from the Nova Scotia Department of Natural Resources (NSDNR) forestry dataset.

## Features
Analyzes forest stands based on leading species and calculates habitat suitability using three criteria:
* Average Tree Diameter (AVDI), Forest Stand Average Tree Height (HEIGHT), Cover Type (COVER_TYPE)
* Generates a summary report of low, medium, and high suitability areas
* Allows for multiple analyses with different leading species

## Data Structure
The script works with a QGIS layer containing forest stand data. 
Key attributes include:
- SP1: Species code
- AVDI: Average tree diameter
- HEIGHT: Average tree height
- COVER_TYPE: Forest cover type
- SHAPE_Area: Polygon area

## Sample Queries
The script performs the following main operations:
- Retrieves unique species from the SP1 field
- Filters polygons based on user-selected species
- Calculates suitability ratings based on AVDI, HEIGHT, and COVER_TYPE
- Summarizes polygon counts and areas for each suitability category

## Installation and Setup
### Prerequisites
- QGIS 3.x with Python 3.x support
- Access to NSDNR forestry dataset

## Instructions
1. Open QGIS and load the forestry shapefile
2. Ensure the forestry layer is active (selected) in QGIS
3. Open the Python Console in QGIS
4. Copy the script into the Python Console or load it from a file

## Usage
1. Load the NSDNR forestry dataset into QGIS and ensure it's the active layer.
2. Run the script from the QGIS Python console.
3. Select a leading species from the provided list.
4. Review the generated suitability report.
5. Choose to run the analysis again with a different species or exit.

Sample Output
===================================================================
                North Mountain Cougar Habitat Suitability Analysis
                         5 of SP Polygons in Study Area.
===================================================================
Low Suitability:
                                - Number of polygons :           2
                                - Minimum polygon area:        100.000
                                - Maximum polygon area:        200.000
                                - Total area :        300.000
                                - Average polygon area:        150.000

Medium Suitability:
                                - Number of polygons :           2
                                - Minimum polygon area:        150.000
                                - Maximum polygon area:        250.000
                                - Total area :        400.000
                                - Average polygon area:        200.000

High Suitability:
                                - Number of polygons :           1
                                - Minimum polygon area:        300.000
                                - Maximum polygon area:        300.000
                                - Total area :        300.000
                                - Average polygon area:        300.000

===================================================================

## Script Drawbacks 
- Limited error handling for unexpected inputs or missing data
- Hard-coded values for suitability ratings, which may not be suitable for all forest types
- Lack of visualization features for the results
- Potential performance issues with large datasets due to multiple iterations through features
- The script is designed for a single species at a time

To Do
- Implement error handling for edge cases
- Add data validation for input forestry dataset
- Create a graphical user interface for easier interaction
- Extend analysis to include additional habitat factors
- Export report data into a csv or .txt file
- Optimize performance for large datasets
- Add visualization of results on the QGIS map canvas

