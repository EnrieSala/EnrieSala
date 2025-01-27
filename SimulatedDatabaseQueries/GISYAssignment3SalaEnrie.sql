------------------------------
-- Programmer: Enrie Sala ---- 
-- Program: Assignment 3 -----
-- For: Darren MacKinnon -----
------------------------------

-- Single table queries: 
-- 1. Display the date and time of readings that were in motion in July 2004, sorted by date and time. 
SELECT readdatetime AS "Date/Time of Vehicles in Motion on July 2004"
FROM reading
WHERE readdatetime >= '2004-07-01' AND readdatetime < '2004-08-01'
AND motion ='true'									
ORDER BY readdatetime;

-- 2. Display the reading ID and date and time for readings with a speed greater than 100, sorted by date and time. 
SELECT id AS "Reading ID for speeds > 100 km/h", readdatetime AS "ReadingDate/Time"
FROM reading
WHERE speed > 100
ORDER BY readdatetime;

-- 3. In 2006, show the names of projects that started in that year, sorted by date. 
SELECT name AS "Names of Projects Started in 2006"
FROM project
WHERE startdate >= '2006-01-01' and startdate < '2007-01-01'
ORDER BY startdate;

-- 4.In the city of Halifax, show the concatenated “Last, First” name of persons of interest, sorted by last then first POI name.
SELECT lastname || ',' || firstname AS "Halifax POI: Last Name, First Name"
FROM poi
WHERE city = 'Halifax'
ORDER BY lastname, firstname 

-- Multiple table queries: 
-- 5. List the concatenated “Last, First” name of persons of interest and their vehicle make and model associated with 
-- GPS serial number 254, sorted by last then first POI name.
SELECT p.lastname || ',' || p.firstname AS "POI Last Name, First Name",
       v.make AS "Vehicle Make associated with GPS serial 254",
       v.model AS "Vehicle Model"
FROM poi as p
JOIN vehicle v ON p.poiid = v.poiid
WHERE v.gps = '254'
ORDER BY p.lastname, p.firstname;

-- 6. List the concatenated ‘latitude, longitude’ for all readings in September 2004 (showing the date column) that 
-- contain ‘Call’ in their record type description, sorted by latitude. 
SELECT latitude ||','|| longitude AS "Coordinates of September 2004 Readings w/ 'Call' in desc."
FROM reading AS read
JOIN rectype AS rec ON read.recordtype = rec.rectypeid
WHERE readdatetime >= '2004-09-01' AND readdatetime < '2004-10-01'
AND rec.description LIKE '%Call%'
ORDER BY latitude;

-- 7. List the project name, and the concatenated “Last, First” name of persons of interest and police associated with the 
-- project, for all projects, sorted by project name.
SELECT name AS "Project Name",
	   p.lastname ||','|| p.firstname AS "Associated POI Last Name, First Name",
	   pol.lastname||','|| pol.firstname AS "Associated Police Last Name, First Name"
FROM project proj
JOIN poi p ON proj.poiid = p.poiid
JOIN projpolice ON proj.projectid = projpolice.prjpoliceid
JOIN police AS pol on projpolice.policeid = pol.policeid
ORDER BY proj.name;

-- Outer Join
-- 8: List all GPS units Models and Serial Numbers and any Vehicle VIN, 
-- Make and Model that they are/were attached to, sorted by GPS Serial Number.
SELECT serialnumber AS "GPS Serial", gps.model AS "GPS Model",
	   v.vin,v.model AS "Vehicle Model",v.make AS "Vehicle Make"
FROM   gpsunit AS gps
LEFT OUTER JOIN vehicle v on gps.serialnumber = v.gps
ORDER BY serialnumber;

-- Subquery: 
-- 9. How many readings were above the average speed, for readings that had a speed greater than 0?
SELECT speed as "Speed (km/h) of readings > 0 and above average speed of 39"
	FROM reading
	WHERE speed >
	(SELECT AVG(speed)
	FROM reading
	WHERE speed > 0);

-- Aggregate: 
-- 10. What are the extents of the readings – i.e. the maximum and minimum longitude and latitude of GPS FIX readings? 
SELECT MAX(latitude) AS "maximum latitude",MAX(longitude)AS "maximum longitude",
MIN(latitude) AS "minimum latitude", MIN(longitude) AS "minimum longitude"
FROM reading;

-- 11. List the average latitude and longitude for each record type. Rounded to the 5th decimal place to match
-- The precision of query 10. 
SELECT AVG(latitude)::numeric(10,5) AS "average latitude", 
AVG(longitude)::numeric(10,5) AS "average longitude", recordtype
FROM reading
GROUP BY recordtype;

-- Group By: 
-- 12. List the dates and the corresponding total number GPS FIX readings taken on each day.  Only show the dates where 
-- the total number of GPS FIX readings is more than 30 in a day?  Sorted from the most to the least readings per day.
SELECT DATE(readdatetime) AS "Reading Date", 
       COUNT(*) AS "Total Daily Readings > 30"
FROM reading
WHERE recordtype IN
    (SELECT recordtype
     FROM reading
     WHERE recordtype = 'GPS FIX')
GROUP BY DATE(readdatetime)
HAVING COUNT(*) > 30
ORDER BY "Total Daily Readings > 30" DESC;
