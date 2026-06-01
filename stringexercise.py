# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

# username.find(" ")  # returns -1 if not found, otherwise returns index of first occurrence
# username.isalpha() # returns True if all characters are letters and there is at least one character, otherwise returns False

if len(username) > 12:
    print("Your Username cant be  more than 12 characters.")
elif not username.find(" ") == -1:
    print("Your Username can't contain spaces.")
elif not username.isalpha():
    print("Your Username can't contain digits.")
else:
    print(f"welcome {username}!")
