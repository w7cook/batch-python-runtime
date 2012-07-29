# $ANTLR 3.1.1 /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g 2012-07-28 22:25:10

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
from batch.Expressions import *
from datetime import date



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=8
EXPONENT=21
T__29=29
T__28=28
OCTAL_ESC=27
FOR=7
FLOAT=17
ID=15
EOF=-1
IF=4
ESC_SEQ=24
THEN=5
IN=13
VAR=10
DIGIT=19
COMMENT=22
T__42=42
T__43=43
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
T__45=45
T__48=48
UNICODE_ESC=26
ELSE=6
HEX_DIGIT=25
INT=16
TRUE=11
ALPHA=20
T__30=30
T__31=31
T__32=32
WS=23
T__33=33
T__34=34
T__35=35
T__36=36
T__37=37
T__38=38
T__39=39
DATE=14
FALSE=12
OUTPUT=9
STRING=18

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "IF", "THEN", "ELSE", "FOR", "FUNCTION", "OUTPUT", "VAR", "TRUE", "FALSE", "IN", "DATE", "ID", "INT", "FLOAT", "STRING", "DIGIT", "ALPHA", "EXPONENT", "COMMENT", "WS", "ESC_SEQ", "HEX_DIGIT", "UNICODE_ESC", "OCTAL_ESC", "';'", "'='", "'{'", "'}'", "'('", "')'", "'||'", "'&&'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'+'", "'-'", "'*'", "'/'", "'!'", "','", "'.'"
]




