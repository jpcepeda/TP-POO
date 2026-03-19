class Animal:
        
    def __init__(self, nom: str,poids: float, taille: float): # Definition construteur, self obligatoire
            self.nom = nom #self metode 
            self.poids= poids
            self.taille= taille
            self.se_deplacer()

    def se_deplacer(self):
            pass
  
lapin = Animal(nom = 'Bugs', #creation objet
                    poids= 6,
                    taille=10)
print (lapin.nom, # print attributes
        lapin.poids,
        lapin.taille)
        
    


