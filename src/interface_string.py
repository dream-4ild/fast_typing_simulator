from src.constants import CORRECT_COLOR, INCORRECT_COLOR, NEUTRAL_COLOR


class InterfaceString:
    def __init__(self, value: str):
        """
        :param value: string to be converted
        """
        self._string = value
        self._last_correct = -1
        self._first_neutral = 0

    def get_current_symbol_and_color(self) -> tuple[str, str]:
        """
        :return: current symbol and it's color
        """
        return self._string[self._last_correct + 1], (
            NEUTRAL_COLOR if self._last_correct == self._first_neutral - 1 else INCORRECT_COLOR)

    def get_string_with_color(self) -> list[(str, str)]:
        """
        Returns the string as blocks of colors
        """
        return [(self._string[:self._last_correct + 1], CORRECT_COLOR),
                (self._string[self._last_correct + 1:self._first_neutral], INCORRECT_COLOR),
                (self._string[self._first_neutral:], NEUTRAL_COLOR)]

    def enter_symbol(self, symbol: str) -> tuple[bool, bool]:
        """
        Checks if the symbol entered is correct.
        :param symbol: entered symbol
        :return: (True if the symbol entered correct && it was the last symbol in string, False otherwise;
                                                                        True if the symbol entered correct)
        """

        if symbol == self._string[self._last_correct + 1]:
            if self._first_neutral == self._last_correct + 1:
                self._first_neutral += 1

            self._last_correct += 1

            return self._first_neutral == len(self._string), True
        else:
            if self._first_neutral == self._last_correct + 1:
                self._first_neutral += 1
            return False, False
