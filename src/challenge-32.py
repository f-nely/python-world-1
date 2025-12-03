"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas
"""

distance = float(input("What is the distance of your trip? "))

print(f"You are about to start a {distance}km journey.")

if distance <= 200:
  prince = distance * 0.50
else:
  prince = distance * 0.45

print(f"And the price of your trip will be R${prince}")