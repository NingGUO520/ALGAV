from FileBinomiale import *
from xlwt import Workbook
from statistics import mean #pour calculer la moyenne de la liste
import os
import time
import sys
#
# Pour la question 3.10:
# Utiliser les jeux de données aléatoires afin de vérifier graphiquement la complexité
# temporelle de la fonction ConsIter
#

def get_nbcles(dic):
	return dic[0] # retourne le 1nd element du tuple

listeFichiers = os.listdir('./cles_alea')
# création du fichier Excel 
book = Workbook()

# la dictionnaire est de format {nbElement: temps de ConsIter pour file binomiale}
dic_ConsIter = {}

# la dictionnaire est de format {nbElement: liste de temps de ConsIter pour file binomiale}
# ce dictionnaire est pour calculer le temps moyen de 5 jeu de données
dic_ConsIter_liste = {}
for i in [100,1000,10000,200,20000,500,5000,50000]:
	dic_ConsIter_liste[i] = []

print("  En train d'écrire les données dans le fichier Question_3_10.xls.....")
for x  in range(0,5): # Pour les 5 jeu de donnees
	for n in range(x*8,x*8+8): 
		with open('./cles_alea/'+listeFichiers[n], 'r') as fichier:
			texte = fichier.read()
			les_cles = texte.split("\n")
			l = []
			for ligne in les_cles :
				if not ligne == "" :
					l.append(ligne)
			fichier.close()
		########### calculer les temps d’exécution de ConsIter #############
		f = file_binomiale()
		debut_consIter = time.time()*1000
		f = ConsIter(f,l)
		t_consIter = time.time()*1000 - debut_consIter
		

		dic_ConsIter[f.nbElement()] = t_consIter
		dic_ConsIter_liste[f.nbElement()].append(t_consIter)
	
	# on tri par nombre de cles
	listeConsIter = sorted(dic_ConsIter.items(), key=get_nbcles)

	############## On crée un fichier Excel et on insère les données ###############
	
	# création de la feuille 
	feuil1 = book.add_sheet("ConsIter_Jeu_" + str(x+1))
	# ajout des en-têtes
	feuil1.write(0,0,'nombre de cles')
	feuil1.write(0,1,'temps d\'execution file binomiale')

	# ajout des valeurs dans la ligne suivante
	i = 0
	for nbElement, temps in listeConsIter : 
		i = i + 1
		ligne = feuil1.row(i)
		ligne.write(0,nbElement)
		ligne.write(1,temps)

	# ajustement éventuel de la largeur d'une colonne
	feuil1.col(0).width = 5000
	feuil1.col(1).width = 10000

############## On crée un fichier Excel pour la moyenne de temps d'execution ###############
listeConsIter_moyenne = sorted(dic_ConsIter_liste.items(), key=get_nbcles)

# création de la feuille pour la moyenne de 5 jeux
feuil_m = book.add_sheet("moyenne_consIter " )
	# ajout des en-têtes
feuil_m.write(0,0,'nombre de cles')
feuil_m.write(0,1,'temps d\'execution en moyenne file binomiale')

# ajout des valeurs dans la ligne suivante
i = 0
for nbElement, liste_temps in listeConsIter_moyenne : 
	i = i + 1
	ligne = feuil_m.row(i)
	ligne.write(0,nbElement)
	ligne.write(1,mean(liste_temps))


# ajustement éventuel de la largeur d'une colonne
feuil_m.col(0).width = 5000
feuil_m.col(1).width = 10000

# création matérielle du fichier résultant
book.save('Question_3_10.xls')
print(" Fin d'écriture de fichier Question_3_10.xls ")

