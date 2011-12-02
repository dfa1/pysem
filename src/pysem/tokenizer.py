from re import compile

def tokenize(line):
    operators = [ '+', '-', '*', '/', '[', ']', ',']
    regexp = compile("\s*(?:(\d+)|(\w+)|\"(.*)\"|(.+))")
    for number, name, string, operator in regexp.findall(line):
        if number:
            yield ("NUMBER", number)
        elif name:
            yield ("NAME", name)
        elif string:
            yield ("STRING", string)
        elif operator in operators:
            yield (operator, None)
        else:
            raise SyntaxError("unknown token '{}'".format(operator))
    yield ("END", None)
