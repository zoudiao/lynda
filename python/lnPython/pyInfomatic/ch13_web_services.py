#13.1 eXtensible Markup Language - XML
# <person>
# <name>Chuck</name>
# <phone type="intl">
# +1 734 303 4456
# </phone>
# <email hide="yes"/>
# </person>


#13.2 Parsing XML
import xml.etree.ElementTree as ET
data = '''
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''
tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print 'Phone:',tree.find('phone').text
print 'Type:',tree.find('phone').get('type')
print 'Attr:',tree.find('email').get('hide')

#13.3 Looping through nodes
input = '''
<stuff>
<users>
<user x="2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id>009</id>
<name>Brent</name>
</user>
</users>
</stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print 'User count:', len(lst)
for item in lst:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get('x')


## exe

import xml.etree.ElementTree as TI
# data2 = '''
# <employees>
# <employee>
# <name>Yi Fang</name>
# <phone type="apple">+8613761623782</phone>
# <email>yi.f.fang@ericsson.com</email>
# </employee>
# <employee>
# <name>Hua Zhang</name>
# <phone type="huawei">+8615026805613</phone>
# <email>hua.zhang@ericsson.com</email>
# </employee>
# <employee>
# <name>Richard Xu</name>
# <phone type="Sumsung">+8613795471883</phone>
# <email>richard.xu@ericsson.com</email>
# </employees>'''
#
# employees = ET.fromstring(data2)
# lst = employees.findall('employees/employee')
# print 'Employee count:', len(lst)
# for employee in lst:
#     print 'Name:', employee.find('name').text
#     print 'Phone:', employee.find('phone').text
#     print 'Phone type:', employee.find('phone').get('type')
#     print 'Email:', employee.find('email').text


#13.4 JavaScript Object Notation - JSON
# {
#     "name" : "Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+1 734 303 4456"
#     },
#     "email" : {
#         "hide" : "yes"
#     }
# }
#13.5 Parsing JSON
import json
input1 = '''
[
{ "id" : "001",
"x" : "2",
"name" : "Chuck"
} ,
{ "id" : "009",
"x" : "7",
"name" : "Brent"
}
]'''

input2 = '''
[
{ "name" : "Yi Fang",
   "phone" : {
        "type": "apple",
        "number" : "+8613761623782"
   },
   "email" : "yi.f.fang@ericsson.com"
},
{ "name" : "Richard Xu",
   "phone" : {
        "type": "Samsung",
        "number" : "+8613795471883"
   },
   "email" : "richard.xu@ericsson.com"
}

]


'''
info1 = json.loads(input1)
print 'User count:', len(info1)
for item in info1:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']


info2 = json.loads(input2)
print 'User count:', len(info2)
for item in info2:
    print 'Name:', item['name']
    print 'Phone Type:', item['phone']['type']
    print 'Phone Number:', item['phone']['number']
    print 'Email:', item['email']

#13.6 Application Programming Interfaces
#13.7 Google geocoding web service
import urllib
import json
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    url = serviceurl + urllib.urlencode({'sensor':'false',
                                     'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
    print data
    #continue
    print "111111111111"
    print json.dumps(js, indent=4)
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print "222222222222"
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print "333333333333"
    print location

#13.8 Security and API usage
