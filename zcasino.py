from random import randint
from math import ceil

bille = randint(0, 49)
budget = 2000
gain = 0

try:
    numero_choisi = int(input("Montrer votre numéro: "))
    somme_mise = int(input("Saisissez le montant à miser: "))
    if 0 <= numero_choisi <= 49:
        if numero_choisi == bille:
            gain = somme_mise * 3
            budget += gain
            print(f"Vous avez le bon numéro et vous avez obtenu un gain de {gain}")
            print(f"Votre budget actualisé est de: {budget}")
        elif numero_choisi % 2 == 0 or numero_choisi % 2 != 0:
            gain = ceil(somme_mise * 0.5)
            budget += gain
            print(f"Vous avez le bon numéro et vous avez obtenu un gain de {gain}")
            print(f"Votre budget actualisé est de: {budget}")
        elif budget < 0 or somme_mise > budget:
            print("Vous n'avez plus de fond, partie terminée.")
    raise ValueError
except ValueError:
        print("Le numéro est invalide, veuillez saisir un numéro compris entre 0 et 49.")




