import re
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

with open('stopWords.txt') as f:
    stop_words = f.read().splitlines()

bjpfile = open("f")

 final_string = ''

 for line in bjpfile:
  line = line.lower()
  new_line = line.replace(",","").replace(".","")
  #for word in line:
  # if word not in stop_words:    #Remove the stop words
  final_string += line 

#YOUR_TEXT = "A tag cloud is a visual representation for text data, typically\
#        used to depict keyword metadata on websites, or to visualize free form text."



#print final_string

 tags = make_tags(get_tag_counts(final_string), maxsize=40)

 print type(tags)

 create_tag_image(tags[0:70], output, size=(600, 400), fontname='Crimson Text')
