with open('Prob15.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

def str_to_int(digit):
	return int(digit)


def find_straight(list_in):
	numbers = list_in
	for n in numbers:
		if n + 1 in numbers and n + 2 in numbers and n + 3 in numbers and n + 4 in numbers:
			return True
	return False



T = int(next_line())

for t in range(T):
	line = next_line()

	digits = list(map(str_to_int,list(line)))
	while 0 in digits:
		digits.remove(0)

	groups = {}
	for i in digits:
		groups[i] = digits.count(i)

	values = list(groups.values())
	max_count = max(values)

	s = ''

	if max_count == 5:
		s = 'FIVE OF A KIND'
	elif max_count == 4:
		s = 'FOUR OF A KIND'
	elif 3 in values and 2 in values:
		s = 'FULL HOUSE'
	elif find_straight(digits):
		s = 'STRAIGHT'
	elif max_count == 3:
		s = 'THREE OF A KIND'
	elif values.count(2) > 1:
		s = 'TWO PAIR'
	elif values.count(2) == 1:
		s = 'PAIR'
	else:
		s = str(max(digits))

	print(line + ' = ' + s)