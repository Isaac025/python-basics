# indexing = accessing elements of a sequence using [] (indexing operator)
#             [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[4]) # prints the fifth character of the string
print((credit_number[0:4])) # prints the first four characters of the string
print(credit_number[:4]) # prints the characters from index 0 to 3
print(credit_number[4:8]) # prints the characters from index 4 to 7
print(credit_number[5:]) # prints the characters from index 5 to the end of the string
print((credit_number[-1])) # prints the last character of the string
print((credit_number[::2])) # prints every second character of the string
print((credit_number[::-1])) # prints the string in reverse order
print((credit_number[::3])) # prints every third character of the string

last_digits = credit_number[-4:] # prints the last four characters of the string
print(f"XXXXX-XXXX-XXXX-{last_digits}") # prints the last four characters of the string with X's in place of the other characters

