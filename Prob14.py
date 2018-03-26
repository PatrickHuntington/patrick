with open('Prob14.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line


class Directory():
	'''Directory() is a parent, has all children inside'''
	def __init__(self, name):
		self.name = name
		self.catalog = []

	def get_name(self):
		return self.name
	def set_name(self,name):
		self.name = name

	def add_dir(self,subdir):
		self.catalog.append(subdir)
	def rem_dir(self,subdir):
		self.catalog.remove(subdir)
	def check_catalog(self,subdir):
		if subdir in self.catalog:
			return True
		for i in self.catalog:
			check_catalog(subdir)
		return False



global_catalog = Directory("globe")

T = int(next_line())

for t in range(T):
	line = next_line()
	child, parent = line.split(',')

	if parent == 'None':
		global_catalog.add_dir(Directory(child))

	else:
		


	