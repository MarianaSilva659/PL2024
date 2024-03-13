import ply.lex as lex


tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'ATRIBUTO',
    'MAIOROUIGUAL',
    'NUMERO',
    'VIRGULA',
)

t_SELECT = r'[Ss][Ee][Ll][Ee][Cc][Tt]'
t_FROM = r'[Ff][Rr][Oo][Mm]'
t_WHERE = r'[Ww][Hh][Ee][Rr][Ee]'
t_MAIOROUIGUAL = r'\>\='
t_VIRGULA = r','

def t_NUMERO(t):
    r"\d+"
    #estamos a converter a string para um inteiro
    t.value = int(t.value)
    return t


# O t.type identifica os casos em que temos um SELECT que entra no cado da expressão regular
# no entanto não queremos que fique como atributo 
def t_ATRIBUTO(t):
    r'\b[a-z]\w+\b'
    palavrasReservadas = {
        'select': 'SELECT',
        'from': 'FROM',
        'where': 'WHERE',
    }

    t.type = palavrasReservadas.get(t.value.lower(), 'ATRIBUTO')
    return t

#Para ignorar os espaços entre números
t_ignore = " \t\n"


# Para dar erro 
def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)
    


lexer = lex.lex()

frase = "Select id, nome, salário fRom empregados WHERE salário >= 820"


lexer.input(frase)

for tok in lexer:
    print(tok)
