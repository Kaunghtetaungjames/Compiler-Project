from lexer import TokenTypes
from astparser import *

class TypeChecker:
    def __init__(self):
        self.variables = {}

    def check(self, node):
        method_name = f'check_{type(node).__name__}'
        checker = getattr(self, method_name, self.generic_check)
        return checker(node)

    def generic_check(self, node):
        raise Exception(f'No check_{type(node).__name__} method')

    def check_Num(self, node):
        return TokenTypes.INTEGER if isinstance(node.value, int) else TokenTypes.FLOAT

    def check_BinOp(self, node):
        left_type = self.check(node.left)
        right_type = self.check(node.right)
        if left_type != right_type:
            raise Exception('Operands must be of the same type')
        if node.op.type in (TokenTypes.PLUS, TokenTypes.MINUS, TokenTypes.MULTIPLY, TokenTypes.DIVIDE):
            if left_type != TokenTypes.INTEGER and left_type != TokenTypes.FLOAT:
                raise Exception('Operands must be numbers')
            return left_type
        elif node.op.type in (TokenTypes.EQ, TokenTypes.NE, TokenTypes.LT, TokenTypes.LE, TokenTypes.GT, TokenTypes.GE):
            if left_type != TokenTypes.INTEGER and left_type != TokenTypes.FLOAT and left_type != TokenTypes.BOOLEAN:
                raise Exception('Operands must be numbers or booleans')
            return TokenTypes.BOOLEAN

    def check_Assign(self, node):
        var_name = node.left.value
        var_type = self.check(node.right)
        if var_name in self.variables:
            if self.variables[var_name] != var_type:
                raise Exception('Variable type mismatch')
        else:
            self.variables[var_name] = var_type
        return var_type

    def check_IfElse(self, node):
        condition_type = self.check(node.condition)
        if condition_type != TokenTypes.BOOLEAN:
            raise Exception('Condition must be a boolean')
        if_block_type = self.check(node.if_block)
        if node.else_block:
            else_block_type = self.check(node.else_block)
            if if_block_type != else_block_type:
                raise Exception('Inconsistent types in if-else blocks')
            return if_block_type

    def check_WhileLoop(self, node):
        condition_type = self.check(node.condition)
        if condition_type != TokenTypes.BOOLEAN:
            raise Exception('Condition must be a boolean')
        return self.check(node.block)

    def check_Print(self, node):
        return self.check(node.expr)

    def check_Literal(self, node):
        if isinstance(node.value, int):
            return TokenTypes.INTEGER
        elif isinstance(node.value, float):
            return TokenTypes.FLOAT
        elif isinstance(node.value, bool):
            return TokenTypes.BOOLEAN
        else:
            raise Exception(f'Unsupported literal type: {type(node.value).__name__}')

