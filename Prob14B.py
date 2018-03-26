with open('Prob14.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

catalog = {}

T = int(next_line())

for t in range(T):
	line = next_line()
	item, parent = line.split(',')

	if not parent in catalog:
		catalog[item] = []
	else:
		catalog[parent].append(item)


for key, value in catalog.items():
	value.sort()

for key, value in catalog.items():
	print(key + ' : ' + str(value))
