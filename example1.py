names = ['John Doe','Jane Doe','Johnu turk']

# Change the first name in the list
names[0] = 'Foo Bar'
print('Names npw:', names)

#Append some more names
names.append('Molly Mormon')
names.append('Joe Bloggs')
print('Names finally:',names)
print('Last name in the list: %s' % names[-1])

#You can join lists using str.join() method

joined_names = '\n'.join(names)
print('\nList of Names:')
print(joined_names)
