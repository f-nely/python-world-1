"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome
"""
fullName = input("Type your name: ").strip()
f = fullName.split()
nameWithoutSpace = fullName.replace(" ", "")
print("Analyzing your name..")
print(f"Your name in capital letters {fullName.upper()}")
print(f"Your name in lowercase letters {fullName.lower()}")
print(f"Your name has {len(nameWithoutSpace)} letters ")
print(f"Your first name is {f[0]} and has {len(f[0])} letters")