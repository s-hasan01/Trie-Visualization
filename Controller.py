import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from AbstractGUI import AbstractGUI
from TrieVisual import TrieVisual


class Controller(AbstractGUI):
    """
    The class that is responsible for controlling the Trie Visual window. All
    user interaction and update signals are through this class. Subclass of
    AbstractGUI. Concrete class and is to be instantiated.

    === Attributes ===
    visual: The TrieVisual to be updated depending on user's input.
    """
    visual: TrieVisual

    def __init__(self, height: int = 300, width: int = 400) -> None:
        """
        Initializes the Controller window.

        :param height: int
        :param width: int
        """
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
        self.button.clicked.connect(lambda x: self.update())

    def insert(self) -> None:
        """
        Command for then the insert button is pressed. Inserts the given word in
        the line text into the Trie.

        :return: None
        """
        word = self.input.text().lower()
        self.visual.trie.insert(word)

    def update(self) -> None:
        self.insert()
        self.visual.show()
        print(self.visual.trie.sort())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())
