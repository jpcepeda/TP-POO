
from animal import Animal

class Zoo:
    def __init__(self, animaux):
        self.animaux = animaux  # liste d'objets Animal

    def ajouter_animal(self, animal):
        if isinstance(animal, Animal):  # vérifie le type
            self.animaux.append(animal)
        else:
            print("Erreur : ce n'est pas un Animal")  