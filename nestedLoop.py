# nested loop = a loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

# for x in range(3): # outer loop
#     for y in range(1, 10): # inner loop
#         print(y, end="") # print numbers 1-9 on the same line opposite of end="/n"
#     print() # print a newline after each inner loop

# outer loop is charge of the rows
# inner loop is in charge of the columns

for x in range(rows): # outer loop
    for y in range(columns): # inner loop
        print(symbol, end="") # print the symbol on the same line opposite of end="/n"
    print() # print a newline after each inner loop
