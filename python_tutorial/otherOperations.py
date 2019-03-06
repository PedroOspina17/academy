
import sys

#sort
numbers = [5,6,9,2,36,8,6]
print("sorted numbers: ", sorted(numbers)) # sorted function return a new list
print(numbers) # the list was not affected 
numbers.sort() #this method  afects the list directly
print(numbers) # now the list is sorted

information = [
                {'Nombre': "pedro", 'age': 22, 'lifesLived':1, 'gender':'M', 'isAlive': True}
                ,{'Nombre': "luis", 'age': 10, 'lifesLived': 3, 'gender':'M','isAlive': False}
                ,{'Nombre': "carlos", 'age': 33, 'lifesLived':11, 'gender':'M','isAlive': True}
                ,{'Nombre': "gabriel", 'age': 55,'lifesLived' :12,'gender':'M', 'isAlive': False}
                ,{'Nombre': "carlos", 'age': 14,'lifesLived' :110, 'gender':'M','isAlive': True}
                ,{'Nombre': "gabriela", 'age': 16,'lifesLived' :3,'gender':'F', 'isAlive': False}
                ,{'Nombre': "luisa", 'age': 23, 'lifesLived': 1, 'gender':'F','isAlive': False}
                ,{'Nombre': "daniela", 'age': 35, 'lifesLived': 2, 'gender':'F','isAlive': True}
            ]
sorted_people = sorted(information, key=lambda fields: fields["age"])
print(sorted_people)

minnumber = min(numbers)
maxnumber = max(numbers)
print("min",minnumber,"max",maxnumber, "ordered list",numbers)

oldestPerson = max(information,key=lambda e: e["age"] * e["lifesLived"]) #You can order by calculated column
print(oldestPerson)

from itertools import groupby

groupedInfoByGender = groupby(sorted(information, key=lambda e: e["gender"]), key= lambda e: e["gender"]) 
""" 
    the result of the groupby operation will be something like 
    [
        ('FieldGrouped',[list of elements ]),
        ('FieldGrouped',[list of elements ]),
        ('FieldGrouped',[list of elements ])
    ]

"""
info = {key: list(values) for key, values in groupedInfoByGender} # since  the result of groupby operation is an array of tuples we have to convert it as a list  in this way
print(info)
displayInfo = [(key, len(values)) for key, values in info.items()] #when i call the method items() i get an array of tuples with ('column',value)
print(displayInfo)

totalAges = map(lambda e: e['age'] * e['lifesLived'], information) # map function pass every item to the function in the first parameter (it could be a lambda function or def function) and then return a new list with the result in the lambda funcition
print(list(totalAges)) 

filteredList = filter(lambda e: e['isAlive'] == True, information) # filter method just return le items that match with the condition specified in the lambda fuction setted in the first parameter
print(list(filteredList))