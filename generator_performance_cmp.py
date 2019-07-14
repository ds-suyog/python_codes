import memory_profiler as mem_profile
import time

def make_list(n): 
    lst = [i for i in range(1,n+1)]
    return lst
 
def make_gen_obj(n): 
    for i in range(1,n+1):
    	yield i

def make_gen_obj2(n): 
    obj = (i for i in range(1,n+1))

print("creating list of 1000000 elements!")
print("memory before: {}Mb".format(mem_profile.memory_usage()))
t1 = time.clock()
lst = make_list(1000000)  
t2 = time.clock()
print("memory after: {}Mb".format(mem_profile.memory_usage()))
print("took seconds: {}".format(t2-t1))
print()
del lst


print("creating 1000000 elements by yield!")
print("memory before: {}Mb".format(mem_profile.memory_usage()))
t1 = time.clock()
gen_obj = make_gen_obj(1000000)
t2 = time.clock()
print("memory after: {}Mb".format(mem_profile.memory_usage()))
print("took seconds: {}".format(t2-t1))
print()
del gen_obj


print("creating gen obj of 1000000 elements by comprehension!")
print("memory before: {}Mb".format(mem_profile.memory_usage()))
t1 = time.clock()
gen_obj = make_gen_obj2(1000000)
t2 = time.clock()
print("memory after: {}Mb".format(mem_profile.memory_usage()))
print()
del gen_obj

#import gc; gc.collect()
#print("memory after: {}Mb".format(mem_profile.memory_usage()))

# print(itr.__next__()) # In Python 2, .next(), or
# for i in gen_obj: print(i)

