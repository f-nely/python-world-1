"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e sua raiz quadrada
"""
import math

num = int(input("Enter a number: "))

print(f"Double {num} is {num*2}.")
print(f"Triple {num} is {num*3}.")
print(f"The square root of {num} is {math.sqrt(num):.2f}.")