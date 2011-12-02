from unittest import TestCase
from combinators import *

class LiteralTest(TestCase):
    
    def test_literal_consume_only_the_match(self):
        literal = Literal("a")
        self.assertEqual("bc", literal.parse("abc"))

    def test_literal_throws_when_not_match(self):
        with self.assertRaises(SyntaxError):
            literal = Literal("a")
            literal.parse("b")


class SequenceTest(TestCase):

    def test_sequence_consume(self):
        sequence = Sequence(Literal("a"), Literal("b"))
        self.assertEqual("c", sequence.parse("abc"))

    def test_sequence_throws_when_not_match(self):
        with self.assertRaises(SyntaxError):
            sequence = Sequence(Literal("a"), Literal("b"))
            sequence.parse("aa")
        

class OptionalTest(TestCase):

    def test_optional_consume(self):
        optional = Optional(Literal("a"))
        self.assertEqual("b", optional.parse("ab"))

    def test_sequence_do_nothing_when_not_match(self):
        optional = Optional(Literal("b"))
        self.assertEqual("a", optional.parse("a"))


class OrTest(TestCase):
    
    parser = Or(Literal("a"), Literal("b"))

    def test_consume_first_parser(self):
        self.assertEqual("", self.parser.parse("a"))

    def test_consume_latter_parser(self):
        self.assertEqual("", self.parser.parse("b"))

    def test_throws(self):
        with self.assertRaises(SyntaxError): 
            self.parser.parse("c")


class OneOrMoreTest(TestCase):

    def test_can_consume_once(self):
        parser = OneOrMore(Literal("a"))    
        self.assertEqual("", parser.parse("a"))

    def test_can_consume_twice(self):
        parser = OneOrMore(Literal("a"))    
        self.assertEqual("b", parser.parse("aab"))

    def test_throws(self):
        with self.assertRaises(SyntaxError): 
            parser = OneOrMore(Literal("a"))    
            parser.parse("c")


class ZeroOrMoreTest(TestCase):
    
    def test_can_consume_nothing(self):
        parser = ZeroOrMore(Literal("a"))    
        self.assertEqual("b", parser.parse("b"))

    def test_can_consume_once(self):
        parser = ZeroOrMore(Literal("a"))    
        self.assertEqual("", parser.parse("a"))

    def test_can_consume_twice(self):
        parser = ZeroOrMore(Literal("a"))    
        self.assertEqual("b", parser.parse("aab"))


class DslTest(TestCase):

    def test_can_define_rule(self):
        ab = Literal("a") | Literal("b")
        self.assertEqual("", ab.parse("a"))

    def test_sequence_operator_twice(self):
        a = Literal("a")
        b = Literal("b")
        ab = a >> b
        self.assertEqual("c", ab.parse("abc"))

    def test_sequence_operator_triple(self):
        a = Literal("a")
        b = Literal("b")
        c = Literal("c")
        abc = a >> b >> c
        self.assertEqual("d", abc.parse("abcd"))

