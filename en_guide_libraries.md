# Creating libraries for MPCode
> Since version 0.0.1 MPCode supports custom libraries.

## Basic information
All libraries for MPCode are created in Python and export their functions to it. <br>
For *more interesting things* you can use the source code of the project!

## Requirements for libraries

### funcs.py
The funcs.py file should contain all the functions that will be used in MPCode itself. <br>
Function names should look like `library_function`. <br>
Example:
- Library name: `mpcmath`
- Function: `mpcmath_ex`

All functions and their names for MPCode must be specified in the dictionary `funcs`. <br>
Example: `funcs = {'ex': mpcmath_ex}`

There should also be a `prefix` variable in the file with the standard *prefix* of the library functions. <br>

Prefix - a short name *before functions from a certain library*, needed so that functions with the same names from different libraries do not get mixed together. <br>
The prefix can be *anything you like*, but we recommend writing a short library name and a dot at the end. <br>

Example:
- Library name: `mpcmath`
- Prefix for functions from the library: `math.`
- What using commands from this library looks like: `math.function`

**Note: all arguments are passed to the function as a *list*, even if the argument is a single argument.** <br>
**Recommendations: if you need to accept additional parameters before the list of some arguments, give them names starting with the `~` character.**

### meta.py
The meta.py file should contain information about the library. <br>

An example that contains everything you need:
```
# Files to be installed
files = ['funcs.py']

# Library short name
name = 'mpcmath'

# Library version
version = '0.0.0.1'

# Author
by = 'mrwek & weksoftware'

# Description
description = 'Библиотека для выполнения математических выражений'

# Github repository
github = 'Mister-Wek/mpcmath'

# Library command prefix
prefix = 'math.'

# MPCode version
mpcode_version = '0.0.1'
```

**Note: loading libraries via the `get_lib` function does not support distribution of files into folders. All files will be located in one folder.**

*Library Short Name* - the name used in function names and by which MPCode will identify your library. <br>
**Note: try to make the name unique and match the name of the repository on github.**

*MPCode version* - the MPCode version on which the library was developed. <br>
**Note: try to work on the latest version.**

## Organising repositories on Github
All library files must be located in the `lib` folder. <br>
This folder must contain the files `meta.py` and `funcs.py`.

**Recommendations: if your library contains Python dependencies, then specify them.**

## Examples
- [mpcmath](https://github.com/Mister-Wek/mpcmath)
- [mpcsymbols](https://github.com/Mister-Wek/mpcsymbols)
