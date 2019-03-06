import sys
 
information = [
                {'Nombre': "pedro", 'age': 22, 'isAlive': True}
                ,{'Nombre': "luis", 'age': 22, 'isAlive': False}
                ,{'Nombre': "carlos", 'age': 33, 'isAlive': True}
                ,{'Nombre': "gabriel", 'age': 55, 'isAlive': False}]


 
InfoGrouped = [ ('valores1',[{'Nombre': "pedro", 'age': 22, 'isAlive': True},{'Nombre': "pedro", 'age': 22, 'isAlive': True},{'Nombre': "pedro", 'age': 22, 'isAlive': True}]),
                ('valores2',[{'Nombre': "pedro", 'age': 22, 'isAlive': True},{'Nombre': "pedro", 'age': 22, 'isAlive': True},{'Nombre': "pedro", 'age': 22, 'isAlive': True}]),
                ('valores3',[{'Nombre': "pedro", 'age': 22, 'isAlive': True},{'Nombre': "pedro", 'age': 22, 'isAlive': True},{'Nombre': "pedro", 'age': 22, 'isAlive': True}])
                ]

comp1 = [item["Nombre"] for item in information] #showing specific fields 
print(comp1)

comp1 = [item["Nombre"] for item in information if item["isAlive"]] # Filtering the información
print(comp1)
comp_all_fields = [item for item in information if item["isAlive"]] # getting all the información
print(comp_all_fields)
comp_custom_fields = [{'field1': item['Nombre'], 'entireInfo': item, 'other field':321} for item in information if item["isAlive"]] # getting with custom fields 
print(comp_custom_fields)

test = {'field': item for item in information}
print(test)