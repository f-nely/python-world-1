"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça
um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
"""
from random import choice
students = list()
for i in range(0, 4):
    name = input("Enter the student's name: ")
    students.append(name)

print(f"The student chosen was {choice(students)}")