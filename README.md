# Launch
```bash
git clone https://github.com/dream-4ild/fast_typing_simulator.git &&
cd fast_typing_simulator &&
git checkout development &&
pip install -r requirements.txt &&
python3 start.py
```

# `window` Class Documentation

## Overview

The `window` class provides the main interface for the fast typing game application. It handles the creation of the GUI, manages the game's state, and processes user input.

## Constructor

### `__init__(self, starter, stopper, best_score: float)`

Initializes a new instance of the `window` class.

#### Parameters:

- `starter`: A method to start the game.
- `stopper`: A method to stop the game.
- `best_score`: The best score achieved in the game, as a float.

Creates the main window, configures its properties, and sets up the game interface.

## Methods

### `_add_text_fields(self)`

Creates and configures the text fields used for displaying game information.

### `render_interface_string(self, string: interface_string, number: int)`

Renders a given string in the interface.

#### Parameters:

- `string`: An instance of `interface_string` containing the text and associated colors.
- `number`: Determines the position of the string; `0` for the upper position, `1` for the lower position.

### `_chose_file(self)`

Opens a file dialog to allow the user to choose a text file for the game.

### `_add_choose(self)`

Creates and adds elements to the interface for choosing the language or loading a file.

### `remove_choose(self)`

Removes the language choice and file loading interface from the main window.

### `_add_start_button(self, starter)`

Adds a start button to the main window and binds it to the `starter` method.

### `_lang_selected(self)`

Updates the currently selected language based on user input.

### `remove_start_button(self)`

Removes the start button from the main window.

### `_add_retry_button(self, stopper, starter)`

Adds a retry button to the main window and binds it to the `stopper` and `starter` methods.

### `add_retry_button(self)`

Makes the retry button visible on the main window.

### `_add_stat_field(self)`

Creates a field for displaying statistics.

### `add_stat_field(self)`

Adds the statistics field to the main window.

### `render_current_statistics(self, stat: float)`

Updates the statistics field with the current stats.

### `remove_stat_field(self)`

Removes the statistics field from the main window.

### `_add_main_word_field(self)`

Creates a field for displaying the main word to type.

### `add_main_word_field(self)`

Adds the main word field to the main window.

### `render_main_word(self, word: str, color: str)`

Displays the current word with the specified color in the main word field.

### `remove_main_word_field(self)`

Removes the main word field from the main window.

### `_key_pressed(self, event)`

Callback function that handles key press events.

### `render_statistics(self, message: str)`

Displays a message in the secondary text field, usually used for statistics or information.

### `get_symbol(self)`

Returns the most recent symbol entered by the user or `None` if no input is available.

### `start(self)`

Begins the Tkinter main loop to start the application.



# `game` Class Documentation

## Overview

The `game` class is responsible for managing the game state, including timing, user input processing, and the game's main loop. It works closely with the `window` class to provide an interactive typing game experience.

## Constructor

### `__init__(self)`

Initializes a new instance of the `game` class. It sets up the game window and starts the game loop.

- Sets up the `window` with callbacks for starting and stopping the game.
- Initializes the text for the game based on user selections or a default.
- Begins the game loop to process user input and update the game state.

## Methods

### `_get_statistics(self, is_game_stopped=True) -> float`

Calculates the game statistics based on typed characters and time elapsed.

#### Parameters:
- `is_game_stopped`: Boolean flag to indicate if the game is currently stopped.

#### Returns:
- The current typing speed in characters per minute.

### `_stop(self, save_statistics=True, refresh_text=False)`

Stops the game, optionally saves statistics, and optionally refreshes the text for a new game round.

#### Parameters:
- `save_statistics`: Flag to save current game statistics.
- `refresh_text`: Flag to refresh the text for a new game round.

### `_refresh_text(self)`

Refreshes the game text based on the current path or language selected by the user in the `window` interface.

### `_get_best_statistics() -> float`

Static method to retrieve the best statistics from the statistics file.

#### Returns:
- The best score from the game's history.

### `_save_statistics(self)`

Compares the current game statistics to the best score and updates the statistics file if the current score is better.

### `start(self)`

Sets up the game environment and starts the main game loop. It configures the `window` to display the game interface and handles the rendering of strings and statistics.

- Prepares the interface for a new game.
- Resets counters and timestamps.
- Enters the game loop for input processing and display updates.

## Game Loop

The game loop handles the following:

- Retrieves the next symbol from the user input.
- Updates the statistics and interface at a defined frequency.
- Switches to the next line of text when needed.
- Handles exit conditions and exceptions.

## Exception Handling

The game loop is designed to handle various exceptions, including `TclError` for window closure, `IndexError` for end of text, and other exceptions for unexpected errors.




# `interface_string` Class Documentation

## Overview

The `interface_string` class is designed to represent the text that users will interact with during the typing game. It tracks the correctness of user input and associates parts of the string with different colors based on user performance.

## Constructor

### `__init__(self, value: str)`

