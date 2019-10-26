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

dic_Ajout = {}
dic_Ajout_moyen = {}
for x in [100,1000,10000,200,20000,500,5000,50000]:
	dic_Ajout_moyen[x]=([],[])
print("  En train d'écrire les données dans le fichier Q6_14_AJOUT.xls.....")
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
		debut_Ajout_tas = time.time()*1000
		tas.Ajout("0x944c816ee15f6009cbc4c77bf8fb0d2")
		tas.Ajout("0x8011c1ceaa95938656057c47d515648e")
		tas.Ajout("0x740d58c74a4f90c3e555f81ab1b2fad3")
		tas.Ajout("0x801111ceaa95938656057c47d515648e")
		tas.Ajout("0x740d28c74a4f90c3e555f81ab1b2fad3")

		t_Ajout_tas = '{:f}'.format(time.time()*1000 - debut_Ajout_tas)

		debut_Ajout_fb = time.time()*1000
		f = Ajout(f,"0x944c816ee15f6009cbc4c77bf8fb0d2")
		f = Ajout(f,"0x8011c1ceaa95938656057c47d515648e")
		f = Ajout(f,"0x740d58c74a4f90c3e555f81ab1b2fad3")
		f = Ajout(f,"0x801111ceaa95938656057c47d515648e")
		f = Ajout(f,"0x740d28c74a4f90c3e555f81ab1b2fad3")

		t_Ajout_fb = '{:f}'.format(time.time()*1000 - debut_Ajout_fb)

		dic_Ajout[len(tas.liste)-5] = (float(t_Ajout_fb), float(t_Ajout_tas))
		dic_Ajout_moyen[len(tas.liste)-5][0].append(float(t_Ajout_fb))
		dic_Ajout_moyen[len(tas.liste)-5][1].append(float(t_Ajout_tas))


	# on tri par nombre de cles
	
	listeAjout = sorted(dic_Ajout.items(), key=get_nbcles)

	############## On crée un fichier Excel et on insère les données ###############

	# ajout d'une autre feuille  pour Ajout
	feuil3 = book.add_sheet("Ajout_jeu_"+str(x+1))
	# ajout des en-têtes
	feuil3.write(0,0,'nombre de cles')
	feuil3.write(0,1,'temps d\'execution file binomiale (milliseconde)')
	feuil3.write(0,2,'temps d\'execution tas min (milliseconde)')

	# ajout des valeurs dans la ligne suivante
	i = 0
	for nbElement, temps in listeAjout : 
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
listeAjoutMoyen = sorted(dic_Ajout_moyen.items(), key=get_nbcles)

feuil3 = book.add_sheet("Ajout_moyen")
# ajout des en-têtes
feuil3.write(0,0,'nombre de cles')
feuil3.write(0,1,'temps d\'execution file binomiale (milliseconde)')
feuil3.write(0,2,'temps d\'execution tas min (milliseconde)')

# ajout des valeurs dans la ligne suivante
i = 0
for nbElement, temps in listeAjoutMoyen : 
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
book.save('Q6_14_AJOUT.xls')

print(" Fin d'écriture dans fichier Q6_14_AJOUT.xls ")

