from unittest import TestCase
from combinators import *

class LiteralTest(TestCase):
    
    def test_literal_consume_only_the_match(self):
        literal = Literal("a")
        self.assertEqual("bc", literal("abc"))

    def test_literal_throws_when_not_match(self):
        with self.assertRaises(SyntaxError):
            literal = Literal("a")
            literal("b")


class RegexpTest(TestCase):
    
    def test_regexp_consume_only_the_match(self):
        parser = Regexp("a+")
        self.assertEqual("b", parser("aaaab"))

    def test_regexp_throws_when_not_match(self):
        with self.assertRaises(SyntaxError):
            parser  = Regexp("a+")
            parser("b")


class SequenceTest(TestCase):

    def test_sequence_consume(self):
        sequence = Sequence(Literal("a"), Literal("b"))
        self.assertEqual("c", sequence("abc"))

    def test_sequence_throws_when_not_match(self):
        with self.assertRaises(SyntaxError):
            sequence = Sequence(Literal("a"), Literal("b"))
            sequence("aa")
        

class OptionalTest(TestCase):

    def test_optional_consume(self):
        optional = Optional(Literal("a"))
        self.assertEqual("b", optional("ab"))

    def test_sequence_do_nothing_when_not_match(self):
        optional = Optional(Literal("b"))
        self.assertEqual("a", optional("a"))


class OrTest(TestCase):
    
    parser = Or(Literal("a"), Literal("b"))

    def test_consume_first_parser(self):
        self.assertEqual("", self.parser("a"))

    def test_consume_latter_parser(self):
        self.assertEqual("", self.parser("b"))

    def test_throws(self):
        with self.assertRaises(SyntaxError): 
            self.parser("c")


class OneOrMoreTest(TestCase):

    def test_can_consume_once(self):
        parser = OneOrMore(Literal("a"))    
        self.assertEqual("", parser("a"))

    def test_can_consume_twice(self):
        parser = OneOrMore(Literal("a"))    
        self.assertEqual("b", parser("aab"))

    def test_throws(self):
        with self.assertRaises(SyntaxError): 
            oneOrMore = OneOrMore(Literal("a"))    
            oneOrMore("c")


class ZeroOrMoreTest(TestCase):
    
    def test_can_consume_nothing(self):
        parser = ZeroOrMore(Literal("a"))    
        self.assertEqual("b", parser("b"))

    def test_can_consume_once(self):
        parser = ZeroOrMore(Literal("a"))    
        self.assertEqual("", parser("a"))

    def test_can_consume_twice(self):
        parser = ZeroOrMore(Literal("a"))    
        self.assertEqual("b", parser("aab"))


class CombinatorTest(TestCase):

    def test_or_operator(self):
        combinator = Literal("a") | Literal("b")
        self.assertEqual("", combinator("a"))

    def test_sequence_operator(self):
        combinator = Literal("a") >> Literal("b")
        self.assertEqual("c", combinator("abc"))

