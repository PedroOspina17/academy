def returningVoidValue(): #in python None is a null value
    pass ## to return None

def test_VoidValueVAlidation(): 
    ''' To define a test case use "test_" at the begining or "_test" at the end of the method name. 
        To execute them you should use the command pytest -q functions.py (or the class name that you want to test.)
    '''
    assert returningVoidValue() == None


print(returningVoidValue())

def optionalParams(a,b,c=10):
    print("{} {} {}".format(a,b,c))
optionalParams(1,2,3)
optionalParams(1,2)

def welcome():
    """
        this is for give the explanation or documentation of the function, to explain what is used for...
    """
    print("Welcome to working with functions")

def multpl_values(): # function that returns a tuple of numbers. you can receive it as a tuple or in a different variables.
    return 1,2,3

def test_multplValuesValidation(): 
    assert multpl_values() == (1,2,3)

    
# def test_multplValuesValidation_error(): an error execution test  will be raised due to the extra number added in the tuple that will be compared
#     assert multpl_values() == (1,2,3,4)

welcome()
result_in_tuple = multpl_values()
print(result_in_tuple) #a tuple is like a list and it can be used similar to it. 
print("using a tuple: {}".format(result_in_tuple[1])) #index base 0

num1, num2, num3 = multpl_values()
print("{} {} {}".format(num1,num2,num3))

def sum(*numbers): # use '*' before the param to specify unlimited numer of parameters
    result = 0
    for number in numbers:
        result+= number
    return result

print(sum(1,2,3,4,5,6))
numbersArray = [1,2,3,4]
print(*numbersArray) # put * before an array to pass it as a unlimited parameter

def sum_dict(**numbers): # use '**' before the param to specify an unlimited keyword params
    print(numbers)    # it will be shown as a dictionary
sum_dict(a=1,b=2,c=3)
numbersDict = {'a':1, 'b':2, 'c':3}
sum_dict(**numbersDict) # put ** before of a dictionary to pass it as a unlimited key word params to a  function

def mix(*unlimited, **kwunlimited): #you can mixed both techniques
    print(unlimited)
    print(kwunlimited)

mix(*numbersArray,**numbersDict)

hellolambda = lambda: "hello world from lambda function" #Define functions without name 
print(hellolambda())

hellolambda2 = lambda name,lastname = "": "hello {} {} from lambda function".format(name,lastname) #Define functions without name 
print(hellolambda2("Pedro","ospina"))
print(hellolambda2("Pedro"))