from random import random
chosenNumber = round(random() * 10)

print("-=-" * 20)
userName = int(input("What number the computer thought? "))
print("-=-" * 20)

if userName == chosenNumber:
  print(f"Awesome! You are the champion. The number was {chosenNumber}!")
else:
  print(f"The computer won! The number was {chosenNumber}! Try again, buddy.")
