import statements
import expressions

class ExprStatement(statements.Statement):
    def __init__(self, parent, stmt):
        super(ExprStatement, self).__init__(parent)

        self.expr = expressions.parse(self, stmt)

    def to_c(self):
        return '{expr};'.format(expr=self.expr.to_c())