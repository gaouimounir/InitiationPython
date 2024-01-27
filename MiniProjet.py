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

print("Devinez le nombre")

nombreADeviner = random.randint(1, 100)
nombreTentative = int(input("Tapez le nombre : "))