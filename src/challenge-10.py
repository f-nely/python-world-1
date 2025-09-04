"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere U$$1.00 = R$3.27
"""

cash = float(input("How much money do you have in your wallet? R$"))
print(f"With R${cash} you can buy U${(cash/3.27):.2f}")