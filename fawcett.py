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

#
# step 2 is to extract a list of candidate place names from the text
#

import re
regex = re.compile('[^a-zA-Z\s\n]')

os.environ["PROJ_LIB"] = "C:\\Users\\Analysis\\Anaconda3\\pkgs\\proj4-5.2.0-h6538335_1003\\Library\\share"

os.chdir('C:\\Users\\Roy Standard\\Documents\\Python_programming\\fawcett')
import string

try:
    maketrans = ''.maketrans
except AttributeError:
    # fallback for Python 2
    from string import maketrans

fawcett = open("fawcett.txt", encoding="utf-8")
all_words = {}

# the english3.txt file is a free text file of valid english words that I found on the internet
# there are many others, and I have lost the link for this file. 
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
