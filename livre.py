
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
