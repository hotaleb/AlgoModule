

############ EXO 1 ############

# Définir une fonction appelée somme_et_moyenne

#     Demander à l'utilisateur d'entrer le premier nombre entier et le stocker dans la variable nombre1
#     Demander à l'utilisateur d'entrer le deuxième nombre entier et le stocker dans la variable nombre2
#     Demander à l'utilisateur d'entrer le troisième nombre entier et le stocker dans la variable nombre3

#     Calculer la somme des trois nombres en additionnant nombre1, nombre2 et nombre3 et stocker le résultat dans la variable somme

#     Calculer la moyenne des trois nombres en divisant la somme par 3 et stocker le résultat dans la variable moyenne

#     Afficher "La somme des nombres est :" suivi de la valeur de somme
#     Afficher "La moyenne des nombres est :" suivi de la valeur de moyenne

# Appeler la fonction somme_et_moyenne



# Fonction pour calculer la somme et la moyenne de trois nombres
def somme_et_moyenne():
    # Saisie des trois nombres
    nombre1 = int(input("Entrez le premier nombre entier : "))
    nombre2 = int(input("Entrez le deuxième nombre entier : "))
    nombre3 = int(input("Entrez le troisième nombre entier : "))

    # Calcul de la somme
    somme = nombre1 + nombre2 + nombre3

    # Calcul de la moyenne
    moyenne = somme / 3

    # Affichage des résultats
    print("La somme des nombres est :", somme)
    print("La moyenne des nombres est :", moyenne)

# Appel de la fonction
somme_et_moyenne()




############ EXO 2 ############


# Définir une fonction appelée statut_candidat

#     Tant que vrai
#         Demander à l'utilisateur d'entrer le pourcentage des voix obtenues par le candidat et le stocker dans la variable pourcentage
#         Convertir l'entrée de l'utilisateur en un nombre décimal (float)
        
#         Si pourcentage est entre 0 et 100 (inclus)
#             Sortir de la boucle
#         Sinon
#             Afficher "Veuillez entrer un pourcentage valide entre 0 et 100."
    
#     Si pourcentage est inférieur à 5
#         Afficher "Candidat éliminé"
#     Sinon si pourcentage est entre 5 et 50 (exclus)
#         Afficher "Candidat qualifié pour le second tour"
#     Sinon si pourcentage est supérieur ou égal à 50
#         Afficher "Candidat élu"

# Appeler la fonction statut_candidat


# Fonction pour déterminer le statut d'un candidat selon son pourcentage de voix
def statut_candidat():
    # Saisie du pourcentage des voix obtenues
    while True:
        pourcentage = float(input("Entrez le pourcentage des voix obtenues par le candidat: "))
        if 0 <= pourcentage <= 100:
            break
        else:
            print("Veuillez entrer un pourcentage valide entre 0 et 100.")

    # Détermination du statut du candidat
    if pourcentage < 5:
        print("Candidat éliminé")
    elif 5 <= pourcentage < 50:
        print("Candidat qualifié pour le second tour")
    elif pourcentage >= 50:
        print("Candidat élu")

# Appel de la fonction
statut_candidat()


############ EXO 3 ############


# Définir une fonction appelée pair_ou_impair_tant_que

#     Déclarer et initialiser un tableau nommé nombres avec les valeurs [3, 8, 15, 22, 7, 12, 9, 18, 5, 14]

#     Initialiser une variable appelée i à 0

#     Tant que i est inférieur à la longueur du tableau nombres
#         Afficher "Nombre :" suivi de la valeur de nombres à l'index i
        
#         Si la valeur de nombres à l'index i est divisible par 2 (nombres[i] % 2 == 0)
#             Afficher "Le nombre est pair"
#         Sinon
#             Afficher "Le nombre est impair"
        
#         Incrémenter i de 1

# Appeler la fonction pair_ou_impair_tant_que


