# Exercice SRP #1 — Classe qui fait “tout”
# Énoncé

# On vous donne une classe Invoice qui :
# - charge des données depuis un fichier JSON,
# - calcule le total,
# - formate un reçu en texte,
# - imprime en console.

# Objectif : appliquer le Single Responsibility Principle.
# Séparer chargement, calcul, formatage, sortie.
# Invoice (ou InvoiceBuilder) ne doit faire que le calcul à partir de données en mémoire

import json

class Invoice:
    def __init__(self, path):
        self.path = path
        self.items = []
        self.total = 0.0

    def run(self):
        # I/O (chargement)
        with open(self.path, "r", encoding="utf-8") as f:
            self.items = json.load(f)

        # Calcul
        t = 0.0
        for it in self.items:
            t += it.get("qty", 0) * it.get("price", 0.0)
        self.total = t

        # Formatage + I/O
        receipt = ["--- RECEIPT ---"]
        for it in self.items:
            receipt.append(f"{it['name']} x{it['qty']}: {it['price']:.2f}€")
        receipt.append(f"TOTAL: {self.total:.2f}€")
        out = "\n".join(receipt)
        print(out)
        return out

# Exercice SRP #2 — Report : calcul vs formatage vs stockage
# Énoncé

# La classe Report ci-dessous mélange calcul du total, formatage et sauvegarde disque.

# Objectif :
# - ReportBuilder retourne un DTO (dict) avec count et total.
# - ReportRenderer produit une chaîne depuis ce DTO.
# - ReportStorage encapsule l’écriture fichier.

# On doit pouvoir générer le rapport sans écrire sur disque.

import json

class Report:
    def __init__(self, path):
        self.path = path

    def generate(self, save_path):
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        total = sum(row.get("amount", 0.0) for row in data)
        text = f"COUNT={len(data)}\nTOTAL={total:.2f}"
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(text)
        return text
