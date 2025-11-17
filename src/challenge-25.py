"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome
"""
fullName = str(input("Type your full name: ")).lower().strip()
print(f"Your name has Silva? {'silva' in fullName}")