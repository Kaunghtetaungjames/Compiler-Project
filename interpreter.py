from lexer import TokenTypes

class Interpreter:
    def __init__(self, parser):
        self.parser = parser
        self.variables = {}

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

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
        elif node.op.type == TokenTypes.EQUAL:
            return self.visit(node.left) == self.visit(node.right)
        elif node.op.type == TokenTypes.NOTEQUAL:
            return self.visit(node.left) != self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def visit_Boolean(self, node):
        return node.value

    def visit_Assign(self, node):
        var_name = node.left.value
        value = self.visit(node.right)
        self.variables[var_name] = value
        return f"{var_name} : {value}"

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
        return result
