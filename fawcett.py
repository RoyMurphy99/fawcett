# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:08:42 2019

@author: Roy Standard

Visualise the explorations of Percy Fawcett:
    identify candidate south american place names in the text of his works.
    determine if the candidate names are on the south american continent.
    plot the locations of the named places on a map of south america.
"""
#
# step 1 is to draw the map of south america
#
import os
os.environ["PROJ_LIB"] = "C:\\Users\\Analysis\\Anaconda3\\pkgs\\proj4-5.2.0-h6538335_1003\\Library\\share" 

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
m = Basemap(projection="cea",llcrnrlat=-60, llcrnrlon=-90, 
            urcrnrlat=15,urcrnrlon=-30, resolution = 'l')

m.drawcoastlines()
m.fillcontinents()
m.drawcountries()
#m.drawrivers()
m.drawmapboundary()

plt.title('Fawcett\'s travels')
plt.show()
