from arbreRecherche import *
import time
from xlwt import Workbook
import os
import sys

# with open('cles_alea/jeu_1_nb_cles_500.txt', 'r') as fichier:
# 	texte = fichier.read()
# 	les_cles = texte.split("\n")
# l = []
# for ligne in les_cles :
# 	if not ligne == "" :
# 		l.append(ligne)
# fichier.close()


# a = ArbreBinareDeRecherche()

# a.ConsIter(l)
# start_time = time.time()

# res = a.rechercherRecursif("0xfbcefeaa6e4e3561d34738e083fed211")
# print("Temps d execution : %s secondes ---" % '{:f}'.format(time.time() - start_time))
# print("Nombre d'élément ",nbElements(a.racine))
# a.printTree()
# print(res)
def get_nbcles(dic):
	return dic[0] # retourne le 1nd element du tuple
listeFichiers = os.listdir('./cles_alea')
# création du fichier Excel 
book = Workbook()
dic_recherche = {}
print("  En train d'écrire les données dans le fichier Q2_4_5.xls.....")
for x  in range(0,5): 
	for n in range(x*8,x*8+8): #Ouvre les fichier de jeu_1
		with open('./cles_alea/'+listeFichiers[n], 'r') as fichier:
			texte = fichier.read()
			les_cles = texte.split("\n")
			l = []
			for ligne in les_cles :
				if not ligne == "" :
					l.append(ligne)
			fichier.close()
		########### calculer les temps d’exécution de Recherche #############
		a = ArbreBinareDeRecherche()
		a.ConsIter(l)
		start_time = time.time()
		res = a.rechercherRecursif("0x6573f512c63ab9947e5f6704d4961585")
		t = time.time() - start_time
		print("Temps d execution : %s secondes ---" % t)
		print("Nombre d'élément ",nbElements(a.racine))
		dic_recherche[nbElements(a.racine)] = t

	# on tri par nombre de cles
	listeRecherche = sorted(dic_recherche.items(), key=get_nbcles)
	############## On crée un fichier Excel et on insère les données ###############
		
	# création de la feuille 
	feuil1 = book.add_sheet("Recherche_Jeu_" + str(x+1))
		# ajout des en-têtes
	feuil1.write(0,0,'nombre de cles')
	feuil1.write(0,1,'temps d\'execution de recherche')
		

	# ajout des valeurs dans la ligne suivante
	i = 0
	for nbElement, temps in listeRecherche : 
		i = i + 1
		ligne = feuil1.row(i)
		ligne.write(0,nbElement)
		ligne.write(1,temps)
		

	# ajustement éventuel de la largeur d'une colonne
	feuil1.col(0).width = 5000
	feuil1.col(1).width = 10000
	feuil1.col(2).width = 10000

	# création matérielle du fichier résultant
book.save('TestArbre_recherche.xls')
print(" Fin d'écriture dans le fichier TestArbre_recherche.xls ")

