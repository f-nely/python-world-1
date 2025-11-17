"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'
"""
city = str(input("Which city were you born in? ")).lower().strip()
print(city[:5] == "santo")