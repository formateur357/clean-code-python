# Code volontairement "sale" mais compact pour exercice de refactoring.

import datetime

# État global simpliste (à éliminer plus tard)
USERS = []          # lecteurs
EMPRUNTS = []       # (id_livre, lecteur, date_debut, date_retour)

class Livre:
    # x1: titre, y2: auteur, id: identifiant
    def __init__(self, x1, y2, id=None, dispo=True, pages=0, tags=None, meta={}):
        self.x1 = x1
        self.y2 = y2
        self.id = id if id else str(hash(x1+y2))[-6:]
        self.t = dispo          # disponibilité
        self.pages = pages          # nb pages
        self.tags = tags or []   # tags
        self.meta = meta        # dict mutable par défaut (mauvaise pratique)
        self.u = None           # lecteur courant (mauvais SRP)
        self._ret = None        # date retour prévue
        self._frais = 0.0
        self.historique = []          # historique texte (mélangé au domaine)

    def __repr__(self):
        return f"Livre<{self.id}:{self.x1}>"

    # --- Duplications & noms obscurs ---
    def dispo(self):
        return self.t

    def dispo2(self):
        # doublon de dispo()
        if self.t:
            return True
        else:
            return False

    def setR(self, v=True):
        # “reserve” au nom peu parlant + side effects
        self.meta["reserved"] = v
        self.hist.append(f"reserve={v}")

    def ttt(self, who):
        # assigne un lecteur (mauvais SRP)
        self.u = who
        if who not in USERS:
            USERS.append(who)
        self.hist.append(f"lecteur={who}")

    # --- Méthode fourre-tout : calcule, I/O, side effects, constantes magiques ---
    def calc(self, a1=0, a2=0, mode="A"):
        # a1/a2 imaginés comme jours de retard
        if mode == "A":
            amende = (a1 + a2) * 0.25
        elif mode == "B":
            amende = (a1 * 2 + a2 * 3) * 0.1
        else:
            amende = 1.99
        self._frais += amende
        print("AMENDE:", amende)  # I/O dans la logique métier
        return amende

    # --- Emprunt/Retour mélangés dans Livre (SRP violé) ---
    def emprunter(self, lecteur, jours=14):
        if not self.t:
            print("pas dispo")   # I/O
            return False
        self.t = False
        self.u = lecteur
        if lecteur not in USERS:
            USERS.append(lecteur)
        d = datetime.datetime.now()
        self._ret = d + datetime.timedelta(days=jours)
        EMPRUNTS.append((self.id, lecteur, d, self._ret))
        self.hist.append(f"EMPRUNT {lecteur} -> {d} ret {self._ret}")
        return True

    def prolonger(self, extra=7):
        if not self._ret:
            return None
        self._ret = self._ret + datetime.timedelta(days=extra)
        self.hist.append(f"PROLONG +{extra} -> {self._ret}")
        return self._ret

    def rendre(self):
        if not self._ret:
            return 0.0
        now = datetime.datetime.now()
        retard = (now - self._ret).days
        if retard < 0: retard = 0
        am = self.calc(retard, 0, "A")  # réutilise la méthode fourre-tout
        self.t = True
        self.u = None
        # nettoie l’état global (couplage)
        global EMPRUNTS
        EMPRUNTS = [e for e in EMPRUNTS if e[0] != self.id]
        self.hist.append(f"RETOUR -> {now} retard={retard} amende={am}")
        return am

    # --- Présentation (I/O) mêlée au domaine ---
    def afficher(self):
        txt = f"[{self.id}] {self.x1} - {self.y2}"
        if not self.t:
            txt += f" (EMPRUNTÉ par {self.u} jusqu'au {self._ret})"
        else:
            txt += " (DISPO)"
        print(txt)  # I/O
        return txt

    # --- Duplications de calcul d’amende “quasi pareil” ---
    def m2(self, a, b):
        c = (a * 0.25) + (b * 0.25)
        self._frais += c
        return c

    def m3(self, a, b):
        c = (a + b) * 0.25
        self._frais += c
        return c

# --- Fonctions procédurales couplées au global (à déplacer plus tard dans Bibliotheque) ---

def create_sample():
    l1 = Livre("Le Soleil", "A.Dupont", pages=321)
    l2 = Livre("Lune Noire", "B.Durand", dispo=False)
    l3 = Livre("Étoiles", "C.Martin", tags=["SCIENCE"], pages=456)
    return [l1, l2, l3]

def list_emprunts():
    print("== EMPRUNTS ==")   # I/O mêlé aux données
    for e in EMPRUNTS:
        print(e)
    return EMPRUNTS

def user_total_fees(user):
    total = 0.0
    # parcourt les emprunts puis reconstruit via un lookup naïf
    ids = [e[0] for e in EMPRUNTS if e[1] == user]
    # ici on ne peut pas retrouver les objets Livre facilement → signe d’un mauvais design
    # hack “pédagogique” : on suppose que l’appelant a encore une liste de livres
    return total

if __name__ == "__main__":
    livres = create_sample()
    l = livres[0]
    l.afficher()
    l.emprunter("alice", 7)
    l.prolonger(3)
    l.afficher()
    list_emprunts()
    # Simule un retard de 2 jours
    l._ret = datetime.datetime.now() - datetime.timedelta(days=2)
    am = l.rendre()
    print("Amende due:", am)
