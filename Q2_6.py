from tasMin import *
from tasMinArbre import *
from xlwt import Workbook
from statistics import mean #pour calculer la moyenne de la liste
import os
import time
import sys

def get_nbcles(dic):
	return dic[0] # retourne le 1nd element du tuple
listeFichiers = os.listdir('./cles_alea')
# création du fichier Excel 
book = Workbook()

# Comparer les temps d’exécution d'Union pour tas min de structure tableau  et de structure arbre
# la dictionnaire est de format {nbElement: (temps pour structure tableau temps, et pour structure Arbre)}
dic_Union = {}
dic_liste_moyen = {}
for i in [200,400,1000,2000,10000,20000,40000,100000]:
	dic_liste_moyen[i] = ([],[])
print("  En train d'écrire les données dans le fichier Q2_6.xls.....")

for x in range(0,4):
	#### On fait Union de jeu-1 et jeu-2 avec les données de même taille
	for n in range(x*8,8*x+8): 
		#Ouvre les fichier de jeu_1 et mettre les données dans l1
		with open('./cles_alea/'+listeFichiers[n], 'r') as fichier:
			texte = fichier.read()
			les_cles = texte.split("\n")
		l1 = []
		for ligne in les_cles :
			if not ligne == "" :
				l1.append(ligne)
		fichier.close()

		#Ouvre les fichier de jeu_2 et mettre les données dans l2
		with open('./cles_alea/'+listeFichiers[n+8], 'r') as fichier:
			texte = fichier.read()
			les_cles = texte.split("\n")
		l2 = []
		for ligne in les_cles :
			if not ligne == "" :
				l2.append(ligne)
		fichier.close()

		########### calculer les temps d’exécution de Union #############
		tas_1 = TasMin()
		tas_1.ConsIter(l1)
		tas_2 = TasMin()
		tas_2.ConsIter(l2)
		# print("nb elelment tas 1",len(tas_1.liste) )
		# print("nb elelment tas 2",len(tas_2.liste) )
		debut_Union_tas = time.time()*1000
		newtas = tas_1.Union(tas_2)
		# print("nb elelment tas 1",len(tas_1.liste) )
		t_Union_tas = time.time()*1000 - debut_Union_tas


		tasArbre_1 = TasMinArbre()
		tasArbre_1.ConsIter(l1)
		tasArbre_2 = TasMinArbre()
		tasArbre_2.ConsIter(l2)
		debut_Union_tasArbre = time.time()*1000
		newTas = TasMinArbre.union(tasArbre_1,tasArbre_2)
		t_Union_tasArbre = time.time()*1000 - debut_Union_tasArbre

		dic_Union[len(newtas.liste)] = (t_Union_tas,t_Union_tasArbre)
		dic_liste_moyen[len(newtas.liste)][0].append(t_Union_tas)
		dic_liste_moyen[len(newtas.liste)][1].append(t_Union_tasArbre)
	# on tri par nombre de cles
	listeUnion = sorted(dic_Union.items(), key=get_nbcles)

	############## On crée un fichier Excel et on insère les données ###############
		
	# création de la feuille 
	feuil1 = book.add_sheet("Union_jeu_"+str(x+1)+"_jeu_" +str(x+2))
	# ajout des en-têtes
	feuil1.write(0,0,'nombre de cles après Union')
	feuil1.write(0,1,'temps d\'execution structure tableau')
	feuil1.write(0,2,'temps d\'execution structure arbre')

	# ajout des valeurs dans la ligne suivante
	i = 0
	for nbElement, temps in listeUnion : 
		i = i + 1
		ligne = feuil1.row(i)
		ligne.write(0,nbElement)
		ligne.write(1,temps[0])
		ligne.write(2,temps[1])


	# ajustement éventuel de la largeur d'une colonne
	feuil1.col(0).width = 5000
	feuil1.col(1).width = 10000
	feuil1.col(2).width = 10000

liste_moyen = sorted(dic_liste_moyen.items(), key=get_nbcles)
# création de la feuille 
feuil = book.add_sheet("Union_moyen")
	# ajout des en-têtes
feuil.write(0,0,'nombre de cles après Union')
feuil.write(0,1,'temps d\'execution en moyen structure tableau')
feuil.write(0,2,'temps d\'execution en moyen structure arbre')

# ajout des valeurs dans la ligne suivante
i = 0
for nbElement, temps in liste_moyen : 
	i = i + 1
	ligne = feuil.row(i)
	ligne.write(0,nbElement)
	ligne.write(1,mean(temps[0]))
	ligne.write(2,mean(temps[1]))


	# ajustement éventuel de la largeur d'une colonne
feuil.col(0).width = 5000
feuil.col(1).width = 10000
feuil.col(2).width = 10000

# création matérielle du fichier résultant
book.save('Q2_6.xls')
print(" Fin d'écriture ")
