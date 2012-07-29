import sys
#  sys.path.append("./syntax")

import antlr3
from batch.syntax.BatchScriptLexer import BatchScriptLexer
from batch.syntax.BatchScriptParser import BatchScriptParser
from Helper import *

class Service :
    
    def __init__(self, root) :
        self.root = root

    def serve(self, script) :
        char_stream = antlr3.ANTLRStringStream(script)

        print "parsing..."
        lexer = BatchScriptLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = BatchScriptParser(tokens)

        print "have script..."
        program = parser.main()
        print str(program)
        out = {}
        program.interp(out, Env('ROOT', self.root, None))
        return out

