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

	kw_indices = []
	for j in range(len(kw)):
		kw_index = ABC.index(kw[j])
		kw_indices.append(kw_index)

	count = 0
	encr = []
	for j in range(len(text_in)):

		offset = kw_indices[count % len(kw_indices)]
		letter = text_in[j]
		if letter == ' ':
			pass
		else:
			number = ABC.index(letter)
			number += offset
			if number >= len(ABC):
				number -= 26
			letter = ABC[number]
			count += 1

		encr.append(letter)
	encr_text = ''.join(encr)


	print(encr_text)