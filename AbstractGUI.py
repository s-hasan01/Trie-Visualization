from PyQt5.QtWidgets import QMainWindow


class AbstractGUI(QMainWindow):
    """
    An class representing an abstract model of a Graphical User Interface
    application using PyQT5 Framework. Not to be instantiated.

    === Attributes ===
    height: The height of the window.
    width: The width of the window.
    """
    height: int
    width: int

    def __init__(self, height: int, width: int) -> None:
        """
        Initializes a GUI Application.

        :param height: int
        :param width: int
        """
        super(AbstractGUI, self).__init__()
        self.height = height
        self.width = width

    def setupGUI(self) -> None:
        """
        Sets up the GUI.

        :return: None
        """
        raise NotImplementedError

    def update(self) -> None:
        """
        Updates the during execution.

        :return: None
        """
        raise NotImplementedError
