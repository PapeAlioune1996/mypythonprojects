import random

def genclubplayer():

    players = ["Sadio Mané","CR7","Mbappé","Kane","Messi","Ndiaye","Rashford","Kolo Muani"]
    club = ["Brentford","PSG","MAnU","City","Montpelier","Chelsea"]
    pays =["Senegalaise","Francaise","Argentin","Portiguaise","Cameroonaise","Anglaise","Espagnol"]

    ident =  {
            "joueurs": f"{random.choice(players)} {random.choice(club)}",
            "description": f"Le joueur {random.choice(players).lower()} qui joue à {random.choice(club).lower()} est de nationalité {random.choice(pays)}"
        }
    

    return ident


def main():
    nombre_joueurs = 5
    print("Génération de joueurs:\n")

    for i in range(nombre_joueurs):
        ident = genclubplayer()
        print(f"{i + 1}. {ident['joueurs']} - {ident['description']}")

if __name__ == "__main__":
    main()