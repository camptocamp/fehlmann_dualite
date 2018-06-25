import pytest

from dualite_transnumerique import calcul, erreur


def test_calcul(donnees):
    assert calcul.calcul(donnees, 7, 18, 2, 3, [1, 4, 5, 7]) == (5, 5)


def test_parametres_invalide(donnees):
    with pytest.raises(erreur.Erreur, match="Le début du secteur de base doit être plus grand que 0"):
        calcul.calcul(donnees, 0, 18, 2, 3, [1, 4, 5, 7])

    with pytest.raises(erreur.Erreur, match="La fin du secteur de base doit être plus grand que le début"):
        calcul.calcul(donnees, 7, 6, 2, 3, [1, 4, 5, 7])

    with pytest.raises(erreur.Erreur,
                       match="La fin du secteur de base doit être plus petit ou égale au nombre d'entrées"):
        calcul.calcul(donnees, 7, len(donnees) + 1, 2, 3, [1, 4, 5, 7])

    with pytest.raises(erreur.Erreur, match="La fin des comparos doit être plus grand ou égale au début"):
        calcul.calcul(donnees, 7, 18, 2, 1, [1, 4, 5, 7])

    with pytest.raises(erreur.Erreur, match="Il faut 4 chiffres pour la formule delta"):
        calcul.calcul(donnees, 7, 18, 2, 3, [1, 4, 5])

    with pytest.raises(erreur.Erreur,
                       match="L'entrée N°3 de la formule delta doit être plus grande que les précédentes"):
        calcul.calcul(donnees, 7, 18, 2, 3, [1, 4, 2, 7])
