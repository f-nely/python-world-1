"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
"""

width = float(input("Enter a width: "))
height = float(input("Enter a height: "))
area = width*height
print(f"Your wall measures {width} x {height} and has an area of {area}m²")
print(f"To paint this wall, you will need {area/2}l gallons of paint.")