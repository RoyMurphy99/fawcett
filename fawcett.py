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
# step 1 is to get the code needed to plot the map of south america,
# but I won't plot it until after I have obtained the coordinates
# of the places that Fawcett visited, in step 4
#
import os
os.environ["PROJ_LIB"] = "C:\\Users\\Analysis\\Anaconda3\\pkgs\\proj4-5.2.0-h6538335_1003\\Library\\share" 

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# move plt.show to the end of section 3, after the latitudes and longitudes 
# of the identified places have been worked out. 
# plt.show()

#
# step 2 is to extract a list of candidate place names from the text
#

import re
regex = re.compile('[^a-zA-Z\s\n]')

os.environ["PROJ_LIB"] = "C:\\Users\\Analysis\\Anaconda3\\pkgs\\proj4-5.2.0-h6538335_1003\\Library\\share"

os.chdir('C:\\Users\\Analysis\\Documents\\Python_programming\\fawcett')
import string

try:
    maketrans = ''.maketrans
except AttributeError:
    # fallback for Python 2
    from string import maketrans

fawcett = open("fawcett.txt", encoding="utf-8")
all_words = {}

with open("english3.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def is_english_word(word):
    return word.lower() in english_words

table = maketrans({key: None for key in string.punctuation})   

count = 0
for line in fawcett:
    count = count + 1
    line = line.rstrip()
    line = regex.sub(' ', line)
#    line = line.translate(table)
    line=line.lower()
    line_words=line.split()
    for word in line_words:
        if not(is_english_word(word)):
            if word not in all_words:
                all_words[word] = 1
            else:
                all_words[word] += 1
                
candidates = [x.title() for x in all_words.keys()]

#
# step 3 is to get co-ordinates if possible from the candidate names
#
countries = ["Argentina", "Brazil", "Bolivia", "Chile", "Colombia",
             "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname",
             "Uruguay", "Venezuela"]

# use opencage geocoder to get coordinates for place names.
# Because I'm using the free version, I will have to run the following
# code chunk on successive nights to check the candidate names against each
# south american country in turn.Then I won't exceed my limits. 

co_ord_list =[]
#import time
import geocoder
range_limit = 12

# confidence_bar is an integer between 1 and 10
confidence_bar = 5

key = '!!this is where you put your opencage geocoding key!!'
conf_dict={}
coord_dict={}

n = 0
for i in range(range_limit):
    # change the value of i to collect data for country[i]
    country = countries[i]
    for candidate in candidates:
        lat = ""
        lng = ""
        results = ""
        query = candidate + "," + country
        n += 1
        g = geocoder.opencage(query, key='6907a9aca714494297c99944e0e6a694')
        json_object = g.json
# access confidence and city as:
# json_object["confidence"] json_object["city"]
        try :
            if "city" in json_object:
                city = json_object["city"]
                confidence = json_object["confidence"]
                if city == candidate and confidence >= confidence_bar:
                    if city in conf_dict.keys():
                        if confidence > conf_dict[city]:
                            conf_dict[city] = confidence
                            coord_dict[city] = [json_object["lat"], json_object["lng"]]
                    else:
                        conf_dict[city] = confidence
                        coord_dict[city] = [json_object["lat"], json_object["lng"]]
        except TypeError as e:
            print(e, n)
#        time.sleep(0.1)

#
# unpack the coord_dict to a list
#
coord_list = list(coord_dict.values())
           
# save to list_i.txt
#with open('list_0.txt', 'w') as f:
#    f.write(json.dumps(co_ord_list))
#    f.close()
    
# to read the list back:
#with open('list_0.txt', 'r') as f:
#    list_0 = json.loads(f.read())
    
# after storing all of the coordinate lists, read them back one by one
# and see where I have unique coordinates for place names. 
  
#
# step 4: plot the points for the places and draw the map
#
import numpy as np

# now extract the lattitudes and longitudes for plotting 
lats = np.array(coord_list)[:, 0]
lons = np.array(coord_list)[:, 1]

# now build the map of south america and plot the points
# corresoonding to the names of the places that Fawcett visited. 
m = Basemap(projection="cea",llcrnrlat=-60, llcrnrlon=-90, 
            urcrnrlat=15,urcrnrlon=-30, resolution = 'l')

m.drawcoastlines()
m.fillcontinents()
m.drawcountries()
#m.drawrivers()
m.drawmapboundary()

plt.title('Fawcett\'s travels')
x, y = m(lons, lats)
m.plot(x, y, 'o')
plt.show()

# end of program
#


