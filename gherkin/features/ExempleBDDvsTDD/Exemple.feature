Fonctionnalité: Gestion du compte bancaire
    Scénario: Retrait refusé si solde insuffisant
        Etant donné un compte avec solde 50
        Quand je retire 100
        Alors le retrait est refusé
        Et le solde reste 50