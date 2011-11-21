class ParseException(BaseException):
    pass

class Parser(object):

    def next(self):
        if len(self.tokens) < 1:
            raise ParseException("No more tokens")
        self.current = self.tokens.pop(0)

    def factor(self):
        if self.current == "number":
            pass
        else:
            raise ParseException("expecting 'number', not '{}'".format(self.current))
            
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
        self.next()
        self.expression()

import unittest

class ParserTest(unittest.TestCase):

    def test_refuse_empty_input(self):
        parser = Parser()
        self.assertRaises(ParseException, parser.parse, [])

    def test_refuse_non_number(self):
        parser = Parser()
        self.assertRaises(ParseException, parser.parse, ["non_number"])

    def test_accepts_number(self):
        parser = Parser()
        parser.parse(["number"]) 

    def test_accepts_additive(self):
        parser = Parser()
        parser.parse(["number", "+", "number"])

    def test_accepts_multiplicative(self):
        parser = Parser()
        parser.parse(["number", "*", "number"])


if __name__ == '__main__':
    unittest.main()

