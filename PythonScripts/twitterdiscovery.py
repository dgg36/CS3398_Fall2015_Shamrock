#!/usr/bin/python 

# Version: 0.8
# Author: Jorge Rangel
#
# This script partitions the csv file by commas, and stores the data accoriding to 
# its corresponding column just how it is in excel. The csv file used is the Twitter_Discovery
# file.

import csv, argparse, sys


##Function:GrabArrayTitle
#Actions: Grabs the first row of the csv file to determine the number of columns 
#in the file  
def GrabColumns(columns):
   try:
     with open('Discovery Twitter_Discovery.csv', 'rb') as csvfile: #open file
      reader = csv.reader(csvfile, delimiter=',')

      count = 0
      for line in reader:
        if count == 0: 
         columns = line #grabs first row of csv file
        count = 1
   except IOError:
      print "File could not be open"
      csvfile.close()
      exit()
              
   numberColumns = len(columns)
   return numberColumns
##Class: TwitterDisvocery
#Parameters: object
#Actions: creates objects of each
class TwitterDiscovery(object):
    def __init__(self, source_text, facet, facets_count): #these are our objects aka the columns and their corresponding data         
        self.source_text = source_text
        self.facet = facet
       
#list for first row
columns = []

attributes = [] #list for rest of data
number_columns = GrabColumns(columns) #variable that holds the number of columns

try:
  with open('Discovery Twitter_Discovery.csv', 'rb') as csvfile: #open file
   reader = csv.reader(csvfile, delimiter=',')
   i = 0
   for line in reader: 
     if i < 1:
      x = TwitterDiscovery(line[0],line[2],line[3])
      attributes.append(x) #add the object to the list
     ++i 
except IOError:
  print "File could not be open"
  csvfile.close
  exit()
  
#print the list of objects
print "SOURCE TEXT\n\n"
for obj in attributes:
 print obj.source_text

print "FACETS\n\n"
for obj in attributes:
 print obj.facet
 
  


