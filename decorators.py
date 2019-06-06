

def hello_decorator(func): 
    print("in decorator")

def function_to_be_used():
    print("This is inside the function !!") 

function_to_be_used = hello_decorator(function_to_be_used)

function_to_be_used
