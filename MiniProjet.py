#MiniProjet Python : JEU DE DES

import random

print("Bienvenue dans le jeu de des")
print("Cliquez sur 0 pour quitter")
print("Cliquez sur 1 pour lancer le de")

while True:
 #Obligation de choisir un nombre
 x=int ( input("cliquez sur un bouton : ") )

 if x==0:
    print ("Bye Bye")
    break

 elif x==1:
  print(random.randint(1, 6))

 else : 
  print("choix invalide")

#fin
  
# MiniProjet Python : Mot de passe aléatoire
  
longueurMdp = int(input("Tapez le nombre de caractères du mot de passe : "))
caractèresPossibles = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789!@#$%^&*()_+"
password = "".join(random.sample(caractèresPossibles, longueurMdp))
print("Votre mot de passe est : ", password)

#fin

# MiniProjet Python : Génerateur d'un accronyme

nom = str(input("Entrez votre nom et prenom : "))
pseudo = nom.split()

print("votre nom est : ", nom)
print("votre pseudo est : ", pseudo)