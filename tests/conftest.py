import pytest


DONNEES = [
    1,
    1,
    0,
    1,
    0,
    1,
    1,
    0,
    0,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0
]


@pytest.fixture
def donnees():
    return DONNEES
