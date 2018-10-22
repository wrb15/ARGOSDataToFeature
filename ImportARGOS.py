##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: willa.brooks@duke.edu (for ENV859)
##---------------------------------------------------------------------

#Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'W:/wrb15/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "W:/wrb15/ARGOSTracking/Scratch/ARGOStrack.shp"