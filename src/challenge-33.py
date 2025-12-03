"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto
"""

from datetime import datetime

currentDatetime = datetime.now()
currentYear = currentDatetime.year

year = int(input("Which year do you wish to analyze? Enter 0 to analyze the current year: "))
if year == 0:
  year = currentYear

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print(f"O ano {year} é bissexto")
else:
  print(f"O {year} não é bissexto")