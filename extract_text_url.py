# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count - '))
position = int(input('Enter position - '))
new_list = []
out_list = []
for i in range(count):
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    #print(i)
# Retrieve all of the anchor tags


    tags = soup('a')
    #for tag in tags:
        #new_list.append(tag) #append all anchors into new_list
    url = tags[position-1].get('href', None) #list use index position that is -1 away from user input

    #print(tag.get('href', None))

print('Retriving: ', url)

#for i in count:
#print(new_list[position])
#print(type(new_list))
#print('type of tag is : ',type(tag))
#print('type of tag is : ',type(tags))
