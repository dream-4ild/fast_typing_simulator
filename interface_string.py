from constants import CORRECT_COLOR, INCORRECT_COLOR, NEUTRAL_COLOR


class interface_string:
    def __init__(self, value: str):
        """
        :param value: string to be converted
        """
        self._string = value
        self._last_correct = -1
        self._first_neutral = 0

    def get_string_with_color(self) -> list[(str, str)]:
        """
        Returns the string as blocks of colors
        """
        return [(self._string[:self._last_correct + 1], CORRECT_COLOR),
                (self._string[self._last_correct + 1:self._first_neutral], INCORRECT_COLOR),
                (self._string[self._first_neutral:], NEUTRAL_COLOR)]

    def enter_symbol(self, symbol: str) -> bool:
        """
        Checks if the symbol entered is correct.
        :param symbol: entered symbol
        :return: True if the symbol entered correct && it was the last symbol in string, False otherwise
        """

        if symbol == self._string[self._last_correct + 1]:
            if self._first_neutral == self._last_correct + 1:
                self._first_neutral += 1

            self._last_correct += 1

            return self._first_neutral == len(self._string)
        else:
            if self._first_neutral == self._last_correct + 1:
                self._first_neutral += 1
            return False
