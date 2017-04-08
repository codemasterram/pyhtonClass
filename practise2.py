n , sum = 0 , 0

while n<5:
	value=input("Enter number  	")

	try:
		value=float(value)
		sum=sum + n
		n += 1
	except ValueError:
		print('Input Error.Please enter a valid number.')
	
print('Sum of entered number is {}'.format(sum))


 