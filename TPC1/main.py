from tpc1 import parser, getModalidadesOrdenada, percentagemAtletasAptos, escalaoEtario
import sys

def main():
    
    conteudo =  sys.stdin
    print(conteudo)
    dados = parser(conteudo)
    modalidades = getModalidadesOrdenada(dados)
    print("Modalidades: ", modalidades)
    
    (aptos, inaptos) = percentagemAtletasAptos(dados)
    print()
    print("Aptos: ", aptos, "% Inaptos: ", inaptos, "%")
    
    print()
    
    lista = escalaoEtario(dados)
    print("Escalão etário: ", lista)
    
main()