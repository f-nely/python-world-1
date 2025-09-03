# Arithmetic Operators

"""
Ordem de Precedência
1 ⟶ ()
2 ⟶ **
3 ⟶ * / // %
4 ⟶ + -
"""

n1 = int(input("Enter a value: "))
n2 = int(input("Enter another value: "))

# addition
print("Sum: {}".format(n1+n2))

# subtraction
print ("Subtraction: {}".format(n1-n2))

# multiplication
print ("Multiplication: {}".format(n1*n2)) 

# division
print ("Division: {:.3f}".format(n1/n2))

# floor division
print("Floor Division: {}".format(n1//n2))

# modulo
print("Modulo: {}".format(n1%n2))

# n1 to the power n2
print("Power: {}".format(n1**n2))