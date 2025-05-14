#################################
#   Programmer: Enrie Sala      #
#   Program: Assignment5        #
#   Purpose: To Scrape Wiki     #
#   Pages in order to create    #
#   a city temperature feature  #
#   class for New Brunswick     #
#   Date: March 3rd, 2025       #
#################################

#Import Libraries
#Used for HTTP requestes
import requests
#Library for parsing HTML and extracting data
from bs4 import BeautifulSoup
#ArcGIS library for geoprocessing and spatial analysis
import arcpy
#Library for URL manipulation and encoding 
import urllib.parse
#Library for regular expressions
import re

### Global Variables ###
#URL Wikipedia Page that contains the names of all major cities in New Brunswick,
#which will be used to create a list in order to create custom urls to search City
#Wiki Pages containing the temperature data 
WIKI_CITIES_URL = "https://en.wikipedia.org/wiki/List_of_cities_in_New_Brunswick"
#Geodatabase Path where the output feature layer will be stored 
GDB = r"C:\Winter_2025_Semester_NSSC\GP&Modeling\Assignments\Assignment5\Assignment5Test\Default.gdb"
#Name of Output Feature Class that will store city temmperature data 
FEATURE_CLASS_NAME = "NB_ClimateData3"
##HEADERS = {'User-Agent': 'Mozilla/5.0'}
#List of temperature stats which will be used to extract temperature data 
Stats = ['Max', 'Mean', 'Min']
#List of months which will represent columns in climate tables 
Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

### Functions ###

#Function to get New Brunswick city names from Wiki page 
def get_valid_cities():
    try:
        #Send a get request to fetch the Wiki page content 
        response = requests.get(WIKI_CITIES_URL) #, headers=HEADERS add this for headers inside the brackets
        #Use BeautifulSoup to read the html 
        soup = BeautifulSoup(response.content, 'html.parser')
        #Using the find method to locate the table with the class wikitable 
        table = soup.find("table", {"class": "wikitable"})
        #Iterating over all the rows "tr" in the table excluding the header and footer rows [1:-2]
        return [row.th.a.get_text(strip=True) 
                for row in table.find_all("tr")[1:-2]
                #checking if the city names are linked to a valid Wiki page (where the temperature data will be extracted from) 
                if row.th and row.th.a]
    except Exception as e:
        #Print error message if scraping fails 
        arcpy.AddError(f"City scraping failed: {str(e)}")
        #return an empty list if error occurs 
        return []

#Function to get temperatures from generated Wiki pages
#Only extracting max, min and median temperature values 
def get_temp_val(row):
    #Create an empty list to store temperatures 
    temps = []
    #Loop over the first 12 cells which contain the temperature values 
    for cell in row.find_all("td")[:12]:
        #Get the text from the cell and strip whitespace 
        text = cell.get_text(strip=True)
        # Handle temperature ranges and special characters
        temp_match = re.search(
            #replace special characters 
            r"(-?\d+\.?\d*)(\s*[\/ ]\s*(-?\d+\.?\d*))?", 
            text.replace('−', '-').replace(',', '.')
        )
        #Use regular expression to match temperature values (including ranges) 
        if not temp_match:
            #Nothing is returned if no valid temperatures are found 
            return None
        #Add the matched temperature value to the list and convert it to a float 
        temps.append(float(temp_match.group(1)))

    #SEE IF YOU CAN CHANGE THIS
    #Only return temps if 12 temps values were extracted 
    return temps if len(temps) == 12 else None

#Function to extract city temperatures 
def get_city_data(city):
    try:
        #Replacing spaces with underscores for proper url formatting 
        city = urllib.parse.quote(city.replace(' ', '_'))
        #constructed City urls 
        url = f"https://en.wikipedia.org/wiki/{city},_New_Brunswick"
        #use get to send a request to access Wiki page 
        response = requests.get(url) #, headers=HEADERS add this for headers inside the brackets 
        #If the requests was succesful, status code should be 200, or else no value will be returned 
        if response.status_code != 200:
            return None
        #Use Beautiful Soup to extract the html content from the Wiki page 
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Coordinate parsing
        #Finding all spans with the class geo or spans with the id "coordinate" 
        geo_span = soup.find('span', {'class': 'geo'}) or soup.find('span', {'id': 'coordinates'})
        #If these are not found, nothing is returned 
        if not geo_span:
            return None
        #Regular expression is used to extract numeric lat and long values 
        coords = re.findall(r"[-+]?\d+\.?\d+", geo_span.text)
    
        if len(coords) != 2:
            return None
        #Here the coordinate strings are converted to floats 
        lat, lon = map(float, coords)

        # Climate table detection
        #Here we are using Beautiful Soup to find tables with the class wiki tables
        climate_table = next((t for t in soup.find_all("table", {"class": "wikitable"})
                            #If the element contains the str climate than None
                            if "climate" in str(t).lower()), None)
        #If not climate table, return None 
        if not climate_table:
            return None

        # Temperature stats mapping
        # Setting up columns for temp data values 
        stat_patterns = {
            'Max': r"mean daily maximum",
            'Mean': r"daily mean",
            'Min': r"mean daily minimum"
            
        }

        #Initiating empty list to store temp data
        tempdata = {}
        #Here we are iterating over the climate table and finding all rows 
        for stat, pattern in stat_patterns.items():
            row = next((r for r in climate_table.find_all("tr") 
                       if re.search(pattern, r.text, re.IGNORECASE)), None)
            #If not a row, nothing is returned
            if not row:
                return None
            #If a valid row is found then the get_temp_val function will be used to validate and extract if it is indeed a temperature 
            temps = get_temp_val(row)
            #If not, nothing will be returned 
            if not temps:
                return None
            #The tempdata is stored in the temps data dictionary 
            tempdata[stat] = temps
        # Return a dictionary containing city name, coordinates, and temperature data
        return {
            "city": city,
            "lat": lat,
            "lon": lon,
            "temperatures": tempdata
        }
    #Error handling for get_city_data function 
    except Exception as e:
        arcpy.AddWarning(f"Error processing {city}: {str(e)}")
        return None

