import random

def generate_creature():
    # Listes de caractéristiques pour créer la créature
    adjectifs = ["Féroce", "Mystérieuse", "Géante", "Éthérée", "Tentaculaire", "Brillante", "Céleste", "Sauvage", "Imposante", "Frénétique"]
    noms_animaux = ["Dragon", "Licorne", "Griffon", "Kraken", "Phénix", "Serpent", "Loup", "Araignée", "Goule", "Chimère"]
    capacites = ["Vol", "Invisibilité", "Régénération", "Manipulation des éléments", "Force surhumaine", "Camouflage", "Contrôle mental", "Métamorphose"]

    # Générer une créature aléatoire
    creature = {
        "nom": f"{random.choice(adjectifs)} {random.choice(noms_animaux)}",
        "description": f"Une créature {random.choice(adjectifs).lower()} avec la capacité de {random.choice(capacites).lower()}."
    }

    return creature

def main():
    nombre_creatures = 5

    print("Génération de créatures pour le film :\n")
    for i in range(nombre_creatures):
        creature = generate_creature()
        print(f"{i + 1}. {creature['nom']} - {creature['description']}")

if __name__ == "__main__":
    main()
