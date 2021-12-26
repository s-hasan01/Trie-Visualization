from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from AbstractGUI import AbstractGUI
from PrefixTree import PrefixTree


class TrieVisual(AbstractGUI):

    def __init__(self, height: int = 600, width: int = 900) -> None:
        super().__init__(height, width)
        self.trie = PrefixTree()
        self.setupGUI()

    def setupGUI(self) -> None:
        self.setGeometry(400, 200, self.width, self.height)

    def update(self) -> None:
        pass
