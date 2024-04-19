# Documentation
> MPCode is an interpreted programming language written in Python.
The main ideas behind MPCode are *open source* and *using the language as a constructor*, with the ability to modify it for whatever you want.

---
## Intro
Everything in mpcode is an object.\
Each object is separated from other objects by *spaces*.

To *comment* a part of the code, you can write `/* comment */` (**comments should also be separated by spaces**).

Note: square brackets *are not separate objects*, but combine other objects into [*groups of objects*](#groups).

---
## Groups
> A group is a number of objects combined into one set of objects inside square brackets\
All objects inside a group are **separated by a space**
```
[ group and objects within it ]
```
Group **is not a separate object**\
`[ 1 2 3 4 5 ]` = `[ 1 2 [ 3 4 5 ] ]` = `[ [ 1 ] 2 3 4 5 ]`...

## Variables
> A variable is a group that has its own name and is stored in RAM\.
Variables can be changed and used.

To declare them, you need to write the `=` symbol and after it write the name of the variable:
```
=variable1 [ any value ]
```
`variable1` = `[ any value ]`

**Note: if the group that is assigned to a variable contains a single object, the variable is not assigned to the group with the object, but to *the object itself***.\
**If you need to convert a group into a single object as a line, use the `line` function**.

## Functions
> A function is python code in the mpcode standard library that has its own name.\
Functions can take values, for this purpose you need to put a group after the function name.
```
p [ any text ]
```
Each function returns some value.

```
p [ b ]
```
In the examples above, `b` and `p` are *functions*.

Note: many standard functions (including `p`) translate a group of values into a single string.

## Libraries
> Library - third-party functions available for installation from repositories on github.com.\
Information on creating libraries is available in [en_guide_libraries.md](en_guide_libraries.md).\
To install a third-party library you should use the `get_lib` function.
```
get_lib [ username/repository_name ]
```
```
get_lib [ Mister-Wek/mpcmath ]
```
You can install one or more libraries at once.

To get information about installed libraries, there is a function `libs_info`, which accepts a group of library names or nothing (then it outputs information about all installed libraries).\
A similar function to get the current versions of installed libraries is `libs_versions`.

In order to use the installed libraries, they must be connected during programme runtime.
```
use [ library_names ]
```
```
use [ mpcmath ]
p [ math.ex [ 2 + 2 ] ]
```

For functions from the library to work, when calling them, the *prefix*, which is defined in the funcs.py file of each library, must be written before the function name.\
To specify a custom prefix, you must pass the `~prefix` or `~p` parameter to the function as the first argument.
```
use [ ~p m. mpcmath ]
p [ m.ex [ 2 + 2 ] ]
```

And to connect individual functions from a particular library without a prefix, use `~o` or `~only` followed by the library name and function names
```
use [ ~o mpcsymbols lq rq ]
p [ lq Roman's quote rq ]
```
In addition, *standard* libraries in the `libs` folder are supplied with MPCode from version 0.1.1 onwards

Note: if downloading functions via `get_lib` doesn't work for you, try to specify a dns server (we recommend Google Public DNS) or enable VPN.\
But you can also manually move repositories content to `libs/library_name/` folder.

## Escaping characters and arguments of the function `p`
The `p` function can not only take a group of values, but can also take the `~ws` parameter as its first argument.\
This parameter removes spaces between objects when outputting to the console.

And to escape objects whose names match function names, precede them with the symbol `\`.
```
p [ a \b c ]
```

## Logical operators and function `l`
> Since version 0.1.0, MPCode supports *logical operators* inside the `l` function, which is used to compare two values.

List of logical operators:
- `=` *equal*
- `!=` *not equal*
- `<` *less than*
- `>` *more*
- `<=` *less then/equal*
- `>=` *more/equal*
- `&` *and*
- `|` *or*

The `l` function takes a group with an expression and returns `true` / `false`.\
Example:
```
p [ l [ 2 = 2 ] ]
```

Its result is used in the constructions [`if`, `ife`, `fino`](#if-ife-fino).

## if, ife, fino

### if
`if` accepts two groups of objects.\
The first group contains the result of `l` (`true`/`false`).\
The second group contains *the code to be executed in case of `true`*.

Example:
```
if [ l [ i = hello ] ] [ p [ Hello! ] ]
```

### ife
`ife` accepts three groups of objects.\
The first two are the same as `if`, the third is the code that will be executed in the case of `false`.

Example:
```
ife [ l [ i = hello ] ] [ p [ Hello! ] ] [ p [ Oh D: ] ]
```

### fino
`fino` takes two groups, similar to `if`, but executes the code not once, but *as long as `true`*.

Example:
```
fino [ l [ i != exit ] ] [ p [ Enter exit to exit ] ]
```
