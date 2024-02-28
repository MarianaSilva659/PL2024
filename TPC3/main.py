import re

def main():
    expressao = r'([Oo][Nn]|[Oo][Ff]{2})|((?:\+|\-)?\d+(?:\.\d+)?E?)|(\=)'
    isON = r'[Oo][Nn]'
    isOFF = r'[Oo][Ff]{2}'
    somaMais = True
    soma = 0
    padraoON = re.compile(r'on', re.IGNORECASE)
    padraoOFF = re.compile(r'of', re.IGNORECASE)
    
    with open("ficheiro.txt", 'r', encoding='utf-8') as file:
        conteudo = file.read() 
        capturas = re.findall(expressao, conteudo)
        for captura in capturas:
            if re.match(isON,captura[0]) and captura[0]:
                somaMais = True
            elif re.match(isOFF, captura[0]) and captura[0]:
                somaMais = False
            elif captura[2]:
                print("Valor da soma = ", soma)
            elif captura[1]:
                if somaMais == True:
                    soma += int(captura[1])
        
main()