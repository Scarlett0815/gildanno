#!/bin/python3

import sys
import argparse

# Global variables
gLanguage = None
gInputFileName = None
gOutputFileName = None
gSymmetry = None
gSign = None
gWidth = None
gText = None


def IsInteger(number):
    try:
        float(number)
    except ValueError:
        return False
    else:
        return float(number).is_integer()


def ReadFile(filename):
    input_file = open(filename, "r")
    line_number = 0  # the line number
    done = False
    while not done:
        result.append(input_file.readline())
        line_number = line_number + 1
        if result[line_number - 1] == "":  # the last line is empty
            done = True  # cease to go on
            line_number = line_number - 1  # delete the empty line
    line_index = 0
    for line_index in range(line_number):
        result[line_index] = result[line_index][:-1]  # delete the '\n' of every line
    input_file.close()
    return result


def ReadCLI():
    result = []
    while True:
        line = input()
        if line:
            # add the new line into the 'result' list
            result.append(line)
        else:
            break
    return result


def PrintFile(filename, result):
    output_file = open(filename, "w")
    for k in len(result):
        # print the finished strings in order
        output_file.write(result[k])
    output_file.close()


def LeftComment():
    result = []
    for p in range(len(gText) + 2):
        result.append(list(gSign * gWidth))
        # create the result and fill the whole list with the certain sign
    head_index = 0
    tail_index = gWidth - 1
    if gLanguage == "fortran":
        for io in range(len(gText) + 2):
            result[io][0] = "!"
            result[io][1] = " "
            head_index = 2
        if gSymmetry:
            for io in range(len(gText) + 2):
                result[io][gWidth - 1] = "!"
                result[io][gWidth - 2] = " "
                tail_index = gWidth - 3
    if gLanguage == "c":
        if not gMode:
            for io in range(len(gText) + 2):
                result[io][0] = "/"
                result[io][1] = "/"
                result[io][2] = " "
                head_index = 3
            if gSymmetry:
                for io in range(len(gText) + 2):
                    result[io][gWidth - 1] = "/"
                    result[io][gWidth - 2] = "/"
                    result[io][gWidth - 3] = " "
                    tail_index = gWidth - 4
        else:
            for io in range(len(gText) + 2):
                result[io][0] = "/"
                result[io][1] = "*"
                result[io][2] = " "
                head_index = 3
            if gSymmetry:
                for io in range(len(gText) + 2):
                    result[io][gWidth - 1] = "/"
                    result[io][gWidth - 2] = "*"
                    result[io][gWidth - 3] = " "
                    tail_index = gWidth - 4

    if gLanguage == "python":
        for io in range(len(gText) + 2):
            result[io][0] = "#"
            result[io][1] = " "
            head_index = 2
        if gSymmetry:
            for io in range(len(gText) + 2):
                result[io][gWidth - 1] = "#"
                result[io][gWidth - 2] = " "
                tail_index = gWidth - 3

    # To make the text more readable
    for o in range(len(gText)):
        gText[o] = " " + gText[o] + " "

    for o in range(len(gText)):
        for id in range(len(gText[o])):
            result[o + 1][head_index + id] = gText[o][id]
    for io in range(len(gText) + 2):
        result[io] = "".join(result[io])
    # turn back into strings
    return result


def RightComment():
    result = []
    for p in range(len(gText) + 2):
        result.append(list(gSign * gWidth))
        # create the result and fill the whole list with the certain sign
    head_index = 0
    tail_index = gWidth - 1
    if gLanguage == "fortran":
        for io in range(len(gText) + 2):
            result[io][0] = "!"
            result[io][1] = " "
            head_index = 2
        if gSymmetry:
            for io in range(len(gText) + 2):
                result[io][gWidth - 1] = "!"
                result[io][gWidth - 2] = " "
                tail_index = gWidth - 3
    if gLanguage == "c":
        if not gMode:
            for io in range(len(gText) + 2):
                result[io][0] = "/"
                result[io][1] = "/"
                result[io][2] = " "
                head_index = 3
            if gSymmetry:
                for io in range(len(gText) + 2):
                    result[io][gWidth - 1] = "/"
                    result[io][gWidth - 2] = "/"
                    result[io][gWidth - 3] = " "
                    tail_index = gWidth - 4
        else:
            for io in range(len(gText) + 2):
                result[io][0] = "/"
                result[io][1] = "*"
                result[io][2] = " "
                head_index = 3
            if gSymmetry:
                for io in range(len(gText) + 2):
                    result[io][gWidth - 1] = "/"
                    result[io][gWidth - 2] = "*"
                    result[io][gWidth - 3] = " "
                    tail_index = gWidth - 4

    if gLanguage == "python":
        for io in range(len(gText) + 2):
            result[io][0] = "#"
            result[io][1] = " "
            head_index = 2
        if gSymmetry:
            for io in range(len(gText) + 2):
                result[io][gWidth - 1] = "#"
                result[io][gWidth - 2] = " "
                tail_index = gWidth - 3

    # To make the text more readable
    for o in range(len(gText)):
        gText[o] = " " + gText[o] + " "

    for o in range(len(gText)):
        for id in range(len(gText[o])):
            result[o + 1][tail_index - id] = gText[o][id]
    for io in range(len(gText) + 2):
        result[io] = "".join(result[io])
    # turn back into strings
    return result


