# language: fr

Fonctionnalité: Calcul des frais d'expédition
    Afin de connaître le montant à payer
    En tant que client
    Je veux que le total intègre les frais d'expédition et options

    # Règles :
    # - Port standard: +5 € si sous-total < 50, sinon 0
    # Express: +10€ toujours
    # Fragile: +2€

    Plan du Scenario: Total avec différentes options d'expédition
        Etant donné un sous-total de <sous_total>
        Et l'option express est "<express>"
        Et l'option fragile est "<fragile>"
        Quand je calcule le total
        Alors le total doit être <total_attendu>

        Exemples:
            | sous_total | express | fragile | total_attendu |
            | 40         | false   | false   | 45            |
            | 40         | true    | false   | 55            |
            | 40         | false   | true    | 47            |
            | 40         | true    | true    | 57            |
            | 50         | false   | false   | 50            |
            | 50         | true    | false   | 60            |
            | 50         | false   | true    | 52            |
            | 50         | true    | true    | 62            |
