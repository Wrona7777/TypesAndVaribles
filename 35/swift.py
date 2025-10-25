swift = input(str("Podaj kod swift: "))
swift_size = len(swift)

if swift_size == 8 or swift_size == 11:
    print(f'Bank Code: {swift[:4]}')
    print(f'Country Code: {swift[4:6]}')
else:
    print("To nie jest kod swift")