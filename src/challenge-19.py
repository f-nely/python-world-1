"""
Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo
"""
from math import radians, sin, cos, tan

angle = float(input("Enter the angle you want? "))
angle = radians(angle)
print(f"The 30º angle has a sine of {(sin(angle)):.2f}")
print(f"The 30º angle has a cosine of {(cos(angle)):.2f}")
print(f"The 30º angle has a tangent of {(tan(angle)):.2f}")
