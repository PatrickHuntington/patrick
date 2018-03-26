from math import sqrt

with open('Prob04.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

def Fib(n):
	a,b = 0,1
	i = 0
	while i < n:
		a, b = b, a + b
		i += 1
	return a

T = int(next_line())

for i in range(T):
	index = int(next_line())
	print(str(index) + ' = ' + str(Fib(index)))

