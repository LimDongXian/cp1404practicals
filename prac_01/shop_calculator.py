DISCOUNT_THRESHOLD = 100
DISCOUNT = 0.1  # 10%

total_price = 0

number_item = int(input("Number of items: "))
for i in range(number_item):
    item_price = float(input("Price of item: "))
    while item_price < 0:
        print("Invalid number of items!")
        item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > DISCOUNT_THRESHOLD:
    total_price = total_price * (1 - DISCOUNT)  # minus 1 to show the price after discount
print(f"Total price for {number_item} items is ${total_price:.2f}")
