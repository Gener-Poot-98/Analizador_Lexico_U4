import sys
import ply.lex as lex

tokens = (

    #Reserved keywords as of ECMAScript 6
    'BREAK','CASE','CLASS','CATCH','CONST','CONTINUE','DEBUGGER','DEFAULT','DELETE',
    'DO','ELSE','EXPORT','EXTENDS','FINALLY','FOR','FUNCTION','IF','IMPORT','IN',
    'INSTANCEOF','LET','NEW','RETURN','SUPER','SWITCH','THIS','THROW','TRY','TYPEOF',
    'VAR','VOID','WHILE','WITH','YIELD', 'ALERT',

    #booleanos
    'TRUE','FALSE',

    # SIMBOLOS
    'SUMA','INCREMENTO','MAS_IGUAL','RESTA','DECREMENTO','MENOS_IGUAL','MULTIPLICACION',
    'EXPONENTE','DIVISION','RESIDUO','MENOR_QUE','MENOR_IGUAL','MAYOR_QUE','MAYOR_IGUAL','IGUAL',
    'DESIGUAL','DISTINTO','ES_IGUAL','PUNTOYCOMA','COMA','PARENT_IZQ','PARENT_DER','CORCHETE_IZQ',
    'CORCHETE_DER','LLAVE_IZQ','LLAVE_DER','DOS_PUNTOS','ET','HASHTAG','PUNTO','COMILLAS',
    'APOSTROFE', 'IGUALDAD_ESTRICTA', 'DESIGUALDAD_ESTRICTA',

    #OPERADORES LOGICOS
    'AND_LOGICO','OR_LOGICO','NOT_LOGICO',

    #OPERADORES DE ASIGNACION
    'ASIGNACION_MULTI','ASIGNACION_DIVISION','ASIGNACION_RESIDUO','ASIGNACION_SUMA',
    'ASIGNACION_RESTA',

    # OTROS
    'COMMENTS','COMMENTS_C99','VARIABLE','IDVAR','NUMERO','STRING',
)


# RE Tokens

# CARACTERES
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print (chr(27)+"[1;31m"+"\t ERROR: CARÁCTER ILEGAL"+chr(27)+"[0m")
    print ("\t\tLine: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)


#Reserved keywords as of ECMAScript 6
def t_BREAK(t):
    r'break'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CONST(t):
    r'const'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DEBUGGER(t):
    r'debugger'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DELETE(t):
    r'delete'
    return t

def t_DO(t):
    r'do'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_EXPORT(t):
    r'export'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_FINALLY(t):
    r'finally'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_IF(t):
    r'if'
    return t

def t_IMPORT(t):
    r'import'
    return t

def t_IN(t):
    r'in'
    return t

def t_INSTANCEOF(t):
    r'instanceof'
    return t

def t_LET(t):
    r'let'
    return t

def t_NEW(t):
    r'new'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_SUPER(t):
    r'super'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_THIS(t):
    r'this'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_TRY(t):
    r'try'
    return t

def t_TYPEOF(t):
    r'typeof'
    return t

def t_VAR(t):
    r'var'
    return t

def t_VOID(t):
    r'void'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_WITH(t):
    r'with'
    return t

def t_YIELD(t):
    r'yield'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_ALERT(t):
    r'alert'
    return t

# RE SIMBOLOS
t_SUMA      = r'\+'
t_RESTA     = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION  = r'/'
t_IGUAL     = r'='
t_DISTINTO  = r'!'
t_MENOR_QUE  = r'<'
t_MAYOR_QUE  = r'>'
t_PUNTOYCOMA = r';'
t_COMA       = r','
t_PARENT_IZQ = r'\('
t_PARENT_DER = r'\)'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_IZQ    = r'{'
t_LLAVE_DER    = r'}'
t_DOS_PUNTOS   = r':'
t_ET        = r'\&'
t_HASHTAG   = r'\#'
t_PUNTO       = r'\.'
t_COMILLAS    = r'\"'
t_APOSTROFE = r'\''
t_RESIDUO   = r'%'
t_IGUALDAD_ESTRICTA = r'==='
t_DESIGUALDAD_ESTRICTA = r'!=='
t_AND_LOGICO = r'&&'
t_OR_LOGICO  = r'\|\|'
t_NOT_LOGICO = r'!'
t_ASIGNACION_MULTI     = r'\*='
t_ASIGNACION_DIVISION  = r'/='
t_ASIGNACION_RESIDUO   = r'%='
t_ASIGNACION_SUMA      = r'\+='
t_ASIGNACION_RESTA     = r'-='

def t_MENOR_IGUAL(t):
    r'<='
    return t

def t_MAYOR_IGUAL(t):
    r'>='
    return t

def t_DESIGUAL(t):
    r'!='
    return t

def t_ES_IGUAL(t):
    r'=='
    return t

def t_DECREMENTO(t):
    r'--'
    return t

def t_INCREMENTO(t):
    r'\+\+'
    return t

def t_EXPONENTE(t):
    r'\*\*'
    return t

# RE OTHERS


def t_COMMENTS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENTS_C99(t):
    r'(\/\/|\#)(.)*?\n'
    t.lexer.lineno += 1

def t_IDVAR(t):
    r'\$\w+(\d\w)*'
    return t

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_VARIABLE(t):
    r'\w+(\w\d)*'
    return t

def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t

lexer = lex.lex()
script = 'prueba.js'
scriptfile = open(script, 'r')
scriptdata = scriptfile.read()
#print (scriptdata)
lexer.input(scriptdata)

print (chr(27)+"[0;36m"+"INICIO DEL ANÁLISIS LÉXICO"+chr(27)+"[0m")
i = 1
while True:
    tok = lexer.token()
    if not tok:
        break
    print ("\t"+str(i)+" - "+"Linea: "+str(tok.lineno)+"\t"+str(tok.type)+"  -->  "+str(tok.value))
    i += 1

print (chr(27)+"[0;36m"+"FIN DEL ANÁLISIS LÉXICO"+chr(27)+"[0m")
print("Programa elaborado por:"+"\n"
        +"<<Mis Oy Cristina de Jesus>>"+"\n"
        +"<<Poot Can Gener Emmanuel>>"+"\n"
        +"<<Uicab Balam Nanci Arai>>")