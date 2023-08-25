import csv

with open('couleurs_preferees.csv') as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=',')
        for ligne in reader:
            print(ligne['nom'] + " travaille en tant que " +
                   ligne['metier'] + 
                  " et sa couleur préférée est " + 
                  ligne['couleur_preferee'])