#!/bin/python3

import sys
import argparse

# Global variables
gLanguage = None
gInputFileName = None
gOutputFileName = None


def ReadFile(filename):
    print(filename)


def ReadCLI():
    pass


def PrintFile(filename):
    print(filename)


def PrintCLI():
    pass


# Main
if __name__ == "__main__":
    # Create a argument parser
    parser = argparse.ArgumentParser(
        description='Gildanno is a comment generator.'
    )

    # Add arguments
    parser.add_argument('-l', '--language', help='Generate language type.')
    parser.add_argument('-i', '--input', help='Input file path.')
    parser.add_argument('-o', '--output', help='Output file path.')
    
    # Parse arguments
    args = parser.parse_args()

    if args.language:
        print(args.language)

    if args.input:
        print(args.input)

    if args.output:
        print(args.output)

