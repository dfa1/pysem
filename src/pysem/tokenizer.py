from __future__ import print_function
import re

class Token(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __str__(self):
        return "Token(name={}, value={})".format(self.name, repr(self.value))

class Tokenizer(object):

    def __init__(self, tokens):
        self.regexp = '|'.join('(?P<%s>%s)' % token for token in tokens)

    def tokenize(self, stream):
        get_token = re.compile(self.regexp).match
        pos = 0
        m = get_token(stream)
        while m is not None:
            name = m.lastgroup
            value = m.group(name)
            yield Token(name, value)
            pos = m.end()
            m = get_token(stream, pos)
        if pos != len(stream):
            raise RuntimeError("Unexpected character '{}' at pos {}".format(stream[pos], pos))
        
if __name__ == '__main__':
    import sys
    tokens = [
        ('NUMBER',  '\d+(\.\d*)?'), 
        ('SET',     'set'),   
        ('WRITE',   'write'),   
        ('PLUS',    '\+'),   
        ('COMMA',   '\,'),   
        ('NEWLINE', '\n'),   
        ('SKIP',    '[ \t]'),     
    ]
    tokenizer = Tokenizer(tokens)
    for token in tokenizer.tokenize(sys.argv[1]):
        print(token)
