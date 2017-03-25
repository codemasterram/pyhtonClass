"""while loop

"""
# ram=0

# while ram<=10:
# 	print("Hello",ram)
# 	ram+= 1


# n = 0
# sum = 0

# # clculate the sum of 5 numbers entred by the user
# while n < 5 :
# 	value = input('Enter Number %s: '% (n+1))
# 	sum = sum + float(value)
# 	n += 1
# print('Sum =  %.2f' % sum) #   %.2f lae chai float pachadi ko decimal place determine garchha


# a=0
# b=1
# n=25

# while a<n:
# 	print(a)
# 	(a,b) = (b,a+b)

# List and the while loop

names = ['Ram Sapkota','G','Ronit','Sonima']
i=0
totals_names = len(names)
print('Users')

while i< totals_names:
	end = 'and \n' if i== totals_names - 2 else '\n'
	print('   %s ' % names[i],end=end)
	i+=1