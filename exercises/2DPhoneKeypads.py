#  the elements in a set are unordered, so we can't use sets
#  a tuple is faster than a list and it is ordered and unchangeable

num_pad = ((1, 2, 3), 
           (4, 5, 6), 
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
