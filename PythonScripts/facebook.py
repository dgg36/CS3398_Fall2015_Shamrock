import csv
from cpot.models import FacebookPost

try:
    with open('facebook.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            print row[0]
except IOError:
    print "Error opening 'facebook.csv'."
    exit()
