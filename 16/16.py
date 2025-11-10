###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"

skrot = ""

for slowo in university.split():
    skrot = skrot + slowo[0].upper()

print(skrot)