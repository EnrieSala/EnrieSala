# Municipality of Halifax Fire Services Inventory Web Map App
This web map application visualizes key fire services infrastructure and geographic features for the Municipality of Halifax. It combines interactive mapping, custom symbology, and informative popups to support fire services planning and public awareness.

## Overview
The application consists of two main files:

index.html: The HTML entry point that sets up the web page container for the map and loads the required JavaScript.

main.js: The core JavaScript file that builds the interactive map using the ArcGIS JavaScript API, adds data layers, configures symbology, and enables interactive widgets.

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
- Open index.html in your browser.
- Interact with the map: pan, zoom, and click features for more information
- Use widgets (Home, Basemap Toggle, Legend, Line of Sight, Elevation Profile) for enhanced navigation and analysis.

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
