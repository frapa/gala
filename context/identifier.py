from code_object import *


class Identifier(CodeObject):
    def __init__(self, parent, expr):
        super(Identifier, self).__init__(parent)

        self.identifier = expr if type(expr) is str else "".join(expr.children)

    def get_fully_qualified_name(self):
        return self.identifier

    def add_to_scope(self):
        self.get_scope().add(self, self.get_parent())

    def add_to_parent_scope(self):
        self.get_scope().get_parent_scope().add(self, self.get_parent())

    def to_c(self):
        return "{id}".format(id=self.identifier)

    def __repr__(self):
        return "ID: {id}".format(id=self.identifier)

    def __str__(self):
        return '`{id}`'.format(id=self.identifier)