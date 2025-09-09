import pytest

@pytest.fixture(scope="session") # Before ALL
def default_rate():
    return 1.20 # taux constant réutilisé

@pytest.fixture # Before EACH
def start_value():
    return 0 # valeur de depart "fraiche" pour chaque test