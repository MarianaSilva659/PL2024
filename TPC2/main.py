import re



def meteTitulo(match):
    num = match.group(1)
    criarStringHTML = "<h" + str(len(num)) + ">" + match.group(2) + "</h" + str(len(num)) + ">"
    return criarStringHTML

def parserMDAndConvertHTML(filename):
    # tag -> #
    tag1 = r"(^#+) (.+)$"
    
    #**exemplo**
    tag2 = r"\*\*(.+)\*\*"
    
    #*exemplo*
    tag3 = r"\*(.+)\*"
    
    #lista
    #encontrar os elementos da  lista
    tag4_1 = r"^[1-9][0-9]*\. (.+)"
    #encontrar o último da lista
    tag4_2 =r'(.+)</li>\n([^"<li>"])'
    #para encontrar o inicio da lista que
    tag4_3 = r'[^"</li>"]\n^<li>(.+)'
    
    #link
    tag5 = r"\[(.+)\]\((.+)\)"
    
    #imagens
    tag6 = r"!\[(.+)\]\((.+)\)"
    
    html = '''

    <!DOCTYPE html>
    <html>
    <head>
        <title>TPC2</title>
        <meta charset="UTF-8">
    </head>
    <body>

    '''
    
    with open(filename, 'r', encoding='utf-8') as file:
        conteudo = file.read()
        #re.MULTILINE é usada para garantir que a expressão regular corresponda a cada linha individualmente

        conteudo = re.sub(tag1, meteTitulo, conteudo, flags=re.MULTILINE)
       # conteudo = re.sub(tag1, r"<h1>\1</h1>", conteudo,  flags=re.MULTILINE)
        conteudo = re.sub(tag2, r"<b>\1</b>", conteudo, flags=re.MULTILINE)
        conteudo = re.sub(tag3, r"<i>\1</i>", conteudo, flags=re.MULTILINE)
        conteudo = re.sub(tag6,  r'<img src="\2" alt="\1">', conteudo, flags=re.MULTILINE)
        conteudo = re.sub(tag5, r'<a href="\2">\1</a>', conteudo, flags=re.MULTILINE)
        
        #listas    
        #mete todos os elementos da lista com uma <li<   
        conteudo = re.sub(tag4_1, r'<li>\1</li>', conteudo,  flags=re.MULTILINE)
        #mete todos os elementos que são o fim da lista o </li>
        conteudo = re.sub(tag4_2, r'\1</li>\n</ol>\n\n', conteudo,  flags=re.MULTILINE)
        #mete todos os elementos que começam a lista o <li>
        conteudo = re.sub(tag4_3, r'\r\n<ol>\r\n<li>\1', conteudo, flags=re.MULTILINE)
        
        #print(conteudo)
        html += conteudo
        html += f'''
            </body>
            </html>
        '''     
    fileHTML = open("convertidoHTML.html", "w", encoding="utf-8")
    fileHTML.write(html)
    fileHTML.close()


def main():
    parserMDAndConvertHTML('ficheiro.md')


main()