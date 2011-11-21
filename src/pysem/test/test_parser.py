from unittest import TestCase
from parser import *

class ParserTest(TestCase):

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




