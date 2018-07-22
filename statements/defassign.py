import statements
import expressions
import var_types
import context


class Definition(statements.Statement):
    def __init__(self, parent, stmt, terminator=';'):
        super(Definition, self).__init__(parent)

        self.terminator = terminator

        self.identifier = context.Identifier(self, stmt.children[0])
        # Make variable visible in current scope
        self.identifier.add_to_scope()

        self.T = var_types.Type(self, stmt.children[1])

    def get_type(self):
        return self.T

    def to_c(self):
        return '{type} {id}{terminator}'.format(
            id         = self.identifier.to_c(),
            type       = self.T.to_c(),
            terminator = self.terminator
        )


class Assignment(statements.Statement):
    def __init__(self, parent, stmt):
        super(Assignment, self).__init__(parent)

        if stmt.children[0].children[0].type != 'identifier':
            raise Exception("Expression not yet supported on left side of assignment")

        if len(stmt.children[0].children) == 2:
            self.left = Definition(self, stmt.children[0], terminator='')
        else:
            self.left = expressions.parse(self, stmt.children[0].children[0])

        # mark as type as to allow proper casts
        self.get_ctx().set('type', self.left.get_type())

        self.right = expressions.parse(self, stmt.children[1])

        print(self.left.identifier, self.left.get_type(), self.right.get_type())
        if self.left.get_type() != self.right.get_type():
            raise Exception("Assigning {assign} to variable of type {var}".format(
                var    = self.left.get_type(),
                assign = self.right.get_type(),
            ))

    def to_c(self):
        return '{left} = {right};'.format(
            left  = self.left.to_c(),
            right = self.right.to_c()
        )