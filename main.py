# this is my first python program
print("I like Beans")
print("It is really good")

# A variable = A conatiner for a value (string, integer, float, boolean)
#              A variable behaves as if it was the value it conatains

#Strings
first_name = "Bro"
food = "Beans"
email = "johndoe@gmail.com"

print(first_name)
print(f"Hello {first_name} ")
print(f"You like {food}")
print(f"Your email is {email}")


#integers -- whole numbers
age = 25
quantity = 3
students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {students} students")

#Float - floating point number (decimal )
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"you ran {distance}km")

#Boolean (True or false)
is_student = False
for_sale = False
is_online = True

print(f"Are you a student?: {is_student}")

if is_student: 
  print("You are a student")
else:
  print("You are not a student")

if for_sale:
  print("That item is for sale")
else:
  print("That item is not available")

if is_online:
  print("you are online")
else:
  print("you are offline")