#   coding=UTF_8
#
#   console.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 23.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

# credits to: http://www.darkcoding.net/software/pretty-command-line-console-output-on-unix-in-python-and-go-lang/
#             http://stackoverflow.com/questions/11918999/key-listeners-in-python#11919074

import sys
import fcntl
import termios
import struct
import time

## @brief class for handling input and output
# @note Call start_up() first before using other methods. Other behaviour will most likely result in error messages.
# example of usage:
# @code
# # exapmle for use of Console
# Console.start_up()
# Console.write_to_pos(Console.bold("Hello!"), Console.screen_height/2, Console.screen_width/2)
# Console.flush()
# # other steps here ...
# # clear screen
# Console.clear()
# Console.flush()
# @endcode
# @see start_up()
class Console():

    assert sys.stdout.encoding == "UTF-8", "Console encoding not set to UTF-8"

    ## @brief console output stream
    OUT = sys.stdout
    ## @brief console input stream
    IN = sys.stdin
    ## @brief copy of default attributes of sys.stdout.
    # MUST be restored (via finally block) when attributes from sys.stdin were altered!
    # e.g. when program is quitted
    IN_attributes_default = termios.tcgetattr(sys.stdin.fileno())[:]
    # input modes
    ## @brief default input mode
    # same as input mode before staring the programm
    # @see set_input_mode()
    IM_DEFAULT = 0
    ## @brief special input mode which disables input echoing and input delimiter
    # @see set_input_mode()
    IM_RAW = 1

    ## @brief message to be promted on start-up.
    # when set to None no message will be displayed
    start_up_message = None
    ## @brief promt indicator
    promt_str = ">>>"
    ## @brief stores screen height (lines).
    # to be handled asread-only, use Console.start_up() or Console.reset() to update this value
    # @see start_up(), reset()
    screen_height = None
    ## @brief stores screen width (columns).
    # to be handled asread-only, use Console.start_up() or Console.reset() to update this value
    # @see start_up(), reset()
    screen_width = None

    ## @brief switches between different input modes.
    # @see IM_DEFAUL, IM_RAW
    @staticmethod
    def set_input_mode(IM):
        if IM == Console.IM_RAW:
            # copy default attributes
            attrs = Console.IN_attributes_default[:]
            # disable input echoing and canonical mode (icludes line by line input etc.)
            attrs[3] = attrs[3] & ~(termios.ECHO | termios.ICANON)
            termios.tcsetattr(Console.IN.fileno(), termios.TCSADRAIN, attrs)
        if IM == Console.IM_DEFAULT:
            # restore default
            termios.tcsetattr(Console.IN.fileno(), termios.TCSADRAIN, Console.IN_attributes_default)

    ## @brief used in input mode IM_DEFAUlT to get next input until new line delimiter.
    # @note Characters will be printed in IM_DEFAULT.
    @staticmethod
    def get_line():
        if sys.version_info > (3, 0):
            return input()
        if sys.version_info > (2, 0):
            return raw_input()

    ## @brief switches input mode to IM_RAW and returns next character wich is in input stream.
    # @note Characters will NOT be printed!
    @staticmethod
    def get_char():
            try:
                Console.set_input_mode(Console.IM_RAW)
                return Console.IN.read(1)
            except (EOFError):
                pass
            finally:
                Console.set_input_mode(Console.IM_DEFAULT)

    ## @brief called once for start-up.
    # prints Console.start_up_message when set
    # @see start_up_message, set_start_up_message
    @staticmethod
    def start_up():
        Console.reset()
        if Console.start_up_message:
            msg = Console.start_up_message
            Console.write_to_pos(msg, Console.screen_height / 2, (Console.screen_width - len(msg)) / 2, True)
            time.sleep(2.0)
            Console.reset()

    ## @brief resets complete status of IO including clearing the screen.
    @staticmethod
    def reset():
        Console.set_input_mode(Console.IM_DEFAULT)
        Console.measure_screen()
        Console.clear()
        Console.set_cursor(0, 0)
        Console.OUT.flush()

    ## @brief sets start-up message
    # @param s when set s must be a string, when unset start-up message is reset to None
    # @see start_up, set_start_up_message
    @staticmethod
    def set_start_up_message(s=None):
        Console.start_up_message = s

    ## @brief updates scree_height and schreen_width to current values of the console window.
    @staticmethod
    def measure_screen():
        lines, cols = struct.unpack('hh',  fcntl.ioctl(sys.stdout, termios.TIOCGWINSZ, "1234"))
        Console.screen_width = cols
        Console.screen_height = lines

    ## @brief clears the complete screen of output inside screen_width and screen_height.
    # @note Call measure_screen first to be sure the whole screen is cleared. Does NOT flush!
    # @see measure_screen(), flush()
    @staticmethod
    def clear():
        sys.stdout.write("\033[2J")

    ## @brief clears complete lines with index start trough end of output.
    @staticmethod
    def clear_lines(start, end):
        if end >= start:
            for line in range(start, end + 1):
                Console.write_to_pos("\033[2K", line, 1)

    ## @brief sets the cursor to given position.
    # @note Indices start with 1 - where (1,1) is the top left corner - and will be clipped to current screen size.
    # @note Call measure_screen() when unsure if screen size is not up to date.
    # @see measure_screen(), move_cursor()
    @staticmethod
    def set_cursor(line, col):
        # clamp position
        if col < 1:
            col = 1
        if line < 1:
            line = 1
        if col > Console.screen_width:
            col = Console.screen_width
        if line > Console.screen_height:
            line = Console.screen_height
        sys.stdout.write("\033[" + str(line) + ";" + str(col) + "H")

    ## @brief moves the cursor by given amount.
    # @note Indices start with 1 - where (1,1) is the top left corner - and will be clipped to current screen size.
    # @note Call measure_screen() when unsure if screen size is up to date.
    # @see measure_screen(), set_cursor()
    @staticmethod
    def move_cursor(line, x):
        if line > 0:
            sys.stdout.write("\033[" + str(line) + "A")
        if line < 0:
            sys.stdout.write("\033[" + str(line) + "B")
        if col > 0:
            sys.stdout.write("\033[" + str(col) + "C")
        if col < 0:
            sys.stdout.write("\033[" + str(col) + "D")

    ## @brief writes string to current location of the cursor.
    # @note When printed text exceeds line width, the behaviour might depend on console and IO mode.
    # @ see write_to_pos(), flush()
    @staticmethod
    def write(s, flush=False):
        Console.OUT.write(s)
        if flush:
            Console.OUT.flush()

    ## @brief flushes output.
    # @ see write(), write_to_pos()
    @staticmethod
    def flush():
        Console.OUT.flush()

    ## @brief sets cursor to given location and writes string.
    # @note When printed text exceeds line width, the behaviour might depend on console and IO mode.
    # @ see write_to_pos(), flush()
    @staticmethod
    def write_to_pos(s, line, col, flush=False):
        Console.set_cursor(line, col)
        Console.OUT.write(s)
        if flush:
            Console.OUT.flush()

    ## @brief returns string with surrounding 'bold' tags
    @staticmethod
    def bold(s):
        return u'\033[1m' + s + '\033[0m'

    ## @brief returns string with surrounding 'grayed out' tags
    @staticmethod
    def grayed(s):
        return u'\033[2m' + s + '\033[0m'

    ## @brief returns string with surrounding 'underlined' tags
    @staticmethod
    def underlined(s):
        return u'\033[4m' + s + '\033[0m'

    ## @brief returns string with surrounding 'blinking' tags
    @staticmethod
    def blinking(s):
        return u'\033[5m' + s + '\033[0m'

    ## @brief returns string with surrounding 'inverted colors' tags
    @staticmethod
    def inverted(s):
        return u'\033[7m' + s + '\033[0m'

    COLOUR_RESET = 0
    COLOUR_FRONT_BLACK = 30
    COLOUR_FRONT_RED = 31
    COLOUR_FRONT_GREEN = 32
    COLOUR_FRONT_YELLOW = 33
    COLOUR_FRONT_PURPLE = 34
    COLOUR_FRONT_MAGENTA = 35
    COLOUR_FRONT_CYAN = 36
    COLOUR_FRONT_GRAY = 37
    COLOUR_BACK_BLACK = 40
    COLOUR_BACK_RED = 41
    COLOUR_BACK_GREEN = 42
    COLOUR_BACK_YELLOW = 43
    COLOUR_BACK_PURPLE = 44
    COLOUR_BACK_MAGENTA = 45
    COLOUR_BACK_CYAN = 46
    COLOUR_BACK_GRAY = 47
    COLOUR_FRONT_LIGHT_BLACK = 90
    COLOUR_FRONT_LIGHT_RED = 91
    COLOUR_FRONT_LIGHT_GREEN = 92
    COLOUR_FRONT_LIGHT_YELLOW = 93
    COLOUR_FRONT_LIGHT_PURPLE = 94
    COLOUR_FRONT_LIGHT_MAGENTA = 95
    COLOUR_FRONT_LIGHT_CYAN = 96
    COLOUR_FRONT_LIGHT_GRAY = 97
    COLOUR_BACK_LIGHT_BLACK = 100
    COLOUR_BACK_LIGHT_RED = 101
    COLOUR_BACK_LIGHT_GREEN = 102
    COLOUR_BACK_LIGHT_YELLOW = 103
    COLOUR_BACK_LIGHT_PURPLE = 104
    COLOUR_BACK_LIGHT_MAGENTA = 105
    COLOUR_BACK_LIGHT_CYAN = 106
    COLOUR_BACK_LIGHT_GRAY = 107

    ## @brief returns string with surrounding 'color' tags
    # @param s a string
    # @param colour constant representing a colour
    @staticmethod
    def coloured(s, colour):
        return u'\033[' + str(colour) + 'm' + s + '\033[0m'
