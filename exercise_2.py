

items = input("item to buy: ")
price = float(input("what is the price:$ "))
quantity = int(input("how many items: "))
total = price * quantity

print(f"you have bought:{items} and the {quantity} x {items}/s")
print(f"total price is: ${total}")
