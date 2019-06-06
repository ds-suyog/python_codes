
import time 
import math 
  
def calculate_time(func): 
      
    def addfunctionality(*args, **kwargs): 
  
        begin = time.time() 
        returned_value = func(*args, **kwargs) 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin)
        return returned_value
 
    return addfunctionality 
  
  
@calculate_time
def factorial(num): 
    time.sleep(2) 
    return math.factorial(num)
  
print(factorial(10)) 

