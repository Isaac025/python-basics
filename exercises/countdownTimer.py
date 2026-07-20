import time

my_time = int(input("Enter the countdown time in seconds: "))

for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1) # wait for 1 second

print("TIME'S UP!")

time.sleep(3) # wait for 3 seconds


for x in range(my_time, 0, -1): # countdown from my_time to 1
    print(x)
    time.sleep(1) # wait for 1 second

print("TIME'S UP!")

for x in range(my_time, 0, -1): # countdown using didgital clock format
    seconds = x % 60 # get the seconds
    minutes = int(x /60) % 60 # get the minutes
    hours = int(x / 3600) # get the hours
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) # wait for 1 second

print("TIME'S UP!")


