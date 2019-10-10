def score(planete, nb_satellite_reel):
 while planete != -1:
  phrase = "Nombre de satellite(s) de la planète " + planete + ": "
  sat =int(input(phrase))
  while sat - nb_satellite_reel != 0:
   if sat - nb_satellite_reel >0:
    print("trop haut, retente !")
    sat = int(input(phrase))
   if sat - nb_satellite_reel < 0:
    print("trop bas, retente !")
    sat = int(input(phrase))
  if sat - nb_satellite_reel == 0:
   print()
   print("bravo, tu as trouvé le nombre de satellite(s) de", planete, "qui est de", nb_satellite_reel, "!")
   print()
   planete = -1
   return planete
  

  
def annonce():
 return str(input("nom de la planète choisie: ").capitalize().strip()) #premiere demande de la planete choisie