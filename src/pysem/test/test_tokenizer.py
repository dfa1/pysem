from unittest import TestCase
from tokenizer import tokenize

class TokenizerTest(TestCase):
    
    def test_number(self):
        self.assertEqual([("NUMBER", "0"), ("END", None)], list(tokenize("0")))
        
    def test_plus(self):
        self.assertEqual([("+", None), ("END", None)], list(tokenize("+")))

