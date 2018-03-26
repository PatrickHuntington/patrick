with open('Prob01.in.txt','r') as f:
	lines = f.read().splitlines()

bookmark = 0

T = int(lines[bookmark])
bookmark += 1

for i in range(T):
	print(lines[bookmark])
	print(lines[bookmark])
	bookmark += 1
