"""
Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
"""

n = int(input("Enter a number: "))

for i in range(1, 11):
  print(f"{n} x {i} = {n*i}")