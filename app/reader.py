def read(filename):
	'''
	It should read the file with 'filename'
	and return it's contents.
	'''
	f = open(filename, 'r')
	data = f.read()
	f.close()
	return data
	
