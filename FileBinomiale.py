
from inf_eg import *

################################ tournoi binomiale #####################
class TournoisB(object):

	def __init__(self, *args) :

		#Sans argument, il crée un tournoi vide
		if len(args) == 0 :
			self.val = None
			self.liste_fils = []
			self.pere = None

		#Un argument il crée un TB0 qui contient un seul noeud 
		if len(args) == 1 :
			self.val = args[0]
			self.liste_fils = []
			self.pere = None

	def EstVide(self):
		return self.val == None

	def Degre(self):
		return len(self.liste_fils)

	# Renvoie la file binomiale obtenue en supprimant la racine du tournoi : TournoiB −> FileB
	def Decapite(self):
		l = []
		for tournoi in self.liste_fils:
			l.append(tournoi)
		return file_binomiale(l)

	def File(self):
		l = []
		l.append(self)
		return file_binomiale(l)

	def nbElement(self):
		return pow(2,self.Degre())

	def __repr__(self):
		# return "TB"+str(self.Degre()) + " avec racine " + str(self.val) + " nb element" + str(self.nbElement())
		return "TB"+str(self.Degre())

	def __str__(self, level = 0):
		ret = "\t" * level + str(self.val) + "\n"
		for fils in self.liste_fils:
			ret += fils.__str__(level+1)
		return ret 

	def copy(self):
		co = TournoisB()
		co.val = self.val
		co.liste_fils = self.liste_fils.copy()
		co.pere = self.pere
		return co
################################ file binomiale #####################
class  file_binomiale(object):

	def __init__(self, *args):

		#Sans argument, il crée une file binomiale vide
		if len(args) == 0 :
			self.listeTB = []

		#Un argument, il crée une file binomiale
		if len(args) == 1 :
			self.listeTB = args[0]

	def EstVide(self):
		return len(self.listeTB) == 0

    # Renvoie le tournoi de degre minimal dans la file.
	def MinDeg(self):
		return self.listeTB[-1]

	# Renvoie la file privee de son tournoi de degre minimal.
	def Reste(self):
		res = self
		res.listeTB.pop()
		return res

	# Revoie une copie de la file binomiale
	def copy(self):
		f = file_binomiale()
		for t in self.listeTB:
			f.listeTB.append(t)
		return f


	# Le minimum de la file est à la racine de l’un des arbres
	def SupprMin(self):

		file = self.copy()
		#Déterminer l’arbre Bk de racine minimale
		if not file.EstVide():
			minTB = file.listeTB[0]
			minval = file.listeTB[0].val
			for t in file.listeTB:
				if inf(t.val,minval) :
					minval = t.val
					minTB = t

		#Suppression de Bk
		file.listeTB.remove(minTB)

		#Supprimer la racine de Bk −→ File < Bk−1, . . . , B0 >
		f = minTB.Decapite()

		#Faire l’union des deux files
		return UnionFile(file,f)




	def nbElement(self):
		somme = 0 
		if not self.EstVide():
			for tb in self.listeTB:
				somme += tb.nbElement()
		return somme


	def __repr__(self):
   		return "File binomiale  : " + str(self.listeTB)+ " Nombre elements "+ str(self.nbElement())

	def printFile(self):
   		for t in self.listeTB:
   			print(t)

# Ajout d’un élément x à une file binomiale
def Ajout(fb,x):

	#Créer une file binomiale FB1 contenant uniquement x
	l = []
	l.append(TournoisB(x))
	fb1 = file_binomiale(l)

	#Puis faire l’union de FB1 et FBn
	return UnionFile(fb,fb1)

def ConsIter(fb,l):

	res = fb
	for i in l :
		res = Ajout(res,i)
	return res


# hypothese : le tournoi TB est de degre inferieur au MinDeg de la file
# Renvoie la file obtenue en ajoutant le tournoi 
def AjoutMin(TB,F):
	res = F
	res.listeTB.append(TB)
	return res

# Renvoie l'union de 2 tournois de meme taille
def Union2Tid(T1,T2):
	res = T1.copy()
	if inf(T1.val, T2.val):  
		res.liste_fils.insert(0,T2)
	else:
		res = T2.copy()
		res.liste_fils.insert(0,T1)
	return res

# renvoie la file binomiale union de 2 files
def UnionFile(F1,F2):
	u_f1 = F1.copy()
	u_f2 = F2.copy()
	return UFret(u_f1,u_f2,TournoisB())

# renvoie la file binomiale union de 2 files et d'un tournoi	
def UFret(F1,F2,T):
	#pas de tournoi en retenue
	if T.EstVide() :
		if F1.EstVide():
			return F2
		if F2.EstVide():
			return F1

		t1 = F1.MinDeg()
		t2 = F2.MinDeg()
		if t1.Degre() < t2.Degre() :
			return AjoutMin(t1,UnionFile(F1.Reste(), F2))
		if t2.Degre() < t1.Degre():
			return AjoutMin(t2 , UnionFile(F2.Reste(), F1))
		if t1.Degre() == t2.Degre() :
			return UFret(F1.Reste(), F2.Reste(), Union2Tid(t1 ,t2))

	else :# tournoi TB en retenue
		if F1.EstVide():
			return UnionFile(T.File(), F2)
		if F2.EstVide():
			return UnionFile(T.File(), F1)

		t1 = F1.MinDeg()
		t2 = F2.MinDeg()
		if T.Degre() < t1.Degre() and T.Degre() < t2.Degre():
			return AjoutMin(T, UnionFile (F1 , F2))
		if T.Degre() == t1.Degre() and T.Degre() == t2.Degre():
			return AjoutMin(T, UFret(F1.Reste(), F2.Reste(),Union2Tid(t1, t2)))
		if T.Degre() == t1.Degre() and T.Degre() < t2.Degre():
			return UFret(F1.Reste(), F2 , Union2Tid (t1, T))
		if T.Degre() == t2.Degre() and T.Degre() < t1.Degre():
			return UFret(F2.Reste(), F1 , Union2Tid (t2, T))

		