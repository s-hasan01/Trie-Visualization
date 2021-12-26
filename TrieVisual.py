from AbstractGUI import AbstractGUI
from PrefixTree import PrefixTree


class TrieVisual(AbstractGUI):
    """
    The window for displaying the Trie Tree. Subclass of AbstractGUI. Is a
    concrete class and can be instantiated.

    === Attributes ===
    trie: The Trie Tree that is to be visualized.
    """
    trie: PrefixTree

    def __init__(self, height: int = 600, width: int = 900) -> None:
        """
        Initializes the Trie Window.

        :param height: int
        :param width: int
        """
        super().__init__(height, width)
        self.trie = PrefixTree()
        self.setupGUI()

    def setupGUI(self) -> None:
        self.setGeometry(400, 200, self.width, self.height)

    def update(self) -> None:
        # TODO: Implement this method.
        pass
