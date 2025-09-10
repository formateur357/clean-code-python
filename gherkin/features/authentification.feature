Fonctionnalité: Authentification
    Afin de sécuriser l'accès au système
    En tant qu'utilisateur
    Je veux pouvoir me connecter avec un identifiant et un mot de passe

    Scenario: Connexion réussie
        Etant donné un utilisateur "alice" avec le mot de passe "1234"
        Quand elle tente de se connecter avec "alice" et "1234"
        Alors l'accès est autorisé