# Simulated Lawrence Town Map Forest Stand Mapping Project
## Overview
This project involves creating a detailed map of the Lawrence Town area using ArcGIS Pro. The map combines various data sources, including road networks, forest cover, and points of interest, to produce a comprehensive visualization of the region.

## Project Background
The Lawrence Town Map is part of an assignment for the Fundamentals of GIS course. It demonstrates the application of GIS techniques, including data conversion, attribute management, and cartographic design principles.

## Features
Conversion of AutoCAD DXF road data to GeoDatabase feature classes
Integration of forest cover data with species classification
Custom-created points of interest
Basemap integration from Esri
Symbolization of forest types and road classifications
Stacked labeling for forest attributes
Comprehensive map elements (legend, scale bar, north arrow, etc.)
## Database Structure
The project utilizes a file GeoDatabase containing:
Roads feature class (converted from DXF)
Forest feature class (with species classification)
NonForest feature class (for non-tree habitats)
Points of Interest feature class (custom created)
Forest species lookup table
Sample Queries
While not explicitly shown, potential queries could include:
Selecting forest stands by dominant species
Calculating total road length by classification
Identifying points of interest within specific forest types
## Installation and Setup
### Prerequisites
ArcGIS Pro (latest version)
Access to Esri basemaps
Provided data files (asn2roads.dxf, utm20nad83.prj)
## Instructions
Create a new ArcGIS Pro project
Import the DXF road data into a new feature class
Add the Asn2Forest layer from the specified portal
Create a new feature class for points of interest
Set up definition queries for forest and non-forest areas
Apply appropriate symbolization and labeling
## Usage
Open the ArcGIS Pro project
Navigate to the Lawrence Town area
Adjust symbology and labels as needed
Use the layout view to arrange map elements
Export the final map as a 17x11 inch PDF
## Sample Output
The final output is a color-coded map showing:
Road network with classification-based symbolization
Forest areas colored by dominant species
Non-forest areas with distinct symbolization
Custom points of interest
Stacked labels for forest attributes
Complete map elements including legend, scale, and north arrow
## TODO
Refine forest species classification if needed
Add additional points of interest
Implement advanced geoprocessing analyses
Create a web map version for interactive use
Develop a story map to provide context for the Lawrence Town area
