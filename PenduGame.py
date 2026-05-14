import random



# Fonction pour lire le fichier texte pour créer la liste de mots

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



# Fonction pour donner une lettre au hasard qui n'est pas dans le mot

def afficher_indice(mot_secret, lettres_utilisees):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mauvaises_lettres = []
    
    # On normalise le mot secret pour bien comparer
    mot_simple = ""
    for car in mot_secret:
        mot_simple = mot_simple + normaliser_lettre(car)
        
    for lettre in alphabet:
        # La lettre ne doit pas être dans le mot et ne doit pas avoir été essayée
        if lettre not in mot_simple and lettre not in lettres_utilisees:
            mauvaises_lettres.append(lettre)
            
    # On choisit une lettre au hasard parmi toutes les mauvaises possibles
    if len(mauvaises_lettres) > 0:
        indice = random.choice(mauvaises_lettres)
        print("INDICE : La lettre '" + indice + "' n'est pas dans le mot.")


# Fonctionnement principale d'une partie

def lancer_une_partie():
    choix_fichier = input("Nom du fichier de mots (ou Entrée pour defaut) : ")
    if choix_fichier == "":
        choix_fichier = "mots_pendu.txt"
    
    mots = lire_fichier_mots(choix_fichier)

    # Si le fichier n'a pas marché et que ce n'était pas déjà le fichier par défaut, on le prend
    if len(mots) == 0 and choix_fichier != "mots_pendu.txt":
        print("Fichier '" + choix_fichier + "' introuvable. Utilisation de mots_pendu.txt par defaut.")
        mots = lire_fichier_mots("mots_pendu.txt")

    if len(mots) == 0:
        print("Erreur : Impossible de charger une liste de mots.")
        return 

    mot_a_deviner = random.choice(mots)
    lettres_essayees = []
    chances = 6

    while chances > 0:
        print("\nMot : " + creer_affichage(mot_a_deviner, lettres_essayees))
        print("Chances restantes :", chances)
        
        if chances == 1:
            afficher_indice(mot_a_deviner, lettres_essayees)

        proposition = input("Entrez une lettre : ").lower()

        if len(proposition) != 1 or not proposition.isalpha():
            print("Erreur : Entrez une seule lettre.")
            continue

        lettre_pure = normaliser_lettre(proposition)

        if lettre_pure in lettres_essayees:
            print("Déjà essayé !")
            continue

        lettres_essayees.append(lettre_pure)

        mot_simplifie = ""
        for car in mot_a_deviner:
            mot_simplifie = mot_simplifie + normaliser_lettre(car)

        if lettre_pure in mot_simplifie:
            print("Oui, la lettre est dans le mot !")
        else:
            print("Non, ce n'est pas la bonne lettre.")
            chances = chances - 1

        victoire = True
        for car in mot_simplifie:
            if car not in lettres_essayees:
                victoire = False
        
        if victoire:
            print("\nGAGNE ! Le mot etait : " + mot_a_deviner)
            break
    
    if chances == 0:
        print("\nPERDU... Le mot etait : " + mot_a_deviner)


# Fonction pour recommencer ou quitter le jeu

def main():
    rejouer = "oui"
    while rejouer == "oui":
        lancer_une_partie()
        rejouer = input("\nVoulez-vous rejouer ? (ecrire oui/non) : ").lower()
    
    print("Au revoir !")

# Appel de la fonction main pour lancement du programme
main()