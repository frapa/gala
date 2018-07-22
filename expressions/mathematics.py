import expressions
import parse

# Dummy class to make the treatment of operators homogeneous
class Operator(object):
    def __init__(self, op):
        self.op = op

    def to_c(self):
        return " {op} ".format(op=self.op)


class OpExpr(expressions.Expression):
    def __init__(self, parent, expr):
        super(OpExpr, self).__init__(parent)

        self.subexprs = []
        for t in expr.children:
            if type(t) is str:
                self.subexprs.append(Operator(t))
            else:
                subexpr = parse.parse(self, t)
                self.subexprs.append(subexpr)

    def get_type(self):
        T = self.subexprs[0].get_type()

        subexpr = [expr for expr in self.subexprs if not isinstance(expr, Operator)];

        # check that they are all equal
        if all([expr.get_type() == T for expr in subexpr]):
            return T
        else:
            diff_T = filter(lambda expr: expr.get_type() != T, subexpr)[0].get_type()
            raise Exception("Operands have different types: {} and {}".format(T, diff_T))

    def to_c(self):
        sum_str = "".join([expr.to_c() for expr in self.subexprs])
        return "({op})".format(op=sum_str)

Sum = OpExpr
Prod = OpExpr
Mod = OpExpr

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
            'float6464': 'pow',
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
            'float6464': 'pow',
        }[repr(T)]

        return "({cast}) {fun}({value}, {exp})".format(
            cast=T.to_c(),
            fun=fun,
            value=self.value.to_c(),
            exp=self.exponent.to_c(),
        )