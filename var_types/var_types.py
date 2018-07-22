import context

class Type(context.CodeObject):
    def __init__(self, parent, T):
        super(Type, self).__init__(parent)

        self.T = T if type(T) is str else "".join(T.children)

    def is_function(self):
        return False

    def to_c(self):
        mapping = {
            'int32': 'int32_t',
            'int64': 'int64_t',
            'float32': 'float',
            'float64': 'double',
            'bool': 'bool',
        }

        return mapping[self.T]

    def __eq__(self, other):
        return self.T == other.T

    def __ne__(self, other):
        return self.T != other.T

    def __repr__(self):
        return '{T}'.format(T=self.T)

    def __str__(self):
        return '`{T}`'.format(T=self.T)

class FunType(Type):
    def __init__(self, parent, T):
        self.arg_types = [arg.get_type() for arg in T.get_arguments()]
        self.return_type = T.get_return_type()

        str_T = 'fun ({arg_types}) {ret_type}'.format(
            arg_types=", ".join(map(repr, self.arg_types)),
            ret_type=repr(self.return_type),
        )

        super(FunType, self).__init__(parent, str_T)

    def get_return_type(self):
        return self.return_type

    def is_function(self):
        return True