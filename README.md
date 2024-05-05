# Compiler-Project
Programming Language Project

|   Student Name  | Student ID | Contribution |
| --------------- | ---------- | ------------ |
| Kaung Htet Aung |   124695   |              |
|                 |            |              |
|                 |            |              |



Astparser

Feature List

1. "AST (Abstract Syntax Tree) Classes": The code defines several classes that represent different nodes in the abstract syntax tree. These classes include:
   - `Num`: Represents a numeric value.
   - `Boolean`: Represents a boolean value.
   - `BinOp`: Represents a binary operation.
   - `UnaryOp`: Represents a unary operation.
   - `Assign`: Represents an assignment statement.
   - `IfElse`: Represents an if-else statement.
   - `WhileLoop`: Represents a while loop.
   - `Print`: Represents a print statement.

2. "Parser Class": The code includes a `Parser` class that is responsible for parsing the input and constructing the abstract syntax tree. It uses a lexer to tokenize the input.

3. "Lexer": The lexer is not provided in the code snippet, but it is assumed to be implemented separately. The lexer is responsible for tokenizing the input code.

Syntax

The code snippet follows the syntax of the Python programming language. It defines classes using the `class` keyword and uses indentation to indicate block structure. The code also includes function definitions using the `def` keyword.

How to Run

To run the code, you need to have the lexer implemented separately. Once you have the lexer, you can follow these steps:

1. Import the `TokenTypes` enum from the `lexer` module.
2. Import the necessary classes from the `lexer` module.
3. Create an instance of the lexer.
4. Create an instance of the parser, passing the lexer as an argument.
5. Call the `parse()` method of the parser to parse the input code and construct the abstract syntax tree.

Here is an example of how to run the code:

```python
from lexer import TokenTypes

# Import necessary classes from the lexer module

# Create an instance of the lexer

# Create an instance of the parser, passing the lexer as an argument
parser = Parser(lexer)

# Call the parse() method of the parser
ast = parser.parse()
```


Interpreter 

Feature List, Syntax, and How to Run

Feature List:
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

Syntax:
The syntax of the provided code follows the Python programming language syntax. It defines a class named `Interpreter` with various methods for interpreting different types of nodes. The code uses indentation to define blocks of code and follows the object-oriented programming paradigm.

How to Run:
To run the provided code, you need to follow these steps:

1. Import the `TokenTypes` class from the `lexer` module.
2. Create an instance of the `Interpreter` class, passing a `parser` object as an argument.
3. Call the `interpret` method on the `Interpreter` instance.

Here is an example of how to run the code:

```python
from lexer import TokenTypes

class Parser:
    # Define the parser logic here

parser = Parser()
interpreter = Interpreter(parser)
interpreter.interpret()
```

