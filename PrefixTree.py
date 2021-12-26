from __future__ import annotations
from typing import Dict, List


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


class PrefixTree:
    """
    A Tree-like Data Structure used for efficiently working with strings. Useful
    for adding, removing, searching and sort strings.

    === Attributes ===

    char: The character stored in the node.
    children: The subtrees of the node.
    value: The word constructed by the path leading upto the node.

    """
    _char: str
    _children: Dict[str, PrefixTree]
    _value: str

    def __init__(self, char: str = '', value: str = '') -> None:
        """
        Initializes a PrefixTree object.

        :param char: str
        :param value: str
        """
        self._char = char
        self._value = value
        self._children = {}

    def insert(self, word: str) -> None:
        """
        Inserts <word> into the PrefixTree.

        :param word: str
        :return: None
        """
        curr = self
        for char in word:
            if char not in curr._children:
                curr._children[char] = PrefixTree(char)
            curr = curr._children[char]
        curr._value = word

    def remove(self, word: str) -> None:
        """
        Removes <word> from the PrefixTree.

        :param word:
        :return: None
        """
        self.delete(word, 0)

    def delete(self, word: str, index: int) -> bool:
        """
        Helper for the remove function.

        :param word: str
        :param index: int
        :return: None
        """
        if len(word) == index:
            self._value = ''

        else:
            char = word[index]
            if (
                    char in self._children
                    and self._children[char].delete(word, index + 1)
            ):
                del self._children[char]

        return not self._value and len(self._children) == 0

    def sort(self, reverse: bool = False) -> List[str]:
        """
        Returns a sorted list of strings in alphabetical order (a-z). If
        <reversed> is <True>, then the array is sorted backwards from reverse
        alphabetical order (z-a).

        :return: List[str]
        """
        if len(self._children) == 0:
            return [self._value]

        letters = ALPHABET if not reverse else ALPHABET[::-1]
        words = [self._value] if not reverse and self._value else []

        for char in letters:
            if char in self._children:
                words.extend(self._children[char].sort(reverse=reverse))

        return words.append(self._value) if self._value and reverse else words

    def contains(self, word: str) -> bool:
        """
        Returns <True> if the given word is in the Tree, <False> otherwise.

        :param word: str
        :return: bool
        """
        return word in self

    def __contains__(self, word: str) -> bool:
        """
        Built-in method for the 'in' operator. Logic for 'contains' method.

        :param word: str
        :return: bool
        """
        curr = self
        for char in word:
            if char in curr._children:
                curr = curr._children[char]

        return curr._value == word


if __name__ == '__main__':
    tree = PrefixTree()
    tree.insert('hello')
    tree.insert('logarithm')
    tree.insert('awesome')
    tree.insert('aardvark')
    print(tree.sort())
