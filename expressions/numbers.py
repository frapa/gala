import expressions


class Decimal(expressions.Expression):
    def __init__(self, parent, expr):
        super(Decimal, self).__init__(parent)

        self.number = "".join(expr.children)

    def get_type(self):
        return self.get_ctx().get('type')

    def to_c(self):
        return "{number}".format(number=self.number)


class Binary(expressions.Expression):
    def __init__(self, parent, expr):
        super(Binary, self).__init__(parent)

        digits = map(int, reversed(expr.children))
        dec = 0
        for m, d in enumerate(digits):
            dec += d * 2**m

        # convert to oct
        self.number = dec

    def get_type(self):
        return self.get_ctx().get('type')

    def to_c(self):
        return "{number}".format(number=self.number)


class Octal(expressions.Expression):
    def __init__(self, parent, expr):
        super(Octal, self).__init__(parent)

        self.number = "0" + "".join(expr.children)

    def get_type(self):
        return self.get_ctx().get('type')

    def to_c(self):
        return "{number}".format(number=self.number)


class Hex(expressions.Expression):
    def __init__(self, parent, expr):
        super(Hex, self).__init__(parent)

        self.number = "0x" + "".join(expr.children)

    def get_type(self):
        return self.get_ctx().get('type')

    def to_c(self):
        return "{number}".format(number=self.number)