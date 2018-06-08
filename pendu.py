#!/usr/local/bin/python
#created and developed by Firologame

import os

debut = 1

while debut == 1:
	motchaine = str()
	fin = 0
	i = 0
	faute = 0
	espaces= str("-")
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Entrez le mot à faire deviner")
	motchaine = input()
	motchaine = motchaine.lower()
	motchaine0 = motchaine
	nbrlettre = len(motchaine)

	for i in range(1,nbrlettre):
		espaces = espaces+"-"
		motchaine2 = list(espaces)
		motchaine2 = ''.join(motchaine2)
		i+=1
	debut = 0

while fin == 0 :
	os.system('cls' if os.name == 'nt' else 'clear')
	print(faute,"erreur(s) sur 10")
	print("")
	print("")
	print(motchaine2)
	print("")
	print("")
	print('Entrez une lettre : ', end='', flush=True)
	choix = input()
	choix = choix.lower()
	p = motchaine.find(choix)
	if p == -1:
#		print("cette lettre n'existe pas")
		faute+=1
	elif p>-1 and p<nbrlettre+1:
#		print("cette lettre existe")
		motchaine2.count(choix)
		motchaine2 = list(motchaine2)
		position = motchaine.find(choix)
		motchaine = list(motchaine)
		motchaine[position] = " "
		motchaine = ''.join(motchaine)
		motchaine2[position] = choix
		motchaine2 = ''.join(motchaine2)
	if faute == 10:
		fin = 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("Vous avez perdu !")
		print("Le mot à trouver était : ",motchaine0,".")
		print("")
		print("")
		input("Appuyez sur la touche ENTREE pour quitter...")
		break
	if motchaine2 in motchaine0:
		fin = 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("C'est gagné !!!")
		print("Vous avez trouvez le mot ",motchaine0," avec ",faute," faute(s).")
		print("")
		print("")
		input("Appuyez sur la touche ENTREE pour quitter...")
		break
#created and developed by Firologame
