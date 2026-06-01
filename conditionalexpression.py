# conditional expression = A one line shortcut for the if-else statemenr (Tenary operator)
#                          print or assign one of two values based on a condition
#                          X if condition else Y

num = 113
a = 6
b = 7
age = 14
temperature = 12
user_role = "admin"

# print("Positive" if num > 0 else "Negative") # X = true, Y = false
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Minor"
# weather = "Hot" if temperature >= 20 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Restricted Access"

print(access_level)
