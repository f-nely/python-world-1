"""
Escreva um programa que leia um valor em metro e o exiba convertido em centímetros e milímetros
"""

d = float(input("Enter a distance in meters: "))

print(f"The measurement is {d} meters corresponds to ")
print(f"{d/1000}km")
print(f"{d/100}hm")
print(f"{d/10}dam")
print(f"{d*10}dm")
print(f"{d*100}cm")
print(f"{d*1000}mm")