#   coding=UTF_8
#
#   main.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from console import Console
from draw import Draw, Header, Footer, Screen_Text, Progress_Bar
from colours import *
from problems_all import *

#########
#General#
#########

# Version
version_major = 0
version_minor = 2

## returns program version as string
def get_version():
    return str(version_major) + '.' + str(version_minor)

###############
#I/O Functions#
###############

def start_up():
    Console.start_up()
    reset_all()

def finalize():
    Console.set_cursor(Console.screen_height, 1)
    Console.write("\n", True)

def get_line():
    Console.clear_lines(Console.screen_height - 1, Console.screen_height - 1)
    Console.write_to_pos(">>>", Console.screen_height - 1, 1)
    return Console.get_line()

def reset_screen():
    Console.measure_screen()
    Screen_Text.first_possible_line = 3
    Screen_Text.last_possible_line = Console.screen_height - 3

def reset_all():
    Console.reset()
    reset_screen()
    Header.reset()
    Screen_Text.reset()
    Footer.reset()
    Progress_Bar.reset()
    Header.set_text_left("ProjectEuler-Solver v." + get_version())
    Footer.set_text_right("type " + dye_input_var("help") + " for help")
    draw_screen()

######################
#Write/Draw Functions#
######################

def clear_all():
    Console.clear()

def draw_screen():
    reset_screen()
    Header.draw()
    Screen_Text.draw()
    Footer.draw()
    Progress_Bar.draw()

## @code
# for i in range(101):
#     set_progress(i)
#     draw_screen()
#     sleep(0.5)
# Progress_Bar.reset()
# @endcode
def set_progress(percentage):
    Progress_Bar.set_current(percentage)

def reset_progress():
    Progress_Bar.set_current(None)

#########
#Actions#
#########

def on_reset():
    reset_all()

def on_start():
    Header.set_text_right("Start")
    Screen_Text.set("Welcome to PorblemSolver v." + get_version() + " built for ProjectEuler problems.\nAll Problems are taken from the ProjectEuler web page (http://projecteuler.net).\nFor more information about a problem see: http://projecteuler.net/problem=[your problem number here!]\n")
    Screen_Text.append("\n\ntype " + dye_input_var("help") + " for help\n")
    Footer.set_text_left("press " + dye_input_var("any key") + " to start")
    draw_screen()
    Console.get_char()
    Footer.set_text_left(None)
    draw_screen()

def on_help():
    Header.set_text_right("Main Menue Help")
    Screen_Text.set("type in the " + dye_input_var("number of a problem") + " for calculations"
          "\n         " + dye_warning("or ") + dye_input_var("help") + " for this page"
          "\n         " + dye_warning("or ") + dye_input_var("info") + " for more information about this programm"
          "\n         " + dye_warning("or ") + dye_input_var("problems") + " for a list of all problems currently available"
          "\n         " + dye_warning("or ") + dye_input_var("quit") + " to quit this program")
    Footer.set_text_left("press " + dye_input_var("any key") + " continue")
    draw_screen()
    Console.get_char()
    Footer.set_text_left(None)
    draw_screen()

def on_info():
    Header.set_text_right("Main Menue Info")
    Screen_Text.set("\nPorblem Solver v." + get_version() + " created by Jens Kwasniok Jul 2012\n\nAll problems were taken from projecteuler.net.\nThe wording of a problems description might differ due to incompatibilities in text representation in this program, changes of the problem page on projecteuler.net or other reasons.\n\nThe intension of this program is neither to spoil anyone nor to encourage anybody to cheat. Its just there to challenge my self and extend the experience of some problems by providing extra information to a solution and/or input variables to explore a problem further.\n\n")
    Footer.set_text_left("press " + dye_input_var("any key") + " continue")
    draw_screen()
    Console.get_char()
    Footer.set_text_left(None)
    draw_screen()

def on_quit():
    Header.set_text_right("Main Menue Quit")
    Screen_Text.set("see you ...")
    draw_screen()

def on_list_all_problems():
    ps = []
    for p in glob_problems.keys():
        ps.append(p)

    Header.set_text_right("List of All Problems")
    Screen_Text.set("List of available problems:")
    Screen_Text.append("\n\n" + list_to_fancy_str(ps, ", "))
    Footer.set_text_left("press " + dye_input_var("any key") + " continue")
    draw_screen()
    Console.get_char()
    Footer.set_text_left(None)
    draw_screen()

###################################
#Request Input for Problem Routine#
###################################

