# Qu'est qu'une bonne fonction

# Une fonction propre est :
# - Courte (<= 20, >= 50)
# - Nom explicite (verbe/action -> CalculerSalaire, envoyerEmail)
# - Une seule responsabilité
# - Sans effets secondaires cachés
# - Réutilisable et Testable

# Une fonction doit dire ce qu'elle fait et ne doit faire que ça.


# Eviter les effets secondaires

# Mauvais
total = 0
def add(x):
    global total
    total += x

# Bon
def add(total, x):
    return total + x

# Niveau d'abstraction unique

# Mauvais
def generer_facture():
    total = somme_articles()
    print("Facture générée :", total)

# Bon
def generer_facture():
    total = somme_articles()
    afficher_factures(total)


# Nombre d'arguments entre 0 et 2, 3 tolérés

# Mauvais
createUser("Alice", True)

# Bon
createUser("Alice")
createUserWithEmail("Alice")

# Déclarations claires, éviter les nombres magiques

# Mauvais
if (vitesse > 120) { ... }

# Bon
const VITESSE_MAX = 120

if (vitesse > VITESSE_MAX) { ... }




# Organisation des classes

# Une classe doit être petite et avoir une seule responsabilité

# Ordre recommandé :
# - Attributs
# - Constructeurs
# - Méthodes publiques
# - Méthodes privées



# Commentaires

# Les bons commentaires expliquent le pourquoi.

# Les mauvais commentaires décrivent le code.

# Mauvais
i = i + 1 # ajoute 1 à i

# Bon
# Correction du bug #132 lié à l'indexation
i = i + 1