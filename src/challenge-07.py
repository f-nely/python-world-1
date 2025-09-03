"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
"""
g1 = float(input("Enter the student's first grade: "))
g2 = float(input("Enter the student's second grade: "))

average = (g1 + g2) / 2

print(f"The average between {g1} and {g2} is {(average):.1f}")