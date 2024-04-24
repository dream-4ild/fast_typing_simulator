from time import sleep
from tkinter import TclError
from time import time

from src.window import window
from src.interface_string import interface_string
from src.text import text
from src.constants import STATS_PATH, SECONDS_PER_MINUTE


class game:
    def __init__(self, path="", language="russian"):
        """

        :param path: the path to your text file
        :param language:
        """

        self.text = text(path, language)

        self.window = window(self.start, self.stop, round(game.get_best_statistics(), 1))

        self.path = path
        self.language = language

        self.start_time = None
        self.stop_time = None

        self.window.start()

    def get_statistics(self) -> float:
        return SECONDS_PER_MINUTE * self.text.number_of_characters() / (self.stop_time - self.start_time)

    def stop(self, save_statistics=True, refresh_text=False):
        """
        Stops the game, saves the statistics and refresh text if you need.
        :param refresh_text:
        :param save_statistics:
        :return:
        """
        self.stop_time = time()
        if save_statistics:
            self.save_statistics()
        if refresh_text:
            self._refresh_text()

    def _refresh_text(self):
        self.text = text(self.path, self.language)

    @staticmethod
    def get_best_statistics() -> float:
        with open(STATS_PATH, 'r') as file:
            return float(file.read().replace('\n', ''))

    def save_statistics(self):
        prev_score = game.get_best_statistics()

        curr_score = self.get_statistics()

        if curr_score > prev_score:
            with open(STATS_PATH, 'w') as file:
                file.write(f"{curr_score}\n")

    def start(self):
        """
        Start the game
        :return:
        """
        self.window.remove_start_button()
        self.window.add_retry_button()

        self.start_time = time()

        main_string = interface_string(self.text.get_string())
        self.window.render_interface_string(main_string, 0)

        side_string = interface_string(self.text.get_string())
        self.window.render_interface_string(side_string, 1)

        try:
            need_next_line = False
            while True:
                elem = self.window.get_symbol()
                if elem is not None:
                    need_next_line = main_string.enter_symbol(elem)
                self.window.render_interface_string(main_string, 0)

                sleep(0.01)
                self.window.root.update()

                if need_next_line:
                    main_string = side_string
                    side_string = interface_string(self.text.get_string())
                    self.window.render_interface_string(main_string, 0)
                    self.window.render_interface_string(side_string, 1)

                    need_next_line = False
        except TclError:
            pass
        except IndexError:
            self.stop()
            self.window.render_statistics(f"You score is {round(self.get_statistics(), 1)} symbols per min")

            self.window.root.update()
        except Exception as e:
            print(e)

        self.window.start()
