"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada
"""

from random import shuffle
students = list()
for i in range(0, 4):
    student = input("Enter the student's name: ")
    students.append(student)
    shuffle(students)
print(f"The order of presentation will be {students}")


