"""This module provide access to Statistic class"""
import os
import string
import itertools


class Statistic:
    """
    This class processes text file. Count number of characters, words, sentences that the text contains.

    Attributes:
        file (str): The name of the text file.
    """

    def __init__(self, file: str):
        """
        Initialisation of the attributes the class Statistic.

        Args:
            file (str): The name of the text file.
        """

        if not os.path.isfile(file):
            raise FileNotFoundError("The file does not exist")

        self.file = file

    def text(self):
        """
        Return sequence of characters contained in the text file.
        """

        with open(self.file, "r", encoding="utf-8") as f:
            for text in f:
                for char in text:
                    yield char

    def count_chars(self):
        """
        Return quantity of characters in the text file.
        """

        chars_quantity = 0
        for char in self.text():
            if not char.isspace():
                chars_quantity += 1
        return chars_quantity

    def ispunct(self, char: str):
        """
        Return True if character is punctuation symbol, otherwise False.

        Args:
            char (str): The character to be checked.
        """

        if char in string.punctuation:
            return True
        return False

    def words(self):
        """
        Return sequence of words contained in the text file.
        """

        word = []
        it = iter(self.text())
        while True:
            for c in itertools.takewhile(lambda x: x not in string.whitespace, it):
                word.append(c)
            else:
                if word:
                    str_word = ''.join(word)
                    if not str_word.isnumeric() and not self.ispunct(str_word):
                        yield str_word
                        word.clear()
                        continue
                else:
                    break

    def count_words(self):
        """
        Return quantity of words in the text file.
        """

        words_quantity = 0
        for _ in self.words():
            words_quantity += 1
        return words_quantity

    def sentences(self):
        """
        Return sequence of sentences contained in the text file.
        """

        sentence = []
        it = iter(self.text())
        while True:
            for c in itertools.takewhile(lambda x: x != "." and x != "!" and x != "?", it):
                sentence.append(c)
            else:
                if sentence:
                    str_sentence = ''.join(sentence)
                    yield str_sentence.strip()
                    sentence.clear()
                    continue
                else:
                    break

    def count_sentences(self):
        """
        Return quantity of sentences in the text file.
        """

        sentences_quantity = 0
        for sentence in self.sentences():
            if sentence:
                sentences_quantity += 1
        return sentences_quantity

    def __str__(self):
        return f"File contains {self.count_chars()} characters, "\
               f"{self.count_words()} words, "\
               f"{self.count_sentences()} sentences."
