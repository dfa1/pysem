from unittest import TestCase
from tokenizer import tokenize, parse

class TokenizerTest(TestCase):
    
    # def test_number(self):
    #     self.assertEquals(["0", "END"], list(tokenize("0")))

    # def test_plus(self):
    #     self.assertEquals(["+", "END"], list(tokenize("+")))

    def test_parse(self):
        self.assertEquals(3, parse("1+2"))
    def test_parse_cool(self):
        self.assertEquals(6, parse("1+2+3"))
