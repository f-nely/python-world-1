"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
"""
from math import trunc

value1 = float(input("Enter a number: "))
print(f"The amount entered was {value1} and its entire portion is {trunc(value1)}")