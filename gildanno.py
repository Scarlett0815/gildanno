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

def Centre(filename,width,sign):
    fo1=open(filename,"r")
    i=0
    n=[]
    length=[]
    line=[]
    done=0
    while not done:
        line.append(fo1.readline())
        length.append(len(line[i]))
        n.append（(width-length[i])//2）
        if(line[i]==""):
            done=1
        i=i+1
    fo2=open(filename,'w')
    m=0
    while m<i-1:
        for j in range(n[m]):
            v=fo2.write(sign)
        for p in range(length[m]-1)
        v=fo2.write(line[m][p])
        for k in range(width-length[m]-n[m]):
            v=fo2.write(sign)
        v=fo2.write("\n")
        m=m+1
    fo1.close()
    fo2.close()
             

# Main
if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description='Gildanno is a comment generator.'
    )

    # Add arguments
    parser.add_argument('-l', '--language', help='Generate language type.')
    parser.add_argument('-i', '--input', help='Input file path.')
    parser.add_argument('-o', '--output', help='Output file path.')
    parser.add_argument('-w','--width',help='Input the whole length.')
    parser.add_argument('-s','--sign',help='Input the adding sign.')
   
    # Parse arguments
    args = parser.parse_args()

    if args.language:
        print(args.language)

    if args.input:
        print(args.input)

    if args.output:
        print(args.output)
   
    if args.width:
        print(args.width)

    if args.sign:
        print(args.sign)


