"""
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
"""

num = int(input("Type any number: "))

if num % 2 == 0:
  print(f"The number {num} is Par")
else:
  print(f"The number {num} is Ímpar")