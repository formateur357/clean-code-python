# Exercice DRY #1 — Trois branches quasi identiques
# Énoncé

# La fonction applique une remise selon le type client, puis la TVA, puis “clip” à 0 et arrondit.
# Le code répète les mêmes opérations dans chaque branche.

# Objectif : DRY — une seule fonction de calcul avec paramètres (discount, TVA), et un mapping type→remise.

def price_after_rules(amount: float, customer_type: str) -> float:
    if customer_type == "VIP":
        price = amount - (amount * 0.2)
        price = price * 1.2
        if price < 0: price = 0
        return round(price, 2)
    elif customer_type == "PRO":
        price = amount - (amount * 0.1)
        price = price * 1.2
        if price < 0: price = 0
        return round(price, 2)
    else:  # STD
        price = amount - (amount * 0.0)
        price = price * 1.2
        if price < 0: price = 0
        return round(price, 2)

# Exercice DRY #2 — Duplication de parsing / normalisation
# Énoncé

# Deux fonctions normalisent des noms presque de la même façon, à un détail près (préfixe appliqué ou non).

# Objectif : DRY — extraire une fonction commune de normalisation,
# puis la réutiliser avec une petite personnalisation (paramètre prefix).

def normalize_user(name: str) -> str:
    name = name.strip().lower()
    name = " ".join(p for p in name.split() if p)
    return name.capitalize()

def normalize_admin(name: str) -> str:
    name = name.strip().lower()
    name = " ".join(p for p in name.split() if p)
    name = name.capitalize()
    return "[admin] " + name
