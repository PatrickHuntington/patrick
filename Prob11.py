with open('Prob11.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

def reverse_word(word):
	ret = ''
	for i in range(len(word)):
		if word[i].isalnum():
			ret = word[i] + ret
	return ret

def char_filter(s):
	chars = list(s)
	char_info = []
	for i in range(len(chars)):
		char = chars[i]
		char_info.append(int(char.isupper()) + (2*(int(char == ' '))) + 3*(int(not char.isalnum())))
	return char_info

T = int(next_line())

for t in range(T):
	line = next_line()
	words = line.split(' ')
	rev = None
	'''
	for i in range(len(words)):
		words[i] = reverse_word(words[i])
	print(' '.join(words))
	'''
	print(char_filter(line))

		