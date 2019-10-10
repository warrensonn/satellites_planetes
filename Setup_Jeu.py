import Fonction_Jeu_Planete

from Fonction_Jeu_Planete import *


sat = -1
planete = 0
P = ("Mercure, Vénus, Terre, Mars, Jupiter, Saturne, Uranus et Neptune !")



while planete!="404": #condition pour que le programme ne s'arrete pas
 if planete == 0:#résumé du but du programme et annonce de la planète choisie
  sat = -1
  P = ("Mercure, Vénus, Terre, Mars, Jupiter, Saturne, Uranus et Neptune !")
  print("Ce programme a pour but de vous faire découvrir le nombre de satellites naturels que possèdent les planètes de notre système solaire !")
  print()
  print("Tu auras donc le choix entre les huit planètes de notre système, dans l'ordre:")
  print(P)
  print()
  print("Pour quelle planète voudras-tu découvrir le nombre de satellites qu'elle possède ?")
  planete= annonce() #premiere demande de la planete choisie
  print()
 if planete == -1: #après premiere planète, pour ne pas remettre le résumé
  print("Tu peux taper 404 pour quitter le programme ou bien continuer en choisissant une nouvelle planète !")
  print()
  print("Je te rappelle les planètes du système solaire pour que tu puisses en choisir une autre:")
  print(P)
  print()
  planete= annonce() #toutes les autres fois ou l'utilisateur saisira une planete
  print()
 elif planete=="Mercure" or planete=="Vénus" or planete=="Terre" or planete=="Mars" or planete=="Jupiter" or planete=="Saturne" or planete=="Uranus" or planete=="Neptune": 
  print("ok, tu vas devoir deviner le nombre de satellite(s) que la planète", planete, "possède !")
  if planete == "Mercure" or planete == "mercure":
   planete = score(planete, 0)
  if planete == "Vénus" or planete == "vénus":
   planete = score(planete, 0)
  if planete == "Terre" or planete == "terre":
   planete = score(planete, 1)
  if planete == "Mars" or planete == "mars":
   planete = score(planete, 2)
  if planete == "Jupiter" or planete == "jupiter":
   planete = score(planete, 79)
  if planete == "Saturne" or planete == "saturne":
   planete = score(planete, 62)
  if planete == "Uranus" or planete == "uranus":
   planete = score(planete, 27)
  if planete == "Neptune" or planete == "neptune":
   planete = score(planete, 14)
 else:
  print("Vérifie bien l'orthographe du nom des planêtes ! :)")
  print("La liste des planètes est:", P)
  print()
  planete = annonce()
  print()

  
  
  
  
  
  
  
  
 
  
  
  
  
  
  
  
  
  
  