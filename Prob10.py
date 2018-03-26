with open('Prob10.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

top_row = ['tab','q','w','e','r','t','y','u','i','o','p']
mid_row = ['cap','a','s','d','f','g','h','i','j','k','l']
bot_row = ['shi','z','x','c','v','b','n','m',',','.']

caps_lock = False

T = int(next_line())

for t in range(T):
	N = int(next_line())
	for n in range(N):

		text_in = next_line()
		text_out = ''

		for i in range(len(text_in)):
			char = text_in[i]

			if char in top_row:
				char_index = top_row.index(char.lower())
				char_index = (char_index - 1) % len(top_row)
				char = top_row[char_index]
				if char == 'tab':
					char = '    '

			elif char in mid_row:
				char_index = mid_row.index(char.lower())
				char_index = (char_index - 1) % len(mid_row)
				char = mid_row[char_index]
				if char == 'cap':
					caps_lock = not caps_lock

			elif char in bot_row:
				char_index = bot_row.index(char.lower())
				char_index = (char_index - 1) % len(bot_row)
				char = bot_row[char_index]

			if caps_lock:
				char = char.upper()
			else:
				char = char.lower()

			text_out += char

		print(text_out)


'''
TODO:
- natural uppercase letters
- fix that first h it's supposed to be a g
- fix all the other letters, some are accurate some aren't
- fix the tab, it's just one space atm
'''