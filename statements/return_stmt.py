import statements
import expressions
import var_types

class Return(statements.Statement):
    def __init__(self, parent, stmt):
        super(Return, self).__init__(parent)

        fun = self.closest('Function')

        # be sure we are inside function
        if fun is None:
            raise Exception('Return must be inside a function')

        # mark as type as to allow proper casts
        self.get_ctx().set('type', fun.get_return_type())

        self.expr = expressions.parse(self, stmt.children[0])

        # check if type if correct
        if fun.get_return_type() != self.expr.get_type():
            raise Exception(
                'Function {fun} returns {fun_ret_type} but return '
                'statement is of type {ret_ret_type}'
                .format(
                    fun          = fun,
                    fun_ret_type = fun.get_return_type(),
                    ret_ret_type = self.expr.get_type(),
                )
            )

    def to_c(self):
        return 'return {expr};'.format(expr=self.expr.to_c())