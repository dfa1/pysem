from tokenizer import tokenize
class literal_token:
    lbp = 1
    def __init__(self, value):
        self.value = value
    def nud(self):  
        return self
    def __str__(self): 
        return "Literal({})".format(self.value)

class add_token:
    lbp = 10
    def led(self, tokens, left):
        self.right = expression(tokens, 10)
        self.left = left
        return self
    def __str__(self):
        return "Plus({},{})".format(self.left, self.right)

class end_token:
    lbp = 0
    def led(self, tokens, left):
        self.left = left
        return self
    def __str__(self):
        return "End({})".format(self.left)
 
def expression(tokens, rbp = 0):
    """Pratt's algorithm

    nud is null denotation for tokens that appears to the beginning of a rule
    led is left denotation when it appears in the construct
    lbp is the binding power (precedence)
    """
    token = next(tokens)
    left = token.nud()
    while rbp < token.lbp:
        token = next(tokens)
        left = token.led(tokens, left)
    return left

def parse(line):
    return expression(tokenize(line))

def evaluate(node):
    if hasattr(node, 'left'):
        left = evaluate(node.left) 

        if hasattr(node, 'right'):
            left += evaluate(node.right)

        return left 

    if hasattr(node, 'value'):
        return int(node.value)
    raise Error("aoh")

            

def test_eval(self):
    self.assertEqual(3, evaluate(parse("1+2")))
    
def test_eval2(self):
    self.assertEqual(6, evaluate(parse("1+2+3")))
