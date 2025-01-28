# State Park Spatial Database

## Overview
This project creates and manages a spatial database for a State Park using PostgreSQL with PostGIS extension. It demonstrates the use of spatial data types and queries to analyze geographical features within the park.

## Features
Creates tables for facilities, rivers, roads, forests, and forest stands. Populates the database with sample data based on a provided map and performs spatial queries to analyze park features. 

## Database Structure
The database consists of five main tables:
facility (point features), river (line features), road (line features), forest (polygon features), foreststand (polygon features) Each table has a geometry column to store spatial data.

## Sample Queries
The script includes several spatial queries, such as:
- Finding the area of the largest forest stand
- Calculating the total length of roads by composition
- Identifying facilities within specific forest stands
- Determining distances between park features

## Installation and Setup
### Prerequisites
PostgreSQL with PostGIS extension installed

### Instructions
1. Create a new PostgreSQL database
2. Enable the PostGIS extension in the database
3. Run the SQL script Assignment4SalaEnrieFinal.sql in your PostgreSQL environment

### Sample Output
Here's an example of a query and its output:
-- List the total length of roads, by composition
SELECT composition AS "Road Composition", 
       ROUND(SUM(ST_Length(geom))::numeric, 2) AS "Total Road Length"
FROM road
GROUP BY composition;
Output:

Road Composition | Total Road Length

GR               | 123.45

PV               | 98.76

## To-Do
- Implement a user interface for easier data visualization
- Expand the database to include more park features (e.g., hiking trails, wildlife habitats)
- Convert the spatial reference system to accurately represent geographical features and measurements 
