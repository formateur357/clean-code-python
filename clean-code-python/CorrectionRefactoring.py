import datetime
import uuid
from datetime import timedelta
from dataclasses import dataclass
from typing import Optional, Dict, List

@dataclass
class Lecteur:
    nom: str

@dataclass
class Emprunt:
    livre_id: str
    lecteur_nom: str
    date_debut: datetime.datetime
    date_retour_prevue: datetime.datetime
    date_retour_effectif: Optional[datetime.datetime] = None
    amende: float = 0.0

    def est_actif(self) -> bool:
        return self.date_retour_effectif is None

class Livre:
    def __init__(self, titre, auteur, id=None, dispo=True, pages=0, tags=None, meta={}):
        self.titre = titre
        self.auteur = auteur
        self.id = id if id else str(hash(titre+auteur))[-6:]
        self.disponible = dispo          # disponibilité
        self.pages = pages          # nb pages
        self.tags = tags or []   # tags

    def est_disponible(self):
        return self.disponible

class Bibliotheque:
    def __init__(self):
        self._livres: Dict[str, Livre] = {}
        self._lecteurs: Dict[str, Lecteur] = {}
        self._emprunts: Dict[str, Emprunt] = {}
        
        self._emprunts_par_livre: Dict[str, str] = {}
        self._emprunts_par_lecteur: Dict[str, List[str]] = {}

    def ajouter_livre(self, titre, auteur, pages=0, tags=None) -> Livre :
        livre = Livre(titre, auteur, id=str(uuid.uuid), pages=pages, tags=tags)
        return livre
    
    def ajouter_lecteur(self, nom: str) -> Lecteur :
        if nom not in self._lecteurs:
            self._lecteurs[nom] = Lecteur(nom=nom)
        return self._lecteurs[nom]
    
    def get_livre(self, livre_id: str) -> Livre:
        return self._livres[livre_id]
    
    def get_lecteur(self, nom_lecteur: str) -> Livre:
        return self._lecteurs[nom_lecteur]
    
    def lister_livres(self) -> List[Livre]:
        return list(self._livres.values())

    def lister_lecteurs(self) -> List[Lecteur]:
        return list(self._lecteurs.values())
    
    def emprunter(self, livre_id: str, nom_lecteur: str, jours=14) -> Emprunt :
        livre = self.get_livre(livre_id)
        if not livre and livre.est_disponible():
            raise ValueError("ce livre est indisponible")

        debut = datetime.now()
        retour_prevu = debut + timedelta(days=jours)

        emprunt = Emprunt(
            id = str(uuid.uuid4())[:8],
            livre_id = livre_id,
            lecteur_nom = nom_lecteur,
            date_debut = debut,
            date_retour_prevue = retour_prevu
        )
        
        livre.disponible = False
        self._emprunts[emprunt.id] = emprunt
        self._emprunts_par_livre[livre_id] = emprunt.id
        self._emprunts_par_lecteur[nom_lecteur] = emprunt.id

        return emprunt
    
    def prolonger(self, emprunt_id: str, jours_suppl=7) -> Emprunt :
        emprunt = self.list_emprunts[emprunt_id]

        if not emprunt.est_actif():
            raise ValueError("Emprunt déjà rendu.")

        emprunt.date_retour_prevu += timedelta(days=jours_suppl)
        
        return emprunt
    
    def rendre(self, emprunt_id: str, date_retour: Optional[datetime.datetime] = None) -> Emprunt:
        emprunt = self._emprunts[emprunt_id]

        if not emprunt.est_actif():
            return emprunt
        
        date_retour = date_retour or datetime.now()
        emprunt.date_retour_effectif = date_retour

        # Calcul du retard
        retard = (date_retour.date() - emprunt.date_retour_prevu.date()).days
        emprunt.amende = calculer_amende(retard)

        # liberer le livre
        livre = self.get_livre(emprunt.livre_id)
        livre.disponible = True

        self._emprunts_par_livre.pop(emprunt.livre_id, None)

        return emprunt
    
    
def calculer_amende(jours_retard: int) -> float :
    if (jours_retard <= 0):
        return 0.0
    
    return 0.25 * jours_retard

def emprunts_pour_lecteur(self, nom_lecteur: str) -> List[Emprunt] :
    return [self._emprunts[eid]  for eid in self._emprunts_par_lecteur.get(nom_lecteur, [])]

def total_amendes_lecteur(self, nom_lecteur: str) -> float : 
    return sum(e.amende for e in self.emprunts_pour_lecteur(nom_lecteur))
