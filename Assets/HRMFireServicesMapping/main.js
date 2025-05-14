/* 
    Program: main.js
    Programmer: Enrie Sala
    Purpose: Javascript for Halifax Fire Services
    Inventory Map: Displays
    Halifax County polygons,
    Provincial roads, Halifax
    County fire stations and
    Halifax County dry hydrants.
    The Halifax county layer has
    interactive popups that display
    the county name and the county 
    area in square metres 
    Date: April 12th, 2025
    
*/
// Enforces strict mode for better error handling and cleaner code
"use strict";

// required modules
require(["esri/config",
    // Configuration and Map Modules
    "esri/Map",
    "esri/views/SceneView",
    // Rendering and Symbology Modules
    "esri/Graphic",
    "esri/renderers/SimpleRenderer",
    "esri/symbols/WebStyleSymbol",
    // Layer Modules
    "esri/layers/MapImageLayer",
    "esri/layers/FeatureLayer",
    // Widget Modules
    "esri/widgets/Home",
    "esri/widgets/BasemapToggle",
    "esri/widgets/Legend",
    "esri/widgets/LineOfSight",
    "esri/widgets/ElevationProfile",
    "esri/widgets/Expand"

    //modules for function
], function (
    esriConfig,
    Map,
    SceneView,
    Graphic,
    SimpleRenderer,
    WebStyleSymbol,
    MapImageLayer,
    FeatureLayer,
    Home,
    BasemapToggle,
    Legend,
    LineOfSight,
    ElevationProfile,
    Expand
) {
    //Declaring the map
    const mainMap = new Map({
        //Choosing basemap type and setting the elevation layer source 
        basemap: "dark-gray-vector",
        ground: "world-topobathymetry"
    });

    //API Key Configuration to access restricted/hosted layers 
    esriConfig.apiKey = "AAPTxy8BH1VEsoebNVZXo8HurBVYBI8i30N7q5P2DuvAq8dTrrdXhN3ePFx2i14mX0XIwh4ZrV3kiRGahxdid40RG_BLqDZIbsrtVHUEhSpzobhZeX0OXWUVSO6BZeuy-6Y6IyOm0V3i5lGnh-UW1QAj9XWLv3v8XkNrrNoOIDpLiaxPtbzoVkYo0D3lUXRRCXpMay3M-J6z3iK0ct5FzUS52XRTVIOynOcpyPIv1ytoMLs.AT1_VBv9TExf"

    //Declaring the SceneView  
    const view = new SceneView({
        //Links the map object to the SceneView 
        map: mainMap,

        container: "mainMap",
        camera: {
            // Sets initial camera position above the Halifax Regional Municipality
            position: [
                -63.25, // Longitude (X, in decimal degrees, WGS84)
                43,     // Latitude (Y, in decimal degrees, WGS84)
                100000  // Elevation (Z, in meters above sea level)
            ],
            heading: 0, // Direction the camera is facing, in degrees (0 = north)
            tilt: 60    // Angle in degrees between the camera and the ground (0 = looking straight down, 90 = looking at the horizon)
        }
    });

    //Initializing the Widgets  

    //Declaring the homeWidget
    let homeWidget = new Home({ view });
    //Adding the homeWidget to the Sceneview
    view.ui.add(homeWidget, "top-left");

    //Declaring the basemapToggleWidget
    let basemapToggleWidget = new BasemapToggle({
        view,
        nextBasemap: "hybrid"
    });
    //Adding the basemapToggleWidget to the Sceneview
    view.ui.add(basemapToggleWidget, "top-right");

    //Declaring the legendWidget
    let legendWidget = new Legend({ view });
    //Creating the expand widget 
    const legendExpand = new Expand({
        //linking the legendExpand widget to the scene view 
        view,
        //Setting the legendExpand widget to the elevationProfile Widget in order to minimize the tool 
        content: legendWidget
    });
    //Adding the legendWidget to the Sceneview
    view.ui.add(legendExpand, "bottom-right");

    //Declaring the lineOfSightWidget
    let lineOfSightWidget = new LineOfSight({ view });
    //Creating the expand widget 
    const lineofSightExpand = new Expand({
        //linking the lineofSightExpand widget to the scene view 
        view,
        //Setting the lineofSightExpand widget to the elevationProfile Widget in order to minimize the tool 
        content: lineOfSightWidget
    });
    //Adding the lineOfSightExpand to the Sceneview
    view.ui.add(lineofSightExpand, { position: "top-left" });

    //Declaring the elevation ProfileWidget
    let elevationProfileWidget = new ElevationProfile({ view });
    //Creating the expand widget 
    const profileExpand = new Expand({
        //linking the expand widget to the scene view 
        view,
        //Setting the profileExpand widget to the elevationProfile Widget in order to minimize the tool 
        content: elevationProfileWidget
    });
    //Adding the elevationProfileWidget
    view.ui.add(profileExpand, "top-left");

    //Declaring the HalifaxRenderer and assigning the HalifaxRenderer
    let HalifaxRenderer = {
        //setting Renderer type to simple, meaning all features in the layer will be drawn with the same symbol 
        type: "simple",
        //defines the symbol that represents the features 
        symbol: {
            //specifying the symbol type, with simple fill you can alter the fill colour and outline 
            type: "simple-fill",
            //changing the layer fill colour
            color: "MidnightBlue",
            //outline details
            outline: {
                //specifying outline width and colour 
                width: 2,
                color: "white"
            }
        }
    };

    //Declaring the HalifaxPopup template
    let HalifaxPopup = {
        //Setting the popup title 
        title: "County Information",
        //content elements for the popups 
        content: [{
            //list of fields from the feature that will be displayed in the popup 
            type: "fields",
            //field content
            fieldInfos: [{
                //Filtering out for the fieldName that will be displayed 
                fieldName: "GSA_NAME",
                //Popup label
                label: "County Name"
            }, {
                //Filtering out for the fieldName that will be displayed 
                fieldName: "SHAPE__Area",
                //Popup label
                label: "Area (sq metres)",
                //setting up numeric formatting
                format: {
                    //declaring a digit separator(,)
                    digitSeparator: true,
                    //condensing to 2 decimal places
                    places: 2
                }
            }]
        }]
    };

    //Web Symbol Initialization 

    //Creating DryHydrant web symbol 
    const DryHydrantSymbol = new WebStyleSymbol({
        name: "Fire_Hydrant",
        styleName: "EsriRealisticStreetSceneStyle"
    });

    //Creating FireStation web symbol 
    const FireStationSymbol = new WebStyleSymbol({
        name: "Firetruck", 
        styleName: "EsriRealisticTransportationStyle" 
    });



    // Layers

    //HalifaxCounty polygon layer
    let HalifaxCounty = new FeatureLayer({
        //Data source - GeoNova Map Service, hosted from ArcGIS Location Platform
        url: "https://services5.arcgis.com/upTY8zbWhHBxvUDs/arcgis/rest/services/HalifaxCounty/FeatureServer",
        //calling the renderer
        renderer: HalifaxRenderer,
        //setting layer opacity
        opacity: 0.3,
        //calling the popup 
        popupTemplate: HalifaxPopup,
        //attribution for data source 
        copyright: "Enrie Sala"
    });

    //Dry Hydrant Point Layer 
    let DryHydrantGeoNova = new FeatureLayer({
        //Data source - GeoNova Map Service 
        url: "https://services2.arcgis.com/11XBiaBYA9Ep0yNJ/arcgis/rest/services/DryHydrant/FeatureServer",
        //attribution for data source 
        copyright: "Enrie Sala"
    });

    //Roads Map Image Layer
    let roadsGeoNOVA = new MapImageLayer({
        //Data source - GeoNova Map Service 
        url: "https://nsgiwa.novascotia.ca/arcgis/rest/services/BASE/BASE_NSTDB_10k_Roads_UT83/MapServer/",
        //attribution for data source 
        copyright: "Enrie Sala"
    });

    let fireStations = new FeatureLayer({
        //Data source - GeoNova Map Service, hosted from ArcGIS Location Platform
        url: "https://services5.arcgis.com/upTY8zbWhHBxvUDs/arcgis/rest/services/HalifaxBuildings/FeatureServer",
        definitionExpression: "FEAT_DESC = 'FIRE STATION point'",
        //attribution for data source 
        copyright: "Enrie Sala"
    });

    // Fetch and resolve Dry Hydrant symbol asynchronously
    DryHydrantSymbol.fetchSymbol()
        .then(function (resolvedSymbol) {
            //Accesses the furst symbol layer in the resolved symbol 
            const objectSymbolLayer = resolvedSymbol.symbolLayers.getItemAt(0);
            //Resizing the dry hydrant symbol 
            objectSymbolLayer.height *= 1100.5;
            objectSymbolLayer.width *= 1100.5;
            //Changing the colour of the dry hydrant symbol
            objectSymbolLayer.material = { color: "yellow" };
            //Clones the existing renderer for this layer to avoid overwriting other properties 
            const updatedRenderer = DryHydrantGeoNova.renderer.clone();
            //Setting the new renderer to the styled dry hydrant web symbol 
            updatedRenderer.symbol = resolvedSymbol;
            //Applying the updated renderer to the Dry Hydrant layer 
            DryHydrantGeoNova.renderer = updatedRenderer;
        });


    // Fetch and resolve Fire Station symbol asynchronously
    FireStationSymbol.fetchSymbol()
        .then(function (FireSym) {
            // Accesses the first symbol layer in the resolved symbol
            const objectSymbolLayer = FireSym.symbolLayers.getItemAt(0);
            //Resizing the fire station symbol 
            objectSymbolLayer.height *= 115; 
            objectSymbolLayer.width *= 115;
            objectSymbolLayer.depth *= 115;
            // Rotate the fire station symbol
            objectSymbolLayer.heading = 120; // Rotate around z-axis



            // Create a new renderer with updated symbol styling
            fireStations.renderer = new SimpleRenderer({
                symbol: FireSym
            });

            // Add Fire Stations layer to the map AFTER updating its renderer
            mainMap.add(fireStations);
        })



// Adds all layers to the map in order of importance or visibility priority:
// - Halifax County polygons are added first as they serve as a base layer.
// - Roads are added next as they provide context.
// - Dry Hydrants and Fire Stations are added last as they are point layers that overlay other layers.
    mainMap.addMany([HalifaxCounty, roadsGeoNOVA, DryHydrantGeoNova, roadsGeoNOVA]);
})