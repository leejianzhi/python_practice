from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
new_list = []
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('text', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    for i in tag.contents:
        new_list.append(i)
for ele in range(0, len(new_list)):
    sum = sum + int(new_list[ele])
print(sum)
