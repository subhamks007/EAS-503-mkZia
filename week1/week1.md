# Week1

## Week 1 Topics
- Course Introduction
- Python Basics (Data types, mathematical operations, variables, strings, input, output), 
- Flow Control (Conditionals)
- NBGrader 

## Introduction
  - Take attendance
  - Go over syllabus
  - Survey class about programming experience and OS
  - Accessing Python
    - use `Ipython` from command-line
    - use `spyder` from Anaconda GUI
    - use `notebook` from Anaconda GUI
  - Sublime -- a good editor 
  - General Features of Python
    - Interpreted language
    - Forced indentation
    - Easy to use and learn syntax. Good first programming language
    - Very popular in data science field along with R

## Command Line Basics
  - organization: folders inside folders
  - absolute path vs relative path;
  - Using `~`
  - `pwd` -- Print name of current/Working Directory
  - `cd` -- Change Directory
  - `ls` -- list directory contents
  - `rm` -- remove directory entries; delete files and folders
  - `cp` -- copy files or folders
  - `mkdir` -- create new directory; `-p` option
  - `touch` -- change file access and modification times, but can     also be used to create a new file
  - `python test.py` -- running a program from command line
  - `python test.py > log.txt` -- saving output from program to command line



## General Overview
  - A modern computer can be defined as “a machine that stores and manipulates information under the control of a changeable program.”
    - Two key elements:
      1. Computers are devices for manipulating information.
      2. Computers operate under the control of a changeable program.
  - What is a computer program?
    - A detailed, step-by-step set of instructions telling a computer what to do.
    - If we change the program, the computer performs a different set of actions or a different task.
    - A program is just a sequence of instructions telling a computer what to do.
  - Natural language has ambiguity and imprecision problems when used to describe complex algorithms.
    - English example: "I saw a man on a hill with a telescope."
        - There’s a man on a hill, and I’m watching him with my telescope.
        - There’s a man on a hill, who I’m seeing, and he has a telescope.
        - There’s a man, and he’s on a hill that also has a telescope on it.
        - I’m on a hill, and I saw a man using a telescope.
        - There’s a man on a hill, and I’m sawing him with a telescope.
    - source: https://www.quora.com/What-are-some-examples-of-ambiguous-sentences
  - Programming Language
    - Programs are expressed in an unambiguous and precise way using programming languages. <strong>Bad code can be ambiguous due to human error. To the machine it is not ambiguous. Be very careful with conditionals.</strong>
    - Every structure in programming language has a precise form, called its <strong>syntax</strong>
  - What does a programming language do?
    - It takes a High-level human readable language expression such as `c = a + b` and translates to machine language that the computer can execute.
    - Compilers convert programs written in a high-level language into the machine language of some computer.
    - Interpreters simulate a computer that understands a high-level language.
    - The source program is not translated into machine language all at once.
    - An interpreter analyzes and executes the source code instruction by instruction (line-by-line).
  - Compiling vs. Interpreting
    - Once program is compiled, it can be executed over and over without the source code or compiler. If it is interpreted, the source code and interpreter are needed each time the program runs
    - Compiled programs generally run faster since the translation of the source code happens only once.
    - Interpreted languages are part of a more flexible programming environment since they can be developed and run interactively
    - Interpreted programs are more portable, meaning the executable code produced from a compiler for a Pentium won’t run on a Mac, without recompiling. If a suitable interpreter already exists, the interpreted code can be run with no modifications.

## Using Ipython
    - Use ipython to evaluate python expressions
    - 2 + 2 
        - 2 is a value
        - + is an operator
        - 2 is a value
        - 2 + 2 is called an expression
        - the value and the operator are combined or reduced to 4 -- i.e., the expression 2 + 2 is evaluted to 4
### Math Operators
#### Operators
  - `+` Addition -- `2+2=4`
  - `-` Subtraction -- `5-2=3`
  - `*` Multiplication -- `2*3=6`
  - `/` Division -- `12/6=2`
  - `**` Exponentiation - raise number to a given power; `2 ^ 3` or `2 * 2 * 2`
    - `64 ** 0.5` is allowed
  - `%` Modulo -- remainder operator. Good for figuring out if a number is even or odd
  - `//` integer division (i.e. quotient without remainder) `10//3 = 3`

