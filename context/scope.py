class Scope(object):
    def __init__(self, parent_scope=None):
        self.parent_scope = parent_scope
        self.child_scopes = []

        if parent_scope:
            parent_scope.add_child_scope(self)

        self.identifiers = {}

    def get_child_scopes(self):
        return self.child_scopes

    def add_child_scope(self, scope):
        self.child_scopes.append(scope)

    def get_parent_scope(self):
        return self.parent_scope

    def resolve(self, identifier):
        if identifier.get_fully_qualified_name() in self.identifiers:
            return self.identifiers[identifier.get_fully_qualified_name()]
        elif self.parent_scope is not None:
            return self.parent_scope.resolve(identifier)

        return None

    def add(self, identifier, object):
        self.identifiers[identifier.get_fully_qualified_name()] = object

    def __repr__(self):
        return "SCOPE:\n\t{scope},\n\t{children}".format(
            scope    = self.identifiers.keys(),
            children = '' if self.get_child_scopes() == [] else "\n\t".join(map(str, self.get_child_scopes()))
        )

    def __str__(self):
        return "SCOPE:\n\t{scope},\n\t{children}".format(
            scope    = self.identifiers.keys(),
            children = '' if self.get_child_scopes() == [] else "\n\t".join(map(str, self.get_child_scopes()))
        )