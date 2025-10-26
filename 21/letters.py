first = input('Enter first letter: ')
last = input('Enter last letter: ')

first_code = ord(first)
last_code = ord(last)

number_of_letters = (last_code - first_code)-1

if number_of_letters < 0:
    number_of_letters = 0

print(f'Between {first} and {last} is {number_of_letters} letters')