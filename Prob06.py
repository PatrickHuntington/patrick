with open('Prob06.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

ICAO = {'A':'Alpha','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo','F':'Foxtrot','G':'Golf','H':'Hotel','I':'India','J':'Juliet','K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar','P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango','U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankee','Z':'Zulu',' ':' '}

T = int(next_line())

for i in range(T):
	N = int(next_line())

	for j in range(N):
		line = next_line()
		characters = list(line)

		for count, char in enumerate(characters):
			characters[count] = characters[count].upper()
			characters[count] = ICAO[characters[count]]

		s = '-'.join(characters)
		s = s.replace('- -',' ')
		print(s)