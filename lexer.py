import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        if self.current_char == '.':
            result += self.current_char
            self.advance()
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()
            return Token(FLOAT, float(result))
        else:
            return Token(INTEGER, int(result))

    def boolean(self):
        if self.text[self.pos:self.pos + 4] == 'True':
            self.pos += 4
            return Token(BOOLEAN, True)
        elif self.text[self.pos:self.pos + 5] == 'False':
            self.pos += 5
            return Token(BOOLEAN, False)
        else:
            self.error()

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.integer()
            
            if self.current_char in '+-*/()=':
                if self.current_char == '+':
                    self.advance()
                    return Token(PLUS, '+')
                elif self.current_char == '-':
                    self.advance()
                    return Token(MINUS, '-')
                elif self.current_char == '*':
                    self.advance()
                    return Token(MULTIPLY, '*')
                elif self.current_char == '/':
                    self.advance()
                    return Token(DIVIDE, '/')
                elif self.current_char == '(':
                    self.advance()
                    return Token(LPAREN, '(')
                elif self.current_char == ')':
                    self.advance()
                    return Token(RPAREN, ')')
                elif self.current_char == '=':
                    self.advance()
                    if self.current_char == '=':
                        self.advance()
                        return Token(EQUAL, '==')
                    else:
                        return Token(ASSIGN, '=')
            
            if self.current_char == '!':
                if self.text[self.pos:self.pos + 2] == '!=':
                    self.pos += 2
                    return Token(NOTEQUAL, '!=')
                else:
                    self.error()

            if self.text[self.pos:self.pos + 2] == 'if':
                self.pos += 2
                return Token(IF, 'if')
            elif self.text[self.pos:self.pos + 4] == 'else':
                self.pos += 4
                return Token(ELSE, 'else')
            elif self.text[self.pos:self.pos + 5] == 'while':
                self.pos += 5
                return Token(WHILE, 'while')
            elif self.text[self.pos:self.pos + 5] == 'print':
                self.pos += 5
                return Token(PRINT, 'print')
            
            if self.current_char.isalpha():
                identifier = ''
                while self.current_char is not None and (self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == '_'):
                    identifier += self.current_char
                    self.advance()
                return Token(ID, identifier)

            self.error()

        return Token(EOF, None)


