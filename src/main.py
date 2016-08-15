#   coding=UTF_8
#
#   main.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from time import sleep
from version_independent_input import get_line
from colours import *
from problems_all import *

#########
#General#
#########

# Version
version_major = 0
version_minor = 0

## returns program version as string
def get_version():
    return str(version_major) + '.' + str(version_minor)

################
#Error Messages#
################

def print_error_no_valid_input(input):
    print(dye_warning("Sorry, " + input + " isn't a valid input."))

###############
#Dynamic Print#
###############

## tests dynamic printing
def dynamic_print_joke():
    sleep(1)
    string = " ... ... ... DYNAMIC PRINT!"
    for i in range(len(string)):
        string2 = ""
        for j in range(i+1):
            string2 += string[j]
            stdout.write("\r" +string2)
            stdout.flush()

        sleep(.1)
    sleep(.66)
    for i in range(3):
        stdout.write("\r"+ " "*len(string) +"\r")
        stdout.flush()
        sleep(.2)
        stdout.write("\r" +string)
        stdout.flush()
        sleep(.2)
    stdout.write("\r"+ " "*len(string) +"\r")
    sleep(.33)
    stdout.flush()

#########
#Actions#
#########

def on_start():
    print("\nWelcome to PorblemSolver v." + get_version() + " built for ProjectEuler problems\nAll Problems are taken from the ProjectEuler web page (http://projecteuler.net). For more information about a problem see: http://projecteuler.net/problem=[your problem number here!]\n")
    print("type " + dye_input_var("help") + " for help\n")

def on_help():
    print("type in the " + dye_input_var("number of a problem") + " for calculations"
          "\n" + dye_warning("or ") + dye_input_var("help") + " for this page"
          "\n" + dye_warning("or ") + dye_input_var("info") + " for more info"
          "\n" + dye_warning("or ") + dye_input_var("problems") + " for a list of all problems currently available"
          "\n" + dye_warning("or ") + dye_input_var("quit") + " to quit this program")

def on_info():
    print("\nPorblem Solver v." + get_version() + " created by Jens Kwasniok Jul 2012\n\nAll problems were taken from projecteuler.net.\nThe wording of a problems description might differ due to incompatibilities in text representation in this program, changes of the problem page on projecteuler.net or other reasons.\n\nThe intension of this program is neither to spoil anyone nor to encourage anybody to cheat. Its just there to challenge my self and extend the experience of some problems by providing extra information to a solution and/or input variables to explore a problem further.\n\n")

def on_quit():
    print("see you ..")

###################################
#Request Input for Problem Routine#
###################################

def request_input_for_problem(number):

    # handles the input of a specific problem including its request

    show_sub_menue = True
    has_calculated_problem = False

    if number in glob_problems:

        p  = glob_problems[number]
        print(p.description())

        if p.should_warn_long_execution_time():
            print("\nThe " + dye_warning("algorithm") + " solving this problem is " + dye_warning("not efficient") + ". Some input might cause a(n extreme) " + dye_warning("long execution time") + " (> 1min.). Even the default one!\n")

        while show_sub_menue:
            input = get_line(">>> ")

            executeProblem = False
            problemInput = None

            if input == "help":
                 print("type in the " + dye_input_var("input") + " for this problem"
                       "\n" + dye_warning("or ") + dye_input_var("help") + " for this page"
                       "\n" + dye_warning("or ") + dye_input_var("default") + " for a calculation with the default value"
                       "\n" + dye_warning("or ") + dye_input_var("usage") + " for more info about the input format"
                       "\n" + dye_warning("or ") + dye_input_var("url") + " to display the problem URL (projecteuler.net)"
                       "\n" + dye_warning("or ") + dye_input_var("more") + " for more info about the calculation (This option is only supported if reasonable.)"
                       "\n" + dye_warning("or ") + dye_input_var("back") + " to go back to main menu")

            elif input == "more":
                if has_calculated_problem:
                    print(p.details())
                else:
                    print("You have to make a " + dye_warning("calculation first") + "!")

            elif input == "usage":
                print(p.usage())

            elif input == "url":
                print(p.url())

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
                        print(vfs[1])
                else:
                    print(dye_warning("no input allowed")  + " only " + dye_input_var("default") + " is supported")


            if executeProblem == True:
                p.execute(problemInput)
                has_calculated_problem = True


    else:
        print(dye_warning("no problem") +  " with this number (yet)")

##############
#Main Routine#
##############

def parse_main_loop_input(input):

    # check for keywords or try to interpret as valid problem number otherwise
    if input == "help":
        on_help()

    elif input == "info":
        on_info()

    elif input == "problems":
        print("list of all problems available:")
        ps = []
        for p in glob_problems.keys():
            ps.append(p)
        print(listToFancyStr(ps, ", "))

    elif input == "quit":
        on_quit()
        return False

    elif input == "dynamic print":
        dynamic_print_joke()

    else: # not a keyword, check if its a valid problem number
        cont = False
        try:
            number = int(input)
            cont = True
        except ValueError:
            print_error_no_valid_input(input)
        if cont:
            request_input_for_problem(number)
    return True

#############
#Entry Point#
#############

# entry point
if __name__ == '__main__':

    run = True
    on_start()

    # main loop
    while run:
        print ("choose a problem ... ")
        run = parse_main_loop_input(get_line(">>> "))
