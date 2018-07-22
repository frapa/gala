import context

class CodeObject(object):
    def __init__(self, parent):
        self.parent = parent

        if parent is None:
            self.ctx = context.Context()
        else:
            self.ctx = context.Context(parent.get_ctx())

    def get_parent(self):
        return self.parent

    def get_ctx(self):
        return self.ctx

    def get_scope(self):
        return self.ctx.get_scope()

    # a la jQuery
    def closest(self, name):
        if self.__class__.__name__ == name:
            return self
        elif self.parent is not None:
            return self.parent.closest(name)

        return None