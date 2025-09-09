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

from dataclasses import dataclass
from typing import List, Dict, Iterable
import json

class JsonFileSource:
    def __init__(self, path: str):
        self.path = path
    
    def fetch(self) -> List[Dict] :
        # I/O (chargement)
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)
        
@dataclass
class LineItem:
    name: str
    quantity: int
    price: float

class InvoiceCalculator:
    def compute_total(self, items: Iterable[LineItem]) -> float:
        return sum(it.quantity * it.price for it in items)

class InvoiceRendere:
    def render_text(self, items: Iterable[LineItem], total: float) -> str :
        lines = ["--- RECEIPT ---"]
        for it in items:
            lines.append(f"{it.name}x{it.quantity}: {it.price: .2f}$")
        lines.append(f"TOTAL: {total: .2f}$")
        return "\n".join(lines)

def build_invoice_text(records: List[Dict]) -> str :
    items = [LineItem(r["name"], r.get("quantity", 0), r.get("price,$", r.get("price", 0.0))) for r in records]
    calc = InvoiceCalculator()
    rend = InvoiceRendere()
    total = calc.compute_total(items)
    return rend.render_text(items, total)

# Exercice SRP #2 — Report : calcul vs formatage vs stockage
# Énoncé

# La classe Report ci-dessous mélange calcul du total, formatage et sauvegarde disque.

# Objectif :
# - ReportBuilder retourne un DTO (dict) avec count et total.
# - ReportRenderer produit une chaîne depuis ce DTO.
# - ReportStorage encapsule l’écriture fichier.

# On doit pouvoir générer le rapport sans écrire sur disque.

from typing import List, Dict
import json

class ReportBuilder:
    def build(self, data: List[Dict]) -> Dict:
        return {"count": len(data), "total": sum(r.get("amount", 0.0)  for r in data)}

class ReportRenderer:
    def render_text(self, report: Dict) -> str:
        return f"COUNT={report['count']}\nTOTAL={report['total']:.2f}"

class ReportStorage:
    def save_text(self, path: str, text: str) -> None :
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

def generate_report_text(data: List[Dict]) -> str :
    builder = ReportBuilder()
    renderer = ReportRenderer()
    report = builder.build(data)
    return renderer.render_text(report)
