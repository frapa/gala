import expressions
import parse

# Dummy class to make the treatment of operators homogeneous
class Operator(object):
    def __init__(self, op):
        mapping = {
            'and': '&&',
            'or': '||',
        }

        self.op = mapping[op] if op in mapping else op

    def to_c(self):
        return " {op} ".format(op=self.op)


class OpExpr(expressions.Expression):
    def __init__(self, parent, expr):
        super(OpExpr, self).__init__(parent)

        self.subexprs = []

        # Operators can have multiple characters
        op = ''
        for t in expr.children:
            if type(t) is str:
                # Collect multi-character operators
                op += t
            else:
                # If it's the first non string after an operator
                # create the operator
                if op != '':
                    self.subexprs.append(Operator(op))
                    op = ''

                subexpr = parse.parse(self, t)
                self.subexprs.append(subexpr)

    def to_c(self):
        sum_str = "".join([expr.to_c() for expr in self.subexprs])
        return "({op})".format(op=sum_str)

# All sub-expressions must have the same type (example: sum)
class OpExprUniform(OpExpr):
    def get_type(self):
        T = self.subexprs[0].get_type()

        subexpr = [expr for expr in self.subexprs if not isinstance(expr, Operator)];

        # check that they are all equal
        if all([expr.get_type() == T for expr in subexpr]):
            return T
        else:
            diff_T = filter(lambda expr: expr.get_type() != T, subexpr)[0].get_type()
            raise Exception("Operands have different types: {} and {}".format(T, diff_T))

# The result of the operation is always a defined type (example: comparison)
class OpExprType(OpExpr):
    def get_type(self):
        return self.T
