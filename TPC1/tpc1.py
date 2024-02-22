

def adicionarValores(dados, id, informacoes,  nomes):
        if id in dados:
            dados_id = dados[id]
            for informacao, nome in zip(informacoes, nomes):
                dados_id[nome] = informacao
        else:
            dados[id] = {}
            dados_id = dados[id]
            for informacao, nome in zip(informacoes, nomes):
                dados_id[nome] = informacao

def parser(arquivo):
    dados = {}
    nomes = []
    indice = 0

    for linha in arquivo:
            informacoes = linha.strip().split(',')
            if indice != 0:
                if informacoes:
                    id = informacoes[0]
                    if id not in dados:
                        dados[id] = {}

                    adicionarValores(dados, id, informacoes[1:], nomes[1:])
                else:
                    print("Linha vazia")
            else:
                    nomes = informacoes
            indice += 1
    return dados


def getModalidadesOrdenada(dados):
    modalidades = []
    for id, informacoes in dados.items():
        if informacoes["modalidade"] not in modalidades:
            modalidades.append(informacoes["modalidade"])
    modalidades.sort()
    return modalidades

def percentagemAtletasAptos(dados):
    resultadosAptos = 0
    resultadosInaptos = 0
    numeroDeAtletas = 0
    for id, informacoes in dados.items():
        if informacoes["resultado"] == "true":
            resultadosAptos += 1
        if informacoes["resultado"] == "false":
            resultadosInaptos += 1
        numeroDeAtletas += 1
    
    return ((resultadosAptos/numeroDeAtletas)*100,(resultadosInaptos/numeroDeAtletas)*100)


def posicaoLista(idadeMenor, idade):
    posicao = 0
    idade1 = idadeMenor+4
    for i in range(idade1, idade, 5):
        posicao += 1
    return posicao
        
def escalaoEtario(dados):
    primeiro_elemento = next(iter(dados.values()))
    idadeMaisBaixa = primeiro_elemento["idade"]
    idadeMaisAlta = primeiro_elemento["idade"]
    listaID = []
    for _, informacoes in dados.items():
        if informacoes["idade"] < idadeMaisBaixa:
            idadeMaisBaixa = informacoes["idade"]
        if informacoes["idade"] > idadeMaisAlta:
            idadeMaisAlta = informacoes["idade"]  
    for i in range(int(idadeMaisBaixa), int(idadeMaisAlta), 5):
        lista = []
        listaID.append(lista)
    for id, informacoes in dados.items():
        listaID[posicaoLista(int(idadeMaisBaixa), int(informacoes["idade"]))].append(id)
    return listaID
    
       
    