def get_long_execution_time_waring():
    return "The " + dye_warning("algorithm") + " solving this problem is " + dye_warning("not efficient") + ". Some input might cause a(n extreme) " + dye_warning("long execution time") + " (> 1min.). Even the default one!"

def request_input_for_problem(number):

    # handles the input of a specific problem including its request

    show_sub_menue = True
    has_calculated_problem = False

    if number in glob_problems:

        Header.set_text_right("Problem " + str(number))

        p  = glob_problems[number]

        Screen_Text.set(p.description())
        if p.should_warn_long_execution_time():
            Screen_Text.append("\n\n" + get_long_execution_time_waring() + "\n")
        draw_screen()

        while show_sub_menue:

            Screen_Text.set(p.description())
            if p.should_warn_long_execution_time():
                Screen_Text.append("\n\n" + get_long_execution_time_waring() + "\n")

            if has_calculated_problem:
                    Screen_Text.append("\n\nlast result for " + p.get_last_input_as_string() + " was " + p.get_last_result_as_string())

            input = get_line()

            executeProblem = False
            problemInput = None

            if input == "help":
                Screen_Text.append("\n\nhelp:\ntype in the " + dye_input_var("input") + " for this problem"
                       "\n         " + dye_warning("or ") + dye_input_var("help") + " for this page"
                       "\n         " + dye_warning("or ") + dye_input_var("default") + " for a calculation with the default value"
                       "\n         " + dye_warning("or ") + dye_input_var("usage") + " for more info about the input format"
                       "\n         " + dye_warning("or ") + dye_input_var("url") + " to display the problem URL (projecteuler.net)"
                       "\n         " + dye_warning("or ") + dye_input_var("more") + " for more info about the calculation"
                       "\n         " + dye_warning("or ") + dye_input_var("back") + " to go back to main menu")
                draw_screen()

            elif input == "more":
                if has_calculated_problem:
                    Screen_Text.append("\n\ndetails:\n" + p.details())
                    draw_screen()
                else:
                    Screen_Text.append("\n\nYou have to " + dye_warning("make a calculation first") + "!")
                    draw_screen()

            elif input == "usage":
                Screen_Text.append("\n\nusage:\n" + p.usage())
                draw_screen()
            elif input == "url":
                Screen_Text.append("\n\nurl:\n" + p.url())
                draw_screen()

            elif input == "back":
                show_sub_menue = False

            elif input == "default":
                executeProblem = True
                if p.supports_input():
                    problemInput = p.default_input

            else: # try to interpret as problem input

                if p.supports_input():
                    # choose input type
                    vfs = valueFromString(p.input_format, input)

                    if vfs[0]:
                        problemInput = vfs[1]
                        executeProblem = True
                    else:
                        Screen_Text.append("\n\n" + vfs[1] + "\n")
                        draw_screen()
                else:
                    Screen_Text.append("\n\n" + dye_warning("no input allowed")  + " only " + dye_input_var("default") + " is supported")
                    draw_screen()

            if executeProblem == True:
                Footer.set_text_left("calculating")
                draw_screen()
                p.execute(problemInput)
                Footer.set_text_left(None)
                Screen_Text.append("\n\nresult for " + p.get_last_input_as_string() + " is " + p.get_last_result_as_string())
                draw_screen()
                has_calculated_problem = True

    else:
        Footer.set_text_left(dye_warning("no problem") +  " with this number (yet)")
        draw_screen()

##############
#Main Routine#
##############

def parse_main_loop_input(input):

    # check for keywords or try to interpret as valid problem number otherwise
    if input == "reset":
        on_reset()
    elif input == "help":
        on_help()
    elif input == "info":
        on_info()
    elif input == "problems":
        on_list_all_problems()
    elif input == "quit":
        on_quit()
        return False
    elif input == "test progress bar":
        for i in range(101):
            set_progress(i)
            draw_screen()
            sleep(0.05)
        reset_progress()
    else: # not a keyword, check if its a valid problem number
        cont = False
        try:
            number = int(input)
            cont = True
        except ValueError:
            Footer.set_text_left(dye_warning("input not supported"))
            draw_screen()
        if cont:
            request_input_for_problem(number)
    return True

#############
#Entry Point#
#############

# entry point
if __name__ == '__main__':
    # start-up routines
    start_up()
    on_start()
    # main loop
    run = True
    while run:
        Header.set_text_right(Console.bold("Main Menue"))
        Screen_Text.set("choose a problem\n")
        draw_screen()
        Footer.set_text_left(None)
        run = parse_main_loop_input(get_line())

    finalize()
