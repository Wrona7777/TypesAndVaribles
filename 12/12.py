# Programme for calculating 23% VAT on a given amount
kwota = float(input("Podaj kwotę (z VAT): "))

vat = kwota * 0.23

print(f"Amount  : {kwota:6.2f}")
print(f"VAT 23% : {vat:6.2f}")