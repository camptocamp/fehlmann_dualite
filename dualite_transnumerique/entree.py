from typing import List

import secrets


def aleatoire(nb: int) -> List[int]:
    return [secrets.randbelow(2) for _ in range(nb)]


def fichier(chemin: str) -> List[int]:
    resultat = []
    with open(chemin) as lignes:
        for ligne in lignes:
            ligne = ligne.strip()
            if ligne != '':
                entier = int(ligne)
                assert entier in (0, 1)
                resultat.append(entier)
    return resultat
