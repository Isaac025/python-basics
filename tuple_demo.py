fruits = ("apple", "orange", "banana", "coconut", "pineapple")

print(dir(fruits)) # prints all the methods available for a tuple
# print(help(fruits)) # prints the documentation for the tuple class
print(len(fruits)) # prints 5
print("banana" in fruits) # prints True
print("grapes" in fruits) # prints False

print(fruits.index("banana")) # prints 2
print(fruits.count("coconut")) # prints 1

# print(fruits)
for fruit in fruits:
    print(fruit) # prints each fruit in the tuple