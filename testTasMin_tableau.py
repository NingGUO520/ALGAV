from tasMin import *
import time

def testConsIter():
	with open('cles_alea/jeu_1_nb_cles_100.txt', 'r') as fichier:
		texte = fichier.read()
		les_cles = texte.split("\n")
	l = []
	for ligne in les_cles :
		if not ligne == "" :
			l.append(ligne)
	fichier.close()


	a = TasMin()
	start_time = time.time()

	a.ConsIter(l)
	print("Temps d execution : %s secondes ---" % (time.time() - start_time))
	print("Nombre d'élément ",len(a.liste))
	print(a)


def testAjout():
	tasMin = TasMin()
	tasMin.Ajout(3)
	tasMin.Ajout(8)
	tasMin.Ajout(9)
	tasMin.Ajout(11)
	tasMin.Ajout(0)
	tasMin.Ajout(5)
	tasMin.Ajout(1)
	print(tasMin)

## Test supprMin( )
def testSupprMin():
	tasMin3 = TasMin()
	l = [2,1,14,13,6,32,0,31,5,10]
	tasMin3.ConsIter(l)
	print("########### avant suppression ##########")
	print(tasMin3)
	print(tasMin3.liste)
	tasMin3.SupprMin()
	print("########### apres 1ere suppression ##########")

	print(tasMin3)
	print(tasMin3.liste)

	tasMin3.SupprMin()
	print("########### apres 2ere suppression ##########")

	print(tasMin3)
	print(tasMin3.liste)
	tasMin3.SupprMin()
	print("########### apres 3ere suppression ##########")

	print(tasMin3)
	print(tasMin3.liste)
### Test union( )
def testUnion():
	list_1 = [2, 34, 0, 44, 27, 23, 24, 46]
	list_2 = [4, 8, 12, 16, 20, 28, 32, 36, 40, 44, 48, 52, 56, 60]


	tas_test_1 = TasMin()
	tas_test_2 = TasMin()

	tas_test_1.ConsIter(list_1)
	tas_test_2.ConsIter(list_2)

	print("########### avant Union ##########")

	print("tas 1 : ",tas_test_1)
	print("tas 2 : ",tas_test_2)

	newtas = tas_test_1.Union(tas_test_2)

	print("########### apres Union ##########")
	print(newtas.liste)
# testConsIter()
# testUnion()
testSupprMin()
# testAjout()