###############################################################
# Program: ForestStandSuitability                             #
# Purpose: Determine stand suitability based on user selection#
# Written By: Enrie Sala   Oct. 2024                          #
###############################################################

# Creating Polygon list and unique species list 
forestLyr = iface.activeLayer()

speclist = []
for feature in forestLyr.getFeatures():
    spec = feature['SP1']
    if spec is not None and spec not in speclist:
        speclist.append(spec)

# User selection of SP1     
def main():
    print("Unique species values from SP1:", speclist)

    title = "Select Species"
    label = "Please select a species code:"
    
    okx1 = False
    spec = None  

    while not okx1 or (spec and spec.upper() not in speclist):
        spec, okx1 = QInputDialog.getText(None, title, label)
        
        if okx1 and spec.upper() in speclist:
            spec = spec.upper()
            print("SP1 species chosen: %s" % spec)
            print("User clicked okay button:", okx1)
        else:
            print("Invalid selection or canceled. Please select a valid species.")
            
    polySP1 = []

    for feature in forestLyr.getFeatures():
        feature_sp1 = feature['SP1']
        
        if feature_sp1 == spec:
            polySP1.append(feature.id())

# Collecting AVDI, height, cover type, and shape area  
    high_suit = []
    medium_suit = []
    low_suit = []
    
    high_min_area = None
    high_max_area = None
    
    medium_min_area = None
    medium_max_area = None
    
    low_min_area = None
    low_max_area = None

    for feature in forestLyr.getFeatures():
        feature_id = feature.id()
        if feature_id in polySP1:
            avdi = feature['AVDI']
            tree_height = feature['HEIGHT']
            cover_type = feature['COVER_TYPE']
            polyarea = feature['SHAPE_Area']

            # Determine AVDI rating
            if avdi < 20:
                avdirate = 0.75
            elif avdi > 30:
                avdirate = 2.5
            else:
                avdirate = 1.75

            # Determine height rating
            if tree_height < 10:
                heightrate = 1.25
            elif tree_height > 20:
                heightrate = 3.75
            else:
                heightrate = 2.5

            # Determine cover type rating
            if cover_type == 2:
                coverrate = 1
            elif cover_type == 8:
                coverrate = 3.75
            else:
                coverrate = 2
            
            total_rate = avdirate + heightrate + coverrate
            
            # Check for positive area before appending to suitability lists 
            if polyarea > 0:
                if total_rate > 8:  
                    high_suit.append(polyarea)
                    if high_min_area is None or polyarea < high_min_area:
                        high_min_area = polyarea
                    if high_max_area is None or polyarea > high_max_area:
                        high_max_area = polyarea
                
                elif total_rate < 5:  
                    low_suit.append(polyarea)
            
                    if low_min_area is None or polyarea < low_min_area:
                        low_min_area = polyarea
                    if low_max_area is None or polyarea > low_max_area:
                        low_max_area = polyarea
                
                else:  
                    medium_suit.append(polyarea)
                    if medium_min_area is None or polyarea < medium_min_area:
                        medium_min_area = polyarea
                    if medium_max_area is None or polyarea > medium_max_area:
                        medium_max_area = polyarea

#Summary report
    print("===================================================================")
    print("\t\tNorth Mountain Cougar Habitat Suitability Analysis\n\t\t\t %i of %s Polygons in Study Area." % (len(polySP1), spec))
    print("===================================================================")

    print("Low Suitability:")
    print("\t\t\t\t- Number of polygons  : %11i" % len(low_suit))
    print("\t\t\t\t- Minimum polygon area: %15.3f" % (low_min_area if low_min_area is not None else 0))
    print("\t\t\t\t- Maximum polygon area: %15.3f" % (low_max_area if low_max_area is not None else 0))
    print("\t\t\t\t- Total area          : %15.3f" % sum(low_suit))
    print("\t\t\t\t- Average polygon area: %15.3f" % (sum(low_suit) / len(low_suit) if len(low_suit) > 0 else 0))
    
    print()

    print("Medium Suitability:")
    print("\t\t\t\t- Number of polygons  : %11i" % len(medium_suit))
    print("\t\t\t\t- Minimum polygon area: %15.3f" % (medium_min_area if medium_min_area is not None else 0))
    print("\t\t\t\t- Maximum polygon area: %15.3f" % (medium_max_area if medium_max_area is not None else 0))
    print("\t\t\t\t- Total area          : %15.3f" % sum(medium_suit))
    print("\t\t\t\t- Average polygon area: %15.3f" % (sum(medium_suit) / len(medium_suit) if len(medium_suit) > 0 else 0))
    
    print()

    print("High Suitability:")
    print("\t\t\t\t- Number of polygons  : %11i" % len(high_suit))
    print("\t\t\t\t- Minimum polygon area: %15.3f" % (high_min_area if high_min_area is not None else 0))
    print("\t\t\t\t- Maximum polygon area: %15.3f" % (high_max_area if high_max_area is not None else 0))
    print("\t\t\t\t- Total area          : %15.3f" % sum(high_suit))
    print("\t\t\t\t- Average polygon area: %15.3f" % (sum(high_suit) / len(high_suit) if len(high_suit) > 0 else 0))

    print()
    
    print("===================================================================")
 
#While loop to rerun the program  
again = "Y"
while again[0].upper() != "N": 
    main()

    valid_input = False
    while not valid_input:
        text, ok = QInputDialog.getText(None, "Run Again", "Run the program again? (Y/N):", QLineEdit.Normal, "Y")

        if ok and text.strip():  
            response = text.strip()
            if response and response[0].upper() in ["Y", "N"]:
                again = response[0].upper()
                valid_input = True
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        else:
            again = "N"
            valid_input = True