with open('Prob12.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line


T = int(next_line())

for t in range(T):
	N = int(next_line())
	balance = 0
	balances = []
	days = []
	for n in range(N):

		line = next_line()
		raw_data = line.split(',')
		day = int(raw_data[0])
		days.append(day)
		charge, payment = 0, 0
		if raw_data[1]:
			charge = float(raw_data[1])
		if raw_data[2]:
			payment = float(raw_data[2])
		
		balance += charge
		balance -= payment
		balances.append(balance)

	# Calculate monthly interest
	num_days = max(days)
	sum_balances = sum(balances)
	interest_charges = (sum_balances / num_days) * (0.18 / 12)
	print('${0:.2f}'.format(interest_charges))

