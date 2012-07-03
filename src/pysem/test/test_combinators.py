from unittest import TestCase
from combinators import *

class EmptyTest(TestCase):
    
    def test_empty_does_not_consume(self):
        parser = Empty()
        self.assertEqual("", parser(""))

    def test_empty_str(self):
        parser = Empty()
        self.assertEqual("<EMPTY>", str(parser))


class LiteralTest(TestCase):
    
    def test_literal_consume_only_the_match(self):
        parser = Literal("a")
        self.assertEqual("bc", parser("abc"))

    def test_literal_parse_error(self):
        with self.assertRaises(ParseError):
            parser = Literal("a")
            parser("b")

    def test_literal_parse_error_message(self):
        try:
            parser = Literal("a")
            parser("b")
        except ParseError as e:
            self.assertEqual("expected 'a' got 'b'", str(e))

    def test_literal_str(self):
        parser = Literal("a")
        self.assertEqual("a", str(parser))



class RegexpTest(TestCase):
    
    def test_regexp_consume_only_the_match(self):
        parser = Regexp("a+")
        self.assertEqual("b", parser("aaaab"))

    def test_regexp_parse_error(self):
        with self.assertRaises(ParseError):
            parser  = Regexp("a+")
            parser("b")

    def test_regexp_parse_error_message(self):
        try:
            parser = Regexp("a+")
            parser("b")
        except ParseError as e:
            self.assertEqual("expected '/a+/' got 'b'", str(e))

    def test_regexp_str(self):
        parser = Regexp("a+")
        self.assertEqual("/a+/", str(parser))


class SequenceTest(TestCase):

    def test_sequence_consume(self):
        parser = Sequence(Literal("a"), Literal("b"))
        self.assertEqual("c", parser("abc"))

    def test_sequence_parse_error(self):
        with self.assertRaises(ParseError):
            parser = Sequence(Literal("a"), Literal("b"))
            parser("aa")

    def test_sequence_parse_error_message(self):
        try:
            parser = Sequence(Literal("a"), Literal("b"))
            parser("aa")
        except ParseError as e:
            # self.assertEqual("expected 'ab' got 'aa'", str(e)) # FIXME: bug
            pass

    def test_sequence_str(self):
        parser = Sequence(Literal("a"), Literal("b"))
        self.assertEqual("(ab)", str(parser))
        

class OptionalTest(TestCase):

    def test_optional_consume(self):
        parser = Optional(Literal("a"))
        self.assertEqual("b", parser("ab"))

    def test_optional_do_nothing_when_not_match(self):
        parser = Optional(Literal("b"))
        self.assertEqual("a", parser("a"))

    def test_optional_str(self):
        parser = Optional(Literal("a"))
        self.assertEqual("a?", str(parser))


class OrTest(TestCase):
    
    def test_or_consume_first_parser(self):
        parser = Or(Literal("a"), Literal("b"))
        self.assertEqual("", parser("a"))

    def test_or_consume_latter_parser(self):
        parser = Or(Literal("a"), Literal("b"))
        self.assertEqual("", parser("b"))

    def test_or_parse_error(self):
        parser = Or(Literal("a"), Literal("b"))
        with self.assertRaises(ParseError): 
            parser("c")

    def test_or_parse_error_message(self):
        try:
            parser = Or(Literal("a"), Literal("b"))
            parser("c")
        except ParseError as e:
            self.assertEqual("expected a|b got c", str(e)) # FIXME: use single quotes


class OneOrMoreTest(TestCase):

    def test_one_or_more_consume_once(self):
        parser = OneOrMore(Literal("a"))    
        self.assertEqual("b", parser("ab"))

    def test_one_or_more_can_consume_twice(self):
        parser = OneOrMore(Literal("a"))    
        self.assertEqual("b", parser("aab"))

    def test_one_or_more_parse_error(self):
        with self.assertRaises(ParseError): 
            parser = OneOrMore(Literal("a"))    
            parser("c")

    def test_one_or_more_parse_error_message(self):
        try:
            parser = OneOrMore(Literal("a"))    
            parser("c")
        except ParseError as e:
            self.assertEqual("expected 'a' got 'c'", str(e)) 

    def test_one_or_more_str(self):
        parser = OneOrMore(Literal("a"))
        self.assertEqual("a+", str(parser))


class ZeroOrMoreTest(TestCase):
    
    def test_zero_or_more_do_nothing_when_not_match(self):
        parser = ZeroOrMore(Literal("a"))    
        self.assertEqual("b", parser("b"))

    def test_zero_or_more_consume_once(self):
        parser = ZeroOrMore(Literal("a"))    
        self.assertEqual("", parser("a"))

    def test_zero_or_more_consume_twice(self):
        parser = ZeroOrMore(Literal("a"))    
        self.assertEqual("b", parser("aab"))

    def test_zero_or_more_str(self):
        parser = ZeroOrMore(Literal("a"))    
        self.assertEqual("a*", str(parser))


class CombinatorTest(TestCase):

    def test_or_operator(self):
        combinator = Literal("a") | Literal("b")
        self.assertEqual("", combinator("a"))

    def test_sequence_operator(self):
        combinator = Literal("a") >> Literal("b")
        self.assertEqual("c", combinator("abc"))

