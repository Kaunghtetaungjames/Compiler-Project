from lexer import Lexer
from astparser import Parser
from interpreter import Interpreter

def main():
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

        try:
            result = interpreter.interpret()
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    main()



