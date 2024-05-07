from lexer import TokenTypes
from astparser import *

class TypeChecker:
    variables = {}

    def check(self, node):
        method_name = f'check_{type(node).__name__}'
        checker = getattr(self, method_name, self.generic_check)
        return checker(node)

    def generic_check(self, node):
        raise Exception(f'No check_{type(node).__name__} method')

    def check_Num(self, node):
        if isinstance(node.value, int):
            return TokenTypes.INTEGER
        elif isinstance(node.value, float):
            return TokenTypes.FLOAT
        else:
            raise Exception(f'Wrong type: {type(node.value).__name__} is not a number')
    
    def check_Boolean(self, node):
        if not isinstance(node.value, bool):
            raise Exception(f'Wrong type: {type(node.value).__name__} is not a boolean')
        return TokenTypes.BOOLEAN
    
    def check_Block(self, node):
        for child in node.children:
            self.check(child)
    
    def check_BinOp(self, node):
        left_type = self.check(node.left)
        right_type = self.check(node.right)
        
        if node.op.type in (TokenTypes.PLUS, TokenTypes.MINUS, TokenTypes.MULTIPLY, TokenTypes.DIVIDE):
            if left_type not in (TokenTypes.INTEGER, TokenTypes.FLOAT) or right_type not in (TokenTypes.INTEGER, TokenTypes.FLOAT):
                raise Exception('Type mismatch: Both operands must be numbers')
        elif node.op.type in (TokenTypes.EQ, TokenTypes.NE, TokenTypes.LT, TokenTypes.LE, TokenTypes.GT, TokenTypes.GE):
            if left_type != right_type:
                raise Exception('Type mismatch: Operands must be the same type')
            if left_type not in (TokenTypes.INTEGER, TokenTypes.FLOAT, TokenTypes.BOOLEAN) or right_type not in (TokenTypes.INTEGER, TokenTypes.FLOAT, TokenTypes.BOOLEAN):
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
    
    def check_Variable(self, node):
        var_name = node.value
        var_type = self.variables.get(var_name)
        return var_type
    
    