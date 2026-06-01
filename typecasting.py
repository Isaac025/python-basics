# Typecasting = the process of converting a variable from one data type to another 
#               str(), int(), float(), bool()

name = ""
age = 25
gpa = 3.2
is_student = True

print(type(is_student))

gpa = int(gpa)
print(gpa)

age = str(age)

age += "1"

print(age)

name = bool(name)
print(name)