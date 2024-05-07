from enum import Enum

class TokenTypes(Enum):
    
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'
    BOOLEAN = 'BOOLEAN'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    EQ = 'EQUAL'
    NE = 'NOTEQUAL'
    LT = 'LESS THAN'
    LE = 'LESS THAN EQUAL'
    GT = 'GREATER THAN'
    GE = 'GREATER THAN EQUAL'
    ASSIGN = 'ASSIGN'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    IF = 'IF'
    THEN = 'THEN'
    ELSE = 'ELSE'
    WHILE = 'WHILE'
    PRINT = 'PRINT'
    ID = 'Identifier'
    EOF = 'End of File'
    EOL = 'End of Line'
    BLOCK_START = "BLOCK_START"
    BLOCK_END = "BLOCK_END"

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
        raise Exception('Invalid Character', self.current_char)

    def advance(self, count):
        self.pos += count
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance(1)

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance(1)
        if self.current_char == '.':
            result += self.current_char
            self.advance(1)
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance(1)
            return Token(TokenTypes.FLOAT, float(result))
        return Token(TokenTypes.INTEGER, int(result))

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.number()
            
            if self.current_char == '+':
                token = Token(TokenTypes.PLUS, self.current_char)
                self.advance(1)
                return token
            
            if self.current_char == '-':
                token = Token(TokenTypes.MINUS, self.current_char)
                self.advance(1)
                return token
            
            if self.current_char == '*':
                token = Token(TokenTypes.MULTIPLY, self.current_char)
                self.advance(1)
                return token
            
            if self.current_char == '/':
                token = Token(TokenTypes.DIVIDE, self.current_char)
                self.advance(1)
                return token
            
            if self.current_char == '(':
                token = Token(TokenTypes.LPAREN, self.current_char)
                self.advance(1)
                return token

            if self.current_char == ')':
                token = Token(TokenTypes.RPAREN, self.current_char)
                self.advance(1)
                return token
            
            if self.current_char == ';':
                token = Token(TokenTypes.EOL, self.current_char)
                self.advance(1)
                return token
            
            if self.current_char == ':':
                self.advance(1)
                if self.current_char == '=':
                    self.advance(1)
                    return Token(TokenTypes.ASSIGN, ':=')
                else:
                    self.error()
            
            if self.current_char == '=':
                self.advance(1)
                if self.current_char == '=':
                    self.advance(1)
                    return Token(TokenTypes.EQ, '==')
                else:
                    self.error()
            
            if self.current_char == '!':
                self.advance(1)
                if self.current_char == '!':
                    self.advance(1)
                    return Token(TokenTypes.NE, '!!')
                else:
                    self.error()

            if self.current_char == '<':
                self.advance(1)
                if self.current_char == '=':
                    self.advance(1)
                    return Token(TokenTypes.LE, '<=')
                elif self.current_char == '<':
                    self.advance(1)
                    return Token(TokenTypes.BLOCK_START, '<<')
                return Token(TokenTypes.LT, '<')
            
            if self.current_char == '>':
                self.advance(1)
                if self.current_char == '=':
                    self.advance(1)
                    return Token(TokenTypes.GE, '>=')
                elif self.current_char == '>':
                    self.advance(1)
                    return Token(TokenTypes.BLOCK_END, '>>')
                return Token(TokenTypes.GT, '>')

            if self.current_char == 'i' and self.text[self.pos:self.pos + 2] == 'if':
                self.advance(2)
                return Token(TokenTypes.IF, 'if')

            if self.current_char == 't' and self.text[self.pos:self.pos + 4] == 'then':
                self.advance(4)
                return Token(TokenTypes.THEN, 'then')

            if self.current_char == 'e' and self.text[self.pos:self.pos + 4] == 'else':
                self.advance(4)
                return Token(TokenTypes.ELSE, 'else')

            if self.current_char == 'w' and self.text[self.pos:self.pos + 5] == 'while':
                self.advance(5)
                return Token(TokenTypes.WHILE, 'while')

            if self.current_char == 'p' and self.text[self.pos:self.pos + 5] == 'print':
                self.advance(5)
                return Token(TokenTypes.PRINT, 'print')
            
            if self.current_char == 'T' and self.text[self.pos:self.pos + 4] == 'True':
                self.advance(4)
                return Token(TokenTypes.BOOLEAN, True)
            elif self.current_char == 'F' and self.text[self.pos:self.pos + 5] == 'False':
                self.advance(5)
                return Token(TokenTypes.BOOLEAN, False)

            if self.current_char.isalpha():
                return self.identifier()

            self.error()

        return Token(TokenTypes.EOF, None)
    
    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance(1)
        return Token(TokenTypes.ID, result)
