# dialecte: fr

Fonctionnalité: Gestion du panier e-commerce
    Afin d'acheter des produits en ligne
    En tant que client
    Je veux pouvoir gérer mon panier et connaître le total à panier

# Contexte (ou Background)
    Contexte:
        Etant donné un panier initialisé
        Et un catalogue de produit existe:
            | référence | libellé | prix unitaire |
            | T-SHIRT   | libellé | 25.00         |
            | Pantalon  | libellé | 45.00         |
            | Pull      | libellé | 65.00         |

    Règle: Un client peut ajouter un produit au panier

        Scénario: Ajouter un produit inexistant dans le panier crée une ligne
            Quand j'ajoute l'exemplaire de "T-SHIRT" au panier
            Alors le panier contient 1 ligne
            Et la ligne "T-SHIRT" a une quantité de 1
            Et le total panier est 25.00 €

        Scénario: Ajouter plusieurs fois le même produit incrémente la quantité
            Etant donné le panier contient déjà :
                | référence | quantité |
                | T-SHIRT   | 1        |
            Quand je retire 1 exemplaires de "T-SHIRT" au panier
            Alors le panier ne contient pas "T-SHIRT"
            Et le total panier est 0.00 €

    Règle: Un client peut retirer un produit du panier

        Scénario: Retirer un produit présent supprime la ligne si quantité atteint 0
            Etant donné le panier contient déjà :
                | référence | quantité |
                | T-SHIRT   | 1        |
            Alors le panier contient 1 ligne
            Et la ligne "T-SHIRT" a une quantité de 1
            Et le total panier est 25.00 €

        Scénario: Retirer un produit non présent renvoie un message fonctionnel
            Quand je retire 1 exemplaire de "T-SHIRT"
            Alors l'opération est refusée avec le message "Produit absent du panier"
            Et le panier est inchangé
            Et le total panier est 0.00 €

    Règle: Le panier calcule automatiquement le total à partir des lignes

        Scénario: Total d'un panier vide
            Quand je consulte le total panier
            Alors le total panier est 0.00 €

        Scénario: Total sur plusieurs produits et quantités
            Etant donné le panier contient déjà :
                | référence | quantité |
                | T-SHIRT   | 3        |
                | PULL      | 1        |
            Quand je consulte le total du panier
            Alors le total panier est 140.00 €

    Règle: Le client peut modifier la quantité directement

        Scénario: Mettre unne quantité à 0 supprime la ligne
            Etant donné le panier contient déjà :
                | référence | quantité |
                | T-SHIRT   | 3        |
            Quand je fixe la quantité de "T-SHIRT" à 0
            Alors le panier ne contient pas "T-SHIRT"
            Et le total panier est 0.00 €

        Scénario: Mettre à jour une quantité positive recalcul le total
            Etant donné le panier contient déjà :
                | référence | quantité |
                | T-SHIRT   | 1        |
            Quand je fixe la quantité de "T-SHIRT" à 3
            Alors la ligne "T-SHIRT" a une quantité de 3
            Et le total panier est 75.00 €

    Plan du Scénario: Ajouter un produit met à jour quantité et total
        Etant donné un panier vide
        Quand j'ajoute <qte> exemplaire(s) de <référence> au panier
        Alors la ligne "<référence>" a une quantité de <qte>
        Et le total panier est <total> €

        Exemples:
            | référence | qte | total   |
            | T-SHIRT   | 1   | 25.00   |
            | Pantalon  | 2   | 90.00   |
            | Pull      | 3   | 195.00  |