from animal import Animal
from oiseau import Oiseau
from Serpent import Serpent
from zoo import Zoo



# Création d'objets
lapin = Animal(nom='Bugs', poids=6, taille=10)
serpent = Serpent(nom='Black', poids=15, taille=30)
oiseau = Oiseau(nom='Blue', poids=0.5, taille=5, altitude_max=7)

# Création du zoo avec une liste d'animaux
zoo = Zoo([lapin, serpent, oiseau])

# Ajouter un animal
zoo.ajouter_animal(oiseau)

# Afficher les animaux du zoo
for animal in zoo.animaux:
    print(animal.nom)     


# Affichage des attributs et appel des méthodes
print(lapin.nom, lapin.poids, lapin.taille)
lapin.se_deplacer()

print(serpent.nom, serpent.poids, serpent.taille)
serpent.se_deplacer()

print(oiseau.nom, oiseau.poids, oiseau.taille)
oiseau.se_deplacer()