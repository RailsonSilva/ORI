# RAILSON DA SILVA MARTINS
# 11811BSI208
# Concluído em 22/08

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

arquivo = open("indice.txt", "w") #cria arquivo indice.txt

for c in palavras: #for na lista das palavras criada em ordem ascii
    i = 1 #contador de indíce do dicionário
    arquivo.write("{}: " .format(c)) #imprime palavra que está sendo analisada
    while i <= len(indice): 
        if c in indice[i]: # se a palavra existe no indice imprime qual o indice e quantas vezes apareceu
            arquivo.write("{},{} " .format(i, indice[i][c])) 
        i+=1
    arquivo.write("\n")# adiciona ENTER após concluir uma palavra
arquivo.close() #fecha arquivo indice.txt