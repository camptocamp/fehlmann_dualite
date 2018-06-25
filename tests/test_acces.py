from dualite_transnumerique import acces


def test_intervale(donnees):
    assert acces.intervale(donnees, 7, 18) == [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]


def test_intervale_reboucle():
    assert acces.intervale([1, 2, 3, 4], 0, 2) == [4, 1, 2]
    assert acces.intervale([1, 2, 3, 4], 3, 5) == [3, 4, 1]
    assert acces.intervale([1, 2, 3, 4], 7, 9) == [3, 4, 1]


def test_itere_comparos(donnees):
    assert list(acces.itere_comparos(donnees, 7, 18, 2, 3)) == [
        [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
    ]


def test_itere_delta():
    assert [list(delta) for delta in acces.itere_delta([1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0], [1, 4, 5, 7])] == [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
