-- Programmer: Enrie Sala --
-- Program: Assignment 4 --
-- For: Darren  MacKinnon --
-- Class: Spatial Database Management --
-- Date: November 27th, 2024 --

--2.
-- Drop tables so that the script is re-runnable
DROP TABLE IF EXISTS facility;
DROP TABLE IF EXISTS river;
DROP TABLE IF EXISTS road;
DROP TABLE IF EXISTS forest;
DROP TABLE IF EXISTS foreststand;

-- load the PostGIS extension
DROP EXTENSION IF EXISTS postgis;
CREATE EXTENSION postgis;

-- check postgis version
-- SELECT postgis_full_version();

-- create tables 
-- i. facility
CREATE TABLE facility (
id SERIAL PRIMARY KEY,
name VARCHAR (30),
facilitycode VARCHAR(2)
);

--ii. river
CREATE TABLE river (
id SERIAL PRIMARY KEY,
name VARCHAR (30)
);

--iii. road
CREATE TABLE road (
id SERIAL PRIMARY KEY, 
name VARCHAR (30),
composition VARCHAR(2)
);

--iv. forest
CREATE TABLE forest (
id SERIAL PRIMARY KEY,
species VARCHAR(30)
);

--v. foreststand
CREATE TABLE foreststand (
id SERIAL PRIMARY KEY,
name VARCHAR(30)
);

-- Add Geometry Columns 
ALTER TABLE facility
ADD column geom GEOMETRY(POINT,0);
ALTER TABLE river
ADD column geom GEOMETRY(LINESTRING, 0);
ALTER TABLE road
ADD column geom GEOMETRY(LINESTRING, 0);
ALTER TABLE forest
ADD column geom GEOMETRY(POLYGON, 0);
ALTER TABLE foreststand
ADD column geom GEOMETRY(POLYGON, 0);

-- Populate tables with non-spatial data
-- Populating facility table with name and code values
INSERT INTO facility (name, facilitycode) VALUES
('Outlander', 'CG'),
('Treeview', 'CG'),
('River Rider', 'CG'),
('NorthEast office', 'OF'),
('Park Ranger', 'OF');

-- Populating river table names 
INSERT INTO river (name) VALUES
('Old Man River'),
('Annapolis River');

-- Populating road table with road names and composition
INSERT INTO road (name, composition) VALUES
('Bourbon Street', 'GR'),
('Old Clements Road', 'GR'),
('UpDown Road', 'GR'),
('ABC Road', 'PV'),
('Backwoods Road', 'PV'),
('NorthSouth Road', 'PV');

-- Populating foreststand names
INSERT INTO foreststand (name) VALUES
('Keji'),
('Spooky Old Forest');

-- Populating forest species
INSERT INTO forest (species) VALUES
('Ash'),
('Beech'),
('Cat Spruce'),
('Elm'),
('Mixed'),
('Oak'),
('Pine'),
('Spruce');

-- Populate geom columns
-- Update facility table to include geometry
UPDATE facility SET geom = ST_GeomFromText('POINT
(5 32)'
, 0)
WHERE name LIKE 'Outlander';
UPDATE facility SET geom = ST_GeomFromText('POINT
(10 16)'
, 0)
WHERE name LIKE 'Treeview';
UPDATE facility SET geom = ST_GeomFromText('POINT
(19 18)'
, 0)
WHERE name LIKE 'River Rider';
UPDATE facility SET geom = ST_GeomFromText('POINT
(22 28)'
, 0)
WHERE name LIKE 'NorthEast office';
UPDATE facility SET geom = ST_GeomFromText('POINT
(16 6)'
, 0)
WHERE name LIKE 'Park Ranger';


-- Update River table to include geometry
UPDATE river SET geom = ST_GeomFromText('LINESTRING
(11 3
,11 16
,4 35)'
, 0)
WHERE name LIKE 'Old Man River';
UPDATE river SET geom = ST_GeomFromText('LINESTRING
(17.5 5
,16 12
,19.5 17.5
,22.5 28
,19 36)'
, 0)
WHERE name LIKE 'Annapolis River';

-- Update Road table to inlude geometry
UPDATE road SET geom = ST_GeomFromText('LINESTRING
(9 3
,9 10
,5 21
,5 35)'
, 0)
WHERE name LIKE 'Bourbon Street';
UPDATE road SET geom = ST_GeomFromText('LINESTRING
(3 10
,11 22
,19 22
,19 36)'
, 0)
WHERE name LIKE 'Old Clements Road';
UPDATE road SET geom = ST_GeomFromText('LINESTRING
(26 5
,22 15
,23 26
,23 34)'
, 0)
WHERE name LIKE 'UpDown Road';
UPDATE road SET geom = ST_GeomFromText('LINESTRING
(23 5
,20 16
,6.5 20.5
,4 30)'
, 0)
WHERE name LIKE 'ABC Road';
UPDATE road SET geom = ST_GeomFromText('LINESTRING
(16 4
,15 11
,14 15
,14 26
,5 32)'
, 0)
WHERE name LIKE 'Backwoods Road';
UPDATE road SET geom = ST_GeomFromText('LINESTRING
(18.5 5
,18.5 9
,24.5 16.5
,24.5 33)'
, 0)
WHERE name LIKE 'NorthSouth Road';

