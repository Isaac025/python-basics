
# name = input("Enter your Full name: ")
phone_number = input("Enter your phone number: ")

# result = len(name) # length of the string
# result = name.find("A") # find the index of the first space character
# result = name.rfind("a") # find the index of the last space character
# if the character is not found, it will return -1
# name = name.capitalize() # capitalize the first letter of the string
# name = name.upper() # convert the string to uppercase
# name = name.lower() # convert the string to lowercase
# is_digit = name.isdigit() # check if the string is a digit (returns a boolean)
# result = name.isalpha() # check if the string is alphabetic (returns a boolean)
# it results in false because of the space character, which is not an alphabetic character
# result = phone_number.count("-") # count the number of dashes in the phone number
result = phone_number.replace("-", "") # remove the dashes from the phone number
# the replace method does not change the original string, it returns a new string with the changes
# the replace method is case sensitive, it will only replace the exact match of the string
#  the replace method is one of the most commonly used string methods in Python, it is used to replace a specific substring with another substring in a string

print(help(str)) # this will print all the string methods available in Python, it is a very useful tool to learn about the different string methods and how to use them

print(result)