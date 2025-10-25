distance = int(input("Enter distance in km: "))
fuel_price = float(input("Enter fuel price per liter: "))
fuel_consumption = float(input("Enter fuel consumption per 100km: "))

total_fuel_consumption = (0.01 * distance) * fuel_consumption
total_cost = total_fuel_consumption * fuel_price

print("Total fuel usage: ", total_fuel_consumption)
print("Total cost generated: ", total_cost)