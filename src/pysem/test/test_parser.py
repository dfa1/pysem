from unittest import TestCase
from parser import Parser

class ParserTest(TestCase):

    def test_refuse_empty_input(self):
        parser = Parser()
        self.assertRaises(SyntaxError, parser.parse, [])

    def test_refuse_non_number(self):
        parser = Parser()
        self.assertRaises(SyntaxError, parser.parse, iter(["non_number"]))

    def test_accepts_number(self):
        parser = Parser()
        parser.parse(iter(["number"]))

    def test_accepts_one_additive_expr(self):
        parser = Parser()
        parser.parse(iter(["number", "+", "number"]))

    def test_accepts_onemultiplicative_expr(self):
        parser = Parser()
        parser.parse(iter(["number", "*", "number"]))

    def test_accepts_two_additive_exprs(self):
        parser = Parser()
        parser.parse(iter(["number", "+", "number", "+", "number"]))

    def test_accepts_two_multiplicative_exprs(self):
        parser = Parser()
        parser.parse(iter(["number", "*", "number", "*", "number"]))


