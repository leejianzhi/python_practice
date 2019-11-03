import json
#dict
data = '''{
    "name":"bob",
    "phone":{
        "type":"intl",
        "number":"+1 234 567 890"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data) #info is a dict
print('Name: ', info["name"]) #a dict from a key with name
print('Phone: ', info["phone"]["type"])
print('Hide: ', info["email"]["hide"])

#list of two dict

data2 = '''[
    {"id":"001",
     "x":"2",
     "name":"bob"
    },
    {"id":"009",
     "x":"7",
     "name":"alice"
     }
]'''

new_info = json.loads(data2)
print('User count: ', len(new_info))
for i in new_info:
    print('Name', i['name'])
    print('Id', i['id'])
    print('Attribute', i['x'])
