# Compiler-Project
Programming Language Project

|   Student Name  | Student ID | Contribution |
| --------------- | ---------- | ------------ |
| Kaung Htet Aung |   124695   |              |
|                 |            |              |
|                 |            |              |





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
