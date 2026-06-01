# logical operators = evaluate multiple conditions (and, or, not )
                      # or = at least one condition must be true
                      # and = all conditions must be true   
                      # not = inverts the condition or reverses the result, returns false if the result is true

# temp = 20
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#   print("The outdoor event is cancelled")
# else:
#   print("The outdoor event is still scheduled to go on")

temp = -2
is_sunny = False

if temp >= 28 and is_sunny:
  print("It is hot and sunny outside 🥵☀")
  print("Go to the beach")
elif temp <= 0 and is_sunny:
  print("It is cold but sunny outside 🥶☀")
  print("Go skiing")
elif 28 > temp > 0 and is_sunny:
  print("It is warm and sunny outside 🙂☀")
  print("Go for a walk")
elif temp >= 28 and not is_sunny:
  print("It is hot and cloudy outside 🥵☁")
  print("Stay indoors")
elif temp <= 0 and not is_sunny:
  print("It is cold and cloudy outside 🥶☁")
  print("Stay indoors")
elif 28 > temp > 0 and not is_sunny:
  print("It is warm and cloudy outside 🙂☁")
  print("Stay indoors")