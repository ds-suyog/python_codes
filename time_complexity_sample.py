
import time

t1 = time.clock()

## code
for i  in range(100000): pass

t2 = time.clock()

print(t2 - t1)
