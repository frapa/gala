import expressions
import var_types

class Boolean(expressions.Expression):
    def __init__(self, parent, expr):
        super(Boolean, self).__init__(parent)

        self.bool = "".join(expr.children)

    def get_type(self):
        return var_types.bool

    def to_c(self):
        return "{bool}".format(bool=self.bool)