from re import compile

TOKENS = compile("\s*(?:(\d+)|(.))")

def tokenize(line):
    for number, operator in TOKENS.findall(line):
        if number:
            yield literal_token(int(number))
        elif operator == '+':
            yield add_token()
        else:
            raise SyntaxError("unknown operator")
    yield end_token()
       
class literal_token:
    lbp = 1
    def __init__(self, value):
        self.value = value
    def nud(self):  
        return self.value
    def __str__(self): 
        return "Literal({})".format(self.value)

class add_token:
    lbp = 10
    def led(self, tokens, left):
        right = expression(tokens, 10)
        return left + right
    def __str__(self):
        return "Plus({},{})".format("left", "right")

class end_token:
    lbp = 0
    def led(self, tokens, left):
        return left
    def __str__(self):
        return "End()"
 
def expression(tokens, rbp = 0):
    """Pratt's algorithm"""
    token = next(tokens)
    print("token is " + str(token))
    left = token.nud()
        
    while rbp < token.lbp:
        token = next(tokens)
        print("token is " + str(token))
        
        left = token.led(tokens, left)
        print("left is {}".format(left))

    return left


def parse(line):
    return expression(tokenize(line))
