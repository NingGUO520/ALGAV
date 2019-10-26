from arbreRecherche import *
from md5_hachage import *
import time
import os
##### pour Question 6.12 et Question 6.13
listeFichiers = os.listdir('./Shakespeare')
# liste des mots de l’œuvre de Shakespeare où chaque mot n’apparaît qu’une seule fois
mots_differents = set([])
liste_mots = []

for file in listeFichiers:
	with open('Shakespeare/'+file, 'r') as fichier:
		texte = fichier.read()
		les_mots = texte.split("\n")
		for mot in les_mots :
			if not mot == "" :
				liste_mots.append(mot)
				mots_differents.add(mot)
		fichier.close()


print("Le nombre de mots totals dans l’œuvre de Shakespeare ",len(liste_mots))
print("Le nombre de mots différents ",len(mots_differents))


# On tocker dans une arbre binaire de recherche, le haché MD5 de chaque mot
a = ArbreBinareDeRecherche()
for mot in mots_differents:
	a.ajouterIteratif(md5_to_hex(md5(mot.encode())))
# print("nombre de mots haché MD5 dans arbre de recherche ",nbElements(a.racine))
# # print(liste_md5)
# a = ArbreBinareDeRecherche()
# 				a.ConsIter(liste_md5)
# start_time = time.time()
# res = a.rechercherRecursif(md5("henry".encode('UTF-8')))
# print("Temps d execution : %s secondes ---" % '{:f}'.format(time.time() - start_time))
# print("Nombre d'élément ",nbElements(a.racine))
# # a.printTree()
# print(res)
# print("nb de mots differents",len(mots_differents))

# ##### pour Question 6.13
# mots = ArbreBinareDeRecherche()
# mots.ConsIter(liste_mots)

# print("nb de mots en collision ",len(mots.mots_collision))
# print(mots.mots_collision)
