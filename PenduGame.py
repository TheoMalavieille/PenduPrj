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
    

# Fonction qui remplace les lettres accentuées par des lettres simples

def normaliser_lettre(lettre):
    accents = {
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'à': 'a', 'â': 'a', 
        'ä': 'a', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'û': 'u', 
        'ù': 'u', 'ü': 'u', 'ç': 'c'
    }
    lettre = lettre.lower()
    if lettre in accents:
        return accents[lettre]
    return lettre



# Fonction qui crée la chaîne de caractères avec les tirets bas pour lettre invisible

def creer_affichage(mot_complet, lettres_deja_trouvees):
    affichage = ""
    for lettre in mot_complet:
        # On compare la version simplifiée de la lettre
        if normaliser_lettre(lettre) in lettres_deja_trouvees:
            affichage = affichage + lettre + " "
        else:
            affichage = affichage + "_ "
    return affichage.strip()
