#MiniProjet Python : JEU DE DES

import random

print("Bienvenue dans le jeu de des")
print("Cliquez sur 0 pour quitter")
print("Cliquez sur 1 pour lancer le de")

while True:
 #Obligation de choisir un nombre
 x=int ( input("cliquez sur un bouton "))

 if x==0:
    print ("Bye Bye")
    break

 elif x==1:
  print(random.randint(1, 6))

 else : 
  print("choix invalide")

  


