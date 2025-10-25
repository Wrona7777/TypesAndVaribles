import math

def odleglosc_do_horyzontu(h):
    """
    Oblicza odległość do horyzontu na podstawie wysokości obserwatora.
    h - wysokość w metrach
    Zwraca odległość w kilometrach
    """
    return 3.57 * math.sqrt(h)

# Pobieranie wysokości od użytkownika
try:
    h = float(input("Podaj wysokość obserwatora w metrach: "))
    if h < 0:
        print("Wysokość nie może być ujemna!")
    else:
        d = odleglosc_do_horyzontu(h)
        print(f"Odległość do horyzontu z wysokości {h} metrów wynosi {d:.2f} kilometrów.")
except ValueError:
    print("Proszę podać prawidłową liczbę!")