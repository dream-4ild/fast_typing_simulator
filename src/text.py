from os import listdir
from random import randint

from src.constants import DEFAULT_PATH, MAX_SYMBOLS_IN_LINE


class Text:
    def __init__(self, path: str, language: str):
        """
        :param path:
        :param language:
        """
        if path == "":
            path = DEFAULT_PATH + language + "/"
            count_files = sum(elem.endswith('.txt') for elem in listdir(path))

            path += "/default_text_" + f"{randint(0, count_files - 1)}.txt"

        with open(path, "r") as file:
            raw_text = file.read()
            self._text = Text._process_text(raw_text)

        self._current_line = 0

    @staticmethod
    def _process_text(raw_text: str) -> list[str]:
        """
        Processes the raw text and returns a list of strings.
        :param raw_text: any text
        :return: list of strings with a length of no more than MAX_SYMBOLS_IN_LINE
        """
        raw_text = raw_text.replace("\r", " ").replace("\t", " ").replace("«", '"').replace("»", '"').replace("–", "-")

        ans = []

        for row in raw_text.split("\n"):
            current_text = ""
            for word in row.split(" "):
                if len(current_text) + len(word) + 1 > MAX_SYMBOLS_IN_LINE:
                    ans.append(current_text + " ")
                    current_text = ""

                current_text += (" " if len(current_text) > 0 else "") + word

            if current_text != "":
                ans.append(current_text + " ")

        ans[-1] = ans[-1][:-1]

        return ans

    def get_string(self) -> str:
        """
        Returns the current line as a string.
        :return: current line
        :exception IndexError: if current text is over
        """
        self._current_line += 1

        if self._current_line == len(self._text) + 1:
            return ""

        if self._current_line > len(self._text) + 1:
            raise IndexError

        return self._text[self._current_line - 1]
