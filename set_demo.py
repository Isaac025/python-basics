fruits = {"apple", "orange", "banana", "coconut", "pineapple"}
print(dir(fruits)) # prints all the methods available for a set
# print(help(fruits)) # prints the documentation for the set class
print(len(fruits)) # prints 5
print("banana" in fruits) # prints True

# print(fruits[0]) # prints set objects is not subscriptable, so we cannot access elements by index

# fruits.add("grapes") # adds "grapes" to the set
# fruits.remove("banana") # removes "banana" from the set
# fruits.pop() # removes a random element from the set
# fruits.clear() # removes all elements from the set

# sets dont work with indexing, slicing, or other sequence-like behavior. They are unordered collections of unique elements.

print(fruits) # prints the entire set
