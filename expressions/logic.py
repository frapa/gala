import expressions
import parse
import operators
import var_types

And = operators.OpExprType
And.T = var_types.bool

Or = operators.OpExprType
And.T = var_types.bool

class Not(expressions.Expression):
    def __init__(self, parent, expr):
        super(Not, self).__init__(parent)

        self.expr = parse.parse(self, expr.children[3])

    def get_type(self):
        return var_types.bool

    def to_c(self):
        return '(!{})'.format(self.expr.to_c())

Eq = operators.OpExprType
Eq.T = var_types.bool

Rel = operators.OpExprType
Rel.T = var_types.bool

BitwiseOr = operators.OpExprUniform
BitwiseXor = operators.OpExprUniform
BitwiseAnd = operators.OpExprUniform

class BitwiseNot(expressions.Expression):
    def __init__(self, parent, expr):
        super(BitwiseNot, self).__init__(parent)

        self.expr = parse.parse(self, expr.children[1])

    def get_type(self):
        return self.expr.get_type()

    def to_c(self):
        return '(~{})'.format(self.expr.to_c())