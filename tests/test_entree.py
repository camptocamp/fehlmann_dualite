import os

from dualite_transnumerique import entree

HERE = os.path.abspath(os.path.dirname(__file__))


def test_aleatoire():
    nb = 1000
    colonnes = entree.aleatoire(nb)
    for valeurs in colonnes:
        assert abs(valeurs.count(1) - nb / 2) < 100


def test_fichier(donnees):
    colonnes = entree.fichier(os.path.join(HERE, 'data.txt'))
    assert colonnes[0] == donnees
