"""
Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra 'A'
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez
"""
sentence = str(input("Type a sentence: ")).lower().strip()
print(f"A letra A aparece {sentence.count('a')} vezes na frase")
print(f"A primeira letra A apareceu na posição {sentence.index('a')}")
print(f"A última letra A apareceu na posição {sentence.rindex('a')}")