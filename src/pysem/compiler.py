class Compiler(object):
    
    def __init__(self, tokenizer, parser):
        self.tokenizer = tokenizer
        self.parser = parser
        
    def compile(self, reader):
        tokens = self.tokenizer(reader)
        
