###
# A program that calculates the volume
# and surface area of a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#a = 3, b = 4, c = 5 --> objętość = 94, powierzchnia = 60
#a = 8, b = 1, c = 2 --> objętość = 16, powierzchnia = 52
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

volume       = a * b * c
surface_area = 2 * (a*b + a*c + b*c)

print(f'Objętość prostopadłościanu: {volume}')
print(f'Pole powierzchni: {surface_area}')