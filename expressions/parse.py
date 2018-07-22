from strings import *
from numbers import *
from booleans import *
from identifiers import *
from mathematics import *
from logic import *
from objects import *

def parse(parent, expr):
    # normalize expressions
    if expr.type == 'expr':
        expr = expr.children[0]

    kind = expr.type

    mapping = {
        'decimal': Decimal,
        'binary': Binary,
        'octal': Octal,
        'hex': Hex,
        'string': String,
        'boolean': Boolean,

        'identifier': Identifier,

        'sum': Sum,
        'prod': Prod,
        'mod': Mod,
        'power': Power,
        'negation': Negation,

        'and': And,
        'or': Or,
        'not': Not,
        'eq': Eq,
        'rel': Rel,
        'bitwise_and': BitwiseOr,
        'bitwise_xor': BitwiseXor,
        'bitwise_or': BitwiseAnd,
        'bitwise_not': BitwiseNot,

        'fun_call': FunCall,
    }

    if kind in mapping:
        cls = mapping[kind]

        expr_inst = cls(parent, expr)

        return expr_inst
    else:
        print(kind)
        print(expr.children)
        raise Exception("Unsupported expression " + kind)
