import urllib.request, urllib.parse, urllib.error
import json
import ssl
#!!!! import is on order matter !!!!
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving: ", url)
open_url = urllib.request.urlopen(url, context=ctx)



#print(data)
data = open_url.read()

trans_data = json.loads(data)
print(trans_data)
print('Retrieved: ', len(trans_data), "characters")

sum = 0

for i in trans_data["comments"]:
    #print(int(i["count"]))
    sum = sum + int(i["count"])
print(sum)
#for item in info:
#    print('Name', item['name'])
#    print('Id', item['id'])
#    print('Attribute', item['x'])
