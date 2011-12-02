out = print
out = lambda x: None

def rule(f):  
    def traced(self, *args, **kwargs):
        out("BEFORE '{}': current = '{}', tokens = {}".format(f.__name__, self.current, self.tokens))
        result = f(self, *args, **kwargs)
        out("AFTER  '{}': current = {}, tokens = {}".format(f.__name__, self.current, self.tokens))
        return result
    return traced
        
class Parser(object):

    def next(self):
        self.current = next(self.tokens)

    @rule
    def factor(self):
        if self.current == "number":
            self.next()
        else:
            raise SyntaxError("expecting 'number', not " + self.current)

    @rule
    def term(self):
        self.factor()
        while self.current == "*":
            self.next()
            self.factor()

    @rule
    def expression(self):
        if self.current == "+":
            self.next()
        self.term()
        while self.current == "+":
            self.next()
            self.term()

    def parse(self, tokens):
        self.tokens = tokens
        self.next()
        self.expression()
        try:
            next(self.tokens)
        except StopIteration as e:
            raise SyntaxError("tokens at end of input", self.tokens)
    
    # TODO
    def set(self):
        '''set write, "Enter a value: "'''
        if self.current == 'set':
            self.next()
            self.expression()
            
    def jump(self):
        '''jump 12'''
        pass

    def jumpt(self):
        '''jumpt 10, D[0] > D[1]'''
        pass

    def halt(self):
        '''halt'''
        pass

    def stmt(self):
        if self.current == 'halt':
            self.halt()
        if self.current == 'set':
            self.set()
        raise SyntaxError("not a valid statement", self.current)


