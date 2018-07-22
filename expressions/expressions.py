import context
import var_types

class Expression(context.CodeObject):
    def __init__(self, parent):
        super(Expression, self).__init__(parent)

    def get_type(self):
        raise NotImplementedError('get_type is not implemented for {}'.format(str(self.__class__.__name__)))