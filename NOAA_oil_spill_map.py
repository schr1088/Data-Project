# -*- coding: utf-8 -*-
"""
Created on Mon May 08 19:44:14 2017

@author: Peter
"""
#NOAA data make sure you download incidents from https://incidentnews.noaa.gov/raw/index

import csv
filename = 'incidents.csv'
lats, lons = [],[]
volumes = []
pollutant = []

with open(filename) as f:
    reader = csv.reader(f)
    
    #ignore headers
    next(reader)
    
    for row in reader:
        try:
            lats.append(float(row[4]))
        except ValueError:
            row[4]=' '
        try:
            lons.append(float(row[5]))
        except ValueError:
            row[5]=' '
        try:            
            volumes.append(float(row[15]))
        except ValueError:
            row[15]=' '        
        #pollutant.append(row[6])
        #would like to color code different types of chemicals with dots

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

V = np.sum(volumes)

m = Basemap(projection='hammer',lon_0=-100)
m.bluemarble(scale=0.5)
min_marker_size = 2.5
for lon, lat, in zip(lons, lats,):
    x,y = m(lons, lats)
    m.plot(x, y, 'ro')
plt.title('NOAA locations of Oil and Hazardous Chemical Spills since 1957')
plt.show()
print( 'minimum', V,  'gallons of primarily oil')