# Fonction pour vérifier pair ou impair avec "while"
def pair_ou_impair():
    # Déclaration et initialisation du tableau
    nombres = [3, 8, 15, 22, 7, 12, 9, 18, 5, 14]

    # Initialisation de l'index
    i = 0

    # Parcours du tableau
    while i < len(nombres):
        # Affichage de l'entier
        print("Nombre :", nombres[i])
        
        # Vérification et affichage pair ou impair
        if nombres[i] % 2 == 0:
            print("Le nombre est pair")
        else:
            print("Le nombre est impair")
        
        # Incrémentation de l'index
        i += 1

# Appel de la fonction
pair_ou_impair()



############ EXO 4 ############

# Définir une fonction appelée compter_moyenne

#     Déclarer et initialiser un tableau nommé notes avec les valeurs [12.5, 9.0, 14.0, 18.0, 8.5, 13.0, 7.5, 11.0, 15.0, 9.5]

#     Déclarer une variable appelée compteur et l'initialiser à 0

#     Pour chaque note dans le tableau notes
#         Si la note est supérieure ou égale à 10
#             Incrémenter compteur de 1

#     Afficher "Nombre d'étudiants ayant obtenu la moyenne :" suivi de la valeur de compteur

# Appeler la fonction compter_moyenne



# Fonction pour compter les étudiants ayant obtenu la moyenne
def compter_moyenne():
    # Déclaration et initialisation du tableau
    notes = [12.5, 9.0, 14.0, 18.0, 8.5, 13.0, 7.5, 11.0, 15.0, 9.5]

    # Déclaration de la variable compteur
    compteur = 0

    # Parcours du tableau pour compter les notes supérieures ou égales à 10
    for note in notes:
        if note >= 10:
            compteur += 1

    # Affichage du résultat
    print("Nombre d'étudiants ayant obtenu la moyenne :", compteur)

# Appel de la fonction
compter_moyenne()



############ EXO 5 ############

# Définir une fonction appelée plus_grand_plus_petit

#     Déclarer et initialiser un tableau nommé nombres avec les valeurs [12, 5, 8, 45, 15, 3, 7, 14, 5, 9]

#     Initialiser une variable appelée plus_petit avec la première valeur du tableau (nombres[0])
#     Initialiser une variable appelée plus_grand avec la première valeur du tableau (nombres[0])

#     Pour chaque nombre dans le tableau nombres à partir du deuxième élément
#         Si le nombre est inférieur à plus_petit
#             Mettre à jour plus_petit avec ce nombre
#         Si le nombre est supérieur à plus_grand
#             Mettre à jour plus_grand avec ce nombre

#     Afficher "La plus petite valeur est :" suivi de la valeur de plus_petit
#     Afficher "La plus grande valeur est :" suivi de la valeur de plus_grand

# Appeler la fonction plus_grand_plus_petit



# Fonction pour trouver la plus petite et la plus grande valeur dans un tableau
def plus_grand_plus_petit():
    # Déclaration et initialisation du tableau
    nombres = [12, 5, 8, 45, 15, 3, 7, 14, 5, 9]

    # Initialisation des variables pour la plus petite et la plus grande valeur
    plus_petit = nombres[0]
    plus_grand = nombres[0]

    # Parcours du tableau pour trouver les valeurs
    for nombre in nombres[1:]:
        if nombre < plus_petit:
            plus_petit = nombre
        if nombre > plus_grand:
            plus_grand = nombre

    # Affichage des résultats
    print("La plus petite valeur est :", plus_petit)
    print("La plus grande valeur est :", plus_grand)

# Appel de la fonction
plus_grand_plus_petit()





############ EXO 6 ############

# Définir une fonction appelée presence_dans_tableau

#     Déclarer et initialiser un tableau nommé nombres avec les valeurs [12, 5, 8, 20, 12, 3, 8, 14, 1, 9]

#     Demander à l'utilisateur d'entrer l'entier à rechercher et le convertir en entier, puis le stocker dans la variable entier_recherche

#     Initialiser une variable appelée compteur à 0

#     Pour chaque nombre dans le tableau nombres
#         Si le nombre est égal à entier_recherche
#             Incrémenter compteur de 1

