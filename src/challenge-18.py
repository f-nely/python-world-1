"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
"""
# from math import sqrt
from math import hypot
oppositeSide = float(input("What is the width of the opposite side? "))
adjacentSide = float(input("What is the width of the adjacent side? "))
# hypotenuse = sqrt(pow(oppositeSide, 2) + pow(adjacentSide, 2)) 
hypotenuse = hypot(oppositeSide, adjacentSide)

print(f"The hypotenuse will measure {(hypotenuse):.2f}")