Fonctionnalité: Gestion de compte bancaire
    Afin de sécuriser les retraits
    En tant que titulaire de compte
    Je veux que le solde ne devienne jamais négatif

    Contexte:
        Etant donné un compte avec un solde initial de 100

    Scénario: Retrait valide
        Quand je retire 40
        Alors le solde doit etre 60

    Scénario: Retrait refusé
        Quand je retire 200
        Alors le retrait est refusé
        Et le solde reste 100
