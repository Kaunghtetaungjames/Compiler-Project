# Compiler-Project
Programming Language Project

|   Student Name   | Student ID |      Contributions        |
| ---------------- | ---------- | ------------------------- |
| Kaung Htet Aung  |   124695   | Types: int, float,        |
|                  |            | Assignment statement,     |
|                  |            | Arithmetic Expressions    |
| Yu Kay Khaing Oo |   124688   | Type: boolean,            |
|                  |            | Boolean Expressions,      |
|                  |            | If-then-else statement    |
|                  |            | print() statement         |
| May Thukha Naing |   124761   | Dynamic type checking     |

### Features List
    Data Types: int, float, boolean
    Dynamic type checking
    Arithmetic operators: +, -, *, / with the usual precedence of * and / over the others two.
    Relational operators: ==, !=, <, <=, >, >=
    Assignment statement
    If-then-else statement
    print() statement

### Grammar
    statement : block_statement
              | assignment_statement
              | if_statement
              | while_statement 
              | print_statement
              | comparison
    
    assignment_statement : variable ASSIGN expr EOL

    if_statement : IF comparison THEN block_statement
                 | IF comparison THEN block_statement ELSE block_statement

    while_statement : WHILE comparison block_statement

    block_statement : BLOCK_START statement_list BLOCK_END

    statement_list : statement EOL statement_list
                   | statement EOL

    print_statement : PRINT comparison EOL

    comparison : expr (EQ|NE|LT|LE|GT|GE) expr
               | expr

    expr : term (PLUS | MINUS) term
         | term
    
    term : factor (MULTIPLY | DIVIDE) factor
         | factor
    
    factor : INTEGER | FLOAT | BOOLEAN
           | LPAREN  comparison LPAREN
           | MINUS factor
           | variable
    
    variable: ID
    
### Tokens
    ID          : letter (letter | digit)*
    INTEGER     : digit+
    FLOAT       : digit+(.digit+)
    BOOLEAN     : True | False
    PLUS        : +
    MINUS       : -
    MULTIPLY    : *
    DIVIDE      : /
    EQ          : ==
    NE          : !!
    LT          : <
    LE          : <=
    GT          : >
    GE          : >=
    ASSIGN      : :=
    LPAREN      : '('
    RPAREN      : ')'
    IF          : 'if'
    THEN        : 'then'
    ELSE        : 'else'
    WHILE       : 'while'
    PRINT       : 'print'
    EOL         : '|'
    BLOCK_START : "<<"
    BLOCK_END   : ">>"

### AST (Abstract Syntax Tree)
"AST Classes": The code defines several classes that represent different nodes in the abstract syntax tree. These classes include:
   - `Num`: Represents a numeric value.
   - `Boolean`: Represents a boolean value.
   - `BinOp`: Represents a binary operation.
   - `UnaryOp`: Represents a unary operation.
   - `Variable`: Represents a variable's name.
   - `Assign`: Represents an assignment statement.
   - `IfElse`: Represents an if-else statement.
   - `WhileLoop`: Represents a while loop.
   - `Print`: Represents a print statement.

### Interpreter 

The interpreter class has the following features:

1. "Initialization": The `Interpreter` class takes a `parser` object as an argument and initializes an empty `variables` dictionary.
2. "Interpretation": The `interpret` method calls the `parse` method of the `parser` object and then calls the `visit` method with the parsed tree as an argument.
3. "Visiting Nodes": The `visit` method dynamically calls the appropriate `visit_<node_type>` method based on the type of the node and returns the result.
4. "Generic Visit": The `generic_visit` method raises an exception if there is no specific `visit_<node_type>` method defined for a node type.
5. "Binary Operations": The `visit_BinOp` method performs different operations based on the type of the binary operator.
6. "Number and Boolean Nodes": The `visit_Num` and `visit_Boolean` methods simply return the value of the respective nodes.
7. "Assignment": The `visit_Assign` method assigns the value of the right node to the variable specified by the left node.
8. "If-Else Statements": The `visit_IfElse` method evaluates the condition node and executes either the if block or the else block based on the result.
9. "While Loops": The `visit_WhileLoop` method repeatedly executes the block node as long as the condition node evaluates to true.
10. "Print Statements": The `visit_Print` method evaluates the expression node and prints the result.

### How to run
Here is an example of how to run the code:

```python
# Import necessary classes
from lexer import Lexer
from astparser import Parser
from interpreter import Interpreter

#Input from user
while True:
    try:
        text = input('>> ')
    except EOFError:
        break
    if not text:
        continue

    # Create an instance of lexer, passing the input text as an argument
    lexer = Lexer(text)

    # Create an instance of AST parser, passing the lexer as an argument
    parser = Parser(lexer)

    # Create an instance of interpreter, passing the parser as an argument
    interpreter = Interpreter(parser)
    result = interpreter.interpret()
    print(result)
```

```
>> x = 10
x : 10
>> print(1+2*3)
7  
>> if 3>4 then print(1) else print(3>4)
False
>>   
```