#### Operator Notes
  - 3/4 is a float in Python! Other languages would cut off the decimal
  - By default division results in a float
  - PEMDAS - use parenthesis to manipulate the order in which things are calculated 
    - what is `8/2(2+2)`?

## Basic Data Types
  - You will mostly use these data types: `int`, `float`, `str`, `True/False`, and `None`

### Numbers
  - Python has the following number data types:
    - int - whole number, positive or negative, unlimited
    - float - number with decimals, positive or negative
    - complex - `7+3j`
  - Ints vs Floats
    - Stored differently
    - floats take more space than int
    - Ints and floats both can have positive and negative
    - type() -- used to figure out which type of data type it is
  - Why use ints? 
    - The underlying algorithms that perform computer arithmetic are simpler, and can therefore be faster, for ints than the more general algorithms required for float values. Maybe not the case anymore?
    - Float can only represent approximations  to real numbers
    - If you do not need fraction values, use int.

#### Identifiers or Naming Variables in Python
  - Variables give names to values (number, string, or boolean); Technically they are called identifiers. They are container of information that a computer program will manipulate using a sequence of instructions. 
  - Variables names MUST follow certain rules and it is BEST to follow Python guidelines for naming 
  - Restrictions for identifiers or naming things in Python
    1. Start with letter or underscore
    2. The rest can have letters, underscore, and numbers
    3. symbols cannot be used in name (@,+)
    4. Don't use Python keywords or reserved words such as `print`, `str`, `int`, `float`
      - `int = 3` do `del int` to restore python keyword
      - `print = 'Yah` do `del print` to restore Python keyword
  - Conventions for identifiers or naming things in Python
    1. use snake_case not camelCase
    2. variables should be lowercase
    3. upper case are used for constants PI = 3.14
    4. UpperCamelCase for classes
    5. `__private__`  double underscore is convention that means you are not supposed access this variable directly. They are by convention like private variables in other languages. 

#### Working with Variables
  - `x = 503`;  
  - `y = "EAS503"`
  - `print(x)`
  - `print(y)`
  - `y = 34` this is allowed because you can reassign value of a variable with the new value having a different data type in Python;
  This is called Dynamic typing;  C++ statically-typed -- cannot change the variable type. Define variable and variable definition will be enforced
  - `x = 3.9 * x * (1 - x)`
  - `x = 10`
  - `x = 11`
    - A variable in Python is like a sticky note on a value. When you change the variable, the sticky note changes to a different value. The variable simply switches to refer to the new value. The old value is not erased immediately. Python has automatic garbage collection.
  - `name = input("What is your name? ")` -- used to prompt user for input; the `name` variable will be a <strong>string!</strong>
    - avoid using `eval` for type casting, meaning changing type of variable from one type to another.
  - `sum, diff = x+y, x-y` -- simultaneous assignment 
    - useful when you want to swap values
      - So instead of doing this:

      ``` Python
        temp = x
        x = y
        y = temp
      ```
     -  do:
        - `x, y = y, x`
 

  - `+=` - `x += 3` is the same as `x = x + 3`
  - `-=` - `x -= 3` is the same as `x = x - 3`
  - `*=` - `x *= 3` is the same as `x = x * 3`
  - `/=` - `x /= 3` is the same as `x = x / 3`


### Casting -- Type Conversion, Rounding, Ceiling, and Flooring
  - Sometimes you have to convert one value from another
    - `age = input("What is your age? ")` - remember that input returns a string
    - ``` Python
      age = input("What is your age? ")
      type(age)
      age = int(age)
      type(age)
      age = int(input("What is your age? "))
      type(age)
      ```
    - int(), float()
  - `round()` will round a number; `round(pi, 3)
  - `math.ceil()` will round up
  - `math.floor()` round down


## Strings
  - A string in Python is a list of characters. A list stores a sequence of thing. In the case of a string, the list stores letters.
  - You can access individual characters with the the first character having index 0
  - You can declare strings using single or double quotes. 
    - Quotes inside other quotes:
      - "What's my name?"
  
  - `greet = 'Hello Bob'`
  - `greet[1]`
  - can do reverse indexing using negative numbers
    - `greet[-1]`
  - can slice strings; does not include the end position
    - `<string>[<start>:<end>:<skip>]` where start, end, and skip are ints
    - `greet[0:3]
    - `greet[:5]`
    - `greet[5:]`
    - `greet[:]`
    - `greet[::2]`
  - Concatenate Strings --
    - ```
      first_name = 'John'
      last_name = 'Doe'
      full_name = first_name + ' ' + 'Doe'
      print(full_name)
      ```
    - can multiply strings!
      - 
      ``` Python
      spam = 'spam'
      spam *= 3
      ```
  - ``` Python
    class_name = 'EAS503'
    print(class_name[3])
    for character in class_name:
      print(character)
    ```
  - Escape sequences or Escape characters
    - Use these to put in special characters
    - Most common ones
      - `'\\` -- how would you print `/\/\`
      - `'\n'`
      - `'\''`
      - `'\"'`
      - `'\t'` -- useful for parsing TSV files

  - Apache log example: https://www.keycdn.com/support/apache-access-log
  - Try to use packages already available online https://github.com/rory/apache-log-parser
  - String methods: https://www.w3schools.com/python/python_ref_string.asp
    - `capitalize() Converts the first character to upper case
    - `count()` Returns the number of times a specified value occurs in a string
    - `lower()` Converts a string into lower case
    - `split()` Splits the string at the specified separator, and returns a list
    - `title()` Converts the first character of each word to upper case
    - `upper()` Converts a string into upper case