Initializes a new instance of the `interface_string` class.

#### Parameters:

- `value`: The string to be used in the game interface.

This method sets up the initial state of the string, marking all characters as neutral to start.

## Methods

### `get_current_symbol_and_color(self) -> tuple[str, str]`

Retrieves the current symbol that the user should type and its associated color.

#### Returns:

- A tuple containing the next symbol to type and its color (`NEUTRAL_COLOR` or `INCORRECT_COLOR`).

### `get_string_with_color(self) -> list[(str, str)]`

Processes the string and separates it into colored segments based on user input accuracy.

#### Returns:

- A list of tuples, each containing a substring of the original string and its associated color (`CORRECT_COLOR`, `INCORRECT_COLOR`, or `NEUTRAL_COLOR`).

### `enter_symbol(self, symbol: str) -> tuple[bool, bool]`

Accepts a symbol entered by the user and updates the state of the string accordingly.

#### Parameters:

- `symbol`: The character entered by the user.

#### Returns:

- A tuple where the first element is `True` if the symbol entered is correct and it was the last symbol in the string (indicating the end of the string has been reached), and `False` otherwise. The second element is `True` if the symbol entered is correct.

This method checks whether the entered symbol matches the expected next character in the string, updates tracking indices for correct and neutral positions, and determines the colors for the rendered string.



# `text` Class Documentation

## Overview

The `text` class is responsible for handling and processing text for the typing game. It loads text from a file or a specified directory, processes it into manageable lines, and tracks the current position within the text.

## Constructor

### `__init__(self, path: str, language: str)`

Initializes a new instance of the `text` class.

#### Parameters:

- `path`: The file path to the specific text file or an empty string to use default text.
- `language`: The language folder to look in for default texts.

If no specific path is provided, the constructor selects a random text file from the default directory of the given language. The text is then processed into lines suitable for the game.

## Static Methods

### `_process_text(raw_text: str) -> list[str]`

Processes the raw text from a file and organizes it into a list of strings, each with a maximum length defined by `MAX_SYMBOLS_IN_LINE`.

#### Parameters:

- `raw_text`: A string containing the unprocessed content of a text file.

#### Returns:

- A list of strings, each representing a line of text no longer than `MAX_SYMBOLS_IN_LINE`.

This method cleans the text by replacing carriage returns, tabs, and certain characters with standardized ones and then splits the text into lines.

## Public Methods

### `get_string(self) -> str`

Retrieves the current line of text for the game to display.

#### Returns:

- The current line as a string.

#### Exceptions:

- `IndexError`: If there are no more lines left to return (the end of the text has been reached).

This method advances the line tracker and returns the next line of processed text for the game.

---

Note that this class should be used with caution as it directly manipulates the line position within the text and expects callers to handle the end-of-text situation appropriately.


# Configuration Constants

This module defines a set of global constants used throughout the typing game application for maintaining a consistent style and behavior.

## Display Settings

`WIDTH` and `HEIGHT` define the dimensions of the main application window. They are dynamically set based on the user's monitor size by the `set_size` function.

`INDENT` represents the indentation space used within text elements in pixels.

`BACKGROUND_COLOR` sets the background color of the application window.

## Text Settings

`CORRECT_COLOR`, `INCORRECT_COLOR`, and `NEUTRAL_COLOR` specify the colors used to indicate the correctness of the user's input.

`FONT_NAME` designates the font family for the text displayed in the application.

`SIDE_FONT_SIZE` and `MAIN_FONT_SIZE` determine the font sizes for secondary and primary text elements, respectively.

`LINES_PADY` specifies the vertical padding around text lines.

## File Paths

`DEFAULT_PATH` specifies the default directory for text files used in the game.

`STATS_PATH` defines the path to the file where game statistics are saved.

## UI Element Styles

Colors and font sizes for various UI elements like the start button, retry button, and file loading button are specified with a corresponding suffix in their names.

## Timing and Statistics

`SECONDS_PER_MINUTE` is a constant used in calculating typing speed.

`STATS_UPDATE_FREQUENCY` defines how often the game updates the statistics displayed to the user.

`STATS_FONT_SIZE` sets the font size for the statistics display.

`AVAILABLE_LANGUAGES` lists the languages supported by the application.

`DEFAULT_LANGUAGE` indicates the default language selected when the application starts.

## `set_size` Function

The `set_size` function is called to dynamically calculate and set the size-related constants based on the user's monitor resolution. It uses the `screeninfo` library to fetch monitor dimensions and calculates appropriate values for `WIDTH`, `HEIGHT`, `MAX_SYMBOLS_IN_LINE`, `ADD_CHOOSE_FRAME_PADX`, `MAIN_WORD_PADY`, and `MAIN_WORD_FONT_SIZE`.

This ensures that the application is displayed correctly on different screen sizes and resolutions.

---

Each constant and function is an integral part of the application's configuration and should be modified with care to maintain the intended look and feel of the game.
