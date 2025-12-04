"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
"""
salary = float(input("What is the employee's salary? R$ "))

if salary > 1250:
  NewSalary = salary + (salary * 0.1)
else:
  NewSalary = salary + (salary * 0.15)

print(f"Those who earned R$ {salary} will earn R$ {NewSalary} now")