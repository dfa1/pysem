class ParseException(BaseException):
    pass

class Parser(object):

    def next(self):
        if len(self.tokens) < 1: return
            #raise ParseException("No more tokens")
        self.current = self.tokens.pop(0)

    def factor(self):
        if self.current == "number":
            self.next()
        else:
            raise ParseException("expecting 'number', not " + self.current)
            
    def term(self):
        self.factor()
        if self.current == "*":
            self.next()
            self.factor()

    def expression(self):
        if self.current == "+":
            self.next()
        self.term()

        if self.current == "+":
            self.next()
            self.term()

    def set(self):
        '''set write, "Enter a value: "'''
        pass
    
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
        if current == 'halt':
            halt()
        if current == 'set':
            set()
        expect('\n')

    def parse(self, tokens):
        self.tokens = tokens
        if len(self.tokens) < 1:
            raise ParseException("empty input")
        self.next()
        self.expression()
        if len(self.tokens) > 0:
            raise ParseException("tokens at end of input", self.tokens)