### String Formatting
  - The fastest and latest way to do string formatting is using the F-strings (https://realpython.com/python-f-strings/)
  - ``` python
    PI = 3.14159265359 
    print(f'{PI:.2f}')
    ```
  - But you have to know the other ways so you can read older code or use these ways if you have to use an older version of Python
    - ``` python
      PI = 3.14159265359 
      name = 'PI'
      print('%s is %.2f' % (name, PI))  # oldest way format specifier is <width>.<precision><type>
      print(('{0} is {1:.2f}'.format('PI', PI)) ) # older way {<index>:<format-specifier>} where the format specifier is <width>.<precision><type>
      print(f'{name} is {PI:.2f}') # newest way
      ```


## Conditionals

  - So far we have only written small programs that are a sequence of instructions. Sometimes you have to alter the sequential flow of a program to suit the needs of a particular situation.
  - When strings are compared, they are compared lexicographic, meaning strings are put into alphabetical order and uppercase comes before lowercase.
  - The conditional operator converts the conditional into a boolean, which is a basic Python data type.

### Conditional Operators
  - `==` Equal to 
  - `!=` Not equal to
  - `<` Less than
  - `>` Greater than
  - `<=` Less than or equal to
  - `>=` Greater than or equal to

  - These operators evaluate to True or False depending on the values you give them.
  - Conditionals are used to instruct computer to make a decision. 
  ```Python
  if some condition is True:
    do something
  elif some other condition is True: # else if 
    do something
  elif some other condition is True: # else if 
    do something
  elif some other condition is True: # else if 
    do something
  else:
    do something 
  ```
  - colons are important and indentation matters
  - can have many elif tests
  - do not need else
  - conditions can be nested

### Truthiness and Falsiness 
  - Things that are false on their own
    - `None` (basic data type)
    - `False` (basic data type)
    - Any empty sequence: `''`, `[]`, `()`
    - Any zero value: 0, 0.0
    - Anything whose `len()` returns 0
    - Empty objects
    - Everything else is True 
  - Assume `a=1` and `b=1`

### Boolean Operators
  | Boolean Operators | What it does?                                | Example       |
|----|---------------------------------------------|---------------|
| == | True if a has the same value as b           | a == b #True  |
| != | True if a does not have the same value as b | a != b #False |
| >  | True if a is greater than b                 | a > b # False |
| <  | True if a is less than b                    | a < b # False |
| >= | True if a is greater than or equal to b     | a >= b # True |
| <= | True if a is less than or equal to b        | a <= b # True |

### Logical Operators

| Operator | What it does?                                        | Example                                                                   |
|----------|------------------------------------------------------|---------------------------------------------------------------------------|
| `and`    | True if both a AND b are true (logical conjunction)  | if is_teacher and is_active:   print('You can access')                    |
| `or`     | True if either a OR b are true (logical disjunction) | if is_superuser or (is_teacher and is active):    print('You can access') |
| `not`    | True if the opposite of a is true (logical negation) | if not is_superuser:   print('You cannot access')    

### is vs ==
- in Python `==` and `is` are very similar comparators, but they are not the same!
```
a = 1
a == 1 # True
a is 1 # True
```
- The `==` operator compares if the values are the same or not. The `is` operator checks whether both the values refer to the same object or not.