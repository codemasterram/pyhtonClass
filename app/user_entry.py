#i = 1
my_list = []
def user_entry():
	while True:
		
	#n = int(input('enter the number of users: '))
	#while i <= n:		
		name = input('enter first name: ')
		last = input('enter last name: ')
		email = input('enter email: ')
		address = input('enter your address: ')
		user_info = { 'name': name, 'last': last, 'email':email, 'address':address }
		my_list.append(user_info)

		try_again=input('do you want to enter moer (Y/N): ')
		if try_again.upper() != 'Y':
			break
	
	print('users: ', my_list)

user_entry()
