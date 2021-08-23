import nltk
from nltk.tokenize import punkt

stopwords = nltk.corpus.stopwords.words("portuguese")
print(stopwords)

#podemos usar o nltk para tokenizar texto:
#por palavras:

print("\n\n\n===========================")
frase = "Oi, Tim! Está vivo? Claro."
palavras = nltk.word_tokenize(frase)
print(palavras)

print("\n\n\n===========================")

#podemos extrair radicais de palavras em português
stemmer = nltk.stem.RSLPStemmer()
print(stemmer.stem("professora")) #retorna radical de professora - profes
print(stemmer.stem("luminosidade")) #retorna radoical de luminosidade

print("\n\n\n===========================")

# from nltk.corpus import mac_morpho
# sentencas_etiquetadas = mac_morpho.tagged_sents()
# sentencas_etiquetadas

# Unigram tagger - Etiquetador baseado em frequência estatística a partir de uma base de treinamento como mac_morpho.tagged_words()

#exemplo: código para classificar as palavras de uma frase:

import nltk

#obtendo as sentencas etiquetadas do corpus mac_morpho
sentencas_etiquetadas = nltk.corpus.mac_morpho.tagged_sents()

#definindo o texto a ser classificado
texto = "Já chegou o disco voador!"

#separa o texto em tokens de palavras
tokens_texto = nltk.word_tokenize(texto)

#instanciando etiquetador unigram e treinando com as sentenças etiquetadas
etiquetador_unigram = nltk.tag.UnigramTagger( sentencas_etiquetadas )

#usando o etiquetador para classificar tokens do texto:
classificacao = etiquetador_unigram.tag( tokens_texto )

print( classificacao )