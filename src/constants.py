from screeninfo import get_monitors

WIDTH = None
HEIGHT = None
MAX_SYMBOLS_IN_LINE = None
ADD_CHOOSE_FRAME_PADX = None
MAIN_WORD_PADY = None
MAIN_WORD_FONT_SIZE = None
INDENT = 10


def set_size():
    global WIDTH, HEIGHT, MAX_SYMBOLS_IN_LINE, ADD_CHOOSE_FRAME_PADX, MAIN_WORD_PADY, MAIN_WORD_FONT_SIZE
    monitor = get_monitors()[0]

    WIDTH = int(monitor.width * 0.625)
    HEIGHT = int(monitor.height * 0.625)

    MAX_SYMBOLS_IN_LINE = (WIDTH - 2 * INDENT) // MAIN_FONT_SIZE
    print(MAX_SYMBOLS_IN_LINE)
    ADD_CHOOSE_FRAME_PADX = HEIGHT // 8
    MAIN_WORD_PADY = HEIGHT // 7

    MAIN_WORD_FONT_SIZE = HEIGHT // 7


BACKGROUND_COLOR = "#FFFFFF"
CORRECT_COLOR = "#32CD32"
INCORRECT_COLOR = "#FF0000"
NEUTRAL_COLOR = "#696969"

FONT_NAME = "Consolas"
SIDE_FONT_SIZE = 20
MAIN_FONT_SIZE = 35
LINES_PADY = 30

DEFAULT_PATH = "./texts/"

START_BUTTON_BACKGROUND_COLOR = "#32CD32"
START_BUTTON_FONT_SIZE = 30

RETRY_BUTTON_BACKGROUND_COLOR = "#F08080"
RETRY_BUTTON_FONT_SIZE = 15
RETRY_PAD = 20

LOAD_FILE_BUTTON_BACKGROUND_COLOR = "#FFEBCD"
LOAD_FILE_FONT_SIZE = 14

SECONDS_PER_MINUTE = 60
STATS_PATH = "./bin/statistics.txt"
STATS_COLOR = "#228B22"
STATS_UPDATE_FREQUENCY = 50  # every ?? ticks
STATS_FONT_SIZE = 30


ADD_CHOOSE_FONT_SIZE = 16

DEFAULT_PADX = 5

AVAILABLE_LANGUAGES = ["russian", "english"]
DEFAULT_LANGUAGE = "russian"
