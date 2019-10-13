
# time.clock() is deprecated, use time.perf_counter or time.process_time instead
# import time
# t1 = time.clock()   # time in seconds
# ## code
# for i  in range(100000): pass
# t2 = time.clock()
# print(t2 - t1)

from time import perf_counter 
# Start the stopwatch / counter 
t1_start = perf_counter()  
for i  in range(100000000): pass
# Stop the stopwatch / counter 
t1_stop = perf_counter() 
print("Elapsed time:", t1_stop, t1_start)  
print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)


import matplotlib.pyplot as plt

def f2(L):
    sum = 0
    i = 1
    times = 0
    while i < len(L):
        sum = sum + L[i]
        i = i * 2
        times += 1    # track how many times the loop gets called
        return times

def main():
    i = range(1200)
    f_i = [f2([1]*n) for n in i]
    plt.plot(i, f_i)
    plt.show()

if __name__=="__main__":
    main()
