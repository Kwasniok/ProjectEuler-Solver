#   coding=UTF_8
#
#   draw.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 24.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from console import Console

## @brief returns length of string without escaped characters
def visible_string_length(s):
    l = len(s)
    i = 0
    while i < len(s):
        if s[i] == "\033":
            # found escape controll character
            l -= 1
            i += 1
            # ecape sequence ends with letter from a-zA-Z
            while (ord(s[i]) < 65 or 90 < ord(s[i])) and (ord(s[i]) < 97 or 122 < ord(s[i])):
                # s[i] is not a letter (a-zA-Z)
                l -= 1
                i += 1
            l -= 1
            i += 1
        i += 1
    return l

## @brief class for handling draw calls.
# @note All methods do NOT flush!
class Draw():

    ## @brief draws a vertical line from given origin with given length.
    # @param line index of line of console where this line begins
    # @param col index of column of console where this line begins
    # @param length length of this line
    # @param stroke_heavy whether to draw line thick (default is False)
    # @see horizontal_line()
    @staticmethod
    def vertical_line(line, col, length, stroke_heavy=False):
        # line characters : ┃ │
        i = 0
        while i < length:
            Console.set_cursor(line + i, col)
            if stroke_heavy:
                Console.write(u"┃")
            else:
                Console.write(u"│")
            i += 1

    ## @brief draws a horizontal line from given origin with given length.
    # @param line index of line of console where this line begins
    # @param col index of column of console where this line begins
    # @param length length of this line
    # @param stroke_heavy whether to draw line thick (default is False)
    # @see vertical_line()
    @staticmethod
    def horizontal_line(line, col, length, stroke_heavy=False):
        # line characters : ━ ─
        i = 0
        while i < length:
            Console.set_cursor(line, col + i)
            if stroke_heavy:
                Console.write(u"━")
            else:
                Console.write(u"─")
            i += 1

    ## @brief draws a box.
    # example of usage:
    # @code
    # #draw a box from (1,1) to (5, 11)
    # Draw.box(1, 1, 4, 10, True)
    # @endcode
    # results in
    # @code
    # ┏━━━━━━━━┓
    # ┃        ┃
    # ┃        ┃
    # ┗━━━━━━━━┛
    # @endcode
    # @param line index of line of top left corner
    # @param col index of column of top left corner
    # @param height height of box (including bounderies)
    # @param width width of box (including bounderies)
    # @param stroke_heavy whether to draw line thick (default is False)
    # @see boxed_text()
    @staticmethod
    def box(line, col, height, width, stroke_heavy=False):
        if stroke_heavy:
            # all box characters: ┏━┓ ┃ ┗━┛ ┣ ┫ ┳ ┻ ╋
            Console.set_cursor(line, col)
            Console.write(u"┏" + u"━"*(width-2) + u"┓")
            i = 1
            while i < height - 1:
                Console.set_cursor(line+i, col)
                Console.write(u"┃")
                Console.set_cursor(line+i, col+width-1)
                Console.write(u"┃")
                i += 1
            Console.set_cursor(line+i, col)
            Console.write(u"┗" + u"━"*(width-2) + u"┛")
        else:
            # all box characters: ┌─┐ │ └─┘ ├ ┤ ┬ ┴ ┼
            Console.set_cursor(line, col)
            Console.write(u"┌" + u"─"*(width-2) + u"┐")
            i = 1
            while i < height - 1:
                Console.set_cursor(line+i, col)
                Console.write(u"│")
                Console.set_cursor(line+i, col+width-1)
                Console.write(u"│")
                i += 1
            Console.set_cursor(line+i, col)
            Console.write(u"└" + u"─"*(width-2) + u"┘")

    ## @brief writes text and draws a box around it.
    # example of usage:
    # @code
    # #write text and draw a box around it at (1,1)
    # Draw.box("hello!", 1, 1, True)
    # @endcode
    # results in
    # @code
    # ┏━━━━━━┓
    # ┃hello!┃
    # ┗━━━━━━┛
    # @endcode
    # @param line index of line of top left corner (of box)
    # @param col index of column of top left corner (of box)
    # @param stroke_heavy whether to draw line thick (default is False)
    # @see boxed_text()
    @staticmethod
    def boxed_text(s, line, col, stroke_heavy=False):
        len = visible_string_length(s)
        Draw.box(line, col, len + 2, 3, stroke_heavy)
        Console.write_to_pos(s, line+1, col+1)

## @brief class handling the Header.
# example of usage:
# @code
# set-up header
# Header.set_text_left("Hello!")
# Header.draw()
# # pause to read text
# time.sleep(2)
# # restore header and screen state
# Header.reset()
# Header.clear()
# @endcode
class Header():

    ## @brief text to be displayed in top left corner.
    # None means display no text
    text_left = None
    ## @brief text to be displayed in top right corner.
    # None means display no text
    text_right = None

    ## @brief draw complete Header in first line including separation line (one line below).
    # @see clear(), set_text_left(), set_text_right()
    @staticmethod
    def draw():
        Header.clear()
        if Header.text_left:
            Console.write_to_pos(Console.bold(Header.text_left), 1, 1)
        if Header.text_right:
            Console.write_to_pos(Console.bold(Header.text_right), 1, Console.screen_width - visible_string_length(Header.text_right) + 1)
        Draw.horizontal_line(2, 1, Console.screen_width, True)
        Console.flush()

    ## @brief clears section of Header on screen (i.e. top line and line below)
    @staticmethod
    def clear():
        Console.clear_lines(1, 2)

    ## @brief resores Header's default values
    @staticmethod
    def reset():
        Header.text_left = None
        Header.text_right = None

    ## @brief sets text to be displayed in top left corner.
    # @note Set to None if no text should be displayed.
    @staticmethod
    def set_text_left(text):
        Header.text_left = text

    ## @brief sets text to be displayed in top right corner.
    # @note Set to None if no text should be displayed.
    @staticmethod
    def set_text_right(text):
        Header.text_right = text

