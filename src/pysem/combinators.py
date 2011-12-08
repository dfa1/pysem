import re

class Combinator(object):

    def __rshift__(self, other):
        return Sequence(self, other)

    def __or__(self, other):
        return Or(self, other)

    def action(self, context=None):
        pass


class Empty(Combinator):

    def __call__(self, stream):
        return stream

def escape(string):
    return repr(string)[1:-1]

class Literal(Combinator):
    
    def __init__(self, literal):
        self.literal = literal 
        self.literal_len = len(literal)

    def __call__(self, stream):
        prefix = stream[:self.literal_len]
        if prefix == self.literal:
            return stream[self.literal_len:]
        else:
            raise SyntaxError("expecting '{}', got '{}'".format(escape(self.literal), escape(stream)))

    def __str__(self):
        return "{}".format(escape(self.literal))


class Regexp(Combinator):

    def __init__(self, pattern):
        self.pattern = pattern
        self.regexp = re.compile(self.pattern)

    def __call__(self, stream):
        match = self.regexp.search(stream)
        if match is not None:
            if match.start() == 0:
                return stream[match.end():]
        
        raise SyntaxError("expecting match for '{}', got '{}'".format(self.pattern, stream)) 

    def __str__(self):
        return "/{}/".format(escape(self.pattern))


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
        except SyntaxError:
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
        except SyntaxError:
            try:
                return self.b(stream)
            except SyntaxError:
                raise SyntaxError("expecting '{}' or '{}', got '{}'".format(self.a, self.b, stream))

    def __str__(self):
        return "{}|{}".format(self.a, self.b)


class OneOrMore(Combinator):

    def __init__(self, parser):
        self.parser = parser

    def __call__(self, stream):
        stream = self.parser(stream)
        return self._advance(stream)

    def _advance(self, stream):
        try:
            return self._advance(self.parser(stream))
        except SyntaxError:
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
        except SyntaxError:
            return stream

    def __str__(self):
        return "{}*".format(self.parser)
        
