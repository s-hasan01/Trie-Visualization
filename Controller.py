import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from AbstractGUI import AbstractGUI
from TrieVisual import TrieVisual


class Controller(AbstractGUI):

    def __init__(self, height: int = 300, width: int = 400) -> None:
        super().__init__(height, width)
        self.input = QtWidgets.QLineEdit(self)
        self.button = QtWidgets.QPushButton(self)
        self.visual = TrieVisual()
        self.setupGUI()

    def setupGUI(self) -> None:
        self.setGeometry(70, 200, self.height, self.width)
        self.setWindowTitle('Trie Visualization')
        self.input.move(20, 30)
        self.button.setText('Insert Word')
        self.button.move(10, 65)
        self.button.clicked.connect(lambda x: self.insert())

    def insert(self) -> None:
        word = self.input.text().lower()
        self.visual.trie.insert(word)
        self.visual.show()
        print(self.visual.trie.sort())

    def update(self) -> None:
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())
