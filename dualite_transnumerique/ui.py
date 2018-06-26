import os
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from typing import List

from . import entree, calcul

HERE = os.path.abspath(os.path.dirname(__file__))


class Fenetre(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(os.path.join(HERE, 'fenetre.ui'), self)
        self._set_valeurs(entree.aleatoire(1000000))


    @pyqtSlot(bool)
    def on_fichierRandom1m_toggled(self, enabled: bool) -> None:
        if enabled:
            self._set_valeurs(entree.aleatoire(1000000))

    @pyqtSlot(int)
    def on_secteurBaseMax_valueChanged(self, valeur: int) -> None:
        self.secteurBaseMin.setMaximum(valeur - 1)

    @pyqtSlot(int)
    def on_comparoMax_valueChanged(self, valeur: int) -> None:
        self.comparoMin.setMaximum(valeur - 1)

    @pyqtSlot(int)
    def on_formuleDelta1_valueChanged(self, valeur: int) -> None:
        self.formuleDelta2.setMinimum(valeur + 1)

    @pyqtSlot(int)
    def on_formuleDelta2_valueChanged(self, valeur: int) -> None:
        self.formuleDelta3.setMinimum(valeur + 1)

    @pyqtSlot(int)
    def on_formuleDelta3_valueChanged(self, valeur: int) -> None:
        self.formuleDelta4.setMinimum(valeur + 1)

    @pyqtSlot()
    def on_execute_clicked(self) -> None:
        plus, moins = calcul.calcul(self._valeurs, self.secteurBaseMin.value(), self.secteurBaseMax.value(),
                                    self.comparoMin.value(), self.comparoMax.value(),
                                    [
                                        self.formuleDelta1.value(),
                                        self.formuleDelta2.value(),
                                        self.formuleDelta3.value(),
                                        self.formuleDelta4.value()
                                    ])
        self.plusA.setText(str(plus))
        self.moinsA.setText(str(moins))

    def _set_valeurs(self, valeurs: List[int]) -> None:
        self._valeurs = valeurs
        for widget in (self.secteurBaseMin, self.secteurBaseMax):
            widget.setMaximum(len(valeurs))


def main() -> None:
    app = QApplication(sys.argv)
    fenetre = Fenetre()
    fenetre.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
