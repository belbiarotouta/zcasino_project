from random import randint
from math import ceil

argent = 2000
continuer_partie = True

print(f"Vous vous installez à la table de roulette avec {argent} euro(s).")

while continuer_partie:  # Tant qu'on doit continuer la partie.
     # on demande à l'utilisateur de saisir le nombre sur lequel il va miser.
    nombre_mise = -1
    while nombre_mise < 0:
        nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
        # On convertit le nombre misé.
        try:
            nombre_mise = int(nombre_mise)
            if nombre_mise < 0 or nombre_mise > 49:
                raise ValueError
        except ValueError:
            print("Vous n'avez pas saisi de nombre valide.")
            nombre_mise = -1
    mise = -1
    while mise <= 0 or mise > argent:
        mise = input("Tapez le montant de votre mise : ")
        # On convertit la mise
        try:
            mise = int(mise)
            if mise <= 0 or mise > argent:
                raise ValueError
        except ValueError:
            print("Vous n'avez pas saisi de mise valide.")
            mise = -1
    # Le nombre misé et la mise ont été sélectionnés par l'utilisateur, on fait tourner la roulette.
    numero_gagnant = randint(0, 49)
    print(f"La roulette tourne.... ... et s'arrête sur le numéro {numero_gagnant}.")

    # On établit le gain du joueur.
    if numero_gagnant == nombre_mise:
        print(f"Félicitations ! Vous obtenez {mise * 3} euro(s) !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2:  # ils sont de la même couleur.
        mise = ceil(mise * 0.5)
        print(f"Vous avez misé sur la bonne couleur. Vous obtenez {mise}")
        argent += mise
    else:
        print("Désolé l'ami, ce n'est pas pour cette fois. Vous perdez votre mise")
        argent -= mise

    #  On interrompt la partie si le joueur est ruiné.
    if argent <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False
    else:
        # On affiche l'argent du joueur
        print(f"Vous avez à présent {argent} euro(s).")
        match input("Souhaitez-vous quitter le casino (o/n) ? ").lower():
            # l'utilisateur entre 'o' ou '0'
            case "o":
                print("Vous quittez le casino avec vos gains.")
                continuer_partie = False

