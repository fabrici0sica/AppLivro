import os

here = os.path.dirname(os.path.abspath(__file__))

def cargascript():
    todas = []
    dicionario = []
    indice = 0
    for i in range(2): # Para cada arquivo na pasta
        filename = os.path.join(here, str(i))
        f = open(filename, 'rt',  encoding='latin-1') #abre o arquivo
        texto = f.read() #transforma em texto
        lista = texto.split() #separa as palavras
        unicos = list(dict.fromkeys(lista)) #palavras unicas antes de tratar
        txtarquivo = []
        for x in unicos: #tratamento
            item = x        
            for y in ['\n', '\t', '.', '-', '(', ')','?','!','[',']','(',')',',',':',';','"']:
                item = item.replace(y, "")        
            txtarquivo.append(item) #palavras tratadas
        txtarquivo = [x.upper() for x in txtarquivo]
        txtarquivo = list(dict.fromkeys(txtarquivo))  #palavras tratadas unicas do texto  
        palavrasnovas = list(set(txtarquivo)-set(todas)) #palavras do arquivo menos a lista de palavras ja existente 
        jaexistem = list(set(todas) & set(txtarquivo)) #intersecção entre palavras ja existentes e as do arquivo
        for x in palavrasnovas:       
            if not x == '':
                dicionario.append((indice,[i])) #adiciona a lista, indice unico, e nome do arquivo
                todas.append(x) #adiciona a palavra ao conjunto de palavras existentes
                indice = indice + 1

        #dicionario = [(dx,dy.append(i)) if dx in jaexistem else (dx,dy) for (dx,dy) in dicionario]
        for x in jaexistem: #para as palavras que ja existem na lista
            dicionario[todas.index(x)][1].append(i) #procura o indice delas na lista e adiciona o arquivo

    filename = os.path.join(here, "dicionario.txt")
    textfile = open(filename, "w")
    for element in dicionario:
        textfile.write(str(element) + "\n")
    textfile.close()

    filename = os.path.join(here, "reverso.txt")
    textfile = open(filename, "w")
    for element in todas:
        textfile.write(str(todas.index(element)) + ': ' + str(element) + "\n")
    textfile.close()