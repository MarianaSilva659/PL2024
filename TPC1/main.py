from tpc1 import parser, getModalidadesOrdenada, percentagemAtletasAptos, escalaoEtario

def main():
    nome_do_arquivo = "emd.csv" 
    dados = parser(nome_do_arquivo)
    modalidades = getModalidadesOrdenada(dados)
    print("Modalidades: ", modalidades)
    
    (aptos, inaptos) = percentagemAtletasAptos(dados)
    print()
    print("Aptos: ", aptos, "% Inaptos: ", inaptos, "%")
    
    print()
    
    lista = escalaoEtario(dados)
    print("Escalão etário: ", lista)
    
main()