from combinators import *

class Parser(object):

    SET = Literal("set")
    READ = Literal("read")
    WRITE = Literal("write")
    WRITELN = Literal("writeln")
    READ = Literal("read")
    HALT = Literal("halt")
    INTEGER = Regexp("[0-9]+")
    COMMA = Literal(",")
    D = Literal("D") >> Literal("[") >> INTEGER >> Literal("]")
    atom = INTEGER | D
    mul_expr = atom | atom >> Literal("*") >> atom
    add_expr = mul_expr | mul_expr >> Literal("+") >> mul_expr
    write = WRITE >> COMMA >> add_expr
    writeln = WRITELN >> COMMA >> add_expr
    read = add_expr >> COMMA >> READ
    set_stmt = Literal("set ") >> (write | writeln | read)
    halt_stmt = HALT
    stmt = set_stmt | halt_stmt
    line = stmt >> Literal("\n")

    def line(self, stream):
        res = self.stmt(stream)
        if res != "":
            raise SyntaxError("not all input consumed: '{}'".format(res))
        return res
