import expressions
import parse

class FunCall(expressions.Expression):
    def __init__(self, parent, expr):
        super(FunCall, self).__init__(parent)

        self.expr = parse.parse(self, expr.children[0])

        if not self.expr.get_type().is_function():
            raise Exception("Calling an object which is not a function: {obj}".format(obj=self.expr.to_c()))

        self.args = [
            parse.parse(self, arg)
                for arg in expr.children[1].children
        ]

    def get_type(self):
        return self.expr.get_type().get_return_type()

    def to_c(self):
        args = ", ".join([args.to_c() for args in self.args])

        return "{expr}({args})".format(
            expr = self.expr.to_c(),
            args = args)
