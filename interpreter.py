from lexer import TokenTypes
from typechecker import TypeChecker

class Interpreter:

    global_variables = {}

    def __init__(self, parser):
        self.parser = parser
        self.type_checker = TypeChecker()

    def interpret(self):
        tree = self.parser.parse()
        self.type_check(tree)
        return self.visit(tree)

    def type_check(self, node):
        self.type_checker.check(node)

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')

    def visit_BinOp(self, node):
        if node.op.type == TokenTypes.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == TokenTypes.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == TokenTypes.MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == TokenTypes.DIVIDE:
            return self.visit(node.left) / self.visit(node.right)
        elif node.op.type == TokenTypes.EQ:
            return self.visit(node.left) == self.visit(node.right)
        elif node.op.type == TokenTypes.NE:
            return self.visit(node.left) != self.visit(node.right)
        elif node.op.type == TokenTypes.LT:
            return self.visit(node.left) < self.visit(node.right)
        elif node.op.type == TokenTypes.LE:
            return self.visit(node.left) <= self.visit(node.right)
        elif node.op.type == TokenTypes.GT:
            return self.visit(node.left) > self.visit(node.right)
        elif node.op.type == TokenTypes.GE:
            return self.visit(node.left) >= self.visit(node.right)
        
    def visit_UnaryOp(self, node):
        return -self.visit(node.expr)

    def visit_Num(self, node):
        return node.value

    def visit_Boolean(self, node):
        return node.value

    def visit_Assign(self, node):
        var_name = node.left.value
        value = self.visit(node.right)
        self.global_variables[var_name] = value
        print(f"{var_name} : {value}")

    def visit_IfElse(self, node):
        if self.visit(node.condition):
            return self.visit(node.if_block)
        elif node.else_block:
            return self.visit(node.else_block)

    def visit_WhileLoop(self, node):
        result = None
        while self.visit(node.condition):
            result = self.visit(node.block)
        return result

    def visit_Print(self, node):
        result = self.visit(node.expr)
        print(result)

    def visit_Variable(self, node):
        var_name = node.value
        value = self.global_variables.get(var_name)
        if value is None:
            raise NameError(repr(var_name))
        else:
            return value

    def visit_Block(self, node):
        for child in node.children:
            self.visit(child)