"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

speed = float(input("What is the car's speed? "))

if speed > 80:
  print("Fined. You have exceeded the speed limit of 80 km/h.")
  multa = (speed - 80) * 7.00
  print(f"You must pay a fine of R${multa}.")

print("Have a good day! Drive carefully!")