from enum import Enum

class TokenTypes(Enum):
    # Token types
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'
    BOOLEAN = 'BOOLEAN'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    EQUAL = 'EQUAL'
    NOTEQUAL = 'NOTEQUAL'
    ASSIGN = 'ASSIGN'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    IF = 'IF'
    THEN = 'THEN'
    ELSE = 'ELSE'
    WHILE = 'WHILE'
    PRINT = 'PRINT'
    ID = 'ID'
    EOF = 'EOF'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {repr(self.value)})'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid Character')

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
            return Token(TokenTypes.FLOAT, float(result))
        return Token(TokenTypes.INTEGER, int(result))

    def boolean(self):
        if self.text[self.pos:self.pos + 4] == 'True':
            self.pos += 4
            return Token(TokenTypes.BOOLEAN, True)
        elif self.text[self.pos:self.pos + 5] == 'False':
            self.pos += 5
            return Token(TokenTypes.BOOLEAN, False)
        else:
            self.error()

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.integer()
            
            if self.current_char == '+':
                token = Token(TokenTypes.PLUS, self.current_char)
                self.advance()
                return token
            
            if self.current_char == '-':
                token = Token(TokenTypes.MINUS, self.current_char)
                self.advance()
                return token
            
            if self.current_char == '*':
                token = Token(TokenTypes.MULTIPLY, self.current_char)
                self.advance()
                return token
            
            if self.current_char == '/':
                token = Token(TokenTypes.DIVIDE, self.current_char)
                self.advance()
                return token
            
            if self.current_char == '(':
                token = Token(TokenTypes.LPAREN, self.current_char)
                self.advance()
                return token

            if self.current_char == ')':
                token = Token(TokenTypes.RPAREN, self.current_char)
                self.advance()
                return token
            
            if self.current_char == '=':
                if self.text[self.pos:self.pos + 2] == '==':
                    self.pos += 2
                    return Token(TokenTypes.EQUAL, '==')
                else:
                    token = Token(TokenTypes.ASSIGN, self.current_char)
                    self.advance()
                    return token
            
            if self.current_char == '!':
                if self.text[self.pos:self.pos + 2] == '!=':
                    self.pos += 2
                    return Token(TokenTypes.NOTEQUAL, '!=')
                else:
                    self.error()

            if self.current_char == 'i' and self.text[self.pos:self.pos + 2] == 'if':
                self.pos += 2
                return Token(TokenTypes.IF, 'if')

            if self.current_char == 't' and self.text[self.pos:self.pos + 4] == 'then':
                self.pos += 4
                return Token(TokenTypes.THEN, 'then')

            if self.current_char == 'e' and self.text[self.pos:self.pos + 4] == 'else':
                self.pos += 4
                return Token(TokenTypes.ELSE, 'else')

            if self.current_char == 'w' and self.text[self.pos:self.pos + 5] == 'while':
                self.pos += 5
                return Token(TokenTypes.WHILE, 'while')

            if self.current_char == 'p' and self.text[self.pos:self.pos + 5] == 'print':
                self.pos += 5
                return Token(TokenTypes.PRINT, 'print')

            if self.current_char.isalpha():
                return self.identifier()

            self.error()

        return Token(TokenTypes.EOF, None)
    
    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return Token(TokenTypes.ID, result)
