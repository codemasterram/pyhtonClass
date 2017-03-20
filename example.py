# you can create even create new lists by precessing existing lists.

words = ['this','is','just','a','test']
capitalize_words = [x.capitalize() for x in words]

print('Words: ',words)
print('Capitalized Words:', capitalize_words)

# can use it for filtering the list items as well.
words = ['hello' 'world','foo','bar','test','python','is','awesome']
short_words = [x for x in words if len(x) <=3]
other_words = [x for x in words if x not in short_words]
words_with_e = [x for x in words if x.count('e') >= 1]

print("\n Words:", words)
print('\nShort Words:', short_words)
print('\nOther Words:', other_words)
print('\nWords with "e":', words_with_e)