from re import compile

TOKENS = compile("\s*(?:(\d+)|(.))")

def tokenize(line):
    for number, operator in TOKENS.findall(line):
        if number:
            yield ("NUMBER", number)
        elif operator == '+':
            yield ("+", None)
        else:
            raise SyntaxError("unknown operator")
    yield ("END", None)
