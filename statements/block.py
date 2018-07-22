import statements
import parse


class Block(statements.Statement):
    def __init__(self, parent, stmt):
        super(Block, self).__init__(parent)

        # Create sub-scope
        self.get_ctx().sub_scope()


        self.statements = [parse.parse(self, s) for s in stmt.children]

    def to_c(self):
        return '{{\n{statements}\n}}'.format(
            statements = ";\n".join([s.to_c() for s in self.statements])
        )