import ply.yacc as yacc
import sys
from gramma_LEX import tokens

simbol = ('Erro', '', 0, 0)


def parserError(s):
    print("Erro sintatico: ", s)

def rec_term(simb):
    global simbol
    if simbol.type == simb:
        simbol = lexer.token() 
    else:
        parserError(simb) 

def rec_elem():
    global simbol
    if simbol.type == 'VAR' or simbol.type == 'NUM':
        print("Reconheci p8, valor=\'" +  str(simbol.value) + '\'')
        simbol = lexer.token() 
    else: 
        parserError("elem nao reconhecido")

def rec_op():
    global simbol
    if (simbol.type == 'SUM' or simbol.type == 'DIV' or simbol.type == 'MUL' or simbol.type == 'SUB'):
        print("Reconheci p9, valor=\'" + str(simbol.value) + '\'')
        simbol = lexer.token() 
    else: 
        parserError("op nao reconhecido")

def rec_expr(): 
    if (simbol.type == 'SUM' or simbol.type == 'DIV' or simbol.type == 'MUL' or simbol.type == 'SUB'):
        rec_op()
        rec_body()
        print("Reconheci p6")
    else:
        print("Reconheci p7")

def rec_body():
    global simbol
    if (simbol.type == 'LPAREN'):
        rec_term('LPAREN')
        rec_body()
        rec_term('RPAREN')
        print("Reconheci p4")
    else: 
        rec_elem()
        rec_expr()
        print("Reconheci p5")

def rec_start():
    global simbol

    if (simbol.type == 'INPUT'): 
        rec_term('INPUT')
        rec_term('VAR')
        print("Reconheci p1")
    elif (simbol.type == 'PRINT'): 
        rec_term('PRINT')
        rec_body()
        print("Reconheci p2")
    elif (simbol.type == 'VAR'):
        rec_term('VAR')
        rec_term('EQ')
        rec_body()
        print("Reconheci p3")
    else:
        parserError(simbol) 

def parser(data):
    global simbol
    print("Parser start")
    lexer.input(data)
    simbol = lexer.token()
    rec_start()
    print("Finish")

linha = input("Insert expression: ")
parser(linha)



