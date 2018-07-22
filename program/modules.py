import functions
import statements
import context

class Module(context.CodeObject):
    def __init__(self, parent, name):
        super(Module, self).__init__(parent)

        # Create sub-scope
        self.get_ctx().sub_scope()

        self.identifier = context.Identifier(self, name)
        # Make module visible inside program
        self.identifier.add_to_parent_scope()

        self.functions = []
        self.classes = []

    def add_function(self, fun):
        name, T, body = fun.children

        fun = functions.Function(self, name, T, body)

        self.functions.append(fun)

    # def add_main_statement(self, stmt):
    #     self.main_statements.append(
    #         statements.statement(stmt, 'file'))

    def to_c(self):
        code = ''

        code += '#include <stdint.h>\n'
        code += '#include <stdio.h>\n'
        code += '#include <math.h>\n'

        for fun in self.functions:
            code += fun.to_c_declaration() + '\n'

        for fun in self.functions:
            code += fun.to_c_definition() + '\n'

        return code