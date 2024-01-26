import random

while True:

 x=int ( input("cliquez sur un bouton "))

 if x==0:
    print ("Bye Bye")
    break

 elif x==1:
  print(random.randint(1, 6))