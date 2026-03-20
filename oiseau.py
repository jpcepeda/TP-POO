
from animal import Animal

class Oiseau(Animal):
    def __init__(self, nom: str, poids: float, taille: float, altitude_max: float): # Appel du constructeur Animal
        super().__init__(nom, poids, taille)  # Appel du constructeur de Animal. Inicialitation heritage, returns a temporary object of the superclass
        self.altitude_max = altitude_max

    def se_deplacer(self):
        print(f"{self.nom} vole à {self.altitude_max} mètres.")

