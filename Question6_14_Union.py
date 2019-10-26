from FileBinomiale import *
from tasMin import *
from xlwt import Workbook
import os
import time
import sys
from statistics import mean #pour calculer la moyenne de la liste

listeFichiers = os.listdir('./cles_alea')
def get_nbcles(dic):
	    return dic[0] # retourne le 1nd element du tuple

# création du fichier Excel 
book = Workbook()

# Comparer les temps d’exécution de Union pour tas min et files binomiales
# la dictionnaire est de format {nbElement: (temps pour Tasmin, temps pour file_binomiale)}
dic_Union = {}
dic_Union_moyen = {}
print("  En train d'écrire les données dans le fichier Q6_14_Union.xls.....")
for x in [200,2000,20000,400,40000,1000,10000,100000]:
	dic_Union_moyen[x]=([],[])
#### On fait Union de jeu-1 et jeu-2, jeu2 et jeu3 .... avec les données de même taille
for x in range(0,4):
	for n in range(x*8,x*8+8): 
		#Ouvre les fichier de jeu_1 et mettre les données dans l1
		l1 = []
		with open('./cles_alea/'+listeFichiers[n], 'r') as fichier:
			texte = fichier.read()
			les_cles = texte.split("\n")
			for ligne in les_cles :
				if not ligne == "" :
					l1.append(ligne)
			fichier.close()

		#Ouvre les fichier de jeu_2 et mettre les données dans l2
		l2 = []
		with open('./cles_alea/'+listeFichiers[n+8], 'r') as fichier:
			texte = fichier.read()
			les_cles = texte.split("\n")
			for ligne in les_cles :
				if not ligne == "" :
					l2.append(ligne)
			fichier.close()

		tas = TasMin()
		tas.ConsIter(l1)
		tas2 = TasMin()
		tas2.ConsIter(l2)

		f1 = file_binomiale()
		f1 = ConsIter(f1,l1)
		f2 = file_binomiale()
		f2 = ConsIter(f2,l2)
		########### calculer les temps d’exécution de Union #############
		
		debut_Union_tas = time.time()*1000
		newtas1 = tas.Union(tas2)
		newtas2 = tas2.Union(tas)
		t_Union_tas = '{:f}'.format(time.time()*1000 - debut_Union_tas)
		print("Temps d execution d\'Union tas min  : %s millisecondes ---" % t_Union_tas)

		debut_Union_fb = time.time()*1000
		f3 = UnionFile(f1,f2)
		f4 = UnionFile(f2,f1)
		t_Union_fb = '{:f}'.format(time.time()*1000 - debut_Union_fb)
		print("Temps d execution d\'Union file binomiale : %s millisecondes ---" % t_Union_fb)

		dic_Union[f3.nbElement()] = (float(t_Union_tas),float(t_Union_fb))
		dic_Union_moyen[f3.nbElement()][0].append(float(t_Union_tas))
		dic_Union_moyen[f3.nbElement()][1].append(float(t_Union_fb))
		
	# on tri par nombre de cles
	listeUnion = sorted(dic_Union.items(), key=get_nbcles)

	############## On crée un fichier Excel et on insère les données ###############
	

	# création de la feuille 
	feuil1 = book.add_sheet("Union_jeu_"+str(x+1)+"_jeu_"+str(x+2))
	# ajout des en-têtes
	feuil1.write(0,0,'nombre de cles après Union')
	feuil1.write(0,1,'temps d\'execution structure tas min')
	feuil1.write(0,2,'temps d\'execution structure file binomiale')

	# ajout des valeurs dans la ligne suivante
	i = 0
	for nbElement, temps in listeUnion : 
		i = i + 1
		ligne = feuil1.row(i)
		ligne.write(0,nbElement)
		ligne.write(1,temps[0])
		ligne.write(2,temps[1])


	# ajustement éventuel de la largeur d'une colonne
	feuil1.col(0).width = 8000
	feuil1.col(1).width = 8000
	feuil1.col(2).width = 8000

listeUnion_moyen = sorted(dic_Union_moyen.items(), key=get_nbcles)
# création de la feuille 
feuil1 = book.add_sheet("Union_moyen")
# ajout des en-têtes
feuil1.write(0,0,'nombre de cles après Union')
feuil1.write(0,1,'temps d\'execution structure tas min')
feuil1.write(0,2,'temps d\'execution structure file binomiale')

# ajout des valeurs dans la ligne suivante
i = 0
for nbElement, temps in listeUnion_moyen : 
	i = i + 1
	ligne = feuil1.row(i)
	ligne.write(0,nbElement)
	ligne.write(1,mean(temps[0]))
	ligne.write(2,mean(temps[1]))


# ajustement éventuel de la largeur d'une colonne
feuil1.col(0).width = 8000
feuil1.col(1).width = 8000
feuil1.col(2).width = 8000


# création matérielle du fichier résultant
book.save('Q6_14_Union.xls')
print(" Fin d'écriture ")