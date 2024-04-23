import sys
import ply.lex as lex


tokens = (
   'INPUT',  
   'PRINT',  
   'EQ',     
   'MUL',    
   'DIV',    
   'SUM',    
   'SUB',    
   'LPAREN', 
   'RPAREN', 
   'NUM',   
   'VAR',    
)

t_INPUT = r'\?'
t_PRINT = r'!'
t_EQ = r'='
t_MUL = r'\*'
t_DIV = r'/'
t_SUM = r'\+'
t_SUB = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUM = r'[1-9]+'
t_VAR = r'[a-zA-Z]+'

t_ignore = ' \t\r\n' 

def t_error(t):
    print("Caracter nao reconhecido:'%s'" % t.value[0])
    t.lexer.skip(1)

def t_eof(t):
    r'$'
    t.value = None

lexer = lex.lex()