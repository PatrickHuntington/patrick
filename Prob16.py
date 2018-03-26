import itertools

with open('Prob16.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line


def operate(expression):
	# expression input, i.e. [4, '*', 3, '/', 9], converts & returns
	return eval(''.join(expression))



def check_expression(line):
	# format data into target, integers and operators
	target, scramble = line.split(':')
	target = int(target)
	#print('target = ' + str(target))
	
	in_and_op = scramble.split(' ')
	expressions = list(itertools.permutations(in_and_op))


	for i in range(len(expressions)):
		try:
			exp = ''.join(expressions[i])
			if int(eval(exp)) == target:
				return True
		except:
			pass

	return False



T = int(next_line())

for t in range(T):
	line = next_line()

	print('TRUE' if check_expression(line) else 'FALSE')
	# ternary operators
