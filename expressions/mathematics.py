import expressions
import parse
import operators

Sum = operators.OpExprUniform
Prod = operators.OpExprUniform
Mod = operators.OpExprUniform

class Power(expressions.Expression):
    def __init__(self, parent, expr):
        super(Power, self).__init__(parent)

        self.value = parse.parse(self, expr.children[0])
        self.exponent = parse.parse(self, expr.children[1])

    def get_type(self):
        return self.get_ctx().get('type')

    def to_c(self):
        T = self.get_type()

        fun = {
            'int32': 'powl',
            'int64': 'powl',
            'float32': 'powf',
            'float64': 'pow',
            'bool': 'pow',
        }[repr(T)]

        return "({cast}) {fun}({value}, {exp})".format(
            cast  = T.to_c(),
            fun   = fun,
            value = self.value.to_c(),
            exp   = self.exponent.to_c(),
        )

class Negation(expressions.Expression):
    def __init__(self, parent, expr):
        super(Negation, self).__init__(parent)

        self.expr = parse.parse(self, expr.children[1])

    def get_type(self):
        return self.expr.get_type()

    def to_c(self):
        return '(-{})'.format(self.expr.to_c())