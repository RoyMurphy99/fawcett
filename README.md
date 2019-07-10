## Visializing the explorations of the explorer Percy Fawcett

I recently read a book about the travels of the explorer Percy Fawcett in the early 20th century, and decided to try to apply some data science techniques to get a better handle on the places he visited in South America, and where they are in relation to each other. 

I purchased the book on my Kindle, "Exploration Fawcett" by Percy Fawcett and Brian Fawcett. To analyze it, I used some software called Calibre to convert it to a text file, then paused to decide what to do next. I came up with the following steps:

1. Draw a map of South America.
2. Somehow identify and extract place names from the text.
3. Somehow get map coordinates for the identified place names. 
4. Plot points on the map of South America corresponding to map coordinates. 

### Draw a map of South America

This involved a bit of research, and then playing around with latitude and longitude values to get a map of the part of the world 
roughly centred on South America. 

### Identify and extract place names from the text

There doesn't seem to be an easy way to do this, so I had to come up with something. 
The method I have decided to use is as follows:

1. Loop through each line of text in the file, check each word in the file against a word dictionary (there are lots of free ones on the web). 

2. If the word does not exist in the dictionary then this is a candidate for being a place name and can be saved. 

### Get map coordinates for place names

There are services that allow you to get GPS coordinates for place names, and some of them let you narrow the search by country. There are 13 countries in South America. Attempt to get coordinates for each candidate name for each of the South American countries.

Ideally I will only get coordinates back from real place names, and only from one particular country, for real place names. I know thats probably not going to hold true, but I'll just try it and see what happens. 

### Plot the coordinates on a map of South America

In principle this should be simple, but some tweaking on size, colour and transparency of points may be needed to make the visualization work.  


### Further Development?

Once I have completed the steps above, there will probably be lots of ways to improve the visualization, as to whether I have the time and inclination do it is another matter! At least it will be there in the repo if I, or you (whoever you are), decide to go further with it. 
