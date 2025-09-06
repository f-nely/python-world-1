"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
"""

product = float(input("How much does this product cost? R$"))
newValue = product - (product * 0.05)

print(f"The product cost R${product}, but with the 5% discount promotion, it will cost R${(newValue):.2f}")