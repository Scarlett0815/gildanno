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
    result = input_file.readline()
    input_file.close()
    return result


# mode:
# 0 - single line mode
# 1 - multiline mode
def ReadCLI(mode):
    result = ""
    if mode == 0:
        # Single line mode
        result = input()
    else:
        while True:
            line = input()
            if line:
                result += line + "\n"
            else:
                break
        # Remove the last new line
        result = result[:-1]
    return result


def PrintFile(filename, result):
    output_file = open(filename, "w")
    output_file.write(result)
    output_file.close()

def PrintCLI(result):
    print(result)


def CenterComment():
    # TODO:
    # More mode need to be provided
    global gText
    global gLanguage
    global gSign
    global gWidth
    global gSymmetry

    # Convert into list
    result = list(gSign * gWidth)

    head_index = 0
    tail_index = gWidth - 1

    if gLanguage == "fortran":
        result[head_index] = '!'
        result[head_index + 1] = ' '
        head_index = head_index + 2
        if gSymmetry:
            result[tail_index] = '!'
            result[tail_index - 1] = ' '
            tail_index = tail_index - 2

    # TODO: exception if gText is too long

    # To make the text more readable
    gText = ' ' + gText + ' '
    
    # Find the start position of the text
    start_point = ((tail_index - head_index + 1) - len(gText)) // 2 + head_index
    for id in range(len(gText)):
        result[start_point + id] = gText[id]
    # Turn back into string
    result = ''.join(result)
    return result


# Main
if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description='Gildanno is a comment generator.'
    )

    # Add arguments
    parser.add_argument('-l', '--language',
        help='Generate language type.')
    parser.add_argument('-i', '--input',
        help='Input file path.')
    parser.add_argument('-o', '--output',
        help='Output file path.')
    parser.add_argument('-w','--width',
        help='Input the whole length.')
    parser.add_argument('-s','--sign',
        help='Input the adding sign.')
    parser.add_argument('-f', '--symmetry',
        help='Input the symmetry flag.')

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
        gSign = ' '

    if args.symmetry:
        gSymmetry = True
    else:
        gSymmetry = False

    # Read Text
    if gInputFileName is not None:
        gText = ReadFile(gInputFileName)
    else:
        gText = ReadCLI(0)

    # Test input
    print(list(gText))

    result = CenterComment()

    if gOutputFileName is not None:
        PrintFile(gOutputFileName, result)
    else:
        print(result)

