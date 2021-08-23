itensRemocao = ["o", "a", "um", "uma", "de", "do"]

texto = input("Digite um texto: ")

textoMinusculo = texto.lower()
palavras = textoMinusculo.split()

# NÃO FAZER
# for p in palavras:
#     if p in itensRemocao:
#         palavras.remove(p)

# ======================================================

# PODE FAZER

# i = 0
# while i< len(palavras):
#     if palavras[i] in itensRemocao:
#         palavras.pop(i)
#     else:
#         i += 1



# ======================================================

# A SOLUÇÃO MAIS ELEGANTE SERIA CONSTRUIR UMA NOVA LISTA
# compreensões de listas
palavrasFiltradas = [p for p in palavras if p not in itensRemocao]
print(" ".join(palavrasFiltradas))

#imprimindo as palavras
print("Palavras do texto: ")
for i in range(len(palavrasFiltradas)):
    print(palavrasFiltradas[i])

# ======================================================
# exemplo função Lambda(anônima)
nomes = ['Zelia', 'raquel', 'flavia', 'jessica', 'Maria']
nomes.sort( key = lambda x: x.lower())
print(nomes)
# resultado = ['flavia', 'jessica', 'Maria', 'raquel', 'Zelia']
# ======================================================
