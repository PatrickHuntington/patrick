with open('Prob07.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

weight = {'BB':0,'K':0,'1B':1,'2B':2,'3B':3,'HR':4}

T = int(next_line())

for i in range(T):
	final_string = ''
	line = next_line()
	sections = line.split(':')
	final_string += sections[0]
	data = sections[1].split(',')
	at_bats = 0
	score = 0

	for j in data:
		if j == 'BB':
			pass
		else:
			at_bats += 1
			score += weight[j]

	if at_bats == 0:
		slg = 0
	else:
		slg = score / at_bats
	final_string += '=' + '{0:.3f}'.format(slg)
	print(final_string)