from re import compile

TOKENS = compile("\s*(?:(\d+)|(\w+)|\"(.*)\"|(.+))")

def tokenize(line):
    for number, name, string, operator in TOKENS.findall(line):
        if number:
            yield ("NUMBER", number)
        elif name:
            yield ("NAME", name)
        elif string:
            yield ("STRING", string)
        elif operator == '+':
            yield ("+", None)
        elif operator == '-':
            yield ("-", None)
        else:
            raise SyntaxError("unknown token '{}'".format(operator))
    yield ("END", None)
