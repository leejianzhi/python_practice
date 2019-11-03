import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving: ", url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#data.decode()
tree = ET.fromstring(data)

findCount = tree.findall('.//count')
print('Number of counts is: ', len(findCount))

sum = 0


for i in findCount:
    sum = sum + int(i.text)




print(sum)
