from inf_eg import *
# # Définir un "Noeud"

class Noeud:
    def __init__(self, valeur):
        self.gauche = None
        self.droite = None
        self.parent = None
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
    
    def possede_parent(self):
        return self.parent != None
    
    def est_racine(self):
        return not self.parent == None
    
    def possede_enfant(self):
        return self.gauche != None or self.droite != None
    
    def est_feuille(self):
        return self.gauche == None and self.droite == None
    
    def est_fils_gauche(self):
        return self.possede_parent() and self.parent.gauche == self
    
    def est_fils_droite(self):
        return self.possede_parent() and self.parent.droite == self
    
    def est_feuille_droite(self):
        return self.est_fils_droite() and self.est_feuille()
        
    def est_feuille_gauche(self):
        return self.est_fils_gauche() and self.est_feuille()   


# # Définir un "Tas Min"

class TasMinArbre:
    
    def __init__(self):
        self.racine = None
        self.dernier = None
        self.keysMap = {}
        
    def estVide(self):
        return self.racine == None
        
    def mettre_a_jour_dernier_noeud(self):
        
        if self.dernier.est_feuille_droite():
            self.dernier = self.dernier.parent.gauche
            return
        
        cur = self.dernier
        
        while True:
            
            if cur.est_fils_droite() or cur.est_racine():
                # est fils droite
                if cur.est_fils_droite():
                    cur = cur.parent.gauche
                    
                while True:
                    if cur.est_feuille_droite():
                        self.dernier = cur
                        return
                    else:
                        # print(cur)
                        cur = cur.droite
            else:
                cur = cur.parent
                # print(cur == None)
         
    def echanger_noeuds_valeurs(self, noeud1, noeud2):
        noeud1.valeur, noeud2.valeur = noeud2.valeur, noeud1.valeur


    
       # Cette méthode sert à monter un noeud en haut (et bien sûr descendre le noeud auparavant en haut)
    def allerEnHaut(self, n):
        
        assert n.parent != None
        
        p = n.parent
        
        if p.parent != None:
            if p == p.parent.droite:
                p.parent.droite = n
            else:
                p.parent.gauche = n
        else:
            self.racine = n
            
        n.parent = p.parent
        
        cote = ''
        if n == p.droite:
            cote = 'droite'
        else:
            cote = 'gauche'
            
        c = None
        if cote == 'gauche':
            c = p.droite
        else:
            c = p.gauche
          
        p.gauche = n.gauche
        if p.gauche != None:
            p.gauche.parent = p
            
        p.droite = n.droite
        if p.droite != None:
            p.droite.parent = p
        
        if cote == 'gauche':
            n.gauche = p
        else:
            n.droite = p
        
        p.parent = n
        
        if cote == 'gauche':
            n.droite = c
        else:
            n.gauche = c
        
        if c != None:
            c.parent = n
            
        if n == self.dernier:
            self.dernier = p   
    
    
    def ajouter(self, valeur):
        
        noeud = Noeud(valeur)

        # Ajouter une clé au map
        self.keysMap[noeud] = valeur
        
        # Si le tas min est vide, nous insérons le noeud à la racine du tas
        if self.estVide():
            self.racine = noeud
            self.dernier = noeud
            return
        
        # Maintenant nous cherchons l'endroit où nous devons insérer le noeud
        courant = self.dernier
        
        while courant.parent != None and courant == courant.parent.droite:
            courant = courant.parent
            
        if courant.parent != None:
            if courant.parent.droite != None:
                courant = courant.parent.droite
                while (courant.gauche != None):
                    courant = courant.gauche
            else:
                courant = courant.parent
        else:
            while courant.gauche != None:
                courant = courant.gauche
    
        if (courant.droite != None):
            print('*********************')
            print('Very big error happed')
            print('*********************')
        
        self.dernier = noeud
        
        if courant.gauche != None:
            courant.droite = noeud
        else:
            courant.gauche = noeud
        
        noeud.parent = courant
        noeud.gauche = None
        noeud.droite = None
        
        while noeud.parent != None and inf(noeud.valeur,noeud.parent.valeur): 
            self.allerEnHaut(noeud)
            
            
            
    def ConsIter(self, l):
        if l == None or len(l) == 0:
            print('Veuillez fournir une liste, ou bien la liste est vide!')
            return
        for item in l:
            self.ajouter(item)
            

    def union(tas1, tas2):
        newTas = TasMinArbre()
        
        keys1 = list(tas1.keysMap.values())
        keys2 = list(tas2.keysMap.values())
        
        allKeys = keys1 + keys2
        
        # print('allKeys = ', allKeys)
        
        newTas.ConsIter(allKeys)  
        return newTas
        
    def aller_en_bas_gauche(self, noeud):
        noeud.gauche.valeur, noeud.valeur = noeud.valeur, noeud.gauche.valeur
        
    def aller_en_bas_droite(self, noeud):
        noeud.droite.valeur, noeud.valeur = noeud.valeur, noeud.droite.valeur
        
        
    def aller_en_bas(self, noeud):
        return
    
    def supprMin(self):
        
        if self.estVide():
            print('***********************************************')
            print('Le tas min est vide, nous ne pouvons rien faire')
            print('***********************************************')
            return
    
        del self.keysMap[self.racine]
        
        
        self.echanger_noeuds_valeurs(self.racine, self.dernier)
       
        dernier_temp = self.dernier
        
        self.mettre_a_jour_dernier_noeud()
        
        
        # Enlever le dernier noeud
        if dernier_temp.est_feuille_gauche():
            dernier_temp.parent.gauche = None
        else:
            dernier_temp.parent.droite = None
        
        
        cur = self.racine
        
        while cur.possede_enfant:
            
            if cur.droite == None:
                if inf( cur.gauche.valeur,cur.valeur):
                    self.echanger_noeuds_valeurs(cur, cur.gauche)
                    return
            
            else:
                if inf(cur.gauche.valeur,cur.valeur) and  inf(cur.droite.valeur,cur.valeur ) :
                    if inf(cur.droite.valeur,cur.gauche.valeur):
                        self.echanger_noeuds_valeurs(cur, cur.droite)
                        cur = cur.droite
                        continue
                    else:
                        self.echanger_noeuds_valeurs(cur, cur.gauche)
                        cur = cur.gauche
                        continue
                if inf(cur.gauche.valeur,cur.valeur )  and inf(cur.valeur , cur.droite.valeur):
                    self.echanger_noeuds_valeurs(cur, cur.droite)
                    cur = cur.droite
                    continue
                if inf(cur.valeur , cur.gauche.valeur) and inf(cur.droite.valeur,cur.valeur): 
                    self.echanger_noeuds_valeurs(cur, cur.gauche)
                    cur = cur.gauche
                    continue


