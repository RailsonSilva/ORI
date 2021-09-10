# NOTEBOOK AULA 5 - 27/07/2021 está com o mesmo link do NOTEBOOK da aula 22/07/2021
################################### Cópia de lista ###################################

L1 = [1,2,3]
print(L1)

L2 = L1     # L2 vai apontar para a mesma lista que L1 aponta(NÃO GERA CÓPIA)

L2[0] = 500
print(L2)
print(L1)
print("\n")

################################### Cópia Rasa ###################################

R1 = [1, 2, 3]
R2 = list(R1)  # o contrutor da classe list gera uma cópia rarsa
R2[0] = 500
print(R2)
print(R1)

# R2 = R1[ : ] - Também gera cópia rasa
# operação de concatenação de lista também gera cópia rasa, gerando uma nova lista
print("\n")
R2 = R1 + []
print(R2)

# A cópia rasa funciona bem quando a lista só tem objetos imutáveis. 
# No caso abaixo, como uma lista dentro da lista, R3 também muda. Nesse caso, utilizar cópia profunda.
print("\n")
R3 = [7,[4,5] ]
R4 = list(R3)
print(R4)
R4[1][0] = 200
print(R4)
print(R3)
print("\n")

################################### Cópia profunda ###################################

import copy
R3 = [7, [4,5] ]
R4 = copy.deepcopy( R3 )
R4[1][0] = 200
print(R4)
print(R3)

################################### Operações com listas ###################################

# Construtor: list
# Compimento: len
# Lista vazia: [ ]
# concatenação: +
# repetição: *
# remoção de elementos: del
# Participação como membro: in, not in

################################### Alguns métodos para lista ###################################

####### Append #######
# append: anexa um elemento ao final da lista
# Importante: o método append não retorna nada! 
# Ex: R7 = R7.append(40) - Você perde sua lista para um elemento None #ERRADO
# R7.append(40) #CERTO

####### sort #######

# sort: ordena a lista - Também retorna None
# R8 = [6, -1, 100, 8, 230, 14]
# R8.sort() #ordena a lista R8 crescente
# resultado: [-1, 6, 8, 14, 100, 230] 
# R8.sort( reverse = True) #ordena a lista R8 decrescente
# resultado: [230, 100, 14, 8, 6, -1]

####### count #######

# count(X): retorna quantas vezes X aparece na lista
# R9 = [1,2,3,2,4,2]
# R9.count(2)
# resultado = 3

######################################################################

################################### Processamento de textos ###################################

# Strings são imutáveis, listas servem para fazer processamento de textos
# Podemos fazer conversão para lista

nome = "jessica"
lnome = list(nome)
print(lnome)

#após fazer a conversão para lista pode editar os elementos

lnome[0] = 'g'
print(lnome)

lnome[2:4] = ['ç']
print(lnome)

# após isso, converter novamente para String

jnome = "".join(lnome)
print(jnome)
print(nome)

################################### Compreensão de lista ###################################

numeros = [1,2,3,4,5,6]
# potencia 2 - Exemplo normal
quadrados = []
for x in numeros:
    quadrados += [x**2]
print(quadrados)

#potencia 2 - Exemplo compreensão de lista
quadrados = [ x**2 for x in numeros]
print(quadrados)

#fatorial - Exemplo compreensão de lista
import math
fatoriais = [ math.factorial(y) for y in numeros]
print(fatoriais)


# apenas impares/pares
impares = [x for x in numeros if x%2 == 1]
print("Impares:", impares )
pares = [x for x in numeros if x%2 == 0]
print("Pares:", pares )

# cubo dos elementos pares
cubo_pares = [x**3 for x in numeros if x%2 == 0]
print("Cubo dos elementos pares da lista: ", cubo_pares)
