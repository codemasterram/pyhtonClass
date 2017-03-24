# Store a list of user information in a list of dictionaries.
#  Each user's information would contain: 
#  first & last name, email and address. 
#  Ask the user to input an email address. 
#  Print the first user's information found by that email address. 
#  Print "Email not found" message if user with email not found. 
#  (Hint: List comprehension)

data = [
    {
        'name': 'Kabir Baidhya',
        'email': 'kabirbaidhya@gmail.com'
    },
    {
        'name': 'John Doe',
        'email': 'johndoe@example.com'
    }
]

# Print information from the dictionary
if data==['Kabir Baidhya']:
	print(data[1])
print('Name: %s' % data[1]['name'])
print('Email: %s' % data[1]['email'])