#Function to create the city feature classes 
def create_feature_class():
    try:
        #Setting the workspace up 
        arcpy.env.workspace = GDB
        #Allowing environment overwriting 
        arcpy.env.overwriteOutput = True
        #Allowing deleting of feature class if it exists 
        if arcpy.Exists(FEATURE_CLASS_NAME):
            arcpy.management.Delete(FEATURE_CLASS_NAME)
            
        # Create spatial reference
        spatial_ref = arcpy.SpatialReference(4326)
        
        # Create a point feature class with the SRID of 4326 
        arcpy.management.CreateFeatureclass(
            arcpy.env.workspace,
            FEATURE_CLASS_NAME,
            "POINT",
            spatial_reference=spatial_ref
        )
        
        # Generate field definitions for temperature table
        #City field will store city name as a text with a scale of 50 
        fields = [("City", "TEXT", 50)]
        #Loop through each month in the Months list 
        for month in Months:
            #Loop through each stat in Stats list 
            for stat in Stats:
                #Here a field combining month and stats will be created 
                field_name = f"{month}_{stat}"
                #Here all fields are added to the feature class 
                fields.append((field_name, "FLOAT"))
        
        # Add fields
        #Looping through the fields to populate them will city and temp values 
        for field in fields:
            arcpy.management.AddField(
                #output feature class 
                FEATURE_CLASS_NAME,
                #field name 
                field[0],
                #field type 
                field[1],
                #Field length for text, if greater than 2 nothing is stored 
                field_length=field[2] if len(field) > 2 else None
            )
        #Print statement for succesful operation
        arcpy.AddMessage("Successfully created feature class with expanded schema")
    #Error handling section of create_feature_class function 
    except arcpy.ExecuteError as e:
        arcpy.AddError(f"ArcGIS error: {str(e)}")
        raise
    
#Main function to run sub functions 
def main():
    #here we are calling the create_feature_class function and storing get_valid_cities() function to a variable called cities 
    create_feature_class()
    cities = get_valid_cities()
    
    # Generate field order for inserting data into the feature class using a cursor
    # The field_order variable will store long and lat coordinates as well as the city name 
    field_order = ["SHAPE@XY", "City"]
    #Here we are looping through each month in Months list 
    for month in Months:
        #Here we are looping through each stat in Stats list 
        for stat in Stats:
            # Append each temperature field name to the order list
            field_order.append(f"{month}_{stat}")
    # Open an InsertCursor to add rows to the feature class based on scraped data
    with arcpy.da.InsertCursor(FEATURE_CLASS_NAME, field_order) as cursor:
        success_count = 0 #Initialize a counter for succesful inserts 
        for city in cities: #Iterate over all scraped city names
            #Fetch climate and coordinate data for each city 
            data = get_city_data(city)
            #Check if valid data was returned and contains temperature info
            if data and 'temperatures' in data:
                try:
                    #Initalize a list to store temp values 
                    # Flatten temperature data into correct field order
                    temp_values = []
                    # Loop through each month in Months list
                    for month in Months:
                        #Here we are looping through each stat in Stats list 
                        for stat in Stats:
                            # Get index of current month in Months list
                            index = Months.index(month)
                            # Append temperature value corresponding to current stat and month
                            temp_values.append(data['temperatures'][stat][index])
                    # Insert longitude and latitude as geometry (XY coordinates)
                    cursor.insertRow([
                        (data["lon"], data["lat"]),
                        # Insert city name into "City" field
                        data["city"],
                        # Insert flattened temperature values into respective fields
                        *temp_values
                    ])
                    # Increment counter for successful inserts
                    success_count += 1
                    #Print statements 
                    arcpy.AddMessage(f"Added: {city}")
                except Exception as e:
                    # Log warning message if inserting row fails
                    arcpy.AddWarning(f"Failed insert for {city}: {str(e)}")
            else:
                # Log warning message if city data is invalid or incomplete
                arcpy.AddWarning(f"Skipped {city} - data validation failed")
        # Log summary message indicating how many cities were processed successfully
        arcpy.AddMessage(f"Processed {success_count}/{len(cities)} cities successfully")
# Call main function when script is executed directly
if __name__ == "__main__":
    main()
