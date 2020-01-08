import random

class Joueur:
    def __init__(self, nom, score):
        self.nom = nom
        self.score = score
 
score_J1, score_ordi = 0, 0
nom = input('Quelle est votre nom ? ')
choix_joueur = ['Pierre', 'Papier', 'Ciseaux']
ordinateur = Joueur('ordi', score_ordi)
# ['Ciseaux', 'Papier', 'Pierre']
renverser = True

def valeur_reverse(choix_J1, choix_ordi, renverser):
    if renverser is False and choix_J1 == 'Pierre':
        return 0
    elif renverser is False and choix_J1 == 'Ciseaux':
        return 2
    return choix_ordi

while score_J1 < 5 and score_ordi < 5:
    choix_ordi = random.choice([0, len(choix_joueur) - 1])
    print(choix_ordi)
    choix_J1 = None
    
    print('Ecrivez (Pierre/Papier/ciseaux) pour jouer ')
    choix_J1 = input(f"{nom}> ").capitalize()
    while choix_J1 != 'Pierre' and choix_J1 != 'Papier' and choix_J1 != 'Ciseaux':
        print("Soyez-sur que votre choix correspondent bien au choix si dessous ")
        print('Ecrivez (Pierre/Papier/ciseaux) pour jouer ')
        choix_J1 = input(f"{nom}> ").capitalize()
    print(choix_J1)
    if (choix_J1 == 'Ciseaux' and choix_ordi == 0) or (choix_J1 == 'Pierre' and choix_ordi == 2):
       renverser = False
    else:
        renverser = True

    for index, choix in enumerate(sorted(choix_joueur, reverse=renverser)):
        if choix == choix_J1:
            
            print(f'{nom}, Votre choix est {choix}')
            print(f"Le choix de l'ordi est {choix_joueur[choix_ordi]}")
            if index > valeur_reverse(choix_J1, choix_ordi, renverser):
                score_J1 += 1
                print(f"{choix} > {choix_joueur[choix_ordi]}")
            elif index < valeur_reverse(choix_J1, choix_ordi, renverser):
                score_ordi += 1
                print(f"{choix} < {choix_joueur[choix_ordi]}")
    print(f"{nom} :{score_J1} - {score_ordi}: ordi")
