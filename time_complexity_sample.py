
import time
t1 = time.clock()
## code
for i  in range(100000): pass
t2 = time.clock()
print(t2 - t1)


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
