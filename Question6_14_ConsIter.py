from FileBinomiale import *
from tasMin import *
from xlwt import Workbook
import os
import time
import sys

listeFichiers = os.listdir('./cles_alea')

# Comparer les temps d’exécution de SupprMin pour tas min et files binomiales
# la dictionnaire est de format {nbElement: (temps pour file_binomiale, temps pour Tasmin)}

dic_ConsIter = {}
print("  En train d'écrire les données dans le fichier Q6_14.xls.....")
for n in range(0,8): #Ouvre les fichier de jeu_1
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
	debut_consIter_tas = time.time()*1000
	tas.ConsIter(l)
	t_consIter_tas = '{:f}'.format(time.time()*1000 - debut_consIter_tas)
	print("Temps d execution de ConsIter TasMin : %s millisecondes ---" % t_consIter_tas)

	f = file_binomiale()
	debut_consIter_fb = time.time()*1000
	f = ConsIter(f,l)
	t_consIter_fb = '{:f}'.format(time.time()*1000 - debut_consIter_fb)
	print("Temps d execution de ConsIter File binomiale : %s millisecondes ---" % t_consIter_fb)
	dic_ConsIter[f.nbElement()] = (float(t_consIter_fb),float(t_consIter_tas))

	
def get_nbcles(dic):
    return dic[0] # retourne le 1nd element du tuple
# on tri par nombre de cles
listeConsIter = sorted(dic_ConsIter.items(), key=get_nbcles)

############## On crée un fichier Excel et on insère les données ###############
# création du fichier Excel 
book = Workbook()

# ajout d'une autre feuille  pour ConsIter
feuil2 = book.add_sheet("ConsIter")
# ajout des en-têtes
feuil2.write(0,0,'nombre de cles')
feuil2.write(0,1,'temps d\'execution file binomiale (milliseconde)')
feuil2.write(0,2,'temps d\'execution tas min (milliseconde)')

# ajout des valeurs dans la ligne suivante
i = 0
for nbElement, temps in listeConsIter : 
	i = i + 1
	ligne = feuil2.row(i)
	ligne.write(0,nbElement)
	ligne.write(1,temps[0])
	ligne.write(2,temps[1])
# ajustement éventuel de la largeur d'une colonne
feuil2.col(0).width = 5000
feuil2.col(1).width = 10000
feuil2.col(2).width = 10000


# création matérielle du fichier résultant
book.save('Q6_14.xls')

print(" Fin d'écriture dans fichier Q6_14.xls ")