def CenterComment():
    # TODO:
    # More mode need to be provided
    global gText
    global gLanguage
    global gSign
    global gWidth
    global gSymmetry
    global gMode
    result = []
    for p in range(len(gText) + 2):
        result.append(list(gSign * gWidth))
        # create the result and fill the whole list with the certain sign
    head_index = 0
    tail_index = gWidth - 1
    if gLanguage == "fortran":
        for io in range(len(gText) + 2):
            result[io][0] = "!"
            result[io][1] = " "
            head_index = 2
        if gSymmetry:
            for io in range(len(gText) + 2):
                result[io][gWidth - 1] = "!"
                result[io][gWidth - 2] = " "
                tail_index = gWidth - 3
    if gLanguage == "c":
        if not gMode:
            for io in range(len(gText) + 2):
                result[io][0] = "/"
                result[io][1] = "/"
                result[io][2] = " "
                head_index = 3
            if gSymmetry:
                for io in range(len(gText) + 2):
                    result[io][gWidth - 1] = "/"
                    result[io][gWidth - 2] = "/"
                    result[io][gWidth - 3] = " "
                    tail_index = gWidth - 4
        else:
            for io in range(len(gText) + 2):
                result[io][0] = "/"
                result[io][1] = "*"
                result[io][2] = " "
                head_index = 3
            if gSymmetry:
                for io in range(len(gText) + 2):
                    result[io][gWidth - 1] = "/"
                    result[io][gWidth - 2] = "*"
                    result[io][gWidth - 3] = " "
                    tail_index = gWidth - 4

    if gLanguage == "python":
        for io in range(len(gText) + 2):
            result[io][0] = "#"
            result[io][1] = " "
            head_index = 2
        if gSymmetry:
            for io in range(len(gText) + 2):
                result[io][gWidth - 1] = "#"
                result[io][gWidth - 2] = " "
                tail_index = gWidth - 3

    # To make the text more readable
    for o in range(len(gText)):
        gText[o] = " " + gText[o] + " "

    # Find the start position of the text
    start_point = []
    for io in range(len(gText)):
        start_point.append(
            ((tail_index - head_index + 1) - len(gText[io])) // 2 + head_index
        )
    for o in range(len(gText)):
        for id in range(len(gText[o])):
            result[o + 1][start_point[o] + id] = gText[o][id]
    for io in range(len(gText) + 2):
        result[io] = "".join(result[io])
    # turn back into strings
    return result


# Main
if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Gildanno is a comment generator.")

    # Add arguments
    parser.add_argument("-l", "--language", help="Generate language type.")
    parser.add_argument("-i", "--input", help="Input file path.")
    parser.add_argument("-o", "--output", help="Output file path.")
    parser.add_argument("-w", "--width", help="Input the whole length.")
    parser.add_argument("-s", "--sign", help="Input the adding sign.")
    parser.add_argument("-f", "--symmetry", help="Input the symmetry flag.")
    parser.add_argument(
        "-m",
        "--mode",
        help="When you choose c/c++ ,you need to select between //(0) and /*(1).",
    )
    parser.add_argument(
        "-e",
        "--selection",
        help="Select centrecomment(c) leftcomment(l) or rightcomment(r).",
    )
    # Parse arguments
    args = parser.parse_args()

    if args.language:
        # Current version:
        # Only 'C', 'Python', 'Fortran' is available
        gLanguage = args.language.lower()
    else:
        # Default language
        gLanguage = "fortran"

    if args.input:
        gInputFileName = args.input
    else:
        gInputFileName = None

    if args.output:
        gOutputFileName = args.output
    else:
        gOutputFileName = None

    if args.width:

        gWidth = int(args.width)
    else:
        # Default width
        gWidth = 80

    if args.sign:
        if IsInteger(args.sign):
            # Allow use ascii code as input
            gSign = chr(int(args.sign))
        else:
            gSign = args.sign[0]
    else:
        # Default sign
        gSign = " "

    if args.symmetry:
        gSymmetry = args.symmetry
    else:
        gSymmetry = False
    if args.mode:
        gMode = args.mode
    else:
        gMode = False

    # Read Text
    if gInputFileName is not None:
        gText = ReadFile(gInputFileName)
    else:
        gText = ReadCLI()
    if args.selection:
        if args.selection == "c":
            result = CenterComment()
        if args.selection == "l":
            result = LeftComment()
        if args.selection == "r":
            result = RightComment()
    else:
        result = CenterComment()
    if gOutputFileName is not None:
        PrintFile(gOutputFileName, result)
    else:
        for line_number1 in range(len(result)):
            print(result[line_number1])
