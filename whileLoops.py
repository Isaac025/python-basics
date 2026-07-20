# while loop = execute code WHILE some conditions remains true

name = input("Enter your name: ")

if name == "":
    print("You didn't enter your name.")
else:
    print(f"Hello {name}!")

while name == "":
    print("You did not enter your name.")
    name = input("Enter your name: ")
print(f"Hello {name}!")

# we could potentially create an infinite loop if we don't change the condition in the while loop, so we need to make sure that we change the condition in the while loop so that it eventually becomes false and the loop stops executing

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"Your age is {age}!")

food = input("Enter a food you like (enter 'q' to quit): ")

while not food == "q":
    print(f"Your favorite food is {food}.")
    food = input("Enter a food you like (enter 'q' to quit): ")
print("bye")

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid. Please try again.")
    num = int(input("Enter a # between 1 - 10: "))

print(f"your number is {num}")