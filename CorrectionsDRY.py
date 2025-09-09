# Exercice DRY #1 — Trois branches quasi identiques
# Énoncé

# La fonction applique une remise selon le type client, puis la TVA, puis “clip” à 0 et arrondit.
# Le code répète les mêmes opérations dans chaque branche.

# Objectif : DRY — une seule fonction de calcul avec paramètres (discount, TVA), et un mapping type→remise.

TVA = 1.20
DISCOUNTS = {"VIP": 0.20, "PRO": 0.10, "STD": 0.00}

def _apply_rules(amount: float, discount: float, tva: float) -> float :
    price = amount * (1 - discount)
    price = price * tva
    price = max(0.0, price)
    return round(price, 2)

def price_after_rules(amount: float, customer_type: str) -> float:
    discount = DISCOUNTS.get(customer_type, DISCOUNTS["STD"])
    return _apply_rules(amount, discount, TVA)

# Exercice DRY #2 — Duplication de parsing / normalisation
# Énoncé

# Deux fonctions normalisent des noms presque de la même façon, à un détail près (préfixe appliqué ou non).

# Objectif : DRY — extraire une fonction commune de normalisation,
# puis la réutiliser avec une petite personnalisation (paramètre prefix).

def _normalize_core(name: str) -> str :
    base = name.strip().lower()
    base = " ".join(p for p in base.split() if p)
    return base.capitalize()

def normalize_user(name: str) -> str:
    return _normalize_core(name)

def normalize_admin(name: str) -> str:
    return "[admin] " + _normalize_core(name)
