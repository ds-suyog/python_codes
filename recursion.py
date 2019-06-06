
#factorial
def fact(n):
	if n<=1:
		return 1
	return n * fact(n-1)

#fibonacci
def fib(n):
    if n<=1:
        return 1
    return fib(n-1) + fib(n-2)

print(fact(5))
print(fib(5))