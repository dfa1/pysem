from unittest import TestCase
from tokenizer import tokenize, parse, evaluate

class TokenizerTest(TestCase):
    
    # def test_number(self):
    #     self.assertEqual(["0", "END"], list(tokenize("0")))

    # def test_plus(self):
    #     self.assertEqual(["+", "END"], list(tokenize("+")))

    def test_eval(self):
        self.assertEqual(3, evaluate(parse("1+2")))

    def test_eval2(self):
        self.assertEqual(6, evaluate(parse("1+2+3")))