-- Populate foreststand names;
UPDATE foreststand SET geom = ST_GeomFromText('POLYGON
((6 2
,1.5 8
,2 37
,19 37
,26.5 32
,26.5 2
,6 2))'
, 0)
WHERE name = 'Keji'; 
UPDATE foreststand SET geom = ST_GeomFromText('POLYGON
((13 5
,11 5
,7 6
,4 8
,2 10
,3 7
,6 4
,11 4
,13 5))'
, 0)
WHERE name = 'Spooky Old Forest';

-- Populate forest species;
UPDATE forest SET geom = ST_GeomFromText('POLYGON
((4 30
,4 35
,14 35
,4 30))'
, 0)
WHERE species = 'Cat Spruce';
UPDATE forest SET geom = ST_GeomFromText('POLYGON
((14 35
,19 36
,25 33
,26 32
,26 26
,20 23
,14 26
,14 35))'
, 0)
WHERE species = 'Spruce';
UPDATE forest SET geom = ST_GeomFromText('POLYGON
((9 20
,4 30
,14 35
,14 20
,9 20))'
, 0)
WHERE species = 'Ash';
UPDATE forest SET geom = ST_GeomFromText('POLYGON
((26 20
,26 26
,20 23
,17 24
,14 21
,14 15
,26 20))'
, 0)
WHERE species = 'Beech';
UPDATE forest SET geom = ST_GeomFromText('POLYGON
((26 12
,26 20
,14 15
,15 11
,13 5
,15 5
,26 12))'
, 0)
WHERE species = 'Oak';
UPDATE forest SET geom = ST_GeomFromText('POLYGON
((26 5
,26 12
,15 5
,26 5))'
, 0)
WHERE species ='Mixed';
UPDATE forest SET geom = ST_GeomFromText('POLYGON
((13 5
,15 11
,14 15
,14 20
,9 20
,10 18
,2 10
,13 5))'
, 0)
WHERE species = 'Elm';
UPDATE forest SET geom = ST_GeomFromText('POLYGON
((2 10
,4 30
,10 18
,2 10))'
, 0)
WHERE species = 'Pine';

-- Part B --
-- 1. What is the area of the largest stand? -- 
SELECT MAX(ST_Area(geom)) AS "Largest Stand Area"
FROM forest;

-- 2.  What is the area of the Beech stand? --
SELECT ST_Area(geom) AS "Beech Stand Area"
FROM forest
WHERE species = 'Beech';

-- 3. List the total length of roads, by composition (i.e., gravel and paved). --
SELECT composition AS "Road Composition", ROUND(SUM(ST_Length(geom)):: numeric, 2) AS "Total Road Length"
FROM road
GROUP BY composition;

-- 4. How long is the shortest road? 
SELECT ROUND(MIN(ST_Length(geom)):: numeric, 2) AS "Shortest Road Length"
FROM road;

-- 5. List the names of facilities within the Spruce stand. 
SELECT f.name AS "Facilities Within Spruce Stand"
FROM facility f
WHERE f.name IN (
	SELECT f.name
	FROM facility f, forest fs
	WHERE fs.species = 'Spruce'
	AND ST_Within(f.geom, fs.geom)
);

-- 6. List the stands that Old Man River crosses. 
-- Nested query
SELECT f.species AS "Stands that cross with Old Man River"
FROM forest f
WHERE f.species IN (
	SELECT f.species
	FROM forest f, river r
	WHERE r.name = 'Old Man River'
	AND ST_Crosses(f.geom, r.geom)
);

-- Returns the same results as above but uses JOIN syntax
SELECT f.species AS "Stands that cross with Old Man River"
FROM forest f
JOIN river r on ST_Crosses(r.geom, f.geom)
WHERE r.name = 'Old Man River';

-- 7. List the names of roads that cross rivers, and the rivers they cross. 
SELECT r.name AS "Road Names That Cross Rivers"
from road r
WHERE r.name IN (
	SELECT r.name
	FROM road r, river ri
	WHERE ST_Crosses(r.geom, ri. geom)
);

-- 8. What is the distance between the Treeview and the River Rider facilities?  
SELECT ROUND(ST_Distance(ftree.geom, friv.geom):: numeric, 2) AS "Distance Between Treeview and River Rider"
FROM facility ftree, facility friv
WHERE ftree.name = 'Treeview' AND friv.name = 'River Rider';

-- 9. What is the distance between the NorthEast Office and the Annapolis River? 
SELECT ROUND(ST_Distance(f.geom, r.geom):: numeric, 2) AS "Distance between the NorthEast Office and Annapolis River"
FROM facility f, river r
WHERE f.name = 'NorthEast office'AND r.name = 'Annapolis River';

-- Returns the same results as above but uses JOIN syntax
SELECT ROUND(ST_Distance(f.geom, r.geom)::numeric, 2) AS "Distance between the NorthEast Office and Annapolis River"
FROM facility f
JOIN river r ON r.name = 'Annapolis River'
WHERE f.name = 'NorthEast office';

-- 10. Which facilities are within 1 map unit of a road, and which road(s) are they close to?
SELECT DISTINCT f.name AS "Name of Facilities within 1 map unit of a road", r.name AS "Name of Roads"
FROM facility f
JOIN road r ON ST_DWithin(f.geom, r.geom, 1);

