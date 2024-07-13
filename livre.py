
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
