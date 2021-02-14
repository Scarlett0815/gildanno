# Gildanno

An annotation gilder for programmers.

Gildanno is a comment generator. If you need make your comments centered, fill the blank with `*` or other punctuations or any other typesetting needs on comments. Gildanno can help you.

## Table Of Contents

* [Quick start options](#quick-start-options)
* [Why Gildanno](#why-gildanno)
* [Short User Manual](#short-user-manual)
* [Examples](#examples)

## Quick Start Options

### Clone the repository

```bash
git clone https://github.com/Scarlett0815/gildanno
```

### Use Gildanno to generate comments

```bash
python gildanno.py
```

## Why Gildanno?

Many programmers have their preferred flavor on comment style. Some may very brief, to conclude idea in the fewest words.

But some programs, especially those which are used in some scientific research, need a lot of words to explain their idea and the scientific principle. So, when the comments come longer, they need to be formatted or typesetting.

Unfortunately, most code format tool does not provide such a function to make up comments.

## Short User Manual

You can get a brief introduction of how to use Gildanno with `-h` option.

```bash
usage: gildanno.py [-h] [-l LANGUAGE] [-i INPUT] [-o OUTPUT] [-w WIDTH] [-s SIGN] [-f SYMMETRY] [-m MODE]

Gildanno is a comment generator.

optional arguments:
  -h, --help            show this help message and exit
  -l LANGUAGE, --language LANGUAGE
                        Generate language type.
  -i INPUT, --input INPUT
                        Input file path.
  -o OUTPUT, --output OUTPUT
                        Output file path.
  -w WIDTH, --width WIDTH
                        Input the whole length.
  -s SIGN, --sign SIGN  Input the adding sign.
  -f SYMMETRY, --symmetry SYMMETRY
                        Input the symmetry flag.
  -m MODE, --mode MODE  
                        When you choose c/c++ ,you need to select between//(0)and /*(1).
  -e SELECTION, --selection SELECTION
                        Select centrecomment(c) leftcomment(l) or rightcomment(r).
```

### Language

-l **LANGUAGE** or --language **LANGUAGE**

Specify the language. Current version, we only support `C`, `Python` and `Fortran`. The default language is `Fortran`.

### Input

-i **INPUT** or --input **INPUT**

Specify the path of the input file. You can ignore this option if you want to give your input in CLI.

### Output

-o **OUTPUT** or --output **OUTPUT**

Specify the path of the output file. You can ignore this option if you want to get your output in CLI.

### Width

-w **WIDTH** or --width **WIDTH**

Specify the width of the comment, default width is 80.

### Sign

-s **SIGN** or --sign **SIGN**

Specify the sign which is used to filling the blank space. The default sign is ' '.
You can use a character or an ascii code here.

### Symmetry

-f **SYMMETRY** or --symmetry **SYMMETRY**

Specify if you want to create a symmetry style. A symmetry mode is add the comment mark in the end each line of comment.

### MODE

-m **MODE** or --mode **MODE**

Specify if you choose the language c/c++.You are supposed to select between the mode like '//'

(0)and the mode like '/*'(1). And if you don't input '-m', the mode is set to an extension of '//'.

### SELECTION

-e **SELECTION** or -- selection **SELECTION**

Specify if you want to choose the adjustment of the location of the text. SELECTION = 'c' represents the center adjustment, SELECTION ='l' represents the left adjustment, and SELECTION ='r' represents the right adjustment.



## Examples

### 1. C comment

#### Example 1 input

```bash
> python gildanno.py -l c -w 30 -s + -f 1 -m 1 -e l
hello
world
```

#### Example 1 output

```c
/* ++++++++++++++++++++++++ */
/*  hello +++++++++++++++++ */
/*  world +++++++++++++++++ */
/* ++++++++++++++++++++++++ */
```


### 2. C comment

#### Example 2 input

```bash
> python gildanno.py -l c -w 30 -s + -f 1 -m 0 -e c
hello
world
```

#### Example 2 output

```c
// ++++++++++++++++++++++++ //
// ++++++++ hello +++++++++ //
// ++++++++ world +++++++++ //
// ++++++++++++++++++++++++ //
```