# # Test ajouter( )

# In[57]:


# tasMin = TasMinArbre()
# for i in range(10):
#     tasMin.ajouter(i)


# print(tasMin.racine)


# # # Test ConsIter( )

# # In[58]:


# tasMin2 = TasMinArbre()
# l = [x**2 for x in range(10)]
# tasMin2.ConsIter(l)
# print(tasMin2.racine)


# # # Test supprMin( )

# # In[59]:


# tasMin3 = TasMinArbre()
# l = [x**2 for x in (range (11, 20))]
# tasMin3.ConsIter(l)
# newTas = tasMin3.supprMin()
# print(tasMin3.racine)


# # # Test union( )

# # In[60]:


# # constract two tas for test
# #list_1 = [x * 3 for x in range(25)]
# list_1 = [2, 34, 2, 44, 23, 23, 24, 46]
# list_2 = [x * 4 for x in range(16)]

# tas_test_1 = TasMinArbre()
# tas_test_2 = TasMinArbre()

# tas_test_1.ConsIter(list_1)
# tas_test_2.ConsIter(list_2)


# #print(tas_test_1.racine)

# tas_final = TasMinArbre.union(tas_test_1, tas_test_2)
# #tas_final.enlever(tas_final.racine.droite)
# print(tas_final.racine)
# #print(tas_test_2.racine)

