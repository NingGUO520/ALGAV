from FileBinomiale import *
from tasMin import *
from xlwt import Workbook
import os
import time
import sys
from statistics import mean #pour calculer la moyenne de la liste

listeFichiers = os.listdir('./cles_alea')

# Comparer les temps d’exécution de SupprMin pour tas min et files binomiales
# la dictionnaire est de format {nbElement: (temps pour file_binomiale, temps pour Tasmin)}
def get_nbcles(dic):
    return dic[0] # retourne le 1nd element du tuple
# création du fichier Excel 
book = Workbook()

dic_supprMin = {}
dic_supprMin_moyen = {}
for x in [100,1000,10000,200,20000,500,5000,50000]:
	dic_supprMin_moyen[x]=([],[])
print("  En train d'écrire les données dans le fichier Q6_14_supprMin.xls.....")
for x in range(0,5):
	for n in range(x*8,x*8+8): #Ouvre les fichier de jeu_1
		with open('./cles_alea/'+listeFichiers[n], 'r') as fichier:
			texte = fichier.read()
			les_cles = texte.split("\n")
		l = []
		for ligne in les_cles :
			if not ligne == "" :
				l.append(ligne)
		fichier.close()
		########### calculer les temps d’exécution de ConsIter #############
		tas = TasMin()
		tas.ConsIter(l)
		
		f = file_binomiale()
		f = ConsIter(f,l)
		
		########### calculer les temps d’exécution de 10 fois Ajout #############
		debut_supp_tas = time.time()*1000
		tas.SupprMin()
		tas.SupprMin()
		tas.SupprMin()
		tas.SupprMin()
		tas.SupprMin()

		t_supp_tas = '{:f}'.format(time.time()*1000 - debut_supp_tas)

		debut_supp_fb = time.time()*1000
		f = f.SupprMin()
		f = f.SupprMin()
		f = f.SupprMin()
		f = f.SupprMin()
		f = f.SupprMin()

		t_supp_fb = '{:f}'.format(time.time()*1000 - debut_supp_fb)

		dic_supprMin[len(tas.liste)+5] = (float(t_supp_fb), float(t_supp_tas))
		dic_supprMin_moyen[len(tas.liste)+5][0].append(float(t_supp_fb))
		dic_supprMin_moyen[len(tas.liste)+5][1].append(float(t_supp_tas))


	# on tri par nombre de cles
	
	listeSupprMin = sorted(dic_supprMin.items(), key=get_nbcles)

	############## On crée un fichier Excel et on insère les données ###############

	# ajout d'une autre feuille  pour Ajout
	feuil3 = book.add_sheet("SupprMin_jeu_"+str(x+1))
	# ajout des en-têtes
	feuil3.write(0,0,'nombre de cles')
	feuil3.write(0,1,'temps d\'execution file binomiale (milliseconde)')
	feuil3.write(0,2,'temps d\'execution tas min (milliseconde)')

	# ajout des valeurs dans la ligne suivante
	i = 0
	for nbElement, temps in listeSupprMin : 
		i = i + 1
		ligne = feuil3.row(i)
		ligne.write(0,nbElement)
		ligne.write(1,temps[0])
		ligne.write(2,temps[1])
	# ajustement éventuel de la largeur d'une colonne
	feuil3.col(0).width = 5000
	feuil3.col(1).width = 10000
	feuil3.col(2).width = 10000

# ajout d'une autre feuille  pour caluler le moyen d'Ajout 
listeSupprMinMoyen = sorted(dic_supprMin_moyen.items(), key=get_nbcles)

feuil3 = book.add_sheet("SupprMin_moyen")
# ajout des en-têtes
feuil3.write(0,0,'nombre de cles')
feuil3.write(0,1,'temps d\'execution file binomiale (milliseconde)')
feuil3.write(0,2,'temps d\'execution tas min (milliseconde)')

# ajout des valeurs dans la ligne suivante
i = 0
for nbElement, temps in listeSupprMinMoyen : 
	i = i + 1
	ligne = feuil3.row(i)
	ligne.write(0,nbElement)
	ligne.write(1,mean(temps[0]))
	ligne.write(2,mean(temps[1]))
	# ajustement éventuel de la largeur d'une colonne
feuil3.col(0).width = 5000
feuil3.col(1).width = 10000
feuil3.col(2).width = 10000 
# création matérielle du fichier résultant
book.save('Q6_14_SupprMin.xls')

print(" Fin d'écriture dans fichier Q6_14_SupprMin.xls ")

