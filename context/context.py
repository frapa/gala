import scope

class Context(object):
    def __init__(self, parent_ctx=None):
        self.parent_ctx = parent_ctx

        self.data = dict(parent_ctx.data) if parent_ctx is not None else {}

        if parent_ctx is None:
            self.scope = scope.Scope()
        else:
            self.scope = parent_ctx.get_scope()

    def sub_scope(self):
        self.scope = scope.Scope(self.scope)

    def get(self, key):
        return self.data[key]

    def set(self, key, val):
        self.data[key] = val

    def get_scope(self):
        return self.scope