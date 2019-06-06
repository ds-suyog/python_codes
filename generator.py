
def simpleGeneratorFunc():
	print("in simpleGeneratorFunc")
	yield 1
	print("in simpleGeneratorFunc")
	yield 2
	print("in simpleGeneratorFunc")	
	yield 3            


for value in simpleGeneratorFunc():  
   print(value) 

print("====================")
print([val for val in simpleGeneratorFunc()])

print("====================")
itr = simpleGeneratorFunc() 
  
# Iterating over the generator object using next 
print(itr.__next__()) # In Python 2, .next() 
print(itr.__next__())
print(itr.__next__())