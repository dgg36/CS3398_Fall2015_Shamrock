# version: 0.8
# Author: Jorge Rangel
#
# This script partitions the csv file by commas, and stores the data accoriding to
# its corresponding column just how it is in excel. The csv file used is the Twitter_Discovery
# file.

import sys, csv, os, django

#import models from models.py
sys.path.append('/home/fall2015shamrock/') #add current directory to python paths
sys.path.append('/home/fall2015shamrock/Python')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from django.db import models #import models.py
django.setup()
from models import Tweet


##Function:GrabArrayTitle
#Actions: Grabs the first row of the csv file to determine the number of columns
#in the file
def GrabColumns(columns):
   try:
     with open('twitterdetailedcity.csv', 'rb') as csvfile: #open file
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
    def __init__(self, id, source_text, facets_count): #these are our objects aka the columns and their corresponding data
        self.source_text = id
        self.facet = source_text
		
#list for first row
columns = []
attributes = [] #list for rest of data

number_columns = GrabColumns(columns) #variable that holds the number of columns
tweet_list = [] #this list is supposed to create instance of the Tweet class from models.py

try:
  with open('twitterdetailedcity.csv', 'rb') as csvfile: #open file
   reader = csv.reader(csvfile, delimiter=',')
   i = 0
   for line in reader:
     if i < 1:
      #x = TwitterDiscovery(line[0],line[1],line[1])
      x = Tweet.objects.get_or_create(content_id=line)
      #x = Tweet(line[0])
      try:
       x.save()
      except:
       print "could not save x"
      #attributes.append(x) #add the object to the list
       tweet_list.append(x) #attempt to add the object to the Tweet list. Maybe get_or_create should go here?
     ++i
except IOError:
  print "File could not be open"
  csvfile.close
  exit()
  
#print the list of objects
#print "ID\n\n"
#for obj in attributes:
 #tweet.content_id = obj.source_text
 #tweet_list.append(tweet.content_id)
 
#check to see if the data was added to
for test in tweet_list:
 print test
