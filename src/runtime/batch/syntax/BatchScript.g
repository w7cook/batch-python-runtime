grammar BatchScript;

options {
    language=Python;
}

tokens {
    IF      =   'if';
    THEN    =   'then';
    ELSE    =   'else';
    FOR     =   'for';
	FUNCTION = 'function';
	OUTPUT = 'OUTPUT';
    VAR     =   'var';
    TRUE    =   'true';
    FALSE   =   'false';
    IN      =   'in';
    DATE    =   'date';
}

@header {
    from batch.Expressions import *
    from datetime import date
}

main returns [value]
    :   e=statements {$value=$e.value;} EOF
    ;

statements returns [value]
    :   e=statement                     {$value=$e.value}
        ( ';'
            (es=statements                   {$value=Seq($value,$es.value);}
            )?
        )?
    |   VAR x=ID '=' e=expr ';' b=statements {$value=Let($x.getText(),$e.value,$b.value);}
    ;

block returns [Expression value]
    : '{' e=statements '}'  {$value = e;} 
    ;

statement returns [value]
    :   FOR '(' x=ID IN e=expr ')' b=block   {$value=For($x.getText(),$e.value,$b.value);}
    |   e=expr                              {$value=$e.value;}
    ;

expr returns [value]
    :   FUNCTION '(' x=ID ')' e=block        {$value=Fun($x.getText(),$e.value);}
    |   a=orexpr                        {$value=$a.value;}
    ;

orexpr returns [value]
    :   a=andexpr           {$value=$a.value;}
        ( '||' b=andexpr    {$value=Or($value,$b.value);}
        )*
    ;

andexpr returns [value]
    :   a=comp           {$value=$a.value;}
        ( '&&' b=comp    {$value=And($value,$b.value);}
        )*
    ;

comp returns [value]
    :   a=term              {$value=$a.value;}
        ( op=compop b=term  {$value=BinOp($op.op,$value,$b.value);}
        )*
    ;

compop returns [op]
    :   '=='    {$op='==';}
    |   '!='    {$op='!=';}
    |   '<'     {$op='<';}
    |   '<='    {$op='<=';}
    |   '>'     {$op='>';}
    |   '>='    {$op='>=';}
    ;

term returns [value]
    :   a=factor            {$value=$a.value;}
        ( op=addop b=factor {$value=BinOp($op.op,$value,$b.value);}
        )*
    ;

addop returns [op]
    :   '+' {$op='+';}
    |   '-' {$op='-';}
    ;

factor returns [value]
    :   a=base              {$value=$a.value;}
        ( op=mulop b=base   {$value=BinOp($op.op,$value,$b.value);}
        )*
    ;

mulop returns [op]
    :   '*' {$op='*';}
    |   '/' {$op='/';}
    ;

base returns [value]
    :   '!' e=base   {$value=Not($e.value);}
    |   e=assign                {$value=$e.value;}
    |   IF a=expr THEN t=block  {$value=If($a.value,$t.value,None);}
        (ELSE e=block)?         {$value=If($a.value,$t.value,$e.value);}
    |   x=INT                   {$value=Data(int($x.getText()));}
    |   x=FLOAT                 {$value=Data(float($x.getText()));}
    |   x=STRING                {$value=Data($x.getText()[1:-1].replace("\\\"","\"").replace("\\\\","\\"));}
    |   DATE '(' d=STRING ')' {$value=Data($d.getText());}
    |   x=TRUE                  {$value=Data(True);}
    |   x=FALSE                 {$value=Data(FALSE);}
    |   '(' e=expr ')'         {$value=$e.value;}
    ;

assign returns [value]
    :   a=prim                  {$value=$a.value;}
        ( '=' b=expr    {$value=Assign($a.value, $b.value);}
        )?
    ;

prim returns [value]
    :   OUTPUT '(' b=STRING ',' e=expr ')'  {$value=Out($b.getText()[1:-1], $e.value);}
    |   b=ID              {$value=Var($b.getText());}
        r=access[value]   {$value=$r.value;}
    ;

access[base] returns [value]
    :   '.' x=ID        {$value=Prop($base, $x.getText());}
        ( '(' a=args?    {$value=Call($base, $x.getText(), $a.arglist);} 
          ')'
        )?
        r=access[value] {$value=$r.value;}
    |                   {$value=$base;}
    ;

args returns [arglist]
    :   {$arglist=[];}
        a=expr          {$arglist=[$a.value];}
        ( ',' rest=args {$arglist+=$rest.arglist;}
        )?
    ;

dateargs returns [value]
    :   y=INT ',' m=INT ',' d=INT   {$value=date(int($y.getText()), int($m.getText()), int($d.getText()));}
    ;

fragment
DIGIT   :   '0'..'9';

fragment
ALPHA   :   ('a'..'z' | 'A'..'Z' | '_');

ID      :   ALPHA (ALPHA | DIGIT)*
        |   ('*')
        ;

INT     :   DIGIT+;
FLOAT   :   DIGIT+ '.' DIGIT* EXPONENT? | '.' DIGIT+ EXPONENT? | DIGIT+ EXPONENT;

COMMENT :   '//' ~('\n'|'\r')* '\r'? '\n'               {$channel=HIDDEN;}
        |   '/*' ( options {greedy=false;} : .)* '*/'   {$channel=HIDDEN;}
        ;

WS      :   ( ' ' | '\t' | '\r' | '\n' )    {$channel=HIDDEN;}
        ;

STRING  :   '"' ( '\\' ('b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\') | UNICODE_ESC | ~('\\'|'"'))*'"'
        ;

fragment
EXPONENT    :   ('e'|'E') ('+'|'-')? DIGIT+;

fragment
HEX_DIGIT   :   ('0'..'9'|'a'..'f'|'A'..'F');

fragment
ESC_SEQ     :   
            |   UNICODE_ESC
            |   OCTAL_ESC
            ;

fragment
OCTAL_ESC   :   '\\' ('0'..'3')('0'..'7')('0'..'7')
            |   '\\' ('0'..'7')('0'..'7')
            |   '\\' ('0'..'7')
            ;

fragment
UNICODE_ESC :   '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            ;
