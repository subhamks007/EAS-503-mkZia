# Week 2


## Chapter 5 -- Lists

### General Information About Lists
  - Strings are a sequence of values. These values can be indexed
  - Lists are also a sequence of values but are more general than strings because they can contain a sequence 
  of different types of variables
  - Lists have many methods
    - `append()` - Used for appending and adding elements to List.It is used to add elements to the last position of List
    - `insert()` - Inserts an elements at specified position
    - `extend()` - Adds contents of a list to the end of another
    - `sum()` - Sum list if it only contains numerical values
    - `count()` - Count number of elements in list
    - `index()` - Returns the index of first occurrence
    - `min()` - Calculate minimum of list if it only contains numerical values
    - `max()` - Calculate maximum of list if it only contains numerical values
    - `sort()` - sort list
    - `reverse()` - reverse list
    - `sorted(my_list)` - return sorted list without changing `my_list`
    - `reversed(my_list)` - return sorted list in reverse order without changing `my_list`
    - `pop()` -  Remove last item from list
    - `pop(idx)` - Remove item at index `idx`
    - `remove(value)` - Remove from list `value` if it exists
    - `del my_list[idx]` - NOT a list method. Using the `del` operator you can remove value at a given index


## Chapter 6 -- Functions

### General Information About Functions
  - Functions are subprograms -- they are a sequence of of statements that have a name
  - Functions can be executed at any point by using their name 
  - Functions remove duplicated code
  - Functions can call other functions
  - Functions can OPTIONALLY take parameters or inputs that they can use inside the function 

### Scope in Python 
  - Remember variables, which can be an int, float, string, or list, are containers for holding data
  - Where these variables can be referenced, meaning used, in your program is called `scope`
  - Since each function is its own little subprogram, the variables that are used inside one function cannot be referenced inside
  another function. This idea that a variable inside one function cannot be used inside another function is called called `scope`, 
  the scope of a variable is the limit or boundaries inside which it can be used. Variables created/declared inside a function 
  are called `local`, meaning they are local to that function. Variables that can be referenced by multiple functions are called `global`.
  - How do you pass variables between functions? You can pass them as parameters or inputs to the function. 
  - Variables in Python are of two types with respect to whether a function can change them or not and this change is preserved outside the function:
    - Immutable: int, float, str, bool, tuple (a tuple is a list that cannot be changed once declared)
    - Mutable: list, dict
  - When you pass mutable variables to a function and make changes inside the function, the variable preserves the changes made inside the function
  - When you pass immutable variables to a function and make changes inside the function, the variable is not changed outside the function 
  - How can you change an immutable variable? 
    - You pass an immutable variable, make changes the local copy inside the function, return the value, and set the output of the function to the variable. 
    - Return values are the main way to send information from a function back to the part of the program that called the function. 
  - NOTE: Strings are immutable and lists are mutable
