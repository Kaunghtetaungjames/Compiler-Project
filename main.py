from lexer import Lexer
from astparser import Parser
from interpreter import Interpreter

# Testing the interpreter
def main():
    variables = {}
    while True:
        try:
            text = input('>> ')
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)

if __name__ == '__main__':
    main()
