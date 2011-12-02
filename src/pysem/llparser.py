class literal:
    def __init__(self, value):
        self.value = value

    def __or__(self, rule):
        self.choice = rule
        return self

    def __rshift__(self, rule):
        self.sequence = rule
        return self
    
    def __repr__(self):
        if getattr(self, 'choice', None):
            return "'{0}' | {1}".format(self.value, repr(self.choice))
        elif getattr(self, 'sequence', None):
            return "'{0}' {1}".format(self.value, repr(self.sequence))
        else:
            return "'{0}'".format(self.value)



term = literal('pippo') 
term_list = term | term_list

print(repr(term_list))
