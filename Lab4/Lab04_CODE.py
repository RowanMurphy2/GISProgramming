import arcpy

folder_path = r'c:\GISPLAB\GISProgramming'
gdb_name = 'GISProgramming_Lab04.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r'c:\GISPLAB\GISProgramming\Lab4\Lab04_Data\garages.csv'
garage_Layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_Layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)

garage_points = gdb_path + '\\' + garage_Layer_name

campus = r'c:\GISPLAB\GISProgramming\Lab4\Lab04_Data\Campus.gdb'
buildings_campus = campus + '\\Structures'

buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

spatial_ref = arcpy.Describe(buildings).spatialReference

arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path +'\Garage_Points_buffered', 150)

arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Buildings_Intersection', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf', r'c:\GISPLAB\GISProgramming\Lab4\Lab04_Data', 'nearbyBuildings.csv')
