#MiniProjet Python : JEU DE DES

import random

print("Bienvenue dans le jeu de des")
print("Cliquez sur 0 pour quitter")
print("Cliquez sur 1 pour lancer le de")

while True:
 #Obligation de choisir un nombre
 x=int ( input("cliquez sur un bouton : ") )

 if x==0:
    print ("Fin du jeu")
    break

 elif x==1:
  print(random.randint(1, 6))

 else : 
  print("choix invalide")

#fin
  
# MiniProjet Python : Mot de passe aléatoire
  
print("Bienvenue dans le generateur de mot de passe aleatoire")
  
longueurMdp = int(input("Tapez le nombre de caractères du mot de passe : "))
caractèresPossibles = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789!@#$%^&*()_+"
password = "".join(random.sample(caractèresPossibles, longueurMdp))
print("Votre mot de passe est : ", password)

print("Fin du programme")

#fin

# MiniProjet Python : Génerateur d'un accronyme

print("Bienvenue dans le générateur d'accronyme")

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

print("Devinez le nombre entre 1 et 100")

nombreADeviner = random.randint(1, 100)
result == 0

for i in range(6):

    nombreTentative = int(input("Tapez un nombre : "))
    if nombreTentative == nombreADeviner:
        result == 1
    elif nombreTentative > nombreADeviner:
        print("Trop grand")
    elif nombreTentative < nombreADeviner:
        print("Trop petit")

if result == 1:
   print("Bravo ! Vous avez devine le nombre.")
   print(f"Le bon nombre est : {nombreADeviner}")
else:
   print("Dommage ! Vous n'avez pas devine le nombre.")
   print(f"Le bon nombre etait : {nombreADeviner}")    

print("Fin du programme")

#fin

# MiniProjet Python : Pierre Feuille Ciseaux

print("Jeu du Pierre Feuille Ciseaux")

choix = ["P", "F", "C"]
cpu = random.choice(choix)

print("Choisissez entre pierre, feuille ou ciseaux")
joueur =str(input("P: Pierre, F: feuille ou C:ciseaux ? ")).capitalize()

if joueur == cpu:
    print("Egalite")

elif joueur == "P":
    if cpu == "F":
        print("Perdu")
    elif cpu == "C":
        print("Gagne")

elif joueur == "F":
    if cpu == "C":
        print("Perdu")
    elif cpu == "P":
        print("Gagne")
        
elif joueur == "C":
    if cpu == "P":
        print("Perdu")
    elif cpu == "F":
        print("Gagne")