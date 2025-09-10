from compte import Compte

def test_retrait_refuse_si_solde_insuffisant():
    compte = Compte(50)
    compte.retrait(100)
    assert compte.solde == 50