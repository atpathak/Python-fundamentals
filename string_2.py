print('hello'.capitalize())

# Return a new string where all characters are lower case
print('Hello'.lower())
print('WORLD'.lower())

# Check whether all characters are numeric.
print('1337'.isdecimal())
print('p2p'.isdecimal())

# Check whether all characters are alpha.
print('hello'.isalpha())
print('p2p'.isalpha())

# Find the index of the first occurance of a substring. 
print('hello'.find('l'))
print('world'.find('l'))

# Check the end of a string.
print('hello'.endswith('o'))
print('world'.endswith('o'))
print('world'.endswith('rld'))

# Split a string into a list of strings at each instance of a
# substring.
print('The-quick-brown-fox'.split('-'))

# Join a list of strings into one single string. Try passing a
# different string into this method.
print('_'.join(['The', 'quick', 'brown', 'fox']))

# "Format" a string by replacing `{}` with the arguments you
# supply to the function.
print('Player {} has {} hit points remaining'.format(1, 42))
print('My favorite drink is {} with {} dashes of {}'.format('whiskey', 3, 'bitters'))

