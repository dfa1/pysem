from unittest import TestCase
from parser import Parser

class ParserTest(TestCase):

    def test_set_writeln(self):
        parser = Parser()
        self.assertEqual("", parser.line("set writeln,123"))

    def test_set_write(self):
        parser = Parser()
        self.assertEqual("", parser.line("set writeln,123"))

    def test_set_read(self):
        parser = Parser()
        self.assertEqual("", parser.line("set 123,read"))
        
