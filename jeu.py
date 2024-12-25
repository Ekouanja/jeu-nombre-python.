import random

def jeu_de_devine():
    print("Bienvenue dans le jeu de devinettes !")
    print("L'ordinateur a choisi un nombre entre 1 et 100.")
    print("Essayez de le deviner !")
    
    # Générer un nombre aléatoire entre 1 et 100
    nombre_secret = random.randint(1, 100)
    tentative = 0
    trouve = False

    while not trouve:
        try:
            # Demander une entrée utilisateur
            devinette = int(input("Entrez votre devinette : "))
            tentative += 1

            if devinette < 1 or devinette > 100:
                print("Veuillez entrer un nombre entre 1 et 100.")
            elif devinette < nombre_secret:
                print("C'est plus grand !")
            elif devinette > nombre_secret:
                print("C'est plus petit !")
            else:
                print(f"Bravo ! Vous avez trouvé le nombre {nombre_secret} en {tentative} tentatives.")
                trouve = True
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Lancer le jeu
if __name__ == "__main__":
    jeu_de_devine()
