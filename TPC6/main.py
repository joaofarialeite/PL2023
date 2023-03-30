import ply.lex as lex


tokens = [
    'INT',
    'FUNCTION',
    'PROGRAM',
    'ID',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'COMMA',
    'COLON',
    'DOT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULO',
    'ASSIGN',
    'LT',
    'GT',
    'LE',
    'GE',
    'EQ',
    'NE',
    'AND',
    'OR',
    'NOT',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'IN',
    'PRINT',
    'COMMENT',
    'NUMBER',
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
]


t_OPEN_BRACKET = r'\['
t_CLOSE_BRACKET = r'\]'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','
t_COLON = r':'
t_DOT = r'\.'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_ASSIGN = r'='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_NUMBER = r'\d'
t_ignore = ' \t'

# Estes tokens tem de ser defenidos ANTES do t_ID e em FUNÇÕES porque se não o que vai acontecer é que o t_ID
# vai ser lido primeiro e vai captar todas as palavras (ex :int, if,else,while...)
# OU SEJA O COMPILADOR LÊ PRIMEIRO OS TOKENS DEFENIDOS EM FUNÇÕES E SO DEPOIS É QUE LÊ OS TOKENS SIMPLES (ex : t_ah = r'ah')

def t_INT(t):
    r'int'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_PROGRAM(t):
    r'program'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t

def t_IN(t):
    r'in'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_COMMENT(t):
    r'\/\/.*'
    pass

# Este tem de ser defenido em ultimo porque se não os print,in,while.. dao todos como t.type = ID,
# porque aparecem depois do t_ID e o t_ID captura-os

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()


codigo = '''/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}'''


lexer.input(codigo)

for token in lexer:
    print(token)