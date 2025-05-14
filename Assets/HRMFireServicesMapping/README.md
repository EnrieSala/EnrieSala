# Municipality of Halifax Fire Services Inventory Web Map App
This web map application visualizes key fire services infrastructure and geographic features for the Municipality of Halifax. It combines interactive mapping, custom symbology, and informative popups to support fire services planning and public awareness.

## Overview
The application consists of the following files, organized for clarity and maintainability:
- index.html (main directory): The entry point that sets up the web page and loads required resources.
- /styles/style.css: Provides all styling for the application, including layout, colors, and logo placement.
- /scripts/main.js: Contains the JavaScript logic for building the interactive map, adding data layers, and enabling widgets.
- /logos/Esri_Canada_Logo_4C_ECFlatLogo_White.jpg: The Esri Canada logo displayed in the application.

### Folder structure 
halifax-fire-services-app/
│
├── index.html
├── styles/
│   └── style.css
├── scripts/
│   └── main.js
└── logos/
    └── Esri_Canada_Logo_4C_ECFlatLogo_White.jpg

## Features
3D Interactive Map: Utilizes the ArcGIS SceneView for a 3D perspective over Halifax.

## Layer Visualization:
- Halifax County polygons: Displayed with custom symbology and interactive popups showing county name and area.
- Provincial Roads: Provides geographic context.
- Fire Stations: Visualized with a realistic fire truck symbol.
- Dry Hydrants: Visualized with a custom yellow fire hydrant symbol.

## Widgets:
- Home, Basemap Toggle, and Legend (with expandable interface)
- Line of Sight and Elevation Profile tools for advanced spatial analysis
- Popups: Clicking on a county polygon reveals its name and area (in square metres) with formatted numeric display.

## Data Sources
- Halifax County polygons: [GeoNova Map Service]
- Provincial Roads: [GeoNova Map Service]
- Fire Stations: [GeoNova Map Service]
- Dry Hydrants: [GeoNova Map Service]
  
## Requirements
- Modern web browser (Chrome, Firefox, Edge)
- Internet connection (data is loaded from ArcGIS Online services)
- No installation required

## Usage
### Download and Organize Files
Download all files and organize them as shown in the folder structure above:
1. Place index.html in the root folder.
2. Place style.css in a styles subfolder.
3. Place main.js in a scripts subfolder.
4. Place the logo image in a logos subfolder.

### Open the Application
1. Open the index.html file from your local drive in a modern web browser (Chrome, Firefox, Edge).
2. Interact with the Map
3. Pan, zoom, and click features for more information.
4. Use widgets for navigation and spatial analysis.

## File Descriptions
### index.html
- Sets up the HTML structure and includes the ArcGIS JavaScript API and CSS.
- Provides a container (<div id="mainMap">) for the map display.
- Loads main.js to initialize the map and all functionality.

### main.js
- Configures the map and scene view (centered over Halifax).
- Adds all data layers with appropriate renderers and popups.
- Customizes symbology for fire stations and dry hydrants using Esri WebStyleSymbols.
- Implements interactive widgets for navigation and spatial analysis.
- Handles asynchronous symbol fetching and applies custom styles to point layers.

## Customization
API Key: The script uses an ArcGIS API key for access to hosted layers. Replace the API key in main.js with your own if deploying for personal or organizational use.
Layer URLs: To use different datasets, update the URLs in the FeatureLayer and MapImageLayer definitions in main.js.