## @brief class handling the Footer.
# example of usage:
# @code
# import time
# set-up footer
# Footer.set_text_left("Hello!")
# Footer.draw()
# # pause to read text
# time.sleep(2)
# # restore footer and screen state
# Footer.reset()
# Footer.clear()
# @endcode
class Footer():

    ## @brief text to be displayed in bottom left corner.
    # None means display no text
    text_left = None
    ## @brief text to be displayed in bottom right corner.
    # None means display no text
    text_right = None

    ## @brief draw complete Footer in last line including seperation line (two lines above).
    # @see clear(), set_text_left(), set_text_right()
    @staticmethod
    def draw():
        Footer.clear()
        if Footer.text_left:
            Console.write_to_pos(Footer.text_left, Console.screen_height, 1)
        if Footer.text_right:
            Console.write_to_pos(Footer.text_right, Console.screen_height, Console.screen_width - visible_string_length(Footer.text_right) + 1)
        Draw.horizontal_line(Console.screen_height - 2, 1, Console.screen_width, True)
        Console.flush()

    ## @brief clears section of Footer on screen (i.e. last line and tow above below)
    # @note The line one above last line is NOT cleared!
    @staticmethod
    def clear():
        Console.clear_lines(Console.screen_height - 1, Console.screen_height - 1)
        Console.clear_lines(Console.screen_height, Console.screen_height)

    ## @brief resores Footer's default values
    @staticmethod
    def reset():
        Footer.text_left = None
        Footer.text_right = None

    ## @brief sets text to be displayed in bottom left corner.
    # @note Set to None if no text should be displayed.
    @staticmethod
    def set_text_left(text):
        Footer.text_left = text

    ## @brief sets text to be displayed in bottom right corner.
    # @note Set to None if no text should be displayed.
    @staticmethod
    def set_text_right(text):
        Footer.text_right = text

## @brief class handling the screen text between Header and Footer.
# example of usage:
# @code
# import time
# # set-up screen text
# Screen_Text.set("Line one")
# Screen_Text.append("\nLine two")
# Screen_Text.draw()
# # pause and read text
# time.sleep(2)
# # clean-up
# Screen_Text.reset()
# Screen_Text.draw()
# @endcode
class Screen_Text():

    first_possible_line = None
    last_possible_line = None
    ## @biref text to be displayed in section between Header and Footer.
    # @note When set to None no text will be displayed.
    text = None

    ## @brief draws screen text.
    # @note Call flushes output.
    @staticmethod
    def draw():
        Screen_Text.clear()
        if Screen_Text.text:
            Console.write_to_pos(Screen_Text.text, Screen_Text.first_possible_line, 1)
        Console.flush()

    ## @brief clears the area of screen text on screen
    # @note Does NOT flush output.
    @staticmethod
    def clear():
        Console.clear_lines(Screen_Text.first_possible_line, Screen_Text.last_possible_line)

    ## @brief resets Scree_Text to default values
    @staticmethod
    def reset():
        Screen_Text.text = None

    ## @brief sets screen text
    @staticmethod
    def set(text):
        Screen_Text.text = text

    ## @brief appends text to screen text
    @staticmethod
    def append(text):
        Screen_Text.text += text

## @brief class handling the progress bar.
# @code
# import time
# # set-up progress bar
# Progress_Bar.set_total(100)
# # simulate progress
# for i in ramge(101):
#     Progress_Bar.set_current(i)
#     Progress_Bar.draw()
#     time.sleep(0.05)
# # restore initial status
# Progress_Bar.reset()
# Progress_Bar.clear()
# @endcode
class Progress_Bar():
    current = 0
    total = 100
    sym_full = u'♦︎'
    sym_empty =u'♢'

    ## @brief draws progress bar if all values (position, width, current and total value) are set.
    # Otherwise draw() does nothing.
    @staticmethod
    def draw():
        if Progress_Bar.current != None and Progress_Bar.total:
            Progress_Bar.clear()

            width = Console.screen_width

            percentage = int(Progress_Bar.current * 100.0 / Progress_Bar.total)
            prefix = str(percentage) + "/100"
            bar_start = '['
            bar_end = ']'

            bar_size = width - len(prefix + bar_start + bar_end)
            amount = int(Progress_Bar.current / (Progress_Bar.total / float(bar_size)))
            remain = bar_size - amount

            bar = Progress_Bar.sym_full * amount + Progress_Bar.sym_empty * remain
            Console.write_to_pos(Console.bold(prefix) + bar_start + bar + bar_end, Console.screen_height - 1, 1)
            Console.flush()

    ## @brief clears line of progress bar.
    @staticmethod
    def clear():
        Console.clear_lines(Console.screen_height - 1, Console.screen_height - 1)

    ## @brief resets Progress_Bar to it's default values.
    # @note: The default values result in a state were no progress bar is displayed (as if it was hidden).
    @staticmethod
    def reset():
        Progress_Bar.current = None
        Progress_Bar.total = 100
        Progress_Bar.sym_full = u'♦︎'
        Progress_Bar.sym_empty = u'♢'

    ## @brief sets value for 100%
    @staticmethod
    def set_total(t):
        Progress_Bar.total = t

    ## @brief sets current value.
    # @note: Percentage is calculated as:
    # @code
    # percentage = current * 100.0 / total
    # @endcode
    @staticmethod
    def set_current(c):
        Progress_Bar.current = c
