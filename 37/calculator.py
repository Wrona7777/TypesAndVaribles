liczba_użytkownika = int(input("Podaj liczbe całkowitą, którą chcesz przekonwertować: "))

konwersja_binarna = bin(liczba_użytkownika)
konwersja_hexadec = hex(liczba_użytkownika)

print("Podana liczba: ", liczba_użytkownika)
print("Konwersja binarna: ", konwersja_binarna)
print("Konwersja szesnastkowa: ", konwersja_hexadec)

#prefiks na początku sybolizuje jakiej konwersji dokonaliśmy