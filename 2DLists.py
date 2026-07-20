# a 2 dimensional list is a list made up of lists
# it is really useful if you need a grid or matrix of data, kind of like an excel spreadsheet

# fruits =      ["apple", "orange", "banana", "coconut"]
# vegetables =  ["celery", "carrots", "potatoes"]
# meats =       ["chicken", "fish", "turkey"]

# each of the list above is a 1 dimensional list
# arranging each list in away that will kind of represents a grid or matrix with rows and columns. 
# each individual list resembles a row. Each element resembles a column

["apple", "orange", "banana", "coconut"]






groceries = [["apple", "orange", "banana", "coconut"], 
            ["celery", "carrots", "potatoes"], 
            ["chicken", "fish", "turkey"]]

# fruits[0] = 'pineapple'
# print(fruits)

print(groceries[1][2])

# to iterate over each element in each row, we use a  nested loop
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# groceries = (("apple", "orange", "banana", "coconut"), 
#             ("celery", "carrots", "potatoes"), 
#             ("chicken", "fish", "turkey"))
# you can make a 2D tuple that is made up of tuples

# groceries = ({"apple", "orange", "banana", "coconut"}, 
#             {"celery", "carrots", "potatoes"}, 
#             {"chicken", "fish", "turkey"})

# you can also make a tuple made up of sets

