import cProfile
from dualite_transnumerique import calcul, entree

cProfile.run('calcul.calcul(entree.aleatoire(300000), 99001, 100000, 101, 400, [1, 3, 5, 7])',
             sort='cumulative')
