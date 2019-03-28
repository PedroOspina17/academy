
#lists
testList = [1,2,3,4,5,6,7] 
print(testList)
print(testList[2:4]) #get a range of the list, 0-bazed list
testList.append(6) #add an element at the end
testList.insert(2,8) # insert a element in a specific position
testList.extend([22,23,24]) #concat two list

#tuples
testTuple = ("adwd",11,True) #a tuple is like a list but you cannot modify the values
print(testTuple)
print(testTuple[0],testTuple[1:2])
#b[1] = "adad" it is an error

#set 
testSet = set() #is like a list but it doesn't alow repeated valuies, 
testSet = {'a','b','c','a','d','c'}
print(testSet)
testSet.add('e')
print(testSet)
testSet2 = {'a','o','p','q','q','c'}
print(testSet.union(testSet2)) #concat two sets
print(testSet.intersection(testSet2)) # elemts in common
print(testSet.difference(testSet2)) # elements from set1 missing on set2

setFromList = set(testList)
print(setFromList)


testDict = {'Nombre': "pedro", 'age': 22, 'isAlive': True}
print(testDict) #dict or dictionary, needs to be written in json format
print(testDict.keys)
print(testDict["Nombre"]) #to get a key value, IT IS A KEY SENSITIVE.
testDict["nombre"] = "pedro mod" #if you try to assing a key that doesn't exist it will be created. IT IS A KEY SENSITIVE AS WELL.
print(testDict["Nombre"])
print(testDict["nombre"]) #a new key was created lowercased
print("nombre" in testDict) #to verify is the key exist in a dict


