

def fib(limit): 
    a, b = 0, 1
    while a < limit: 
    	print("in func fib, yielding value")
    	yield a
    	print("in func fib, after yield")
    	a, b = b, a + b 
  
# Create a generator object 
itr = fib(5) 
  
# Iterating over the generator object using next 
print(itr.__next__()) # In Python 2, .next() 
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print("============================")
 
print("\nUsing for in loop,") 
for i in fib(5):
    print(i) 
