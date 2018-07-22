import context
import var_types

class Expression(context.CodeObject):
    def __init__(self, parent):
        super(Expression, self).__init__(parent)

    def get_type(self):
        return self.get_ctx().get('type')