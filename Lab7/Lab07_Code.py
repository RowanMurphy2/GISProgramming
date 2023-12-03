

import arcpy
source = r"c:\\GISPLAB\\GISProgramming\\Lab7\\Lab07_Data\\"
result = r"c:\\GISPLAB\\GISProgramming\\Lab7\\Lab07_Results\\"
band1 = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF") # blue
band2 = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF") # green
band3 = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF") # red
band4 = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.TIF") # NIR

composite = arcpy.CompositeBands_management([band1,band2,band3,band4], result + "combined.tif")

azimuth = 315
altitiude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(source + r"\\n30_w097_1arc_v3.tif", result + r"//hillshade.tif", azimuth, altitiude, shadows, z_factor)

output_measure = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + r"\\n30_w097_1arc_v3.tif", result + r"\\slopes.tif", output_measure, z_factor)