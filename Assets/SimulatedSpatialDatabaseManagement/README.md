# State Park Spatial Database
## Overview
This project creates and manages a spatial database for a State Park using PostgreSQL with PostGIS extension. It demonstrates the use of spatial data types and queries to analyze geographical features within the park.
## Author
Enrie Sala
## Project Background
As a student in the Spatial Database Management class, I developed this project to apply spatial database concepts to a real-world scenario. The State Park database interested me because it combines various geographical elements (points, lines, and polygons) and allows for complex spatial queries that can aid in park management and planning.
## Features
Creates tables for facilities, rivers, roads, forests, and forest stands. Populates the database with sample data based on a provided map and performs spatial queries to analyze park features. 
## Database Structure
The database consists of five main tables:
facility (point features), river (line features), road (line features), forest (polygon features), foreststand (polygon features) Each table has a geometry column to store spatial data.
## Sample Queries
The script includes several spatial queries, such as:
Finding the area of the largest forest stand
Calculating the total length of roads by composition
Identifying facilities within specific forest stands
Determining distances between park features
Installation and Setup
Prerequisites
PostgreSQL with PostGIS extension installed
Instructions
Create a new PostgreSQL database
Enable the PostGIS extension in the database
Run the SQL script Assignment4SalaEnrieFinal.sql in your PostgreSQL environment
Usage
After running the script, you can execute the provided spatial queries or create your own to analyze the State Park data.
Sample Output
Here's an example of a query and its output:
sql
-- List the total length of roads, by composition
SELECT composition AS "Road Composition", 
       ROUND(SUM(ST_Length(geom))::numeric, 2) AS "Total Road Length"
FROM road
GROUP BY composition;
Output:
text
Road Composition | Total Road Length
------------------+-------------------
GR               | 123.45
PV               | 98.76
Known Issues
The spatial reference system used (0) is a simplified Cartesian coordinate system and may not accurately represent real-world geography.
To-Do
Add more complex spatial queries for advanced analysis
Implement a user interface for easier data visualization
Expand the database to include more park features (e.g., hiking trails, wildlife habitats)
Testing
Currently, there is no automated test suite. Manual testing can be performed by running the provided queries and verifying the results against the expected output based on the StatePark.pdf map.
