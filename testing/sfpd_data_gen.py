# going to use this to generate random police data 

import csv
import time
from numpy.random import randint

with open('../data/SFPD_Incidents_-_from_1_January_2003.csv') as f:
    data = [row for row in csv.reader(f.read().splitlines())]

# grab just the crime description (2) and hour from time data (5)
crimes = [(r[2].lower(), int(r[5].split(':')[0])) for r in data[1:]]

# total number of possible crimes
n = len(crimes)

# keep generating crime data
while True:
	print crimes[randint(0, n)]
	time.sleep(1)