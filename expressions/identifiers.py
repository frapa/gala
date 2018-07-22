import context
import expressions

class Identifier(expressions.Expression):
    def __init__(self, parent, expr):
        super(Identifier, self).__init__(parent)

        self.identifier = context.Identifier(self, expr)

        if parent.get_scope().resolve(self.identifier) is None:
            raise Exception('{id} was not defined'.format(id=self.identifier))

    def get_fully_qualified_name(self):
        return self.identifier.get_fully_qualified_name()

    def get_type(self):
        obj = self.get_scope().resolve(self)
        return obj.get_type()

    def to_c(self):
        return self.identifier.to_c()
