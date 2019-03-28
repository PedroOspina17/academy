import sys

def try_catch(num1):
    try:
        print("the number is ", int(num1))
    except ValueError as ex:
        print("an error has happened",ex)
    else:
        print("everithing goes well")
    finally:
        print("this message alwas will be appers, no matters if there was an error")

try_catch(1)
try_catch("awd")