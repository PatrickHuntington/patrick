with open('Prob02.in.txt','r') as f:
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
	words = line.split(' ')
	ind = int(words[1])
	newstr = words[0][:ind] + words[0][ind+1:]
	print(newstr)