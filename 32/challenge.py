import random

computer = random.randint(1,6)

you = int(input("Zgaduj zakres 1-6: "))

if computer == you:
    print("Wygrales")
else:
    print(f"Przegrales, poprawna to {computer}")