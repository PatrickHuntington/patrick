with open('Prob09.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

T = int(next_line())

for i in range(T):
	text_in = next_line()
	kw = next_line()

	print('keyword ' + kw)

	# full keyword to iterate
	text_in_len = len(text_in)
	kw_len = len(kw)
	full_kw = ''
	for j in range(text_in_len):
		if text_in[j] == ' ':
			full_kw += ' '
		else:
			full_kw += kw[j%kw_len]
	# full keyword is full_kw

	print('full keyword ' + full_kw)

	text_out = ''

	# encript every character separately
	for k in range(text_in_len):
		
		if text_in[k] == ' ':
			text_out += ' '
		else:
			kw_char = full_kw[k]
			kw_char_index = ABC.find(kw_char)
			encr = ABC[kw_char_index:]
			encr += ABC[:kw_char_index]

			char = text_in[k]
			char_index = ABC.find(char)

			encr_char = encr[char_index]

			text_out += encr_char
	

	#print(text_out)