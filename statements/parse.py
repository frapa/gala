from expr_stmt import *
from return_stmt import *
from defassign import *
from block import *
from if_stmt import *

def parse(parent, stmt):
    kind = stmt.type

    mapping = {
        "return": Return,
        "expr": ExprStatement,
        "definition": Definition,
        "assignment": Assignment,
        "block": Block,
        "if": If,
    }

    if kind in mapping:
        cls = mapping[kind]

        stmt_inst = cls(parent, stmt)

        return stmt_inst
    else:
        print stmt.type
        print stmt.children
        raise Exception("Unsupported statement " + stmt.type)