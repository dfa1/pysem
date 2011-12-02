class Empty(object):

    def parse(self, stream):
        return stream


class Combinator(object):
    
    def __rshift__(self, other):
        return Sequence(self, other)

    def __or__(self, other):
        return Or(self, other)


class Literal(Combinator):
    
    def __init__(self, literal):
        self.literal = literal 
        self.literal_len = len(literal)

    def parse(self, stream):
        prefix = stream[:self.literal_len]
        if prefix == self.literal:
            return stream[self.literal_len:]
        else:
            raise SyntaxError("expecting '{}', got '{}'".format(self.literal,  stream))

    def __str__(self):
        return "<literal '{}'>".format(self.literal)


class Sequence(Combinator):
    
    def __init__(self, *parsers):
        self.parsers = list(parsers)

    def __rshift__(self, parser):
        self.parsers.append(parser)
        return self

    def parse(self, stream):
        for parser in self.parsers:
            stream = parser.parse(stream)
        return stream
        

class Optional(Combinator):

    def __init__(self, parser):
        self.parser = parser

    def parse(self, stream):
        try:
            return self.parser.parse(stream)
        except SyntaxError:
            return stream


class Or(Combinator):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def parse(self, stream):
        try:
            return self.a.parse(stream)
        except SyntaxError:
            try:
                return self.b.parse(stream)
            except SyntaxError:
                raise SyntaxError("expecting '{}' or '{}', got '{}'".format(self.a, self.b, stream))


class OneOrMore(Combinator):

    def __init__(self, parser):
        self.parser = parser

    def parse(self, stream):
        stream = self.parser.parse(stream)
        return self._advance(stream)

    def _advance(self, stream):
        try:
            return self._advance(self.parser.parse(stream))
        except SyntaxError:
            return stream
    

class ZeroOrMore(Combinator):
    
    def __init__(self, parser):
        self.parser = parser

    def parse(self, stream):
        return self._advance(stream)

    def _advance(self, stream):
        try:
            return self._advance(self.parser.parse(stream))
        except SyntaxError:
            return stream
        
