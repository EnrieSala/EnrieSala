# Simulated Lawrencetown Forest Stand Mapping Project
## Overview
This project involves creating a detailed map of the Lawrence Town area using ArcGIS Pro. The map combines various data sources, including road networks, forest cover, and points of interest, to produce a comprehensive visualization of the region.

## Features
- Conversion of AutoCAD DXF road data to GeoDatabase feature classes
- Integration of forest cover data with species classification
- Custom-created points of interest
- Basemap integration from Esri
- Symbolization of forest types and road classifications
- Stacked labeling for forest attributes
- Comprehensive map elements (legend, scale bar, north arrow, etc.)

## Database Structure
The project utilizes a file GeoDatabase containing:
- Roads feature class (converted from DXF)
- Forest feature class (with species classification)
- NonForest feature class (for non-tree habitats)
- Points of Interest feature class (custom created)
- Forest species lookup table

## Installation and Setup
### Prerequisites
ArcGIS Pro (latest version)
Access to Esri basemaps
Provided data files (asn2roads.dxf, utm20nad83.prj)

## Instructions
1. Create a new ArcGIS Pro project
2. Import the DXF road data into a new feature clas
3. Add the Asn2Forest layer from the specified portal
4. Create a new feature class for points of interest
5. Set up definition queries for forest and non-forest areas
6. Apply appropriate symbolization and labeling

## Sample Output
- The final output is a color-coded map showing:
- Road network with classification-based symbolization
- Forest areas colored by dominant species
- Non-forest areas with distinct symbolization
- Custom points of interest
- Stacked labels for forest attributes
- Complete map elements including legend, scale, and north arrow

## To Do 
- Add additional points of interest
- Create a web map version for interactive use
- Develop a story map to provide context for the Lawrencetown area
