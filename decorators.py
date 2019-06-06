
def hello_decorator(func): 
    def inner1():
        print("Hello, this is before myfunc execution") 
        func() 
        print("This is after myfunc execution")      
    return inner1

@hello_decorator
def myfunc(): 
    print("This is inside the function !!") 
  
# passing 'myfunc' inside the decorator to control its behavior 
# Either do this or write @hello_decorator above definition of 'myfunc'
# myfunc = hello_decorator(myfunc) 

myfunc() 
