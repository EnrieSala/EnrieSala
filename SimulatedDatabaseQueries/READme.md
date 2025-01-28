# GPS Tracking System SQL Queries
## Overview
This project contains a set of SQL queries designed to extract and analyze data from a GPS tracking system database. The queries demonstrate various SQL techniques including single table queries, multiple table joins, outer joins, subqueries, aggregations, and group by clauses.

## Project Background
The database stores GPS tracking system data  used for monitoring vehicles and persons of interest. It includes information about GPS readings, vehicles, persons of interest (POIs), police officers, and projects.

## Features
- Single table queries for basic data retrieval and subqueries for advanced data filtering
- Multiple table joins for complex data relationships and outer joins to include all records from one table
- Aggregate functions for data summarization and group by clauses for data grouping and analysis

## Database Structure
- reading: Contains GPS readings with datetime, motion, speed, latitude, and longitude
- project: Stores information about projects including start dates
- poi: Persons of interest information
- vehicle: Vehicle details including make, model, and associated GPS
- gpsunit: GPS unit information
- rectype: Record type descriptions
- police: Police officer information
- projpolice: Linking table for projects and police officers

## Installation and Setup
### Prerequisites
- PostgreSQL database system
- Access to the provided Azure Cloud database

### Instructions
1. Ensure you have PostgreSQL client installed on your system
2. Connect to the Azure Cloud database using the provided credentials
3. Copy the SQL queries into your PostgreSQL client or a .sql file
4. Execute the queries one by one or run the entire script

## Sample Output
### Query 1
Date/Time of Vehicles in Motion on July 2004
-------------------------------------------
2004-07-01 00:00:15
2004-07-01 00:00:30
2004-07-01 00:00:45
...

## TODO
- Add error handling for queries
- Optimize queries for large datasets
- Create views for frequently used complex queries
- Implement stored procedures for common operations
- Add data visualization capabilities

