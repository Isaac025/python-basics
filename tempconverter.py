unit = input("is this temperature in Celsius or Fahrenheit? (C or F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9/5) + 32, 1)
    print(f"The temperature in celsius is {temp}ºF")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
    print(f"The temperature in fahrenheit is {temp}ºC")
else:
    print(f"{unit} is not a valid unit of measurement")

