with open('Prob03.in.txt', 'r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

T = int(next_line())

for i in range(T):
	line = next_line()
	numbers = line.split(' ')
	num1 = int(numbers[0])
	num2 = int(numbers[1])
	add = num1 + num2
	mult = num1 * num2
	print(str(add) + ' ' + str(mult))