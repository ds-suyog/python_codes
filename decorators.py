

def hello_decorator(func): 
    print("in decorator")
    def inner(): 
        print("Hello, this is before function execution") 
        function_to_be_used() 
        print("This is after function execution") 
        return inner
    
def function_to_be_used():
    print("This is inside the function !!") 

function_to_be_used = hello_decorator(function_to_be_used)

function_to_be_used
