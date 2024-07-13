import json

FICHIER_JSON = 'livres.json'

def chargerLivres():
    try :
        with open(FICHIER_JSON, 'r', encoding='utf-8') as fichier:
            livres = json.load(fichier)
        if livres :
            dernier_id = max(livre['id'] for livre in livres)
        else :
            dernier_id = 0
        return livres, dernier_id
    except FileNotFoundError :
        return [], 0
    except json.JSONDecodeError :
        return [], 0

def sauvegarderLivres(livres):
    with open(FICHIER_JSON, 'w', encoding='utf-8') as fichier :
        json.dump(livres, fichier, ensure_ascii=False, indent=4)

livres = chargerLivres()

def afficherLivres():
    livres, _ = chargerLivres()
    if livres :
        for livre in livres:
            print(f"ID: {livre['id']}, Titre: {livre['titre']}, Auteur: {livre['auteur']}, Genre: {livre['genre']}")
    else :
        print("Aucun livre n'est enregistré")

def rechercherLivre():
    livres, _ = chargerLivres()
    livres_trouves = []

    criteres = input("entrer le critère de recherche(Titre, Auteur, Genre ou Disponibilité) : ")
    for livre in livres:
        if (criteres.lower() in livre['titre'].lower() or
            criteres.lower() in livre['auteur'].lower() or
            criteres.lower() in livre['genre'].lower() or
            criteres.lower() == 'disponible' and livre['disponible'] or
            criteres.lower() == 'non disponible' and not livre['disponible']):
            livres_trouves.append(livre)

        if livres_trouves:
            print("Livres trouvés : ")
            for livre in livres_trouves:
                print(f"ID: {livre['id']}, Titre: {livre['titre']}, Auteur: {livre['auteur']}, Genre: {livre['genre']}, Disponible: {'Oui' if livre['disponible'] else 'Non'}")
        else :
            print("Aucun livre correspondant aux critères de recherche n'a été trouvé")

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

    nouveau_id = dernier_id + 1
    livre = {"id": nouveau_id, "titre": titreLivre, "auteur": auteurLivre, "genre": genreLivre, "disponible" : statusLivre}
    livres.append(livre)
    sauvegarderLivres(livres)
    print(livres)
    print("Livre ajouté avec succès")


def supprimerLivre():
    livres, _ = chargerLivres()

    if not livres:
        print("Aucun livre n'est enregistré")
        return

    try:
        idLivre = int(input("Entrez l'ID du livre à supprimer : "))
    except ValueError:
        print("L'ID doit être un nombre entier")
        return

    livreDel = None
    for livre in livres:
        if livre['id'] == idLivre:
            livreDel = livre
            break

    if livreDel:
        livres.remove(livreDel)
        sauvegarderLivres(livres)
        print(f"Le livre avec l'ID {idLivre} a été supprimé avec succès")
    else:
        print(f"Aucun livre trouvé avec l'ID {idLivre}")


def emprunterLivre():
    livres, _ = chargerLivres()
    if not livres:
        print("Aucun livre n'est enregistré")
        return

    try:
        idLivre = int(input("Entrez l'ID du livre à archiver : "))
    except ValueError:
        print("L'ID doit être un nombre entier")
        return

    livre_a_archiver = None
    for livre in livres:
        if livre['id'] == idLivre:
            livre_a_archiver = livre
            break

    if livre_a_archiver:
        if not livre_a_archiver['disponible']:
            print(f"le livre avec l'id {idLivre} est déjà archivé")
        else :
            livre_a_archiver['disponible'] = False
            sauvegarderLivres(livres)
            print(f"le livre avec l'ID {idLivre}a été archivé avec succès")
    else:
        print(f"Aucun livre trouvé avec l'ID {idLivre}")

def retournerLivre():
    livres, _ = chargerLivres()
    if not livres:
        print("Aucun livre n'est enregistré")
        return

    try:
        idLivre = int(input("Entrez l'ID du livre à retourner : "))
    except ValueError:
        print("L'ID doit être un nombre entier")
        return

    livre_a_retourner = None
    for livre in livres:
        if livre['id'] == idLivre:
            livre_a_retourner = livre
            break

    if livre_a_retourner:
        if livre_a_retourner['disponible']:
            print(f"Le livre avec l'ID {idLivre} est déjà disponible")
        else:
            livre_a_retourner['disponible'] = True
            sauvegarderLivres(livres)
            print(f"Le livre avec l'ID {idLivre} a été retourné avec succès")
    else:
        print(f"Aucun livre trouvé avec l'ID {idLivre}")
