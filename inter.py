class NodeVisitor:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class Interpreter(NodeVisitor):
    def __init__(self):
        self.variables = {}

    def visit_Num(self, node):
        return node.value

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIVIDE:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Assign(self, node):
        self.variables[node.var_name] = self.visit(node.value)

    def visit_BooleanOp(self, node):
        if node.op.type == EQUAL:
            return self.visit(node.left) == self.visit(node.right)
        elif node.op.type == NOTEQUAL:
            return self.visit(node.left) != self.visit(node.right)

    def visit_IfElse(self, node):
        if self.visit(node.condition):
            self.visit(node.true_statement)
        else:
            self.visit(node.false_statement)

    def visit_WhileLoop(self, node):
        while self.visit(node.condition):
            self.visit(node.statement)

    def visit_Print(self, node):
        print(self.visit(node.value))

    def interpret(self, tree):
        if tree is None:
            return ''
        return self.visit(tree)

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
        interpreter = Interpreter()
        result = interpreter.interpret(parser.parse())
        print(result)

if __name__ == '__main__':
    main()
