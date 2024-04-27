from tkinter import Tk, Text, Button, Frame, Label, StringVar
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from queue import Queue

from src.constants import *
from src.interface_string import interface_string


class window:
    def __init__(self, starter, stopper, best_score: float):
        """
        :param starter: method to start the game
        :param stopper: method to stop the game
        :param best_score: best score of game
        """
        self.root = Tk()
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.title("fast typing")
        self.root.configure(background=BACKGROUND_COLOR)

        self.text_widget_0 = None
        self.text_widget_1 = None
        self._add_text_fields()

        self.render_statistics(f"Your best now is {best_score}")

        self.language = ""
        self.path = ""
        self.stat_field = None

        self._add_choose()

        self._add_start_button(starter)

        self._add_retry_button(stopper, starter)

        self._add_stat_field()

        self.root.bind("<Key>", self._key_pressed)

        self.input_que = Queue()

    def remove_stat_field(self):
        self.stat_field.pack_forget()

    def _add_stat_field(self):
        self.stat_field = Text(
            self.root,
            width=10,
            height=1,
            borderwidth=0,
            highlightthickness=0,
            bg=BACKGROUND_COLOR,
            font=(FONT_NAME, STATS_FONT_SIZE)
        )

    def add_stat_field(self):
        self.stat_field.pack(side='bottom', anchor='w')

    def _add_text_fields(self):
        self.text_widget_0 = Text(
            self.root,
            width=MAX_SYMBOLS_IN_LINE,
            height=1,
            borderwidth=0,
            highlightthickness=0,
            bg=BACKGROUND_COLOR,
            font=(FONT_NAME, SIDE_FONT_SIZE)
        )
        self.text_widget_1 = Text(
            self.root,
            width=MAX_SYMBOLS_IN_LINE,
            height=1,
            borderwidth=0,
            highlightthickness=0,
            bg=BACKGROUND_COLOR,
            font=(FONT_NAME, MAIN_FONT_SIZE)
        )

        self.text_widget_0.tag_configure("center", justify='center')
        self.text_widget_1.tag_configure("center", justify='center')

        self.text_widget_0.pack(pady=LINES_PADY)
        self.text_widget_1.pack()

    def remove_choose(self):
        self.frame_for_choosing.pack_forget()

    def _add_choose(self):
        self.frame_for_choosing = Frame(
            self.root,
            bg=BACKGROUND_COLOR
        )
        self.frame_for_choosing.pack(pady=ADD_CHOOSE_FRAME_PADX)

        label_0 = Label(
            self.frame_for_choosing,
            text="Choose language:",
            font=(FONT_NAME, ADD_CHOOSE_FONT_SIZE),
            bg=BACKGROUND_COLOR
        )
        label_0.pack(side="left", padx=DEFAULT_PADX)

        self.selected_language = StringVar()
        self.selected_language.set(DEFAULT_LANGUAGE)
        self.combo_lang = Combobox(
            self.frame_for_choosing,
            values=AVAILABLE_LANGUAGES,
            textvariable=self.selected_language,
            state="readonly",
        )
        self.combo_lang.set(DEFAULT_LANGUAGE)

        self.combo_lang.pack(
            side='left',
            padx=DEFAULT_PADX
        )

        label_1 = Label(
            self.frame_for_choosing,
            text="or",
            font=(FONT_NAME, ADD_CHOOSE_FONT_SIZE),
            bg=BACKGROUND_COLOR
        )
        label_1.pack(side="left", padx=5)

        self.load_file_btn = Button(
            self.frame_for_choosing,
            text="Load File",
            command=self._chose_file,
            font=(FONT_NAME, LOAD_FILE_FONT_SIZE),
            bg=LOAD_FILE_BUTTON_BACKGROUND_COLOR
        )
        self.load_file_btn.pack(
            side='left',
            padx=DEFAULT_PADX
        )

    def _lang_selected(self):
        self.language = self.selected_language.get()

    def _chose_file(self):
        filetypes = [("Text files", "*.txt")]
        filename = askopenfilename(
            title="Choose a file with your own text",
            initialdir="/",
            filetypes=filetypes
        )

        self.path = filename

    def _add_retry_button(self, stopper, starter):
        """
        Adds a retry button to the main window.
        :param stopper: method to stop previous game
        :param starter: method to start the new game
        :return:
        """
        frame = Frame(self.root, bg=BACKGROUND_COLOR)
        frame.pack(side='bottom', anchor='e')

        self.retry_button = Button(
            frame,
            text="Retry",
            command=lambda: (stopper(False, True), starter()),
            bg=RETRY_BUTTON_BACKGROUND_COLOR,
            font=(FONT_NAME, RETRY_BUTTON_FONT_SIZE)
        )

    def _add_start_button(self, starter):
        """
        Adds a start button to the main window.
        :param starter: method to start the new game
        :return:
        """
        frame = Frame(self.root, bg=BACKGROUND_COLOR)
        frame.place(relx=0.5, rely=0.6, anchor='center')

        self.start_button = Button(
            frame,
            text="Start",
            bg=START_BUTTON_BACKGROUND_COLOR,
            command=lambda: (self._lang_selected(), starter()),
            font=(FONT_NAME, START_BUTTON_FONT_SIZE),
            width=20,
            height=2
        )

        self.start_button.pack()

    def remove_start_button(self):
        """
        Removes the start button from the main window.
        :return:
        """
        self.start_button.pack_forget()

    def remove_load_file_button(self):
        self.load_file_btn.pack_forget()

    def add_retry_button(self):
        """
        Adds a retry button to the main window.
        :return:
        """
        self.retry_button.pack(side='right', pady=RETRY_PAD, padx=RETRY_PAD)

    def _key_pressed(self, event):
        """
        Handles keypress events
        :param event:
        :return:
        """
        self.input_que.put(event.char)

    def get_symbol(self):
        """
        get_entered_symbol
        :return: None if no symbol was entered or it was 'Shift', otherwise the entered symbol
        """
        if self.input_que.empty():
            return None

        elem = self.input_que.get()
        return elem if elem != '' else None

    def start(self):
        """
        Start the main window.
        :return:
        """
        self.root.mainloop()

    def render_interface_string(self, string: interface_string, number: int):
        """
        :param string: string to render
        :param number: which one is on top
        :return: None
        """

        list_string = string.get_string_with_color()

        attr_name = f"text_widget_{1 - number}"
        copy_attr = getattr(self, attr_name)

        copy_attr.configure(state='normal')

        copy_attr.delete('1.0', 'end')

        for elem in list_string:
            tag_name = f"tag_{elem[1]}"
            copy_attr.tag_configure(tag_name, foreground=elem[1], justify='center')

            copy_attr.insert("end", elem[0], ("center", tag_name))

        copy_attr.configure(state='disabled')

    def render_statistics(self, message: str):

        self.text_widget_1.configure(state='normal')

        self.text_widget_1.delete('1.0', 'end')

        self.text_widget_1.tag_configure("curr_tag", foreground=STATS_COLOR, justify='center')

        self.text_widget_1.insert("end", message, ("center", "curr_tag"))

        self.text_widget_1.configure(state='disabled')

    def render_current_statistics(self, stat: float):
        self.stat_field.configure(state='normal')
        tag_name = "some_tag"
        self.stat_field.tag_configure(tag_name, foreground=STATS_COLOR, justify='center')

        self.stat_field.delete('1.0', 'end')

        self.stat_field.insert("end", str(stat), ("center", tag_name))

        self.stat_field.configure(state='disabled')
