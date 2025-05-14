
# WikipediaWebScrapinScript.py: New Brunswick City Temperature Feature Class Creator
This script scrapes Wikipedia to extract climate data for major cities in New Brunswick, Canada, and generates an ArcGIS feature class containing city locations and monthly temperature statistics (Max, Mean, Min) for each city.

## Overview
The script automates the creation of a spatial dataset (feature class) in ArcGIS containing:
- City names and geographic coordinates (latitude, longitude)
- Monthly maximum, mean, and minimum temperatures for each city

Steps taken: 
1. Scraping the list of New Brunswick cities from Wikipedia
2. Visiting each city's Wikipedia page to extract climate data and coordinates
3. Creating a point feature class in a specified geodatabase
4. Adding fields for each temperature statistic per month
5. Populating the feature class with the scraped data

## Requirements
- Python 3.x
- ArcPy (ArcGIS Pro Python environment)
- requests (pip install requests)
- BeautifulSoup4 (pip install beautifulsoup4)
- re (Python standard library)
- urllib.parse (Python standard library)

## Usage
1. Set Up Your Environment
Ensure you are running the script in an environment with ArcPy (typically the ArcGIS Pro Python environment).
2. Configure the Geodatabase Path
Update the GDB variable in the script to point to your target geodatabase:
3. Run the Script

## Result
A feature class named NB_ClimateData3 will be created in your geodatabase, containing a point for each city with associated temperature attributes.

## How It Works
The script is organized into several key functions that together automate the process of creating a spatial dataset of New Brunswick city temperatures. The get_valid_cities() function scrapes the Wikipedia page listing New Brunswick cities to compile a list of valid city names. For each city, the get_city_data(city) function accesses its Wikipedia page, extracts geographic coordinates, and retrieves monthly climate data-including maximum, mean, and minimum temperatures-from the climate table. The create_feature_class() function sets up an ArcGIS feature class in the specified geodatabase, defining fields for each temperature statistic for every month, as well as the city name and spatial location. Finally, the main() function orchestrates the workflow by first creating the feature class, then scraping all city names, extracting their respective data, and inserting the compiled information into the feature class, resulting in a comprehensive spatial dataset of city temperature statistics.

## Error Handling
The script logs warnings if it cannot scrape a city or if temperature data is missing. If a feature class with the same name exists, it will be deleted and recreated. Any ArcGIS or scraping errors are reported using ArcPy's messaging system.

## Notes
The script assumes Wikipedia pages for each city follow a standard structure and contain a climate table.

Some cities may be skipped if their Wikipedia page lacks the required data.

The script must be run in an environment with access to ArcPy and the specified geodatabase.
