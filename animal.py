class Animal:
    def __init__(self, nom: str, poids: float, taille: float):
        self.nom = nom
        self.set_poids(poids)  # validation ici Le poids ne peut pas être négatif
        self.taille = taille
    
    # Getters
    def get_nom(self):
        return self.nom

    # Setters
    def set_nom(self, nom):
        self.nom = nom

    def set_poids(self, poids):
        if poids < 0:
            raise ValueError("Le poids ne peut pas être négatif")
        self.poids = poids

    def se_deplacer(self):
        print(f"{self.nom} se déplace.")