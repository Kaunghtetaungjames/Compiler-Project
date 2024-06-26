from lexer import TokenTypes

class AST:
    pass

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Boolean(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr

class Variable:
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class IfElse(AST):
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

class WhileLoop(AST):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

class Block(AST):
    def __init__(self):
        self.children = []

class Print(AST):
    def __init__(self, expr):
        self.expr = expr

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid Syntax')

    def consume(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def parse(self):
        node = self.block_statement()
        if self.current_token.type != TokenTypes.EOF:
            self.error()
        return node

    def block_statement(self):
        self.consume(TokenTypes.BLOCK_START)
        nodes = self.statement_list()
        self.consume(TokenTypes.BLOCK_END)

        root = Block()
        for node in nodes:
            root.children.append(node)
        return root

    def statement_list(self):
        node = self.statement()
        results = [node]

        while self.current_token.type == TokenTypes.SEMI:
            self.consume(TokenTypes.SEMI)
            results.append(self.statement())
            
        if self.current_token.type == TokenTypes.ID:
            self.error()
        return results
    
    def statement(self):
        if self.current_token.type == TokenTypes.BLOCK_START:
            node = self.block_statement()
        elif self.current_token.type == TokenTypes.ID:
            node = self.assignment_statement()
        elif self.current_token.type == TokenTypes.IF:
            node = self.if_statement()
        elif self.current_token.type == TokenTypes.WHILE:
            node = self.while_statement()
        elif self.current_token.type == TokenTypes.PRINT:
            node = self.print_statement()
        else:
            node = self.comparison()
        return node

    def assignment_statement(self):
        left = self.variable()
        token = self.current_token
        self.consume(TokenTypes.ASSIGN)
        right = self.expr()
        return Assign(left, token, right)

    def variable(self):
        node = Variable(self.current_token)
        self.consume(TokenTypes.ID)
        return node

    def if_statement(self):
        self.consume(TokenTypes.IF)
        condition = self.comparison()
        self.consume(TokenTypes.THEN)
        if_block = self.statement()
        if self.current_token.type == TokenTypes.ELSE:
            self.consume(TokenTypes.ELSE)
            else_block = self.statement()
            return IfElse(condition, if_block, else_block)
        return IfElse(condition, if_block)

    def while_statement(self):
        self.consume(TokenTypes.WHILE)
        condition = self.comparison()
        block = self.block_statement()
        return WhileLoop(condition, block)

    def print_statement(self):
        self.consume(TokenTypes.PRINT)
        expr = self.comparison()
        return Print(expr)

    def comparison(self):
        node = self.expr()
        if self.current_token.type in (TokenTypes.EQ, TokenTypes.NE, TokenTypes.LT, TokenTypes.LE, TokenTypes.GT, TokenTypes.GE):
            token = self.current_token
            self.consume(token.type)
            return BinOp(left=node, op=token, right=self.expr())
        else:
            return node
    
    def expr(self):
        node = self.term()
        while self.current_token.type in (TokenTypes.PLUS, TokenTypes.MINUS):
            token = self.current_token
            self.consume(token.type)
            node = BinOp(left=node, op=token, right=self.term())
        return node
    
    def term(self):
        node = self.factor()
        while self.current_token.type in (TokenTypes.MULTIPLY, TokenTypes.DIVIDE):
            token = self.current_token
            self.consume(token.type)
            node = BinOp(left=node, op=token, right=self.factor())
        return node
    
    def factor(self):
        token = self.current_token
        if token.type == TokenTypes.INTEGER or token.type == TokenTypes.FLOAT:
            self.consume(token.type)
            return Num(token)
        elif token.type == TokenTypes.BOOLEAN:
            self.consume(token.type)
            return Boolean(token)
        elif token.type == TokenTypes.LPAREN:
            self.consume(TokenTypes.LPAREN)
            node = self.comparison()
            self.consume(TokenTypes.RPAREN)
            return node
        elif token.type == TokenTypes.MINUS:
            self.consume(TokenTypes.MINUS)
            return UnaryOp(token, self.factor())
        else:
            return self.variable()