class BatchScriptParser(Parser):
    grammarFileName = "/Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g"
    antlr_version = version_str_to_tuple("3.1.1")
    antlr_version_str = "3.1.1"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)







                


        



    # $ANTLR start "main"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:26:1: main returns [value] : e= statements EOF ;
    def main(self, ):

        value = None

        e = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:27:5: (e= statements EOF )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:27:9: e= statements EOF
                pass 
                self._state.following.append(self.FOLLOW_statements_in_main212)
                e = self.statements()

                self._state.following.pop()
                #action start
                value = e
                #action end
                self.match(self.input, EOF, self.FOLLOW_EOF_in_main216)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "main"


    # $ANTLR start "statements"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:30:1: statements returns [value] : (e= statement ( ';' (es= statements )? )? | VAR x= ID '=' e= expr ';' b= statements );
    def statements(self, ):

        value = None

        x = None
        e = None

        es = None

        b = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:31:5: (e= statement ( ';' (es= statements )? )? | VAR x= ID '=' e= expr ';' b= statements )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == IF or (FOR <= LA3_0 <= OUTPUT) or (TRUE <= LA3_0 <= FALSE) or (DATE <= LA3_0 <= STRING) or LA3_0 == 32 or LA3_0 == 46) :
                    alt3 = 1
                elif (LA3_0 == VAR) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:31:9: e= statement ( ';' (es= statements )? )?
                    pass 
                    self._state.following.append(self.FOLLOW_statement_in_statements241)
                    e = self.statement()

                    self._state.following.pop()
                    #action start
                    value=e
                    #action end
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:32:9: ( ';' (es= statements )? )?
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 28) :
                        alt2 = 1
                    if alt2 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:32:11: ';' (es= statements )?
                        pass 
                        self.match(self.input, 28, self.FOLLOW_28_in_statements275)
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:33:13: (es= statements )?
                        alt1 = 2
                        LA1_0 = self.input.LA(1)

                        if (LA1_0 == IF or (FOR <= LA1_0 <= FALSE) or (DATE <= LA1_0 <= STRING) or LA1_0 == 32 or LA1_0 == 46) :
                            alt1 = 1
                        if alt1 == 1:
                            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:33:14: es= statements
                            pass 
                            self._state.following.append(self.FOLLOW_statements_in_statements292)
                            es = self.statements()

                            self._state.following.pop()
                            #action start
                            value = Seq(value,es)
                            #action end








                elif alt3 == 2:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:36:9: VAR x= ID '=' e= expr ';' b= statements
                    pass 
                    self.match(self.input, VAR, self.FOLLOW_VAR_in_statements348)
                    x=self.match(self.input, ID, self.FOLLOW_ID_in_statements352)
                    self.match(self.input, 29, self.FOLLOW_29_in_statements354)
                    self._state.following.append(self.FOLLOW_expr_in_statements358)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 28, self.FOLLOW_28_in_statements360)
                    self._state.following.append(self.FOLLOW_statements_in_statements364)
                    b = self.statements()

                    self._state.following.pop()
                    #action start
                    value = Let(x.getText(),e,b)
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "statements"


    # $ANTLR start "block"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:39:1: block returns [Expression value] : '{' e= statements '}' ;
    def block(self, ):

        value = None

        e = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:40:5: ( '{' e= statements '}' )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:40:7: '{' e= statements '}'
                pass 
                self.match(self.input, 30, self.FOLLOW_30_in_block387)
                self._state.following.append(self.FOLLOW_statements_in_block391)
                e = self.statements()

                self._state.following.pop()
                self.match(self.input, 31, self.FOLLOW_31_in_block393)
                #action start
                value =  e
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "block"


    # $ANTLR start "statement"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:43:1: statement returns [value] : ( FOR '(' x= ID IN e= expr ')' b= block | e= expr );
    def statement(self, ):

        value = None

        x = None
        e = None

        b = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:44:5: ( FOR '(' x= ID IN e= expr ')' b= block | e= expr )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == FOR) :
                    alt4 = 1
                elif (LA4_0 == IF or (FUNCTION <= LA4_0 <= OUTPUT) or (TRUE <= LA4_0 <= FALSE) or (DATE <= LA4_0 <= STRING) or LA4_0 == 32 or LA4_0 == 46) :
                    alt4 = 2
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:44:9: FOR '(' x= ID IN e= expr ')' b= block
                    pass 
                    self.match(self.input, FOR, self.FOLLOW_FOR_in_statement420)
                    self.match(self.input, 32, self.FOLLOW_32_in_statement422)
                    x=self.match(self.input, ID, self.FOLLOW_ID_in_statement426)
                    self.match(self.input, IN, self.FOLLOW_IN_in_statement428)
                    self._state.following.append(self.FOLLOW_expr_in_statement432)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 33, self.FOLLOW_33_in_statement434)
                    self._state.following.append(self.FOLLOW_block_in_statement438)
                    b = self.block()

                    self._state.following.pop()
                    #action start
                    value = For(x.getText(),e,b)
                    #action end


                elif alt4 == 2:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:45:9: e= expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_statement454)
                    e = self.expr()

                    self._state.following.pop()
                    #action start
                    value = e
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "statement"


    # $ANTLR start "expr"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:48:1: expr returns [value] : ( FUNCTION '(' x= ID ')' e= block | a= orexpr );
    def expr(self, ):

        value = None

        x = None
        e = None

        a = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:49:5: ( FUNCTION '(' x= ID ')' e= block | a= orexpr )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == FUNCTION) :
                    alt5 = 1
                elif (LA5_0 == IF or LA5_0 == OUTPUT or (TRUE <= LA5_0 <= FALSE) or (DATE <= LA5_0 <= STRING) or LA5_0 == 32 or LA5_0 == 46) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:49:9: FUNCTION '(' x= ID ')' e= block
                    pass 
                    self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_expr508)
                    self.match(self.input, 32, self.FOLLOW_32_in_expr510)
                    x=self.match(self.input, ID, self.FOLLOW_ID_in_expr514)
                    self.match(self.input, 33, self.FOLLOW_33_in_expr516)
                    self._state.following.append(self.FOLLOW_block_in_expr520)
                    e = self.block()

                    self._state.following.pop()
                    #action start
                    value = Fun(x.getText(),e)
                    #action end


                elif alt5 == 2:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:50:9: a= orexpr
                    pass 
                    self._state.following.append(self.FOLLOW_orexpr_in_expr541)
                    a = self.orexpr()

                    self._state.following.pop()
                    #action start
                    value = a
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "expr"


    # $ANTLR start "orexpr"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:53:1: orexpr returns [value] : a= andexpr ( '||' b= andexpr )* ;
    def orexpr(self, ):

        value = None

        a = None

        b = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:54:5: (a= andexpr ( '||' b= andexpr )* )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:54:9: a= andexpr ( '||' b= andexpr )*
                pass 
                self._state.following.append(self.FOLLOW_andexpr_in_orexpr591)
                a = self.andexpr()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:55:9: ( '||' b= andexpr )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == 34) :
                        alt6 = 1


                    if alt6 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:55:11: '||' b= andexpr
                        pass 
                        self.match(self.input, 34, self.FOLLOW_34_in_orexpr615)
                        self._state.following.append(self.FOLLOW_andexpr_in_orexpr619)
                        b = self.andexpr()

                        self._state.following.pop()
                        #action start
                        value = Or(value,b)
                        #action end


                    else:
                        break #loop6






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "orexpr"


    # $ANTLR start "andexpr"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:59:1: andexpr returns [value] : a= comp ( '&&' b= comp )* ;
    def andexpr(self, ):

        value = None

        a = None

        b = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:60:5: (a= comp ( '&&' b= comp )* )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:60:9: a= comp ( '&&' b= comp )*
                pass 
                self._state.following.append(self.FOLLOW_comp_in_andexpr660)
                a = self.comp()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:61:9: ( '&&' b= comp )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 35) :
                        alt7 = 1


                    if alt7 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:61:11: '&&' b= comp
                        pass 
                        self.match(self.input, 35, self.FOLLOW_35_in_andexpr684)
                        self._state.following.append(self.FOLLOW_comp_in_andexpr688)
                        b = self.comp()

                        self._state.following.pop()
                        #action start
                        value = And(value,b)
                        #action end


                    else:
                        break #loop7






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "andexpr"


    # $ANTLR start "comp"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:65:1: comp returns [value] : a= term (op= compop b= term )* ;
    def comp(self, ):

        value = None

        a = None

        op = None

        b = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:66:5: (a= term (op= compop b= term )* )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:66:9: a= term (op= compop b= term )*
                pass 
                self._state.following.append(self.FOLLOW_term_in_comp729)
                a = self.term()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:67:9: (op= compop b= term )*
                while True: #loop8
                    alt8 = 2
                    LA8 = self.input.LA(1)
                    if LA8 == 36:
                        alt8 = 1
                    elif LA8 == 37:
                        alt8 = 1
                    elif LA8 == 38:
                        alt8 = 1
                    elif LA8 == 39:
                        alt8 = 1
                    elif LA8 == 40:
                        alt8 = 1
                    elif LA8 == 41:
                        alt8 = 1

                    if alt8 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:67:11: op= compop b= term
                        pass 
                        self._state.following.append(self.FOLLOW_compop_in_comp758)
                        op = self.compop()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_term_in_comp762)
                        b = self.term()

                        self._state.following.pop()
                        #action start
                        value = BinOp(op,value,b)
                        #action end


                    else:
                        break #loop8






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "comp"


    # $ANTLR start "compop"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:71:1: compop returns [op] : ( '==' | '!=' | '<' | '<=' | '>' | '>=' );
    def compop(self, ):

        op = None

        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:72:5: ( '==' | '!=' | '<' | '<=' | '>' | '>=' )
                alt9 = 6
                LA9 = self.input.LA(1)
                if LA9 == 36:
                    alt9 = 1
                elif LA9 == 37:
                    alt9 = 2
                elif LA9 == 38:
                    alt9 = 3
                elif LA9 == 39:
                    alt9 = 4
                elif LA9 == 40:
                    alt9 = 5
                elif LA9 == 41:
                    alt9 = 6
                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae

                if alt9 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:72:9: '=='
                    pass 
                    self.match(self.input, 36, self.FOLLOW_36_in_compop799)
                    #action start
                    op = '=='
                    #action end


                elif alt9 == 2:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:73:9: '!='
                    pass 
                    self.match(self.input, 37, self.FOLLOW_37_in_compop814)
                    #action start
                    op = '!='
                    #action end


                elif alt9 == 3:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:74:9: '<'
                    pass 
                    self.match(self.input, 38, self.FOLLOW_38_in_compop829)
                    #action start
                    op = '<'
                    #action end


                elif alt9 == 4:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:75:9: '<='
                    pass 
                    self.match(self.input, 39, self.FOLLOW_39_in_compop845)
                    #action start
                    op = '<='
                    #action end


                elif alt9 == 5:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:76:9: '>'
                    pass 
                    self.match(self.input, 40, self.FOLLOW_40_in_compop860)
                    #action start
                    op = '>'
                    #action end


                elif alt9 == 6:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:77:9: '>='
                    pass 
                    self.match(self.input, 41, self.FOLLOW_41_in_compop876)
                    #action start
                    op = '>='
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return op

    # $ANTLR end "compop"


    # $ANTLR start "term"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:80:1: term returns [value] : a= factor (op= addop b= factor )* ;
    def term(self, ):

        value = None

        a = None

        op = None

        b = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:81:5: (a= factor (op= addop b= factor )* )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:81:9: a= factor (op= addop b= factor )*
                pass 
                self._state.following.append(self.FOLLOW_factor_in_term906)
                a = self.factor()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:82:9: (op= addop b= factor )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 42) :
                        alt10 = 1
                    elif (LA10_0 == 43) :
                        alt10 = 1


                    if alt10 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:82:11: op= addop b= factor
                        pass 
                        self._state.following.append(self.FOLLOW_addop_in_term933)
                        op = self.addop()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_factor_in_term937)
                        b = self.factor()

                        self._state.following.pop()
                        #action start
                        value = BinOp(op,value,b)
                        #action end


                    else:
                        break #loop10






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "term"


    # $ANTLR start "addop"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:86:1: addop returns [op] : ( '+' | '-' );
    def addop(self, ):

        op = None

        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:87:5: ( '+' | '-' )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 42) :
                    alt11 = 1
                elif (LA11_0 == 43) :
                    alt11 = 2
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:87:9: '+'
                    pass 
                    self.match(self.input, 42, self.FOLLOW_42_in_addop973)
                    #action start
                    op = '+'
                    #action end


                elif alt11 == 2:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:88:9: '-'
                    pass 
                    self.match(self.input, 43, self.FOLLOW_43_in_addop985)
                    #action start
                    op = '-'
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return op

    # $ANTLR end "addop"


    # $ANTLR start "factor"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:91:1: factor returns [value] : a= base (op= mulop b= base )* ;
    def factor(self, ):

        value = None

        a = None

        op = None

        b = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:92:5: (a= base (op= mulop b= base )* )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:92:9: a= base (op= mulop b= base )*
                pass 
                self._state.following.append(self.FOLLOW_base_in_factor1012)
                a = self.base()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:93:9: (op= mulop b= base )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == 44) :
                        alt12 = 1
                    elif (LA12_0 == 45) :
                        alt12 = 1


                    if alt12 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:93:11: op= mulop b= base
                        pass 
                        self._state.following.append(self.FOLLOW_mulop_in_factor1041)
                        op = self.mulop()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_base_in_factor1045)
                        b = self.base()

                        self._state.following.pop()
                        #action start
                        value = BinOp(op,value,b)
                        #action end


                    else:
                        break #loop12






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "factor"


    # $ANTLR start "mulop"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:97:1: mulop returns [op] : ( '*' | '/' );
    def mulop(self, ):

        op = None

        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:98:5: ( '*' | '/' )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == 44) :
                    alt13 = 1
                elif (LA13_0 == 45) :
                    alt13 = 2
                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:98:9: '*'
                    pass 
                    self.match(self.input, 44, self.FOLLOW_44_in_mulop1083)
                    #action start
                    op = '*'
                    #action end


                elif alt13 == 2:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:99:9: '/'
                    pass 
                    self.match(self.input, 45, self.FOLLOW_45_in_mulop1095)
                    #action start
                    op = '/'
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return op

    # $ANTLR end "mulop"


    # $ANTLR start "base"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:102:1: base returns [value] : ( '!' e= base | e= assign | IF a= expr THEN t= block ( ELSE e= block )? | x= INT | x= FLOAT | x= STRING | DATE '(' d= STRING ')' | x= TRUE | x= FALSE | '(' e= block ')' );
    def base(self, ):

        value = None

        x = None
        d = None
        e = None

        a = None

        t = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:103:5: ( '!' e= base | e= assign | IF a= expr THEN t= block ( ELSE e= block )? | x= INT | x= FLOAT | x= STRING | DATE '(' d= STRING ')' | x= TRUE | x= FALSE | '(' e= block ')' )
                alt15 = 10
                LA15 = self.input.LA(1)
                if LA15 == 46:
                    alt15 = 1
                elif LA15 == OUTPUT or LA15 == ID:
                    alt15 = 2
                elif LA15 == IF:
                    alt15 = 3
                elif LA15 == INT:
                    alt15 = 4
                elif LA15 == FLOAT:
                    alt15 = 5
                elif LA15 == STRING:
                    alt15 = 6
                elif LA15 == DATE:
                    alt15 = 7
                elif LA15 == TRUE:
                    alt15 = 8
                elif LA15 == FALSE:
                    alt15 = 9
                elif LA15 == 32:
                    alt15 = 10
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:103:9: '!' e= base
                    pass 
                    self.match(self.input, 46, self.FOLLOW_46_in_base1120)
                    self._state.following.append(self.FOLLOW_base_in_base1124)
                    e = self.base()

                    self._state.following.pop()
                    #action start
                    value = Not(e)
                    #action end


                elif alt15 == 2:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:104:9: e= assign
                    pass 
                    self._state.following.append(self.FOLLOW_assign_in_base1140)
                    e = self.assign()

                    self._state.following.pop()
                    #action start
                    value = e
                    #action end


                elif alt15 == 3:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:105:9: IF a= expr THEN t= block ( ELSE e= block )?
                    pass 
                    self.match(self.input, IF, self.FOLLOW_IF_in_base1167)
                    self._state.following.append(self.FOLLOW_expr_in_base1171)
                    a = self.expr()

                    self._state.following.pop()
                    self.match(self.input, THEN, self.FOLLOW_THEN_in_base1173)
                    self._state.following.append(self.FOLLOW_block_in_base1177)
                    t = self.block()

                    self._state.following.pop()
                    #action start
                    value = If(a,t,None)
                    #action end
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:106:9: ( ELSE e= block )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == ELSE) :
                        alt14 = 1
                    if alt14 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:106:10: ELSE e= block
                        pass 
                        self.match(self.input, ELSE, self.FOLLOW_ELSE_in_base1191)
                        self._state.following.append(self.FOLLOW_block_in_base1195)
                        e = self.block()

                        self._state.following.pop()



                    #action start
                    value = If(a,t,e)
                    #action end


                elif alt15 == 4:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:107:9: x= INT
                    pass 
                    x=self.match(self.input, INT, self.FOLLOW_INT_in_base1219)
                    #action start
                    value = Data(int(x.getText()))
                    #action end


                elif alt15 == 5:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:108:9: x= FLOAT
                    pass 
                    x=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_base1251)
                    #action start
                    value = Data(float(x.getText()))
                    #action end


                elif alt15 == 6:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:109:9: x= STRING
                    pass 
                    x=self.match(self.input, STRING, self.FOLLOW_STRING_in_base1281)
                    #action start
                    value = Data(x.getText()[1:-1].replace("\\\"","\"").replace("\\\\","\\"))
                    #action end


                elif alt15 == 7:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:110:9: DATE '(' d= STRING ')'
                    pass 
                    self.match(self.input, DATE, self.FOLLOW_DATE_in_base1308)
                    self.match(self.input, 32, self.FOLLOW_32_in_base1310)
                    d=self.match(self.input, STRING, self.FOLLOW_STRING_in_base1314)
                    self.match(self.input, 33, self.FOLLOW_33_in_base1316)
                    #action start
                    value = Data(d.getText())
                    #action end


                elif alt15 == 8:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:111:9: x= TRUE
                    pass 
                    x=self.match(self.input, TRUE, self.FOLLOW_TRUE_in_base1330)
                    #action start
                    value = Data(True)
                    #action end


                elif alt15 == 9:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:112:9: x= FALSE
                    pass 
                    x=self.match(self.input, FALSE, self.FOLLOW_FALSE_in_base1361)
                    #action start
                    value = Data(FALSE)
                    #action end


                elif alt15 == 10:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:113:9: '(' e= block ')'
                    pass 
                    self.match(self.input, 32, self.FOLLOW_32_in_base1389)
                    self._state.following.append(self.FOLLOW_block_in_base1393)
                    e = self.block()

                    self._state.following.pop()
                    self.match(self.input, 33, self.FOLLOW_33_in_base1395)
                    #action start
                    value = e
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "base"


    # $ANTLR start "assign"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:116:1: assign returns [value] : a= prim ( '=' b= expr )? ;
    def assign(self, ):

        value = None

        a = None

        b = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:117:5: (a= prim ( '=' b= expr )? )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:117:9: a= prim ( '=' b= expr )?
                pass 
                self._state.following.append(self.FOLLOW_prim_in_assign1430)
                a = self.prim()

                self._state.following.pop()
                #action start
                value = a
                #action end
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:118:9: ( '=' b= expr )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == 29) :
                    alt16 = 1
                if alt16 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:118:11: '=' b= expr
                    pass 
                    self.match(self.input, 29, self.FOLLOW_29_in_assign1461)
                    self._state.following.append(self.FOLLOW_expr_in_assign1465)
                    b = self.expr()

                    self._state.following.pop()
                    #action start
                    value = Assign(a, b)
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "assign"


    # $ANTLR start "prim"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:122:1: prim returns [value] : ( OUTPUT '(' b= STRING ',' e= expr ')' | b= ID r= access[value] );
    def prim(self, ):

        value = None

        b = None
        e = None

        r = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:123:5: ( OUTPUT '(' b= STRING ',' e= expr ')' | b= ID r= access[value] )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == OUTPUT) :
                    alt17 = 1
                elif (LA17_0 == ID) :
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:123:9: OUTPUT '(' b= STRING ',' e= expr ')'
                    pass 
                    self.match(self.input, OUTPUT, self.FOLLOW_OUTPUT_in_prim1504)
                    self.match(self.input, 32, self.FOLLOW_32_in_prim1506)
                    b=self.match(self.input, STRING, self.FOLLOW_STRING_in_prim1510)
                    self.match(self.input, 47, self.FOLLOW_47_in_prim1512)
                    self._state.following.append(self.FOLLOW_expr_in_prim1516)
                    e = self.expr()

                    self._state.following.pop()
                    self.match(self.input, 33, self.FOLLOW_33_in_prim1518)
                    #action start
                    value = Out(b.getText()[1:-1], e)
                    #action end


                elif alt17 == 2:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:124:9: b= ID r= access[value]
                    pass 
                    b=self.match(self.input, ID, self.FOLLOW_ID_in_prim1533)
                    #action start
                    value = Var(b.getText())
                    #action end
                    self._state.following.append(self.FOLLOW_access_in_prim1560)
                    r = self.access(value)

                    self._state.following.pop()
                    #action start
                    value = r
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "prim"


    # $ANTLR start "access"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:128:1: access[base] returns [value] : ( '.' x= ID ( '(' (a= args )? ')' )? r= access[value] | );
    def access(self, base):

        value = None

        x = None
        a = None

        r = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:129:5: ( '.' x= ID ( '(' (a= args )? ')' )? r= access[value] | )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == 48) :
                    alt20 = 1
                elif (LA20_0 == EOF or LA20_0 == THEN or (28 <= LA20_0 <= 29) or LA20_0 == 31 or (33 <= LA20_0 <= 45) or LA20_0 == 47) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:129:9: '.' x= ID ( '(' (a= args )? ')' )? r= access[value]
                    pass 
                    self.match(self.input, 48, self.FOLLOW_48_in_access1589)
                    x=self.match(self.input, ID, self.FOLLOW_ID_in_access1593)
                    #action start
                    value = Prop(base, x.getText())
                    #action end
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:130:9: ( '(' (a= args )? ')' )?
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == 32) :
                        alt19 = 1
                    if alt19 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:130:11: '(' (a= args )? ')'
                        pass 
                        self.match(self.input, 32, self.FOLLOW_32_in_access1614)
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:130:16: (a= args )?
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == IF or (FUNCTION <= LA18_0 <= OUTPUT) or (TRUE <= LA18_0 <= FALSE) or (DATE <= LA18_0 <= STRING) or LA18_0 == 32 or LA18_0 == 46) :
                            alt18 = 1
                        if alt18 == 1:
                            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:130:16: a= args
                            pass 
                            self._state.following.append(self.FOLLOW_args_in_access1618)
                            a = self.args()

                            self._state.following.pop()



                        #action start
                        value = Call(base, x.getText(), a)
                        #action end
                        self.match(self.input, 33, self.FOLLOW_33_in_access1637)



                    self._state.following.append(self.FOLLOW_access_in_access1660)
                    r = self.access(value)

                    self._state.following.pop()
                    #action start
                    value = r
                    #action end


                elif alt20 == 2:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:134:25: 
                    pass 
                    #action start
                    value = base
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "access"


    # $ANTLR start "args"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:137:1: args returns [arglist] : a= expr ( ',' rest= args )? ;
    def args(self, ):

        arglist = None

        a = None

        rest = None


        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:138:5: (a= expr ( ',' rest= args )? )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:138:9: a= expr ( ',' rest= args )?
                pass 
                #action start
                arglist = []
                #action end
                self._state.following.append(self.FOLLOW_expr_in_args1724)
                a = self.expr()

                self._state.following.pop()
                #action start
                arglist = [a]
                #action end
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:140:9: ( ',' rest= args )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == 47) :
                    alt21 = 1
                if alt21 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:140:11: ',' rest= args
                    pass 
                    self.match(self.input, 47, self.FOLLOW_47_in_args1747)
                    self._state.following.append(self.FOLLOW_args_in_args1751)
                    rest = self.args()

                    self._state.following.pop()
                    #action start
                    arglist+=rest;
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return arglist

    # $ANTLR end "args"


    # $ANTLR start "dateargs"
    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:144:1: dateargs returns [value] : y= INT ',' m= INT ',' d= INT ;
    def dateargs(self, ):

        value = None

        y = None
        m = None
        d = None

        try:
            try:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:145:5: (y= INT ',' m= INT ',' d= INT )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:145:9: y= INT ',' m= INT ',' d= INT
                pass 
                y=self.match(self.input, INT, self.FOLLOW_INT_in_dateargs1789)
                self.match(self.input, 47, self.FOLLOW_47_in_dateargs1791)
                m=self.match(self.input, INT, self.FOLLOW_INT_in_dateargs1795)
                self.match(self.input, 47, self.FOLLOW_47_in_dateargs1797)
                d=self.match(self.input, INT, self.FOLLOW_INT_in_dateargs1801)
                #action start
                value = date(int(y.getText()), int(m.getText()), int(d.getText()))
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return value

    # $ANTLR end "dateargs"


    # Delegated rules


 

    FOLLOW_statements_in_main212 = frozenset([])
    FOLLOW_EOF_in_main216 = frozenset([1])
    FOLLOW_statement_in_statements241 = frozenset([1, 28])
    FOLLOW_28_in_statements275 = frozenset([1, 4, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_statements_in_statements292 = frozenset([1])
    FOLLOW_VAR_in_statements348 = frozenset([15])
    FOLLOW_ID_in_statements352 = frozenset([29])
    FOLLOW_29_in_statements354 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_expr_in_statements358 = frozenset([28])
    FOLLOW_28_in_statements360 = frozenset([4, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_statements_in_statements364 = frozenset([1])
    FOLLOW_30_in_block387 = frozenset([4, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_statements_in_block391 = frozenset([31])
    FOLLOW_31_in_block393 = frozenset([1])
    FOLLOW_FOR_in_statement420 = frozenset([32])
    FOLLOW_32_in_statement422 = frozenset([15])
    FOLLOW_ID_in_statement426 = frozenset([13])
    FOLLOW_IN_in_statement428 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_expr_in_statement432 = frozenset([33])
    FOLLOW_33_in_statement434 = frozenset([30])
    FOLLOW_block_in_statement438 = frozenset([1])
    FOLLOW_expr_in_statement454 = frozenset([1])
    FOLLOW_FUNCTION_in_expr508 = frozenset([32])
    FOLLOW_32_in_expr510 = frozenset([15])
    FOLLOW_ID_in_expr514 = frozenset([33])
    FOLLOW_33_in_expr516 = frozenset([30])
    FOLLOW_block_in_expr520 = frozenset([1])
    FOLLOW_orexpr_in_expr541 = frozenset([1])
    FOLLOW_andexpr_in_orexpr591 = frozenset([1, 34])
    FOLLOW_34_in_orexpr615 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_andexpr_in_orexpr619 = frozenset([1, 34])
    FOLLOW_comp_in_andexpr660 = frozenset([1, 35])
    FOLLOW_35_in_andexpr684 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_comp_in_andexpr688 = frozenset([1, 35])
    FOLLOW_term_in_comp729 = frozenset([1, 36, 37, 38, 39, 40, 41])
    FOLLOW_compop_in_comp758 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_term_in_comp762 = frozenset([1, 36, 37, 38, 39, 40, 41])
    FOLLOW_36_in_compop799 = frozenset([1])
    FOLLOW_37_in_compop814 = frozenset([1])
    FOLLOW_38_in_compop829 = frozenset([1])
    FOLLOW_39_in_compop845 = frozenset([1])
    FOLLOW_40_in_compop860 = frozenset([1])
    FOLLOW_41_in_compop876 = frozenset([1])
    FOLLOW_factor_in_term906 = frozenset([1, 42, 43])
    FOLLOW_addop_in_term933 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_factor_in_term937 = frozenset([1, 42, 43])
    FOLLOW_42_in_addop973 = frozenset([1])
    FOLLOW_43_in_addop985 = frozenset([1])
    FOLLOW_base_in_factor1012 = frozenset([1, 44, 45])
    FOLLOW_mulop_in_factor1041 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_base_in_factor1045 = frozenset([1, 44, 45])
    FOLLOW_44_in_mulop1083 = frozenset([1])
    FOLLOW_45_in_mulop1095 = frozenset([1])
    FOLLOW_46_in_base1120 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_base_in_base1124 = frozenset([1])
    FOLLOW_assign_in_base1140 = frozenset([1])
    FOLLOW_IF_in_base1167 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_expr_in_base1171 = frozenset([5])
    FOLLOW_THEN_in_base1173 = frozenset([30])
    FOLLOW_block_in_base1177 = frozenset([1, 6])
    FOLLOW_ELSE_in_base1191 = frozenset([30])
    FOLLOW_block_in_base1195 = frozenset([1])
    FOLLOW_INT_in_base1219 = frozenset([1])
    FOLLOW_FLOAT_in_base1251 = frozenset([1])
    FOLLOW_STRING_in_base1281 = frozenset([1])
    FOLLOW_DATE_in_base1308 = frozenset([32])
    FOLLOW_32_in_base1310 = frozenset([18])
    FOLLOW_STRING_in_base1314 = frozenset([33])
    FOLLOW_33_in_base1316 = frozenset([1])
    FOLLOW_TRUE_in_base1330 = frozenset([1])
    FOLLOW_FALSE_in_base1361 = frozenset([1])
    FOLLOW_32_in_base1389 = frozenset([30])
    FOLLOW_block_in_base1393 = frozenset([33])
    FOLLOW_33_in_base1395 = frozenset([1])
    FOLLOW_prim_in_assign1430 = frozenset([1, 29])
    FOLLOW_29_in_assign1461 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_expr_in_assign1465 = frozenset([1])
    FOLLOW_OUTPUT_in_prim1504 = frozenset([32])
    FOLLOW_32_in_prim1506 = frozenset([18])
    FOLLOW_STRING_in_prim1510 = frozenset([47])
    FOLLOW_47_in_prim1512 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_expr_in_prim1516 = frozenset([33])
    FOLLOW_33_in_prim1518 = frozenset([1])
    FOLLOW_ID_in_prim1533 = frozenset([48])
    FOLLOW_access_in_prim1560 = frozenset([1])
    FOLLOW_48_in_access1589 = frozenset([15])
    FOLLOW_ID_in_access1593 = frozenset([32, 48])
    FOLLOW_32_in_access1614 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 33, 46])
    FOLLOW_args_in_access1618 = frozenset([33])
    FOLLOW_33_in_access1637 = frozenset([48])
    FOLLOW_access_in_access1660 = frozenset([1])
    FOLLOW_expr_in_args1724 = frozenset([1, 47])
    FOLLOW_47_in_args1747 = frozenset([4, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 32, 46])
    FOLLOW_args_in_args1751 = frozenset([1])
    FOLLOW_INT_in_dateargs1789 = frozenset([47])
    FOLLOW_47_in_dateargs1791 = frozenset([16])
    FOLLOW_INT_in_dateargs1795 = frozenset([47])
    FOLLOW_47_in_dateargs1797 = frozenset([16])
    FOLLOW_INT_in_dateargs1801 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("BatchScriptLexer", BatchScriptParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
