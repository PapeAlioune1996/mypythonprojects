import sys


LISTE = []

MENU="""Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
Votre choix : """
MENU_CHOICES = ["1","2","3","4","5"]

while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES :
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES :
            print("Veuillez choisir une option valide...")
    if user_choice == "1":
        item = input("Entrez le nom de l'élément à ajouter :")
        LISTE.append()
        print(f"L'élément {item} a été ajouté à la liste") 
    elif user_choice == "2":
      item = input("Entrez la position de l'élément à supprimer :")
      if item in LISTE :
            LISTE.remove(item)
            print(f"L'élément {item} a été retirer à la liste") 
      else :
            print(f"L'élément {item} n'est pas dans la liste")
    elif user_choice == "3":
        if LISTE :
            print("Voici le contenu de votre liste :")
            for i in enumerate(LISTE, 1):
                print(f"{i}. {item}")
    elif user_choice == "4":
        LISTE.clear()
    elif user_choice == "5":
        sys.exit()

    print("_" *50)