import random
from math import ceil

bille = random.randint(0, 49)
somme_mise = int(input("Saisissez le montant à miser: "))
gain = 0
numero_choisi = int(input("Montrer votre numéro: "))

if 0 <= numero_choisi <= 49:
    print("La valeur saisie est valide")
    if numero_choisi == bille:
        gain = somme_mise * 3
        somme_mise = somme_mise + gain
        print(f"Vous avez gagné et la somme gagné est: {gain} et votre nouveau solde est: {somme_mise}")
    elif numero_choisi != bille and (numero_choisi % 2 == 0 or numero_choisi % 2 != 0):
        gain = somme_mise / 2
        gain = ceil(gain)
        somme_mise = somme_mise + gain
        print(f"Vous avez la moitié de votre mise et la somme est: {gain} et votre nouveau solde est: {somme_mise}")
    else:
        gain = gain
        print("Vous avez perdu !")
else:
    print("La valeur saisie est invalide, veuillez réessayer.")



