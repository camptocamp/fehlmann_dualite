import timeit

t = timeit.timeit(stmt='calcul.calcul(entrees, 99001, 100000, 101, 400, [1, 3, 5, 7])',
                  setup='from dualite_transnumerique import calcul, entree; entrees=entree.aleatoire(300000)',
                  number=1)
print(t)
