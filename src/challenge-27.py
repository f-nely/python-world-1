"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
"""
fullName = str(input("Type your first name: ")).lower().strip()
f = fullName.split()
print("Nice to meet you!")
print(f"Your first name is {f[0]}")
print(f"Your last name is {f[len(f) - 1]}")