from time import sleep
from tkinter import TclError
from time import time

from src.window import window
from src.interface_string import interface_string
from src.text import text
from src.constants import STATS_PATH, SECONDS_PER_MINUTE, STATS_UPDATE_FREQUENCY


class game:
    def __init__(self):
        self.window = window(self.start, self._stop, round(game._get_best_statistics(), 1))
        self.text = None

        self.start_time = None
        self.stop_time = None
        self._count_of_current_chars = 0

        self.window.start()

    def _get_statistics(self, is_game_stopped=True) -> float:
        """
        Returns game statistics
        :param is_game_stopped:
        :return: statistic
        """
        return (SECONDS_PER_MINUTE * self._count_of_current_chars /
                ((self.stop_time if is_game_stopped else time()) - self.start_time))

    def _stop(self, save_statistics=True, refresh_text=False):
        """
        Stops the game, saves the statistics and refresh text if you need.
        :param refresh_text:
        :param save_statistics:
        :return:
        """
        self.stop_time = time()
        if save_statistics:
            self._save_statistics()
        if refresh_text:
            self._refresh_text()

        self.window.remove_stat_field()
        self.window.remove_main_word_field()

    def _refresh_text(self):
        """
        Refreshes the text field
        :return: 
        """
        self.text = text(self.window.path, self.window.language)

    @staticmethod
    def _get_best_statistics() -> float:
        """
        Returns game statistics
        :return: 
        """
        with open(STATS_PATH, 'r') as file:
            return float(file.read().replace('\n', ''))

    def _save_statistics(self):
        prev_score = game._get_best_statistics()

        curr_score = self._get_statistics()

        if curr_score > prev_score:
            with open(STATS_PATH, 'w') as file:
                file.write(f"{curr_score}\n")

    def start(self):
        """
        Start the game
        :return:
        """
        self._refresh_text()
        self.window.remove_start_button()
        self.window.remove_choose()
        self.window.add_retry_button()
        self.window.add_stat_field()
        self.window.add_main_word_field()

        self._count_of_current_chars = 0

        self.start_time = time()

        main_string = interface_string(self.text.get_string())
        self.window.render_interface_string(main_string, 0)

        side_string = interface_string(self.text.get_string())
        self.window.render_interface_string(side_string, 1)

        counter_for_render_current_statistics = 0

        try:
            need_next_line = False
            while True:
                elem = self.window.get_symbol()
                if elem is not None:
                    need_next_line, correct = main_string.enter_symbol(elem)
                    self._count_of_current_chars += correct

                self.window.render_interface_string(main_string, 0)

                sleep(0.01)
                counter_for_render_current_statistics += 1
                self.window.root.update()

                if counter_for_render_current_statistics % STATS_UPDATE_FREQUENCY == 0:
                    self.window.render_current_statistics(round(self._get_statistics(False), 1))

                if need_next_line:
                    main_string = side_string
                    side_string = interface_string(self.text.get_string())
                    self.window.render_interface_string(main_string, 0)
                    self.window.render_interface_string(side_string, 1)

                    need_next_line = False
                self.window.render_main_word(*main_string.get_current_symbol_and_color())
        except TclError:
            pass
        except IndexError:
            self._stop()
            self.window.render_statistics(f"Your score {round(self._get_statistics(), 1)} symbols per min")

            self.window.root.update()
        except Exception as e:
            print(e)

        self.window.start()
