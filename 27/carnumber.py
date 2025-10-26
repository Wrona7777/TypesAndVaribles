car_number = input("Podaj numer auta ")  
is_krakow = car_number[0:2] == "KR"

if is_krakow:
    print("Auto jest z krakowa")
else:
    print("Nie jest z krakowa")