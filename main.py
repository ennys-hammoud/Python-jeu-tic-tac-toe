#Etape du jeu tic tac toe 
        
#etape 1: choix du joueur 
#etape 2: affiche de la grille 
#etape 3: boucle de jeu (fin_jeu==False)
      #si fin_jeu est false = le jeu continue 
      #si fin_jeu est vrai = le jeu est terminer(victoire,match nul,arretmanuel)
#etape 4: tour(joeur actuel)
#etape 5: verifier_fin_jeu (si victoire ou match nul)
#etape 6: joeur_suivant (si le jeu n'est pas terminé = fonction joueur suivant)
#etape 7: resulat() : si le jeu est terminé (fin_jeu == True)
          #fonction qui affiche le resullat du jeu (nom du gagant ou match nul)
#ce flux permet de gerer un jeu de morpion pour deux joueurs dans une boucle continue jusqu'a ce qu'une condition de fin soit atteinte

def choisir_joueur():
    """Étape 1: Permet aux joueurs de choisir leur nom et leur symbole."""
    # Demander le nom du joueur 1
    joueur1 = input("Joueur 1, entrez votre nom : ")
    
    # Demander le symbole du joueur 1
    symbole1 = input(f"{joueur1}, choisissez votre symbole (X ou O) : ").upper()
    
    # Attribuer le symbole du joueur 2
    symbole2 = "O" if symbole1 == "X" else "X"
    
    # Demander le nom du joueur 2
    joueur2 = input("Joueur 2, entrez votre nom : ")
    
    return (joueur1, symbole1), (joueur2, symbole2)



def afficher_grille(plateau):
    """Affiche le plateau de jeu."""
    print("État actuel du plateau :")
    for ligne in plateau:
        print(" | ".join(ligne))  # Affiche chaque ligne du plateau
        print("-" * 9)            # Ligne de séparation

# Cette fonction est essentielle pour visualiser
# l'état actuel du jeu à chaque tour,
# permettant aux joueurs de suivre le déroulement de la partie.






  
def verifier_victoire(plateau):
    """Étape 5: Vérifie si un joueur a gagné."""
    # Vérifier les lignes
    for ligne in plateau:
        if ligne.count(ligne[0]) == 3 and ligne[0] != " ":
            return True  # Un joueur a gagné
    
    # Vérifier les colonnes
    for col in range(3):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] != " ":
            return True  # Un joueur a gagné

    # Vérifier les diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != " ":
        return True  # Un joueur a gagné
    
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != " ":
        return True  # Un joueur a gagné

    return False  # Pas de gagnant



def verifier_match_nul(plateau):
    """Étape 5: Vérifie si le jeu est un match nul."""
    # Vérifie si toutes les cases sont remplies
    return all(cell != " " for row in plateau for cell in row)



def joueur_suivant(tour):
    """Étape 6: Retourne le joueur suivant."""
    return tour % 2



def resultat(gagnant, type_resultat):
    """Étape 7: Affiche le résultat du jeu."""
    if type_resultat == "gagne":
        print(f"Félicitations {gagnant}, vous avez gagné !")
    elif type_resultat == "nul":
        print("C'est un match nul !")

def jeu_tic_tac_toe():
    """Fonction principale pour gérer le jeu Tic Tac Toe."""
    # Étape 2: Initialiser le plateau
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    
    # Étape 1: Choisir les joueurs
    (joueur1, symbole1), (joueur2, symbole2) = choisir_joueur()
    
    # Initialiser le compteur de tours
    tour = 0
    fin_jeu = False  # Booléen pour contrôler la fin du jeu

    # Étape 3: Boucle de jeu
    while not fin_jeu:
        afficher_grille(plateau)  # Afficher la grille
        
        # Déterminer le joueur courant
        joueur_courant = joueur1 if joueur_suivant(tour) == 0 else joueur2
        symbole_courant = symbole1 if joueur_suivant(tour) == 0 else symbole2
        
        # Étape 4: Tour du joueur actuel
        print(f"C'est le tour de {joueur_courant} ({symbole_courant})")
        ligne = int(input("Choisissez une ligne (0-2) : "))
        col = int(input("Choisissez une colonne (0-2) : "))
        
        # Vérification si la case est vide
        if plateau[ligne][col] == " ":
            plateau[ligne][col] = symbole_courant  # Marquer la case
            
            # Vérifier les conditions de fin de jeu
            if verifier_victoire(plateau):
                fin_jeu = True
                resultat(joueur_courant, "gagne")  # Afficher le résultat
            elif verifier_match_nul(plateau):
                fin_jeu = True
                resultat("", "nul")  # Afficher le résultat
            else:
                tour += 1  # Passer au joueur suivant
        else:
            print("Cette case est déjà occupée, choisissez-en une autre.")

if __name__ == "__main__":
    jeu_tic_tac_toe()  # Lancer le jeu


    