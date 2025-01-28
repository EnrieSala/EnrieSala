# Landsat Image Enhancement Project
## Overview
This project focuses on creating and comparing two enhanced Landsat composites using PCI Focus: a standard enhancement and a custom enhancement emphasizing specific land cover types or features. The goal is to improve the interpretability and analysis of remotely sensed imagery for various applications.

## Features
- Download and preparation of Landsat imagery
- Creation of standard enhanced composite
- Development of custom enhanced composite for specific land cover types
- Comparison of enhancement techniques
- Image interpretation and analysis

## Database Structure
- The project uses Landsat imagery stored in PIX file format which includes an unenhanced clipped composite, standard enhanced clipped composite
and a custom enhanced clipped composite
- Each PIX file contains 3 bands used for the composite (e.g., Blue, Green, Red, NIR).

## Installation and Setup
### Prerequisites
- PCI Geomatica Focus
- USGS Earth Explorer account

## Instructions
1. Download Landsat imagery from USGS Earth Explorer
2. Import imagery into PCI Geomatica Focus
3. Perform atmospheric correction (if necessary)
4. Clip the image to the area of interest (~30km x 30km)
5. Rename bands for easier identification
6. Create standard enhanced composite
7. Develop custom enhanced composite
8. Export enhanced composites as separate PIX files

## Usage
- Open PIX files in PCI Geomatica Focus or ArcMap
- Compare standard and custom enhancements
- Analyze improvements in feature identification and interpretation
- Use enhanced images for further remote sensing applications

## Sample Output
- True color image of the study area
- Standard enhanced composite image
- Custom enhanced composite image

## To Do
- Implement regular data updates using the latest Landsat imagery
- Explore enhancement techniques for different sensors (e.g., Sentinel-2)
- Develop automated scripts for batch processing of image enhancements
- Create a web-based interface for easy comparison of enhancement techniques
- Integrate machine learning algorithms for optimized custom enhancements
