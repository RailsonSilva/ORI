# RAILSON DA SILVA MARTINS
# 11811BSI208
# CONCLUIDO DIA 10/09 

from os import close
import nltk

arq = open("base.txt")
linhas = arq.readlines() #le o arquivo e armazena as linhas

arquivos = {}
i = 0
for linha in linhas:
    linha = [p for p in linha if p not in ("\n")] #tira o \n da separação das linhas
    linha = "".join(linha) #transforma em string
    arquivos[i] = linha
    
    i+=1

arq.close() # fecha arquio base.txt

str1_arq = open(arquivos[0]) 
str1 = str1_arq.readlines()
str1 = "".join(str1)
str1 = str1.lower()
str1_arq.close() #fecha arquio a.txt

str2_arq = open(arquivos[1])
str2 = str2_arq.readlines()
str2 = "".join(str2)
str2 = str2.lower()
str2_arq.close() #fecha arquio b.txt

str3_arq = open(arquivos[2])
str3 = str3_arq.readlines()
str3 = "".join(str3)
str3 = str3.lower()
str3_arq.close() #fecha arquio c.txt

def limpaTexto(texto): # tira a pontuação e cria uma nova lista
    str = list(texto) #transforma para lista
    texto_filtrado = [p for p in str if p not in ("!", ".", ",", "?", "...")] #cria uma nova lista sem a pontuação
    texto_filtrado = "".join(texto_filtrado) #transforma novamente para string
    texto_filtrado = texto_filtrado.split() #transforma em uma lista de strings
    texto_filtrado = [i for i in texto_filtrado if i not in nltk.corpus.stopwords.words("portuguese")]
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

str1_filtrada = limpaTexto(str1) #chama função para limpar texto e retirar as stopwords
str2_filtrada = limpaTexto(str2)
str3_filtrada = limpaTexto(str3)

palavras = set()
#adicionar todas as palavras em um conjunto
for c in str1_filtrada: 
    if c not in palavras:
        palavras.add(c)
for c in str3_filtrada:
    if c not in palavras:
        palavras.add(c)
for c in str2_filtrada:
    if c not in palavras:
        palavras.add(c)
palavras = sorted(palavras) # deixa o conjunto em ordem alfabética(ascii)

indice = {}
indice[1] = contaCaracteres(str1_filtrada) #faz a contagem de vezes que a palavra apareceu na frase
indice[2] = contaCaracteres(str2_filtrada)
indice[3] = contaCaracteres(str3_filtrada)

indice1 = set()
indice2 = set()
indice3 = set()

palavras_indice = dict()
arquivo = open("indice.txt", "w") #cria arquivo indice.txt
for c in palavras: #for na lista das palavras criada em ordem ascii
    i = 1 #contador de indíce do dicionário
    arquivo.write("{}: " .format(c)) #imprime palavra que está sendo analisada
    while i <= len(indice): 
        if c in indice[i]: # se a palavra existe no indice imprime qual o indice e quantas vezes apareceu
            arquivo.write("{},{} " .format(i, indice[i][c]))
            if i == 1:
                indice1.add(c) #armazena as palavras que estão no indice invertido informado
            if i == 2:
                indice2.add(c)
            if i == 3:
                indice3.add(c)
        i+=1
    arquivo.write("\n")# adiciona ENTER após concluir uma palavra
arquivo.close() #fecha arquivo indice.txt
# Indice invertido ---------------------------------------

consulta = open("consulta.txt") # lê o arquivo 
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
    
    i1 = 0
    i2 = 0
    i3 = 0
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
                if c not in indice1:
                    i1 = i1 + 1
                    if(i1 == len(s1)) or len(s1) == 1:
                        conjunto.add("a.txt")
                if c not in indice2:
                    i2 = i2 + 1
                    if(i2 == len(s1)) or len(s1) == 1:
                        conjunto.add("b.txt")
                if c not in indice3:
                    i3 = i3 + 1
                    if(i3 == len(s1)) or len(s1) == 1:
                        conjunto.add("c.txt")
            else:
                if c in indice1:
                    i1 = i1 + 1
                    if(i1 == len(s1)) or len(s1) == 1:
                        conjunto.add("a.txt")
                if c in indice2:
                    i2 = i2 + 1
                    if(i2 == len(s1)) or len(s1) == 1:
                        conjunto.add("b.txt")
                if c in indice3:
                    i3 = i3 + 1
                    if(i3 == len(s1)) or len(s1) == 1:
                        conjunto.add("c.txt")
        else:
            if c in indice1:
                i1 = i1 + 1
                if(i1 == len(s1)) or len(s1) == 1:
                    conjunto.add("a.txt")
            if c in indice2:
                i2 = i2 + 1
                if(i2 == len(s1)) or len(s1) == 1:
                    conjunto.add("b.txt")
            if c in indice3:
                i3 = i3 + 1
                if(i3 == len(s1)) or len(s1) == 1:
                    conjunto.add("c.txt")
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