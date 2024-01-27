#MiniProjet Python : JEU DE DES

import random

print("Bienvenue dans le 1er projet de jeu de des")

while True:
 
 print("Cliquez sur 0 pour quitter")
 print("Cliquez sur 1 pour lancer le de")

 x=( input("cliquez sur un bouton : ") )

 if x=="0":
    print ("Fin du jeu")
    break

 elif x=="1":
  print(random.randint(1, 6))

 else : 
  print("choix invalide")

#fin
  
# MiniProjet Python : Mot de passe aléatoire
  
print("Bienvenue dans le 2eme projet de generateur de mot de passe aleatoire")
  
longueurMdp = int(input("Tapez le nombre de caractères du mot de passe : "))
caractèresPossibles = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789!@#$%^&*()_+"
password = "".join(random.sample(caractèresPossibles, longueurMdp))
print("Votre mot de passe est : ", password)

print("Fin du programme")

#fin

# MiniProjet Python : Génerateur d'un accronyme

print("Bienvenue dans le 3eme projet de générateur d'accronyme")

nom = str(input("Entrez votre nom et prenom : "))

def accroGen(pseudo):
  mots = pseudo.split()
  accronyme = ""
  for i in mots:
    accronyme = accronyme + str (i[0]).upper()
  return accronyme

result = accroGen(nom)

print("votre accronyme est : ", result)

print("Fin du programme")

#fin

# MiniProjet Python : Devine le nombre

print("Bienvenue dans le 4eme projet de deviner le nombre")
print("Devinez le nombre entre 1 et 100")

nombreADeviner = random.randint(1, 100)
result = 0

for i in range(6):

    nombreTentative = int(input("Tapez un nombre : "))
    if nombreTentative == nombreADeviner:
        result = 1
        break
    elif nombreTentative > nombreADeviner:
        print("Trop grand, le nombre a trouver est plus petit")
    elif nombreTentative < nombreADeviner:
        print("Trop petit, le nombre a trouver est plus grand")

if result == 1:
   print("Bravo ! Vous avez devine le bon nombre.")
   print(f"Le nombre a deviner etait : {nombreADeviner}")
   
else:
   print("Dommage ! Vous n'avez pas devine le bon nombre.")
   print(f"Le bon nombre etait : {nombreADeviner}")    

print("Fin du programme")

#fin

# MiniProjet Python : Pierre Feuille Ciseaux

print("Bienvenue dans le 5eme projet de Pierre Feuille Ciseaux")
print("Jeu du Pierre Feuille Ciseaux")
print("Le Premier arrive a 3 points gagne !")

choix = ["P", "F", "C"]
scoreJoueur = 0
scoreCpu = 0

while True:

    cpu = random.choice(choix)

    print("Choisissez entre pierre, feuille ou ciseaux")
    joueur =str(input("P: Pierre, F: feuille ou C:ciseaux ? ")).capitalize()

    if joueur == cpu:
        print("Egalite")

    elif joueur == "P":
        if cpu == "F":
            print("Perdu")
            scoreCpu += 1
        elif cpu == "C":
            print("Gagne")
            scoreJoueur += 1

    elif joueur == "F":
        if cpu == "C":
            print("Perdu")
            scoreCpu += 1
        elif cpu == "P":
            print("Gagne")
            scoreJoueur += 1

    elif joueur == "C":
        if cpu == "P":
            print("Perdu")
            scoreCpu += 1
        elif cpu == "F":
            print("Gagne")
            scoreJoueur += 1

    print(f"Score : Joueur {scoreJoueur} point // Cpu {scoreCpu} point")

    if scoreJoueur == 3 or scoreCpu == 3:
        print("Fin du jeu")
        if scoreJoueur == 3:
            print("Bravo vous avez gagne")
        elif scoreCpu == 3:
            print("Dommage vous avez perdu")
        break

#fin