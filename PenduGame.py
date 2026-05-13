# Cette fonction lit le fichier texte pour créer la liste de mots

def lire_fichier_mots(nom_du_fichier):
    try:
        # On ouvre le fichier en mode lecture avec l'encodage pour les accents
        f = open(nom_du_fichier, "r", encoding="utf-8")
        contenu = f.readlines()
        f.close()
        
        liste_finale = []
        for ligne in contenu:
            mot = ligne.strip() # On retire les espaces et sauts de ligne
            if mot != "":
                liste_finale.append(mot)
        return liste_finale
    except:
        # Quand utilisateur donne un mauvais nom, on affiche une erreur
        print("Erreur : Impossible de lire le fichier", nom_du_fichier)
        return []
    
