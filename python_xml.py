import xml.etree.ElementTree as ET

data = '''<person>

    <name> bob </name>
    <phone type = "intl">
        +1 123 456 789
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data) #assign tree object. If there is any error from data string then the program will blow up
print('Name:', tree.find('name').text) #tree object would like to find name, phone, and email
print('phone:', tree.find('phone').text)
print('Attr:',tree.find('email').get('hide'))

#2nd example
# "'''" triple quote means many lines
data2 = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>alice</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Li</name>
        </user>
    </users>

</stuff>'''
# user tags will be in a list when called [user, user]
stuff = ET.fromstring(data2) #the text above will pass to the fromstring
findUser = stuff.findall('users/user') #user findall function to search all of users under users tag below users
print('User count:', len(findUser)) #count how many users under users tag
for item in findUser: #loop into the list
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute',item.get("x")) #to find the attribute numbers that assigned to x
#the loop will run 2 times since there are two users
