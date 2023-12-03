# -*- coding: utf-8 -*-

import arcpy
import os


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Building Proximity"
        self.description = "Determines which building on TAMU's campus are near a targeted building"
        self.canRunInBackground = False
        self.catagory = "Building Tools"

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(displayName="work GDB folder path", name="GBDfolderpath",datatype="DEFolder",parameterType="Required",direction="Input")
        param1 = arcpy.Parameter(displayName="work GDB name", name="GBD_Name",datatype="GPString",parameterType="Required",direction="Input")
        param2 = arcpy.Parameter(displayName="garage CSV file path", name="garageCSVfileadress",datatype="DEFolder",parameterType="required",direction="Input")
        param3 = arcpy.Parameter(displayName="garage Name", name="garage_Name",datatype="GPString",parameterType="required",direction="Input")
        param4 = arcpy.Parameter(displayName="campus GBD folder path", name="campusGDBfolderpath",datatype="DEFolder",parameterType="required",direction="Input")
        param5 = arcpy.Parameter(displayName="selected garage name", name="selectedGarageName",datatype="GPString",parameterType="required",direction="Input")
        param6 = arcpy.Parameter(displayName="Buffer radius", name="bufferRadius",datatype="GPDouble",parameterType="required",direction="Input")
        params = [param0,param1,param2,param3,param4,param5,param6]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        GDB_Folder = parameters[0].valueAsText
        GDB_Name = parameters[1].valueAsText
        garage_csv_file = parameters[2].valueAsText
        garageLayer_name = parameters[3].valueAsText
        campusGDB_Folder = parameters[4].valueAsText
        Selected_Garage_Name = parameters[5].valueAsText
        bufferSize_input = parameters[6].valueAsText

        campus = os.path.join(campusGDB_Folder, 'Campus.gdb')
        WorkGDB = GDB_Name + ".gdb"
        database = os.path.join(GDB_Folder, WorkGDB)
        arcpy.env.overwriteOutput = True
        if arcpy.Exists(database):
            pass
        else:
            arcpy.CreateFileGDB_management(GDB_Folder, WorkGDB)
        arcpy.env.workspace = database

        garages = arcpy.management.MakeXYEventLayer(garage_csv_file, "x", "y", garageLayer_name)

        structures = campus + "/Structures"
        where_clause = "BldgName = '%s" % Selected_Garage_Name
        cursor = arcpy.SearchCursor(structures, where_clause=where_clause)

        shouldProceed = False

        for row in cursor:
            if row.getValue("BldgName") == Selected_Garage_Name:
                shouldProceed = True
                break
        
        if shouldProceed:
            Selected_Garage_layer_name = database + "/garage_selected"
            garage_feature = arcpy.Select_analysis(structures, Selected_Garage_layer_name, where_clause)

            garage_buff_name = database +"/building_buffed_%s" % (bufferSize_input)
            arcpy.Buffer_analysis(garage_feature, garage_buff_name, bufferSize_input + " meter")

            arcpy.Clip_analysis(structures, garage_buff_name, database + "/clip")
            arcpy.AddMessage("Success!")
        else:
            arcpy.AddError("Cant find building entered")
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
