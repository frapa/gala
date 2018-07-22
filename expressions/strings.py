import expressions

class String(expressions.Expression):
    def __init__(self, parent, expr):
        super(String, self).__init__(parent)

        self.string = "".join(["".join(ch.children) for ch in expr.children])

    def to_c(self):
        return '"{string}"'.format(string=self.string)