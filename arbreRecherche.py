from inf_eg import * 

class Noeud:
    def __init__(self, valeur):
        self.gauche = None
        self.droite = None
        self.valeur = valeur
        
    def hasChildren(self):
        return self.gauche != None or self.droite != None
        
    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.droite != None:
            ret += self.droite.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.valeur)

        # Print left branch
        if self.gauche != None:
            ret += self.gauche.__str__(depth + 1)

        return ret    
        

class ArbreBinareDeRecherche:
    # Constructeur par défaut
    def __init__(self):
        self.racine = None
        self.mots_collision = set([])# pour Question 6.13
    # Ajouter une clé à l'arbre
    def ajouterIteratif(self, valeur):
                
        # Si l'arbre est initiallement vide, on insère la clé
        if self.estVide():
            self.racine = Noeud(valeur)
            return

        
        noeud_courant = self.racine
        
        while True:

            if eg(noeud_courant.valeur, valeur):
                self.mots_collision.add(valeur)
                return
            
            if inf(valeur , noeud_courant.valeur):
                if noeud_courant.gauche == None:
                    noeud_courant.gauche = Noeud(valeur)
                    return
                else:
                    noeud_courant = noeud_courant.gauche
                    
            if inf(noeud_courant.valeur,valeur):
                if noeud_courant.droite == None:
                    noeud_courant.droite = Noeud(valeur)
                    return
                else:
                    noeud_courant = noeud_courant.droite
                    
    def rechercherIteratif(self, valeur):
        # Si l'arbre est initiallement vide, on retourne "None"
        if self.estVide():
            print('self.racine est None, ne peux pas rechercher')
            return False
    
        # Initialiser noeud_courant
        noeud_courant = self.racine
        
        while True:
            
            if eg(noeud_courant.valeur, valeur):
                return True
            
            if inf(valeur,noeud_courant.valeur):
                if noeud_courant.gauche == None:
                    return False
                noeud_courant = noeud_courant.gauche
                
            if inf(noeud_courant.valeur,valeur):
                if noeud_courant.droite == None:
                    return False
                noeud_courant = noeud_courant.droite

    def ConsIter(self,l):
        for e in l :
            self.ajouterIteratif(e)
    
    def rechercherRecursif(self, valeur):
        if self.estVide():
            print('self.racine est None, ne peux pas rechercher')
            return False
        else:
            return self._rechercherRecursif(self.racine, valeur)
            
    def _rechercherRecursif(self, noeud, valeur):
        
        if eg(noeud.valeur , valeur):
            print("Réussi : La valeur a été trouvé")
            return True
        
        if inf(valeur , noeud.valeur):
            if noeud.gauche == None:
                print("La valeur n'a pas été trouvé")
                return False
            else:
                return self._rechercherRecursif(noeud.gauche, valeur)
        else:
            if noeud.droite == None:
                print("La valeur n'a pas été trouvé")
                return False
            else:
                return self._rechercherRecursif(noeud.droite, valeur)
    
        
    
    # parcours infixe
    def printTree(self):
        if(self.racine != None):
            self._printTree(self.racine)

    def _printTree(self, noeud):
        if(noeud != None):
            self._printTree(noeud.gauche)
            print(str(noeud.valeur) + ' ')
            self._printTree(noeud.droite)
            
    def estVide(self):
        return self.racine == None
    
    
def nbElements(noeud):
    if noeud == None:
        return 0 
    else:
        return 1+nbElements(noeud.gauche)+nbElements(noeud.droite)



