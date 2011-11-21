def rule(f):  
    def traced(self, *args, **kwargs):
        print("BEFORE '{}': current = '{}', tokens = {}".format(f.__name__, self.current, self.tokens))
        result = f(self, *args, **kwargs)
        print("AFTER  '{}': current = {}, tokens = {}".format(f.__name__, self.current, self.tokens))
        return result
    return traced

        
class ParseException(BaseException):
    pass

class Parser(object):

    def next(self):
        if len(self.tokens) < 1: 
            return
        self.current = self.tokens.pop(0)

    @rule
    def factor(self):
        if self.current == "number":
            self.next()
        else:
            raise ParseException("expecting 'number', not " + self.current)

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
        if len(self.tokens) < 1:
            raise ParseException("empty input")
        self.next()
        self.expression()
        if len(self.tokens) > 0:
            raise ParseException("tokens at end of input", self.tokens)
    
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
        raise ParseException("not a valid statement", self.current)


