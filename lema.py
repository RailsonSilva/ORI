#exemplo de lematização com o pacote stanza

import stanza


nlp = stanza.Pipeline('pt')

text = ""
pos = ""
lemma = ""

frase = "Está tudo muitíssimo mais do que estudado, professoras"

for sent in nlp(frase).sentences:

    for word in sent.words:
        text += word.text + '\t'
        pos += word.upos + '\t'
        lemma += word.lemma + '\t'

print("text: ", text)
print("pos : ", pos)
print("lemma: ", lemma)