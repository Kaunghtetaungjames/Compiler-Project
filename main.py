from lexer import Lexer
from astparser import Parser
from interpreter import Interpreter
from typechecker import TypeChecker

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
        type_checker = TypeChecker()
        interpreter = Interpreter(parser, type_checker)

        try:
            result = interpreter.interpret()
            print("Interpreter result:", result)
            print ("Type checking passed successfully.")
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    main()



