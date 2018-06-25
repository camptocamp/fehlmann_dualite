from dualite_transnumerique import algo


def test_compare():
    assert algo.compare([1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0]) == \
        [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]


def test_delta():
    assert algo.delta(1, 1, 0, 0) is False
    assert algo.delta(1, 0, 0, 1) is False
    assert algo.delta(1, 0, 0, 0) is True
    assert algo.delta(1, 0, 1, 0) is False
    assert algo.delta(0, 1, 0, 0) is True
    assert algo.delta(0, 0, 0, 0) is True


def test_binomes():
    assert algo.binomes([False, False, True, False, True, True]) == [True, False, False, False, True]


def test_decompte():
    assert algo.decompte([True, False, False, False, True]) == (2, 3)
