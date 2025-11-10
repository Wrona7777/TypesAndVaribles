price = float(input("Enter price: "))
discount_percent = float(input("Enter discount %: "))


discount_amount = price * discount_percent / 100

final_price = price - discount_amount

print(f"Price with discount: {final_price:.2f}")
print(f"Reduction: {discount_amount:.2f}")