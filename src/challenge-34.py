"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
"""

value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
value3 = int(input("Enter the third value: "))

# Check the lowest value
lowestValue = value1
if value2 < value1 and value2 < value3:
  lowestValue = value2
if value3 < value1 and value3 < value2:
  lowestValue = value3

# Check the highest value
highestValue = value2
if value1 > value2 and value1 > value3:
  highestValue = value1
if value3 > value1 and value3 > value2:
  highestValue = value3

print(f"The lowest value entered was {lowestValue}")
print(f"The highest value entered was {highestValue}")
