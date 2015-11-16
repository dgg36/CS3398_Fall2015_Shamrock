#!/usr/bin/python 

# Author: Jorge Rangel
#
# This script partitions the csv file by commas, and stores the data accoriding to 
# its corresponding column just how it is in excel. The csv file used is the Twitter_Discovery
# file

import csv, argparse, sys

##Function:GrabArrayTitle
#Actions: Grabs the first row of the csv file  
def GrabColumns(columns):
   try:
     with open('Discovery Twitter_Discovery.csv', 'rb') as csvfile: #open file
      reader = csv.reader(csvfile, delimiter=',')

      count = 0
      for line in reader:
        if count == 0: 
         columns = line #grabs first row of csv file
         print columns
        count = 1
   except IOError:
      print "File could not be open"
      exit()
              
   numberColumns = len(columns)
   return numberColumns
#######
class TwitterDiscovery:
    def __init__(twitter = []):
       try:
         with open('Discovery Twitter_Discovery.csv', 'rb') as csvfile: #open file
          reader = csv.reader(csvfile, delimiter=',')
          i = 0
       #store data to corresponding list
          for line in reader:
           if i == 0:         
            twitter[i].source_text = reader
            twitter[i].facet = reader
           i == 1
       except IOError:
         print "File could not be open"
         exit()

#array for first row
columns = []
twitter = []

GrabColumns(columns)
TwitterDiscovery()



