
WikipediaWebScrapinScript.[y: New Brunswick City Temperature Feature Class Creator
This script scrapes Wikipedia to extract climate data for major cities in New Brunswick, Canada, and generates an ArcGIS feature class containing city locations and monthly temperature statistics (Max, Mean, Min) for each city.

Author: Enrie Sala
Date: March 3, 2025

Overview
The script automates the creation of a spatial dataset (feature class) in ArcGIS containing:

City names and geographic coordinates (latitude, longitude)

Monthly maximum, mean, and minimum temperatures for each city

It does this by:

Scraping the list of New Brunswick cities from Wikipedia

Visiting each city's Wikipedia page to extract climate data and coordinates

Creating a point feature class in a specified geodatabase

Adding fields for each temperature statistic per month

Populating the feature class with the scraped data

Requirements
Python 3.x

ArcPy (ArcGIS Pro Python environment)

requests (pip install requests)

BeautifulSoup4 (pip install beautifulsoup4)

re (Python standard library)

urllib.parse (Python standard library)

Usage
Set Up Your Environment

Ensure you are running the script in an environment with ArcPy (typically the ArcGIS Pro Python environment).

Configure the Geodatabase Path

Update the GDB variable in the script to point to your target geodatabase:

python
GDB = r"C:\Path\To\Your\Geodatabase.gdb"
Run the Script

Execute the script directly:

bash
python Assignment5SalaEnrie.py
Result

A feature class named NB_ClimateData3 will be created in your geodatabase, containing a point for each city with associated temperature attributes.

Feature Class Schema
Field Name	Type	Description
City	Text	Name of the city
Jan_Max ...	Float	Max temperature for January (and so on)
Jan_Mean ...	Float	Mean temperature for January (and so on)
Jan_Min ...	Float	Min temperature for January (and so on)
...	...	... for each month (Feb, Mar, ..., Dec)
Geometry	Point	Longitude and latitude (WGS84, EPSG:4326)
How It Works
get_valid_cities(): Scrapes the Wikipedia page for the list of New Brunswick cities.

get_city_data(city): For each city, fetches its Wikipedia page, extracts coordinates and climate table data.

create_feature_class(): Sets up the ArcGIS feature class with fields for each temperature statistic per month.

main(): Orchestrates the workflow: creates the feature class, scrapes all cities, and inserts the data.

Error Handling
The script logs warnings if it cannot scrape a city or if temperature data is missing.

If a feature class with the same name exists, it will be deleted and recreated.

Any ArcGIS or scraping errors are reported using ArcPy's messaging system.

Notes
The script assumes Wikipedia pages for each city follow a standard structure and contain a climate table.

Some cities may be skipped if their Wikipedia page lacks the required data.

The script must be run in an environment with access to ArcPy and the specified geodatabase.
