import re

class Combinator(object):

    action = lambda *args: None

    def __rshift__(self, other):
        return Sequence(self, other)

    def __or__(self, other):
        return Or(self, other)

    def __str__(self):
        selfType = type(self).__name__
        raise NotImplementedError("combinator {} must override __str__".format(selfType))


class Empty(Combinator):

    def __call__(self, stream):
        return stream

    def __str__(self):
        return "<EMPTY>"


class Literal(Combinator):
    
    def __init__(self, literal):
        self.literal = literal 
        self.literal_len = len(literal)

    def __call__(self, stream):
        prefix = stream[:self.literal_len]
        if prefix != self.literal:
            raise ParseError(repr(self.literal), repr(stream))
        self.action(Literal, self.literal)
        return stream[self.literal_len:]

    def __str__(self):
        return "{}".format(self.literal)


class Regexp(Combinator):

    def __init__(self, pattern):
        self.pattern = pattern
        self.regexp = re.compile(self.pattern)

    def __call__(self, stream):
        match = self.regexp.search(stream)
        if match is not None and match.start() == 0:
            self.action(Regexp, stream[match.start():match.end()])
            return stream[match.end():]
        raise ParseError(repr("/" + self.pattern + "/"), repr(stream))

    def __str__(self):
        return "/{}/".format(self.pattern)


class Sequence(Combinator):
    
    def __init__(self, *parsers):
        self.parsers = list(parsers)

    def __rshift__(self, parser):
        self.parsers.append(parser)
        return self

    def __call__(self, stream):
        for parser in self.parsers:
            stream = parser(stream)
        return stream

    def __str__(self):
        return "({})".format("".join(map(str, self.parsers)))


class Optional(Combinator):

    def __init__(self, parser):
        self.parser = parser

    def __call__(self, stream):
        try:
            return self.parser(stream)
        except ParseError:
            return stream

    def __str__(self):
        return "{}?".format(str(self.parser))


class Or(Combinator):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, stream):
        try:
            return self.a(stream)
        except ParseError:
            try:
                return self.b(stream)
            except ParseError:
                expected = "{}|{}".format(str(self.a), str(self.b))    
                raise ParseError(expected, stream)

    def __str__(self):
        return "{}|{}".format(str(self.a), str(self.b))


class OneOrMore(Combinator):

    def __init__(self, parser):
        self.parser = parser

    def __call__(self, stream):
        stream = self.parser(stream)
        return self._advance(stream)

    def _advance(self, stream):
        try:
            return self._advance(self.parser(stream))
        except ParseError:
            return stream
    
    def __str__(self):
        return "{}+".format(self.parser)


class ZeroOrMore(Combinator):
    
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, stream):
        return self._advance(stream)

    def _advance(self, stream):
        try:
            return self._advance(self.parser(stream))
        except ParseError:
            return stream

    def __str__(self):
        return "{}*".format(str(self.parser))
        


class ParseError(Exception):

    template = "expected {} got {}"

    def __init__(self, expected, got):
        self.expected = expected
        self.got = got

    def __str__(self):
        return self.template.format(self.expected, self.got)
