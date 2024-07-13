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