# Problem 11: Drow Lasrever | 25 Points

# Custom code to open and read the file line by line, get the next line in the file with next_line()
with open('Prob11.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line


def filter_word(word):
	# Creates filter for the word, True/False is upper/lowercase and punctuation is from the original string.
	letters = list(word)

	filt = []
	
	for i in range(len(letters)):
		if letters[i].isalnum():
			filt.append(letters[i].isupper())
		else:
			filt.append(letters[i])
		letters[i] = letters[i].lower()

	return filt

def remove_punct(word):
	# Removes all punctuation from the word. Punctuation data is already stored in the filter.
	letters = list(word)
	removal = []
	for i in letters:
		if not i.isalnum():
			removal.append(i)
		for i in removal:
			letters.remove(i)
	return ''.join(letters)

def reverse_word(word):
	# Reverses the word in lowercase
	return remove_punct(word)[::-1].lower()

def apply_filter(zipped_word):
	# Applies filter data to the reversed word, fixing capitalization and adding punctuation. Returns string
	word, data = zipped_word # 'reversed word', [capitals and punctuation]
	letters = list(word)
	for count, i in enumerate(data):
		if type(i) == type(True): # if type boolean --> character was alphanumeric
			if i: # if True --> character was uppercase
				letters[count] = letters[count].upper()
		else: # if not boolean --> character was punctuation so shove it back in where it was
			letters.insert(count, i)

	word = ''.join(letters)
	return word

def process(line):
	# Manages filter, words and data. Then processes data and returns to a string for printing.
	word_list = line.split(' ') # turn line into list of words

	filters = list(map(filter_word, word_list))
	reversed_words = list(map(reverse_word, word_list))
	zipped_list = list(zip(reversed_words, filters))
	
	final_words = list(map(apply_filter, zipped_list))
	final_line = ' '.join(final_words) # turn list of words back into line
	return final_line

	# all in one line because it looks cool and why not
	# return ' '.join(list(map(apply_filter, list(zip(list(map(reverse_word, line.split(' '))), list(map(filter_word, line.split(' '))))))))


T = int(next_line()) # number of test cases

for t in range(T):
	line = next_line() # store next line in string
	print(process(line)) # prints formatted reversed line