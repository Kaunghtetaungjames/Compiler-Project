class AST:
    pass

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Assign(AST):
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value

class BooleanOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class IfElse(AST):
    def __init__(self, condition, true_statement, false_statement):
        self.condition = condition
        self.true_statement = true_statement
        self.false_statement = false_statement

class WhileLoop(AST):
    def __init__(self, condition, statement):
        self.condition = condition
        self.statement = statement

class Print(AST):
    def __init__(self, value):
        self.value = value

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == INTEGER or token.type == FLOAT:
            self.eat(token.type)
            return Num(token)
        elif token.type == BOOLEAN:
            self.eat(BOOLEAN)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        elif token.type == ID:
            node = Assign(token.value, None)
            self.eat(ID)
            return node

    def term(self):
        node = self.factor()

        while self.current_token.type in (MULTIPLY, DIVIDE):
            token = self.current_token
            if token.type == MULTIPLY:
                self.eat(MULTIPLY)
            elif token.type == DIVIDE:
                self.eat(DIVIDE)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def boolean_expr(self):
        node = self.expr()
        token = self.current_token

        if token.type in (EQUAL, NOTEQUAL):
            self.eat(token.type)
            return BooleanOp(left=node, op=token, right=self.expr())
        else:
            self.error()

    def statement(self):
        token = self.current_token
        if token.type == ID:
            var_name = token.value
            self.eat(ID)
            self.eat(ASSIGN)
            value = self.expr()
            return Assign(var_name, value)
        elif token.type == IF:
            self.eat(IF)
            condition = self.boolean_expr()
            self.eat(':')
            true_statement = self.statement()
            self.eat(ELSE)
            false_statement = self.statement()
            return IfElse(condition, true_statement, false_statement)
        elif token.type == WHILE:
            self.eat(WHILE)
            condition = self.boolean_expr()
            self.eat(':')
            statement = self.statement()
            return WhileLoop(condition, statement)
        elif token.type == PRINT:
            self.eat(PRINT)
            value = self.expr()
            return Print(value)
        else:
            return self.expr()

    def parse(self):
        return self.statement()
