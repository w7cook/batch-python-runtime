# $ANTLR 3.1.1 /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g 2012-07-28 22:25:11

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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
IN=13
THEN=5
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


class BatchScriptLexer(Lexer):

    grammarFileName = "/Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g"
    antlr_version = version_str_to_tuple("3.1.1")
    antlr_version_str = "3.1.1"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )

        self.dfa20 = self.DFA20(
            self, 20,
            eot = self.DFA20_eot,
            eof = self.DFA20_eof,
            min = self.DFA20_min,
            max = self.DFA20_max,
            accept = self.DFA20_accept,
            special = self.DFA20_special,
            transition = self.DFA20_transition
            )






    # $ANTLR start "IF"
    def mIF(self, ):

        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:7:4: ( 'if' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:7:6: 'if'
            pass 
            self.match("if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IF"



    # $ANTLR start "THEN"
    def mTHEN(self, ):

        try:
            _type = THEN
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:8:6: ( 'then' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:8:8: 'then'
            pass 
            self.match("then")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THEN"



    # $ANTLR start "ELSE"
    def mELSE(self, ):

        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:9:6: ( 'else' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:9:8: 'else'
            pass 
            self.match("else")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "FOR"
    def mFOR(self, ):

        try:
            _type = FOR
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:10:5: ( 'for' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:10:7: 'for'
            pass 
            self.match("for")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FOR"



    # $ANTLR start "FUNCTION"
    def mFUNCTION(self, ):

        try:
            _type = FUNCTION
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:11:10: ( 'function' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:11:12: 'function'
            pass 
            self.match("function")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FUNCTION"



    # $ANTLR start "OUTPUT"
    def mOUTPUT(self, ):

        try:
            _type = OUTPUT
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:12:8: ( 'OUTPUT' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:12:10: 'OUTPUT'
            pass 
            self.match("OUTPUT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OUTPUT"



    # $ANTLR start "VAR"
    def mVAR(self, ):

        try:
            _type = VAR
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:13:5: ( 'var' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:13:7: 'var'
            pass 
            self.match("var")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VAR"



    # $ANTLR start "TRUE"
    def mTRUE(self, ):

        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:14:6: ( 'true' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:14:8: 'true'
            pass 
            self.match("true")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TRUE"



    # $ANTLR start "FALSE"
    def mFALSE(self, ):

        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:15:7: ( 'false' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:15:9: 'false'
            pass 
            self.match("false")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "IN"
    def mIN(self, ):

        try:
            _type = IN
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:16:4: ( 'in' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:16:6: 'in'
            pass 
            self.match("in")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IN"



    # $ANTLR start "DATE"
    def mDATE(self, ):

        try:
            _type = DATE
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:17:6: ( 'date' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:17:8: 'date'
            pass 
            self.match("date")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DATE"



    # $ANTLR start "T__28"
    def mT__28(self, ):

        try:
            _type = T__28
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:18:7: ( ';' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:18:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__28"



    # $ANTLR start "T__29"
    def mT__29(self, ):

        try:
            _type = T__29
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:19:7: ( '=' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:19:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__29"



    # $ANTLR start "T__30"
    def mT__30(self, ):

        try:
            _type = T__30
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:20:7: ( '{' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:20:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__30"



    # $ANTLR start "T__31"
    def mT__31(self, ):

        try:
            _type = T__31
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:21:7: ( '}' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:21:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__31"



    # $ANTLR start "T__32"
    def mT__32(self, ):

        try:
            _type = T__32
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:22:7: ( '(' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:22:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__32"



    # $ANTLR start "T__33"
    def mT__33(self, ):

        try:
            _type = T__33
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:23:7: ( ')' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:23:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__33"



    # $ANTLR start "T__34"
    def mT__34(self, ):

        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:24:7: ( '||' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:24:9: '||'
            pass 
            self.match("||")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__34"



    # $ANTLR start "T__35"
    def mT__35(self, ):

        try:
            _type = T__35
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:25:7: ( '&&' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:25:9: '&&'
            pass 
            self.match("&&")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__35"



    # $ANTLR start "T__36"
    def mT__36(self, ):

        try:
            _type = T__36
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:26:7: ( '==' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:26:9: '=='
            pass 
            self.match("==")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__36"



    # $ANTLR start "T__37"
    def mT__37(self, ):

        try:
            _type = T__37
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:27:7: ( '!=' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:27:9: '!='
            pass 
            self.match("!=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__37"



    # $ANTLR start "T__38"
    def mT__38(self, ):

        try:
            _type = T__38
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:28:7: ( '<' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:28:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__38"



    # $ANTLR start "T__39"
    def mT__39(self, ):

        try:
            _type = T__39
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:29:7: ( '<=' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:29:9: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__39"



    # $ANTLR start "T__40"
    def mT__40(self, ):

        try:
            _type = T__40
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:30:7: ( '>' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:30:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__40"



    # $ANTLR start "T__41"
    def mT__41(self, ):

        try:
            _type = T__41
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:31:7: ( '>=' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:31:9: '>='
            pass 
            self.match(">=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__41"



    # $ANTLR start "T__42"
    def mT__42(self, ):

        try:
            _type = T__42
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:32:7: ( '+' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:32:9: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__42"



    # $ANTLR start "T__43"
    def mT__43(self, ):

        try:
            _type = T__43
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:33:7: ( '-' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:33:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__43"



    # $ANTLR start "T__44"
    def mT__44(self, ):

        try:
            _type = T__44
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:34:7: ( '*' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:34:9: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__44"



    # $ANTLR start "T__45"
    def mT__45(self, ):

        try:
            _type = T__45
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:35:7: ( '/' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:35:9: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__45"



    # $ANTLR start "T__46"
    def mT__46(self, ):

        try:
            _type = T__46
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:36:7: ( '!' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:36:9: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__46"



    # $ANTLR start "T__47"
    def mT__47(self, ):

        try:
            _type = T__47
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:37:7: ( ',' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:37:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__47"



    # $ANTLR start "T__48"
    def mT__48(self, ):

        try:
            _type = T__48
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:38:7: ( '.' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:38:9: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__48"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:149:9: ( '0' .. '9' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:149:13: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "ALPHA"
    def mALPHA(self, ):

        try:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:152:9: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:152:13: ( 'a' .. 'z' | 'A' .. 'Z' | '_' )
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ALPHA"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:154:9: ( ALPHA ( ALPHA | DIGIT )* | ( '*' ) )
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if ((65 <= LA2_0 <= 90) or LA2_0 == 95 or (97 <= LA2_0 <= 122)) :
                alt2 = 1
            elif (LA2_0 == 42) :
                alt2 = 2
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae

            if alt2 == 1:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:154:13: ALPHA ( ALPHA | DIGIT )*
                pass 
                self.mALPHA()
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:154:19: ( ALPHA | DIGIT )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                        alt1 = 1


                    if alt1 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop1




            elif alt2 == 2:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:155:13: ( '*' )
                pass 
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:155:13: ( '*' )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:155:14: '*'
                pass 
                self.match(42)





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:158:9: ( ( DIGIT )+ )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:158:13: ( DIGIT )+
            pass 
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:158:13: ( DIGIT )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57)) :
                    alt3 = 1


                if alt3 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:158:13: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):

        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:9: ( ( DIGIT )+ '.' ( DIGIT )* ( EXPONENT )? | '.' ( DIGIT )+ ( EXPONENT )? | ( DIGIT )+ EXPONENT )
            alt10 = 3
            alt10 = self.dfa10.predict(self.input)
            if alt10 == 1:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:13: ( DIGIT )+ '.' ( DIGIT )* ( EXPONENT )?
                pass 
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:13: ( DIGIT )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((48 <= LA4_0 <= 57)) :
                        alt4 = 1


                    if alt4 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:13: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1


                self.match(46)
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:24: ( DIGIT )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((48 <= LA5_0 <= 57)) :
                        alt5 = 1


                    if alt5 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:24: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        break #loop5


                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:31: ( EXPONENT )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 69 or LA6_0 == 101) :
                    alt6 = 1
                if alt6 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:31: EXPONENT
                    pass 
                    self.mEXPONENT()





            elif alt10 == 2:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:43: '.' ( DIGIT )+ ( EXPONENT )?
                pass 
                self.match(46)
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:47: ( DIGIT )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((48 <= LA7_0 <= 57)) :
                        alt7 = 1


                    if alt7 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:47: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1


                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:54: ( EXPONENT )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 69 or LA8_0 == 101) :
                    alt8 = 1
                if alt8 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:54: EXPONENT
                    pass 
                    self.mEXPONENT()





            elif alt10 == 3:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:66: ( DIGIT )+ EXPONENT
                pass 
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:66: ( DIGIT )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((48 <= LA9_0 <= 57)) :
                        alt9 = 1


                    if alt9 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:159:66: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1


                self.mEXPONENT()


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:161:9: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' | '/*' ( options {greedy=false; } : . )* '*/' )
            alt14 = 2
            LA14_0 = self.input.LA(1)

            if (LA14_0 == 47) :
                LA14_1 = self.input.LA(2)

                if (LA14_1 == 47) :
                    alt14 = 1
                elif (LA14_1 == 42) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 14, 0, self.input)

                raise nvae

            if alt14 == 1:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:161:13: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match("//")
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:161:18: (~ ( '\\n' | '\\r' ) )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((0 <= LA11_0 <= 9) or (11 <= LA11_0 <= 12) or (14 <= LA11_0 <= 65535)) :
                        alt11 = 1


                    if alt11 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:161:18: ~ ( '\\n' | '\\r' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop11


                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:161:32: ( '\\r' )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 13) :
                    alt12 = 1
                if alt12 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:161:32: '\\r'
                    pass 
                    self.match(13)



                self.match(10)
                #action start
                _channel=HIDDEN;
                #action end


            elif alt14 == 2:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:162:13: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:162:18: ( options {greedy=false; } : . )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 42) :
                        LA13_1 = self.input.LA(2)

                        if (LA13_1 == 47) :
                            alt13 = 2
                        elif ((0 <= LA13_1 <= 46) or (48 <= LA13_1 <= 65535)) :
                            alt13 = 1


                    elif ((0 <= LA13_0 <= 41) or (43 <= LA13_0 <= 65535)) :
                        alt13 = 1


                    if alt13 == 1:
                        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:162:46: .
                        pass 
                        self.matchAny()


                    else:
                        break #loop13


                self.match("*/")
                #action start
                _channel=HIDDEN;
                #action end


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:165:9: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:165:13: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:168:9: ( '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"' )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:168:13: '\"' ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:168:17: ( ESC_SEQ | ~ ( '\\\\' | '\"' ) )*
            while True: #loop15
                alt15 = 3
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 92) :
                    alt15 = 1
                elif ((0 <= LA15_0 <= 33) or (35 <= LA15_0 <= 91) or (93 <= LA15_0 <= 65535)) :
                    alt15 = 2


                if alt15 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:168:19: ESC_SEQ
                    pass 
                    self.mESC_SEQ()


                elif alt15 == 2:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:168:29: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop15


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):

        try:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:172:13: ( ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+ )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:172:17: ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:172:27: ( '+' | '-' )?
            alt16 = 2
            LA16_0 = self.input.LA(1)

            if (LA16_0 == 43 or LA16_0 == 45) :
                alt16 = 1
            if alt16 == 1:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:172:38: ( DIGIT )+
            cnt17 = 0
            while True: #loop17
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if ((48 <= LA17_0 <= 57)) :
                    alt17 = 1


                if alt17 == 1:
                    # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:172:38: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt17 >= 1:
                        break #loop17

                    eee = EarlyExitException(17, self.input)
                    raise eee

                cnt17 += 1






        finally:

            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):

        try:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:175:13: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:175:17: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "ESC_SEQ"
    def mESC_SEQ(self, ):

        try:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:178:13: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | OCTAL_ESC )
            alt18 = 3
            LA18_0 = self.input.LA(1)

            if (LA18_0 == 92) :
                LA18 = self.input.LA(2)
                if LA18 == 34 or LA18 == 39 or LA18 == 92 or LA18 == 98 or LA18 == 102 or LA18 == 110 or LA18 == 114 or LA18 == 116:
                    alt18 = 1
                elif LA18 == 117:
                    alt18 = 2
                elif LA18 == 48 or LA18 == 49 or LA18 == 50 or LA18 == 51 or LA18 == 52 or LA18 == 53 or LA18 == 54 or LA18 == 55:
                    alt18 = 3
                else:
                    nvae = NoViableAltException("", 18, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 18, 0, self.input)

                raise nvae

            if alt18 == 1:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:178:17: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)
                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt18 == 2:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:179:17: UNICODE_ESC
                pass 
                self.mUNICODE_ESC()


            elif alt18 == 3:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:180:17: OCTAL_ESC
                pass 
                self.mOCTAL_ESC()



        finally:

            pass

    # $ANTLR end "ESC_SEQ"



    # $ANTLR start "OCTAL_ESC"
    def mOCTAL_ESC(self, ):

        try:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:184:13: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt19 = 3
            LA19_0 = self.input.LA(1)

            if (LA19_0 == 92) :
                LA19_1 = self.input.LA(2)

                if ((48 <= LA19_1 <= 51)) :
                    LA19_2 = self.input.LA(3)

                    if ((48 <= LA19_2 <= 55)) :
                        LA19_5 = self.input.LA(4)

                        if ((48 <= LA19_5 <= 55)) :
                            alt19 = 1
                        else:
                            alt19 = 2
                    else:
                        alt19 = 3
                elif ((52 <= LA19_1 <= 55)) :
                    LA19_3 = self.input.LA(3)

                    if ((48 <= LA19_3 <= 55)) :
                        alt19 = 2
                    else:
                        alt19 = 3
                else:
                    nvae = NoViableAltException("", 19, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 19, 0, self.input)

                raise nvae

            if alt19 == 1:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:184:17: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:184:22: ( '0' .. '3' )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:184:23: '0' .. '3'
                pass 
                self.matchRange(48, 51)



                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:184:32: ( '0' .. '7' )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:184:33: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:184:42: ( '0' .. '7' )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:184:43: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt19 == 2:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:185:17: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:185:22: ( '0' .. '7' )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:185:23: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:185:32: ( '0' .. '7' )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:185:33: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt19 == 3:
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:186:17: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:186:22: ( '0' .. '7' )
                # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:186:23: '0' .. '7'
                pass 
                self.matchRange(48, 55)






        finally:

            pass

    # $ANTLR end "OCTAL_ESC"



    # $ANTLR start "UNICODE_ESC"
    def mUNICODE_ESC(self, ):

        try:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:190:13: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:190:17: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            pass 
            self.match(92)
            self.match(117)
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()




        finally:

            pass

    # $ANTLR end "UNICODE_ESC"



    def mTokens(self):
        # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:8: ( IF | THEN | ELSE | FOR | FUNCTION | OUTPUT | VAR | TRUE | FALSE | IN | DATE | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | ID | INT | FLOAT | COMMENT | WS | STRING )
        alt20 = 38
        alt20 = self.dfa20.predict(self.input)
        if alt20 == 1:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:10: IF
            pass 
            self.mIF()


        elif alt20 == 2:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:13: THEN
            pass 
            self.mTHEN()


        elif alt20 == 3:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:18: ELSE
            pass 
            self.mELSE()


        elif alt20 == 4:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:23: FOR
            pass 
            self.mFOR()


        elif alt20 == 5:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:27: FUNCTION
            pass 
            self.mFUNCTION()


        elif alt20 == 6:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:36: OUTPUT
            pass 
            self.mOUTPUT()


        elif alt20 == 7:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:43: VAR
            pass 
            self.mVAR()


        elif alt20 == 8:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:47: TRUE
            pass 
            self.mTRUE()


        elif alt20 == 9:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:52: FALSE
            pass 
            self.mFALSE()


        elif alt20 == 10:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:58: IN
            pass 
            self.mIN()


        elif alt20 == 11:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:61: DATE
            pass 
            self.mDATE()


        elif alt20 == 12:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:66: T__28
            pass 
            self.mT__28()


        elif alt20 == 13:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:72: T__29
            pass 
            self.mT__29()


        elif alt20 == 14:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:78: T__30
            pass 
            self.mT__30()


        elif alt20 == 15:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:84: T__31
            pass 
            self.mT__31()


        elif alt20 == 16:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:90: T__32
            pass 
            self.mT__32()


        elif alt20 == 17:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:96: T__33
            pass 
            self.mT__33()


        elif alt20 == 18:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:102: T__34
            pass 
            self.mT__34()


        elif alt20 == 19:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:108: T__35
            pass 
            self.mT__35()


        elif alt20 == 20:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:114: T__36
            pass 
            self.mT__36()


        elif alt20 == 21:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:120: T__37
            pass 
            self.mT__37()


        elif alt20 == 22:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:126: T__38
            pass 
            self.mT__38()


        elif alt20 == 23:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:132: T__39
            pass 
            self.mT__39()


        elif alt20 == 24:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:138: T__40
            pass 
            self.mT__40()


        elif alt20 == 25:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:144: T__41
            pass 
            self.mT__41()


        elif alt20 == 26:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:150: T__42
            pass 
            self.mT__42()


        elif alt20 == 27:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:156: T__43
            pass 
            self.mT__43()


        elif alt20 == 28:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:162: T__44
            pass 
            self.mT__44()


        elif alt20 == 29:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:168: T__45
            pass 
            self.mT__45()


        elif alt20 == 30:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:174: T__46
            pass 
            self.mT__46()


        elif alt20 == 31:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:180: T__47
            pass 
            self.mT__47()


        elif alt20 == 32:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:186: T__48
            pass 
            self.mT__48()


        elif alt20 == 33:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:192: ID
            pass 
            self.mID()


        elif alt20 == 34:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:195: INT
            pass 
            self.mINT()


        elif alt20 == 35:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:199: FLOAT
            pass 
            self.mFLOAT()


        elif alt20 == 36:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:205: COMMENT
            pass 
            self.mCOMMENT()


        elif alt20 == 37:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:213: WS
            pass 
            self.mWS()


        elif alt20 == 38:
            # /Users/wcook/workspace/batch-python-runtime/src/runtime/batch/syntax/BatchScript.g:1:216: STRING
            pass 
            self.mSTRING()







    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\2\56\3\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\1\71\1\145\3\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\1"
        )

    DFA10_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\4\1\uffff\12\1\13\uffff\1\3\37\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #10

    DFA10 = DFA
    # lookup tables for DFA #20

    DFA20_eot = DFA.unpack(
        u"\1\uffff\7\31\1\uffff\1\51\6\uffff\1\53\1\55\1\57\3\uffff\1\62"
        u"\1\uffff\1\63\1\uffff\1\65\2\uffff\1\66\1\67\11\31\20\uffff\3\31"
        u"\1\104\3\31\1\110\1\31\1\112\1\113\1\114\1\uffff\3\31\1\uffff\1"
        u"\120\3\uffff\1\31\1\122\1\31\1\uffff\1\31\1\uffff\1\125\1\31\1"
        u"\uffff\1\127\1\uffff"
        )

    DFA20_eof = DFA.unpack(
        u"\130\uffff"
        )

    DFA20_min = DFA.unpack(
        u"\1\11\1\146\1\150\1\154\1\141\1\125\2\141\1\uffff\1\75\6\uffff"
        u"\3\75\3\uffff\1\52\1\uffff\1\60\1\uffff\1\56\2\uffff\2\60\1\145"
        u"\1\165\1\163\1\162\1\156\1\154\1\124\1\162\1\164\20\uffff\1\156"
        u"\2\145\1\60\1\143\1\163\1\120\1\60\1\145\3\60\1\uffff\1\164\1\145"
        u"\1\125\1\uffff\1\60\3\uffff\1\151\1\60\1\124\1\uffff\1\157\1\uffff"
        u"\1\60\1\156\1\uffff\1\60\1\uffff"
        )

    DFA20_max = DFA.unpack(
        u"\1\175\1\156\1\162\1\154\1\165\1\125\2\141\1\uffff\1\75\6\uffff"
        u"\3\75\3\uffff\1\57\1\uffff\1\71\1\uffff\1\145\2\uffff\2\172\1\145"
        u"\1\165\1\163\1\162\1\156\1\154\1\124\1\162\1\164\20\uffff\1\156"
        u"\2\145\1\172\1\143\1\163\1\120\1\172\1\145\3\172\1\uffff\1\164"
        u"\1\145\1\125\1\uffff\1\172\3\uffff\1\151\1\172\1\124\1\uffff\1"
        u"\157\1\uffff\1\172\1\156\1\uffff\1\172\1\uffff"
        )

    DFA20_accept = DFA.unpack(
        u"\10\uffff\1\14\1\uffff\1\16\1\17\1\20\1\21\1\22\1\23\3\uffff\1"
        u"\32\1\33\1\34\1\uffff\1\37\1\uffff\1\41\1\uffff\1\45\1\46\13\uffff"
        u"\1\24\1\15\1\25\1\36\1\27\1\26\1\31\1\30\1\34\1\44\1\35\1\40\1"
        u"\43\1\42\1\1\1\12\14\uffff\1\4\3\uffff\1\7\1\uffff\1\2\1\10\1\3"
        u"\3\uffff\1\13\1\uffff\1\11\2\uffff\1\6\1\uffff\1\5"
        )

    DFA20_special = DFA.unpack(
        u"\130\uffff"
        )

            
    DFA20_transition = [
        DFA.unpack(u"\2\33\2\uffff\1\33\22\uffff\1\33\1\20\1\34\3\uffff\1"
        u"\17\1\uffff\1\14\1\15\1\25\1\23\1\27\1\24\1\30\1\26\12\32\1\uffff"
        u"\1\10\1\21\1\11\1\22\2\uffff\16\31\1\5\13\31\4\uffff\1\31\1\uffff"
        u"\3\31\1\7\1\3\1\4\2\31\1\1\12\31\1\2\1\31\1\6\4\31\1\12\1\16\1"
        u"\13"),
        DFA.unpack(u"\1\35\7\uffff\1\36"),
        DFA.unpack(u"\1\37\11\uffff\1\40"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\44\15\uffff\1\42\5\uffff\1\43"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\61\4\uffff\1\61"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\64"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\64\1\uffff\12\32\13\uffff\1\64\37\uffff\1\64"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #20

    DFA20 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(BatchScriptLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
