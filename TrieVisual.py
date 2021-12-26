from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from AbstractGUI import AbstractGUI


class TrieVisual(AbstractGUI):

    def __init__(self, height: int = 600, width: int = 900) -> None:
        super().__init__(height, width)
        self.setupGUI()

    def setupGUI(self) -> None:
        self.setGeometry(400, 200, self.width, self.height)

    def update(self) -> None:
        pass


if __name__ == '__main__':
    app = TrieVisual()
    app.run()
