from inf_eg import *

class TasMin(object):

    def __init__(self):
        # t : un tableau contenant un tas
        self.liste = []

    def Ajout(self, e):
        self.liste.append(e)

        courant = len(self.liste) - 1
        pere = (courant - 1)//2

        while courant > 0:
            if inf(self.liste[pere],self.liste[courant]):
                break
            else:
                self.liste[courant], self.liste[pere] = self.liste[pere], self.liste[courant]
                courant = pere
                pere = (courant - 1)//2

    #supprimer l’élément de clé minimale dans la structure
    def SupprMin(self):
        if len(self.liste) == 0: #si la liste est vide 
            print("suppression échouée : tas vide !")
        else :

            tmp = self.liste.pop()

            if not len(self.liste) == 0: #si la liste n'est pas vide 
                self.liste[0] = tmp
                courant = 0
                fils_gauche = courant * 2 + 1
                fils_droite = courant * 2 + 2
                while fils_gauche <= len(self.liste) - 1 :

                    #si le noeud courant n'a que fils_gauche mais pas de fils droite
                    if fils_gauche == len(self.liste) - 1 :
                        if inf(self.liste[courant],self.liste[-1]):
                            break
                        else:
                            self.liste[courant], self.liste[-1] = self.liste[-1],self.liste[courant]
                            break

                    #si le noeud courant a fils gauche et fils droite
                    min = self.liste[fils_gauche]
                    if inf(self.liste[fils_droite],self.liste[fils_gauche]) :
                        min = self.liste[fils_droite]
                    if self.liste[courant] < min:
                        break
                    else :
                        if inf(self.liste[fils_droite],self.liste[fils_gauche]):

                            self.liste[fils_droite], self.liste[courant] = self.liste[courant],self.liste[fils_droite]
                            courant = fils_droite
                            fils_gauche = courant * 2 + 1
                            fils_droite = courant * 2 + 2

                        else:
                            self.liste[courant], self.liste[fils_gauche] = self.liste[fils_gauche],self.liste[courant]
                            courant = fils_gauche
                            fils_gauche = courant * 2 + 1
                            fils_droite = courant * 2 + 2


    #construire itérativement un tas à partir d’une liste d’éléments
    def ConsIter(self,liste):
        for e in liste:
            self.Ajout(e)

    def Union(self, other):  
        l = []
        for x in self.liste:
            l.append(x)
        for x in other.liste:
            l.append(x) 

        new_tas = TasMin()
        new_tas.ConsIter(l)          
        return new_tas        
    def __repr__(self):
        return "Tas min :   nb d'éléments "+ str(len(self.liste))

    def printTableau(self):
        print(self.liste)

