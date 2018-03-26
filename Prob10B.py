with open('Prob10.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

top_row = ['tab','q','w','e','r','t','y','u','i','o','p']
mid_row = ['cap','a','s','d','f','g','h','j','k','l']
bot_row = ['shi','z','x','c','v','b','n','m',',','.']

T = int(next_line())

for t in range(T):
	N = int(next_line())
	caps_lock = False
	for n in range(N):

		line = next_line()
		line_length = len(line)
		new_line = ''

		for i in range(line_length):
			key = line[i]
			uppercase = key.isupper()
			is_space = key == ' '
			key = key.lower()
			
			index, new_index, new_key = None, None, None

			if key in top_row:
				index = top_row.index(key)
				new_index = (index - 1) % len(top_row)
				new_key = top_row[new_index]

			elif key in mid_row:
				index = mid_row.index(key)
				new_index = (index - 1) % len(mid_row)
				new_key = mid_row[new_index]

			elif key in bot_row:
				index = bot_row.index(key)
				new_index = (index - 1) % len(bot_row)
				new_key = bot_row[new_index]


			if new_key == 'cap':
				caps_lock = not caps_lock
				new_key = ''
			elif new_key == 'tab':
				new_key = '    '
			elif is_space:
				new_key = ' '

			if caps_lock:
				new_key = new_key.upper()

			if uppercase:
				if caps_lock:
					new_key = new_key.lower()
				else:
					new_key = new_key.upper()


			new_line = new_line + new_key

		print(new_line)

