def validerTitre(titre):
    if titre.isdigit():
        print("Écrivez correctement le titre du livre")
        return False
    else:
        return True

def validerAuteur(auteur):
    if auteur.isdigit():
        print("Écrivez correctement le nom de l'auteur")
        return False
    else :
        return True

def validerGenre(genre):
    if genre.isdigit():
        print("Écrivez correctement le genre du livre")
        return False
    else :
        return True
    
def livreExiste(livres, titre, auteur):
    for livre in livres:
        if livre['titre'].lower() == titre.lower() and livre['auteur'].lower() == auteur.lower():
            return True
    return False

def ajouterLivre():

    statusLivre = True

    while True:
        titreLivre = input("entrer le titre du livre : ")
        if validerTitre(titreLivre):
            break

    while True:
        auteurLivre = input("entrer l'auteur du livre : ")
        if validerAuteur(auteurLivre):
            break

    while True:
        genreLivre = input("entrer le genre du livre : ")
        if validerTitre(genreLivre):
            break

    livres, dernier_id = chargerLivres()

    if livreExiste(livres, titreLivre, auteurLivre):
        print("le livre existe déjà")
        return