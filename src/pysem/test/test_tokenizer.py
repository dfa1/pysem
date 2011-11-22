from unittest import TestCase
from tokenizer import tokenize

class TokenizerTest(TestCase):
    
    def test_empty(self):
        self.assertEqual(("END", None), next(tokenize("")))

    def test_number(self):
        self.assertEqual(("NUMBER", "0"), next(tokenize("0")))
        
    def test_plus(self):
        self.assertEqual(("+", None), next(tokenize("+")))

    def test_minus(self):
        self.assertEqual(("-", None), next(tokenize("-")))

    def test_slash(self):
        self.assertEqual(("*", None), next(tokenize("*")))

    def test_slash(self):
        self.assertEqual(("/", None), next(tokenize("/")))

    def test_lbracket(self):
        self.assertEqual(("[", None), next(tokenize("[")))

    def test_rbracket(self):
        self.assertEqual(("]", None), next(tokenize("]")))

    def test_name(self):
        self.assertEqual(("NAME", "foo"), next(tokenize("foo")))

    def test_string(self):
        self.assertEqual(("STRING", "foo 123!"), next(tokenize("\"foo 123!\"")))

    def test_end_is_the_last_token(self):
        for last in tokenize("foo"): pass
        self.assertEqual(("END", None), last)

    def test_unknown_token_leads_to_syntax_error(self):
        with self.assertRaises(SyntaxError):
            next(tokenize("%%"))

