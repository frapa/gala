import var_types
import statements
import context


class Argument(context.CodeObject):
    def __init__(self, parent, name, T):
        super(Argument, self).__init__(parent)

        self.identifier = context.Identifier(self, name)
        # Make variable visible in the function
        self.identifier.add_to_scope()

        self.T = var_types.Type(self, T)

    def get_type(self):
        return self.T

    def to_c(self):
        return '{T} {name}'.format(
            T=self.T.to_c(),
            name=self.identifier.to_c()
        )


class Function(context.CodeObject):
    def __init__(self, parent, name, T, body):
        super(Function, self).__init__(parent)

        # Create sub-scope
        self.get_ctx().sub_scope()

        self.identifier = context.Identifier(self, name)
        # Make the function visible in the scope of the parent
        self.identifier.add_to_parent_scope()

        self.parse_type(T)
        self.parse_body(body)

    def parse_type(self, T):
        self.arguments = []

        deflist, return_type = T.children

        for arg_def in deflist.children:
            arg_name, arg_T = arg_def.children
            arg = Argument(self, arg_name, arg_T)
            self.arguments.append(arg)

        self.return_type = var_types.Type(self, return_type)

    def parse_body(self, body):
        self.body_statements = []

        for stmt in body.children:
            stmt = statements.parse(self, stmt)
            self.body_statements.append(stmt)

    def get_arguments(self):
        return self.arguments

    def get_type(self):
        return var_types.FunType(self, self)

    def get_return_type(self):
        return self.return_type

    def to_c_declaration(self, suffix=';'):
        return '{return_type} {name} ({args}){suffix}'.format(
            return_type = self.return_type.to_c(),
            name = self.identifier.to_c(),
            args = ", ".join([a.to_c() for a in self.arguments]),
            suffix = suffix
        )

    def to_c_definition(self):
        head = self.to_c_declaration(suffix='')
        body = "\n\t".join([bs.to_c() for bs in self.body_statements])

        return '{head} {{\n\t{body}\n}}'.format(
            head = head,
            body = body
        )