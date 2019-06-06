
# defining a decorator 
def hello_decorator(func): 
    # inner1 is a Wrapper function in which the argument is called  
    # inner1 function can access the outer local functions like in this case "func" 
    def inner1():
        print("Hello, this is before myfunc execution") 
  
        # calling the actual function now inside the wrapper function. 
        func() 
  
        print("This is after myfunc execution") 
          
    return inner1
  
  
# defining a function, to be called inside wrapper 
@hello_decorator
def myfunc(): 
    print("This is inside the function !!") 
  
# Either do this or write @hello_decorator above definition of 'myfunc'
# passing 'myfunc' inside the decorator to control its behavior 
# myfunc = hello_decorator(myfunc) 
  
  
# calling the function 
myfunc() 
