import livre

def menu():
    print("1. Ajouter un livre\n")
    print("2. Chercher un livre\n")
    print("3. supprimer un livre\n")
    print("4. Afficher un livre\n")
    print("5. Emprunter un livre\n")
    print("6. Retourner un livre\n")
    print("7. Quitter le programme\n")
    choix = int(input("\tSelectionner une option : "))
    return choix

def main():
    while True :
        choix = menu()
        if choix == 1:
            livre.ajouterLivre()
        elif choix == 2:
            livre.rechercherLivre()
        elif choix == 3:
            livre.supprimerLivre()
        elif choix == 4:
            livre.afficherLivres()
        elif choix == 5:
            livre.emprunterLivre()
        elif choix == 6:
            livre.retournerLivre()
        elif choix == 7:
            pass
        else :
            print("Veuillez choisir une option valide\n")

if __name__ == "__main__":
    main()