with open('Prob08.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

def format_time(seconds):
	s = 'Time to Mars: '
	days = seconds // 86400
	seconds -= days * 86400
	hours = seconds // 3600
	seconds -= hours * 3600
	minutes = seconds // 60
	seconds -= minutes * 60
	s += str(int(days)) + ' days, ' + str(int(hours)) + ' hours, ' + str(int(minutes)) + ' minutes, ' + str(int(seconds)) + ' seconds'
	return s

T = int(next_line())

for i in range(T):
	line = next_line()
	numbers = line.split(' ')
	for count, n in enumerate(numbers):
		numbers[count] = float(n)

	distance = numbers[0] * 1000000 # miles
	velocity = numbers[1] / 60 / 60 # miles per second

	time = distance / velocity # seconds

	print(format_time(time))
	


