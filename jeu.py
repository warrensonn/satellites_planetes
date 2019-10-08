 
 
 
 

def score(planete, nb_satellite_reel):
 while planete != -1:
  phrase = "Nombre de satellite(s) de la planète " + planete + ": "
  sat =int(input(phrase))
  while sat - nb_satellite_reel != 0:
   if sat - nb_satellite_reel >0:
    print("trop haut, retente ! ")
    sat = int(input(phrase))
   if sat - nb_satellite_reel < 0:
    print("trop bas, retente !")
    sat = int(input(phrase))
  if sat - nb_satellite_reel == 0: 
   print()
   print("bravo, tu as trouvé le nombre de satellite(s) de", planete, "la planète la plus éloignée du soleil, qui est de", nb_satellite_reel, "!")     
   print()
   planete = -1
   return planete 
  







sat = -1
planete = 0
P = ("Mercure, Vénus, Terre, Mars, Jupiter, Saturne, Uranus et Neptune !")



while planete!="404": #résumé du but du programme et annonce de la planète choisie
 if planete == 0:
  sat = -1
  P = ("Mercure, Vénus, Terre, Mars, Jupiter, Saturne, Uranus et Neptune !")
  print("Ce programme a pour but de vous faire découvrir le nombre de satellites naturels que possèdent les planètes de notre système solaire !")
  print()
  print("Tu auras donc le choix entre les huit planètes de notre système, dans l'ordre:")
  print(P)
  print()
  print("Pour quelle planète voudras-tu découvrir le nombre de satellites qu'elle possède ?")
  planete = str(input("nom de la planète choisie: ")) #premiere demande de la planete choisie
  print()
 if planete == -1:
  print("tu peux taper 404 pour quitter le programme ou bien continuer en choisissant une nouvelle planète !")
  print()
  print("Je te rappelle les planètes du système solaire pour que tu puisses en choisir une autre:")
  print(P)
  print()
  planete = str(input("nom de la planète choisie: "))
  print()
 elif planete=="Mercure" or planete=="mercure" or planete=="Vénus" or planete=="vénus" or planete=="Terre" or planete=="terre" or planete=="Mars" or planete=="mars" or planete=="Jupiter" or planete=="jupiter" or planete=="Saturne" or planete=="saturne" or planete=="Uranus" or planete=="uranus" or planete=="Neptune" or planete=="neptune": 
  print("ok, tu vas devoir deviner le nombre de satellite(s) que la planète", planete, "possède !")
  if planete == "Mercure" or planete == "mercure":
   planete = score(planete, 0)
  if planete == "Vénus" or planete == "vénus":
   score(planete, 0)
  if planete == "Terre" or planete == "terre":
   score(planete, 1)
  if planete == "Mars" or planete == "mars":
   score(planete, 2)
  if planete == "Jupiter" or planete == "jupiter":
   score(planete, 79)
  if planete == "Saturne" or planete == "saturne":
   score(planete, 62)
  if planete == "Uranus" or planete == "uranus":
   score(planete, 27)
  if planete == "Neptune" or planete == "neptune":
   score(planete, 14)   
 else:
  print("Vérifiez bien l'orthographe du nom des planêtes ! :)")
  print("La liste des planètes est:", P)
  print()
  planete = str(input("Nom de la planète choisie: "))
  print()
  
  
  
  
  
  
  
  
  
  
  
 
  
  
  
  
  
  
  
  
  
  