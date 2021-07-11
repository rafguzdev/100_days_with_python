from os import error

# FileNotFound------------------------------------------
try:
    file = open('nofile.txt')
except FileNotFoundError:
    file = open('nofile.txt', 'w')

# KeyError----------------------------------------------
dictionary = {'key': 'value'}
try:
    value = dictionary['non_existent_key']
except KeyError as error_message:
    print(f'The key {error_message} does not exist.')

# IndexError--------------------------------------------
lista = [1, 12, 22]
try:
    number = lista[4]
except IndexError as error_message:
    print(error_message)

# TypeError---------------------------------------------
text = 'abc'
try:
    print(text + 5)
except TypeError as error_message:
    print(error_message)

# Error handling----------------------------------------
try:
    # something that might cause an exception
    pass
except:
    # do this if there was an exception
    pass
else:
    # do this if there were no exceptions
    pass
finally:
    # do this no matter what happens
    pass

# Rasing own exceptions--------------------------------
try:
    open('test.txt')
except FileNotFoundError as message:
    print(message)
# finally:
#     raise FileNotFoundError('Error anyway')

height = float(input('Your height: '))
if height > 3:
    raise ValueError('Human height should not be over 3 meters.')