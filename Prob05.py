with open('Prob05.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

def remove_duplicates(l):
	return list(set(l))

def list_string(l):
	return ','.join(l)

T = int(next_line())

for i in range(T):
	last_donors_raw = next_line().split(',')
	current_donors_raw = next_line().split(',')

	last_year = []
	this_year = []
	both_year = []

	for donor in last_donors_raw:
		if donor in current_donors_raw:
			both_year.append(donor)
		else:
			last_year.append(donor)

	for donor in current_donors_raw:
		if donor in last_donors_raw:
			both_year.append(donor)
		else:
			this_year.append(donor)

	last_year = remove_duplicates(last_year)
	this_year = remove_duplicates(this_year)
	both_year = remove_duplicates(both_year)

	last_year.sort()
	both_year.sort()
	this_year.sort()

	print(list_string(last_year))
	print(list_string(both_year))
	print(list_string(this_year))
