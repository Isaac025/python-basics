# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable, Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. No duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut", "pineapple",]

print(fruits[1])  # prints "orange"
print(fruits[3]) # prints "coconut"
# print(fruits[4]) # IndexError: list index out of range
print(fruits[0:3]) # prints ['apple', 'orange', 'banana']
print(fruits[::2]) # prints ['apple', 'banana']
print(fruits[::-1]) # prints ['coconut', 'banana', 'orange', 'apple']



# to list the different methods available for a list, we can use the dir() function
# print(dir(fruits))

# help is a built-in function that can be used to get more information about a specific method or function. For example, we can use help() to get more information about the append() method for lists.
# print(help(fruits))
print(len(fruits)) # prints 4
print("banana" in fruits) # prints True
print("grapes" in fruits) # prints False
# fruits[1] = "grapes" # changes the first element of the list to "grapes"
# fruits.append("grapes") # adds "grapes" to the end of the list
# fruits.remove("banana") # removes "banana" from the list
# fruits.insert(2, "kiwi") # adds "kiwi" to the list at index 2
# fruits.sort() # sorts the list in alphabetical order
# fruits.reverse() # reverses the order of the list
# fruits.clear() # removes all elements from the list
# print(fruits.index("banana")) # prints 2
print(fruits.count("banana")) # prints 1
print(fruits.count("watermelon")) # prints 0


# for fruit in fruits:
#     print(fruit) # prints each fruit in the list

print(fruits) # prints the entire list
