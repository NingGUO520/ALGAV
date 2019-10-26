from FileBinomiale import *
from xlwt import Workbook
from statistics import mean #pour calculer la moyenne de la liste
import os
import time
import sys
#
# Pour la question 3.11:
# Utiliser les jeux de données aléatoires afin de vérifier graphiquement la complexité temporelle
# de la fonction Union
#

def get_nbcles(dic):
	return dic[0] # retourne le 1nd element du tuple

listeFichiers = os.listdir('./cles_alea')
# création du fichier Excel 
book = Workbook()



# la dictionnaire est de format {nbElement: liste de temps de Union pour file binomiale}
# ce dictionnaire est pour calculer le temps moyen de 5 jeu de données
dic_Union_liste = {}
for i in [200,2000,20000,400,40000,1000,10000,100000]:
	dic_Union_liste[i] = []
dic_Union = {}
print("  En train d'écrire les données dans le fichier Question_3_11.xls.....")

for x in range(0,4):
	for n in range(8*x,8*x+8): 
		#Ouvre les fichier de jeu_1 et mettre les données dans l1
		l1 = []
		with open('./cles_alea/'+listeFichiers[n], 'r') as fichier:
			texte = fichier.read()
			les_cles = texte.split("\n")
			for ligne in les_cles :
				if not ligne == "" :
					l1.append(ligne)
			fichier.close()
		f1 = file_binomiale()
		f1 = ConsIter(f1,l1)

		#Ouvre les fichier de jeu_2 et mettre les données dans l2
		l2 = []
		with open('./cles_alea/'+listeFichiers[n+8], 'r') as fichier:
			texte = fichier.read()
			les_cles = texte.split("\n")
			for ligne in les_cles :
				if not ligne == "" :
					l2.append(ligne)
			fichier.close()

		
		f2 = file_binomiale()
		f2 = ConsIter(f2,l2)
		########### calculer les temps d’exécution de Union #############
		

		debut_Union_fb = time.time()*1000
		f3 = UnionFile(f2,f1)
		f4 = UnionFile(f1,f2)
		t_Union_fb = time.time()*1000 - debut_Union_fb
		print("Temps d execution d\'Union file binomiale : %s millisecondes ---" % t_Union_fb)

		dic_Union[f3.nbElement()] = t_Union_fb
		dic_Union_liste[f3.nbElement()].append(t_Union_fb)
	# on tri par nombre de cles
	listeUnion = sorted(dic_Union.items(), key=get_nbcles)

	############## On crée un fichier Excel et on insère les données ###############

	# création de la feuille 
	feuil1 = book.add_sheet("Union_jeu_"+str(x+1)+ "jeu_"+str(x+2))
	# ajout des en-têtes
	feuil1.write(0,0,'nombre de cles après Union')
	feuil1.write(0,1,'temps d\'execution structure file binomiale')

	# ajout des valeurs dans la ligne suivante
	i = 0
	for nbElement, temps in listeUnion : 
		i = i + 1
		ligne = feuil1.row(i)
		ligne.write(0,nbElement)
		ligne.write(1,temps)


	# ajustement éventuel de la largeur d'une colonne
	feuil1.col(0).width = 8000
	feuil1.col(1).width = 8000




listeUnion_moyen = sorted(dic_Union_liste.items(), key=get_nbcles)
# création de la feuille 
feuil = book.add_sheet("Union_jeu_moyen")
# ajout des en-têtes
feuil.write(0,0,'nombre de cles après Union')
feuil.write(0,1,'temps d\'execution structure file binomiale')

# ajout des valeurs dans la ligne suivante
i = 0
for nbElement, temps in listeUnion_moyen : 
	i = i + 1
	ligne = feuil.row(i)
	ligne.write(0,nbElement)
	ligne.write(1,mean(temps))


# ajustement éventuel de la largeur d'une colonne
feuil.col(0).width = 8000
feuil.col(1).width = 8000
# création matérielle du fichier résultant
book.save('Question_3_11.xls')
print(" Fin d'écriture de fichier Question_3_11.xls ")
