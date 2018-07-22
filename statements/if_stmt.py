import statements
import parse
import expressions


class If(statements.Statement):
    def __init__(self, parent, stmt):
        super(If, self).__init__(parent)

        # Create sub-scope
        self.get_ctx().sub_scope()

        self.condition = expressions.parse(self, stmt.children[0])
        self.if_stmt = parse.parse(self, stmt.children[1])
        self.else_stmt = parse.parse(self, stmt.children[2]) if len(stmt.children) == 3 else None

    def to_c(self):
        else_stmt_str = 'else ' + self.else_stmt.to_c() if self.else_stmt is not None else ''

        return ('if ({condition}) {if_stmt}\n{else_stmt}'.format(
            condition = self.condition.to_c(),
            if_stmt   = self.if_stmt.to_c(),
            else_stmt   = else_stmt_str,
        ))