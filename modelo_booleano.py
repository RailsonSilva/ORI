# RAILSON DA SILVA MARTINS
# 11811BSI208
# CONCLUIDO DIA 27/09 


from os import close
import nltk
import sys

if __name__ == "__main__":
    arq = open(sys.argv[1])
    linhas = arq.readlines() #le o arquivo e armazena as linhas

    arquivos = {}
    i = 0
    for linha in linhas:
        linha = [p for p in linha if p not in ("\n")] #tira o \n da separação das linhas
        linha = "".join(linha) #transforma em string
        arquivos[i] = linha

        i+=1

    arq.close() # fecha arquio base.txt

    str_arquivo = {}
    i = 0
    while i < len(linhas):
        str_arq = open(arquivos[i])
        str_arquivo[i] = str_arq.readlines()
        str_arquivo[i] = "".join(str_arquivo[i])
        str_arquivo[i] = str_arquivo[i].lower()
        str_arq.close()
        i = i + 1

    def limpaTexto(texto): # tira a pontuação e cria uma nova lista
        texto_filtrado_stopwords = []
        texto_filtrado_token = nltk.word_tokenize(texto)
        texto_filtrado = [p for p in texto_filtrado_token if p not in ("!", ".", ",", "?", "...")] #cria uma nova lista sem a pontuação
        texto_filtrado = [i for i in texto_filtrado if i not in nltk.corpus.stopwords.words("portuguese")]
        sentencas_etiquetadas = nltk.corpus.mac_morpho.tagged_sents()
        etiquetador_unigram = nltk.tag.UnigramTagger(sentencas_etiquetadas)
        classificação = etiquetador_unigram.tag(texto_filtrado)
        i = 0 
        while i < len(classificação):
            if classificação[i][1] not in ("PREP", "KC", "KS", "ART"):
                texto_filtrado_stopwords.append(classificação[i][0])
            i = i + 1

        texto_filtrado = texto_filtrado_stopwords
        stemmer = nltk.stem.RSLPStemmer()
        i = 0
        while i < len(texto_filtrado):
            texto_filtrado[i] = stemmer.stem(texto_filtrado[i])
            i = i + 1

        return texto_filtrado

    def contaCaracteres(texto):
        freqs = {} #dicionário vazio
        for c in texto:
            if c not in freqs: #verifica se c já é chave
                freqs[c] = 1
            else:
                freqs[c] = freqs[c] + 1
        return freqs

    str_arquivo_filtrado = {}
    i = 0
    while i < len(linhas):
        str_arquivo_filtrado[i] = limpaTexto(str_arquivo[i])
        i = i + 1

    palavras = set()
    #adicionar todas as palavras em um conjunto

    i = 0
    while i < len(linhas):
        for c in str_arquivo_filtrado[i]:
            if c not in palavras:
                palavras.add(c)
        i = i + 1

    palavras = sorted(palavras) # deixa o conjunto em ordem alfabética(ascii)

    indice = {}
    i = 0
    while i < len(linhas):
        indice[i + 1] = contaCaracteres(str_arquivo_filtrado[i]) #faz a contagem de vezes que a palavra apareceu na frase
        i = i + 1

    indice_invert = dict()
    indice_a_dict = dict()
    indice1 = set()
    indice2 = set()
    indice3 = set()

    j = 0
    arquivo = open("indice.txt", "w") #cria arquivo indice.txt
    for c in palavras: #for na lista das palavras criada em ordem ascii
        indice_invertido = []
        i = 1 #contador de indíce do dicionário
        arquivo.write("{}: " .format(c)) #imprime palavra que está sendo analisada
        while i <= len(indice): 
            if c in indice[i]: # se a palavra existe no indice imprime qual o indice e quantas vezes apareceu
                
                arquivo.write("{},{} " .format(i, indice[i][c]))
                indice_invertido.append((i, indice[i][c]))
            i = i + 1
        indice_invert[c] = indice_invertido
        j = j + 1
        arquivo.write("\n")# adiciona ENTER após concluir uma palavra
    arquivo.close() #fecha arquivo indice.txt
    # Indice invertido --------------------------------------
    print(indice_invert['cas'][1][1]) # quantidade de vezes que a palavra "cas" apareceu no documento 2
    i = 1
    while i <= len(indice):
        indice_a = set()
        for c in palavras:
            if c in indice[i]:
                indice_a.add(c)
                
        indice_a_dict[i] = indice_a
        i = i + 1


    consulta = open(sys.argv[2]) # lê o arquivo 
    consulta_read = consulta.readline() #lê a linha do arquivo
    consulta_read = consulta_read.lower()
    consulta_read_filter = consulta_read.split() # separa a frase por palavra

    tem_ou = 0
    i = 0
    while i < len(consulta_read_filter):
            if consulta_read_filter[i][0] == '!' or consulta_read_filter[i].isalpha(): #identifica se é letra ou palavra negativa
                stemmer = nltk.stem.RSLPStemmer() #retira o radical da palavra
                consulta_read_filter[i] = stemmer.stem(consulta_read_filter[i]) #salva na variável
            if consulta_read_filter[i] == "|": 
                tem_ou = 1
            i = i + 1

    consulta_read_filter_radical = " ".join(consulta_read_filter) # junta novamente a string já com o radical da palavra


    def verifica_E_e_NOT(consulta):
        s1 = consulta
        s1 = s1.replace(" ", "") # remove espaços da string 
        s1 = s1.split("&") #separa as strings pelo operador &
        
        i1 = [0]*(len(linhas)+1)
        conjunto = set()
        c2 = set()

        for c in s1: #checa se tem alguma palavra com not e retira o "!" e faz uma lista de palavras que tem not
            if c[0] == "!":
                c1 = c.split("!")
                c1 = c1[1]
                c2.add(c1) #adiciona todas as palavras negativas encontradas

        for c in s1:
            if len(c2) > 0:
                tem = 0
                if c[0] == "!":
                    c = c.split("!")
                    c = c[1]
                    tem = 1

                if tem == 1:
                    i = 1
                    
                    while i <= len(indice_a_dict):
                        
                        if c not in indice_a_dict[i]:
                            i1[i] = i1[i] + 1
                            if(i1[i] == len(s1)) or len(s1) == 1:
                                conjunto.add(linhas[i-1])
                        i = i + 1
                else:
                    i = 1
                    
                    while i <= len(indice_a_dict):
                        
                        if c in indice_a_dict[i]:
                            i1[i] = i1[i] + 1
                            if(i1[i] == len(s1)) or len(s1) == 1:
                                conjunto.add(linhas[i-1])
                        i = i + 1
            else:
                i = 1
                while i <= len(indice_a_dict):
                    
                    if c in indice_a_dict[i]:
                        i1[i]= i1[i] + 1
                        if(i1[i] == len(s1)) or len(s1) == 1:
                            conjunto.add(linhas[i-1])
                    i = i + 1

        return conjunto

    if tem_ou == 1:
        consulta_read_filter_radical = consulta_read_filter_radical.split("|") #separa as frases pelo operador OU
    else:
        consulta_read_filter_radical = consulta_read_filter_radical.split("  ") #deixa a consulta inteira como apenas uma consulta se não tiver operador OU

    consulta_e_not_conj = set()
    i = 0
    while i < len(consulta_read_filter_radical):
        consulta_e_not = dict() # determina como dicioário
        consulta_e_not[i+1] = verifica_E_e_NOT(consulta_read_filter_radical[i]) # chama função e armazena o valor na variavel
        consulta_e_not[i+1] = " ".join(consulta_e_not[i+1]) #transforma em string
        consulta_e_not_conj.add(consulta_e_not[i+1]) #adiciona ao conjunto evitando repetições de documentos
        i = i + 1

    consulta_e_not_conj = " ".join(consulta_e_not_conj) # transforma em string 
    consulta_e_not_conj = consulta_e_not_conj.split() # transforma em lista
    consulta_aparece = len(consulta_e_not_conj) # verifica quantas vezes a consulta é verdadeira
    consulta_e_not_conj = set(consulta_e_not_conj) #trasnforma em conjunto impedindo a repitição para a impressão
    consulta_e_not_conj = sorted(consulta_e_not_conj) #coloca em ordem ASCII

    # --------------------------------------------------
    # gerando arquivo 
    arquivo_resposta = open("resposta.txt", "w") #cria o arquivo
    arquivo_resposta.write("{}" .format(consulta_aparece))
    arquivo_resposta.write("\n")# adiciona ENTER
    for c in consulta_e_not_conj: # for dentro 
        arquivo_resposta.write("{}" .format(c)) # imprime os arquivos que fazem a conjunção verdadeira
        arquivo_resposta.write("\n")# adiciona ENTER
    arquivo_resposta.close() #fecha arquivo resposta.txt
else:
    print("Programa não está sendo executado como principal!")