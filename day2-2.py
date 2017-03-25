#The for loop



# # loop over a list of numbers
# for num in [1,2,3,4,5,6,7,8,9,10]:
# 	print(num)
# print('---')

# # Do the same thing using range.
# for num in range(10):
# 	print(num + 1)

# list and the for loop


# names = ['John Doe','Jane Doe','Jonny Turk','Molly Mormon']
# print('Users:')


# for name in names:
# 	end = '     \nand \n' if name == names[-2] else '\n'


# 	print(' - %s' % name, end=end)	


# index in the loop


names = ['John Doe','Jane Doe','Jonny Turk','Molly Mormon']

for (index, value) in enumerate(names):
	print ('%d \t %s'%(index, value))