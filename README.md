# Table of contents
1. [General presentation](#1-general-presentation)
2. [Operations](#2-operations)
3. [Syntax](#3-syntax)
4. [How **computor-v2** processes a command ?](#4-how-computor-v2-processes-a-command)

# 1. General presentation
**computor-v2** is an instruction interpreter that processes user inputs for advanced computations.
Its features include:

- Support for the following mathematical types:
    - Rational numbers
    - Complex numbers (with rational coefficients)
    - Matrices
    - Polynomial equations of degrees less than or equal to 2
- Variable assignment by type inference
- Function assignment (with one variable)
- Resolution of a mathematical expression with or without defined variable(s)
- Resolution of an equation of degree less than or equal to 2
- Operations between types

# 2. Operations

The conventional operators can be used: **\* / + -**
Moreover, **computor-v2** supports the following operators:
- **%**: modulo
- **\*\***: matrix multiplication
- **\***: Hadamard product and multiplication by a scalar
- **^**: exponentiation to a non-negative integer

The program handles parenthesis and computation priorities.  

It supports the following types of commands:  
Evaluate an expresion: ```<expression> = ?```  
Variable assignment: ```varName = <expression>```  
Function assignment: ```funcName( varName ) = <expression(varName)>```  
Solve polynomial equation: ```<expression(x)> = <expression(x)> ?```  

# 3. Syntax

## 3.1 Matrices
The matrix syntax is of the form $[[A_{0,0}, A_{0,1}, \dots];[A_{1,0}, A_{1,1}, \dots];\dots]$

## 3.2 Functions
The syntax for functions is of the form: functionName(variable) = ...

# 4. How **computor-v2** processes a command ?

During the lifetime of the program, a ```ComputorSession``` object is responsible for reading, parsing, processing the user's commands and storing the defined variables and functions.
When it reads a command, **computor-v2** breaks it down into tokens that can be *simple* (e.g. rational number, imaginary unit, identifier, operator) or *composite* (e.g. parenthesized expression, matrix). Composite tokens are recursively tokenized.
The semantics are then analyzed to decide what to do with the command.

## 4.1 Expression evaluation

Commands of the form: ```<expression> = ?```  
Variables are replaced by their values. Then functions are replaced by their expressions as parenthesized expressions. Finally, elements are evaluated starting with the innermost elements.

## 4.2 Variable assignment

Commands of the form: ```varName = <expression>```  
The right-hand side expression is evaluated as in the previous section. The result is assigned to the variable name.

## 4.3 Function assignment

Commands of the form: ```funcName( varName ) = <expression(varName)>```  
Variables in the right-hand side expression are replaced by their values except for ```varName```. Summands that do not depend on ```varName``` are added together for simplification. The resulting expression --that depends on ```varName```-- is assigned to ```funcName```.

## 4.4 Polynomial equation solving

Commands of the form: ```<expression(x)> = <expression(x)> ?```  
Every variable other than ```x``` is replaced by its value. Every function is replaced by its expression as a parenthesized expression. Then every simple token that corresponds to a mathematical type is interpreted as a polynomial. The reduced form is computed using polynomial operations. Then, the equation is solved.