#     Si compteur est supérieur à 0
#         Afficher "L'entier [entier_recherche] est présent [compteur] fois dans le tableau."
#     Sinon
#         Afficher "L'entier [entier_recherche] n'est pas présent dans le tableau."

# Appeler la fonction presence_dans_tableau

# Fonction pour rechercher un entier dans un tableau et compter ses occurrences
def presence_dans_tableau():
    # Déclaration et initialisation du tableau
    nombres = [12, 5, 8, 20, 12, 3, 8, 14, 1, 9]

    # Saisie de l'entier à rechercher
    entier_recherche = int(input("Entrez l'entier à rechercher : "))

    # Initialisation du compteur
    compteur = 0

    # Parcours du tableau pour rechercher l'entier
    for nombre in nombres:
        if nombre == entier_recherche:
            compteur += 1

    # Affichage des résultats
    if compteur > 0:
        print(f"L'entier {entier_recherche} est présent {compteur} fois dans le tableau.")
    else:
        print(f"L'entier {entier_recherche} n'est pas présent dans le tableau.")

# Appel de la fonction
presence_dans_tableau()


############ EXO 7 ############
def calculatrice():
    print("Bienvenue dans la calculette")

    # Initialiser le résultat à None pour vérifier s'il s'agit du premier calcul
    resultat = None

    # Boucle infinie pour permettre des calculs en chaîne
    while True:
        # Si c'est le premier calcul, demander le premier nombre
        if resultat is None:
            a = input("Entrez le premier nombre : ")
            try:
                # Convertir l'entrée en nombre flottant
                a = float(a)
            except ValueError:
                # Afficher un message d'erreur si l'entrée n'est pas un nombre valide
                print("Veuillez entrer un nombre valide.")
                continue
        else:
            # Utiliser le résultat précédent comme premier nombre pour les calculs en chaîne
            a = resultat

        # Demander l'opérateur de l'opération
        operateur = input("Entrez l'opérateur (+, -, *, /) : ")

        # Demander le second nombre pour l'opération
        b = input("Entrez le second nombre : ")
        try:
            # Convertir l'entrée en nombre flottant
            b = float(b)
        except ValueError:
            # Afficher un message d'erreur si l'entrée n'est pas un nombre valide
            print("Veuillez entrer un nombre valide.")
            continue

        # Effectuer l'opération en fonction de l'opérateur entré
        if operateur == '+':
            resultat = a + b
        elif operateur == '-':
            resultat = a - b
        elif operateur == '*':
            resultat = a * b
        elif operateur == '/':
            # Vérifier la division par zéro
            if b == 0:
                print("Erreur : Division par zéro.")
                continue
            resultat = a / b
        else:
            # Afficher un message d'erreur si l'opérateur est invalide
            print("Opérateur non valide.")
            continue

        # Afficher le résultat de l'opération
        print(f"Résultat : {resultat}")

# Appeler la fonction calculatrice lorsque le script est exécuté
if __name__ == "__main__":
    calculatrice()



############ EXO 8 ############


# Initialisation du tableau avec des valeurs non triées
tableau = []

print("Veuillez entrer 10 entiers non triés:")
for _ in range(10):
    valeur = int(input("Entrez un entier: "))
    tableau.append(valeur)

def tri_a_bulles(tableau):
    n = len(tableau)
    # Parcours de tous les éléments du tableau
    for i in range(n):
        # Derniers i éléments sont déjà en place
        for j in range(0, n-i-1):
            # Parcours du tableau de 0 à n-i-1
            # Échanger si l'élément trouvé est plus grand que le suivant
            if tableau[j] > tableau[j+1]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
                # Affichage du tableau après chaque échange
                print("Échange effectué: ", tableau)

# Affichage du tableau avant le tri
print("Tableau avant tri: ", tableau)

# Appel de la fonction de tri
tri_a_bulles(tableau)

# Affichage du tableau après le tri
print("Tableau après tri: ", tableau)
