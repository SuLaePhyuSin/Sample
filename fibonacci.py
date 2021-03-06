fibonacci.py

# fibonacci numbers module
#n = int(input('Please enter a number: '))

def fib(n): #write fibonacci series up to n
	a, b = 0, 1
	while a < n:
		print(a, end='')
		a, b = b, a+b
	print()

0 1 1 2 3 5 8 13 21 34 55 89 144e3e3e3e33eeee3e3e3ee3333323

#Go to Fibonacci Powerpoint

def fib2(n): #return fibonacci series up to n
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result


# >>> fib #import