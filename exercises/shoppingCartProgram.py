# shopping cart program

foods = []
prices = []
total = 0

# tuples are not used bcos they are unchangeable and we need to add items to the list
#  not using sets bcos sets are unordered and we need to maintain the order of items in the list

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    # total = total + price
    total += price

print()
print(f"Your total is ${total}")
