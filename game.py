from time import sleep
from tkinter import TclError

from window import window
from interface_string import interface_string
from text import text


class game:
    def __init__(self, path="", language="russian"):
        """

        :param path: the path to your text file
        :param language:
        """
        self.window = window(self.start, self.stop)

        self.text = text(path, language)

        self.path = path
        self.language = language

        self.window.start()

    def stop(self):
        self.text = text(self.path, self.language)

    def start(self):
        """
        Start the game
        :return:
        """
        self.window.remove_start_button()
        self.window.add_retry_button()

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
            pass
            # TODO render statistics and quit
        except Exception as e:
            print(e)

        self.window.start()
