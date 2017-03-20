names = ['john doe' , 'jane doe' , 'jhonny']
names[0] = 'foo bar'
print('names now:' , names)
names.append('molly mormon')
names.append('joe bloggs')
print(' names finally:',names)
print('last name in the list: %s' % names[-1])
joined_names = '\n'.join(names)
print('nlist of names:')
print(joined_names)