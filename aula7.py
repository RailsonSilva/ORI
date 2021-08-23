# Conjunto e Dicionário


# =======================================================
# =======================================================
# CONJUNTOS
# =======================================================
# =======================================================

conjunto = { 2,7, True, "Jessica" }
print(conjunto)

#=====================================
#Um item pode aparecer somente 1 vez
c = {3,4,4,4,4,4,4,3}
print(c)

#=====================================
#Não existe ordem para os elementos de um conjunto
#tentativas de procurar por indices gera erro, ex.: c[0]
#OU ESTÁ DENTRO OU FORA

#=====================================
#apenas objetos imutáveis
# c3 = {4,[7,8,9]} # - gera erro

primos = {1,3,4,5,6,11,13,17}
result = 10 in primos # a operação de verificação de item é mais rápida com conjunto(em teoria)
print(result)

intervalo = range(0, 1000000)
lista = list(intervalo)
print(len(lista))
conjunto = set(intervalo) #set é o nome da classe dos conjuntos
print(len(conjunto))

print(999999 in lista)
print(999999 in conjunto)

#=====================================
#Métodos para conjuntos:

# DADO UM CONJUNTO C

# C.add(x) : adiciona x ao conjunto
# C.clear() : remove todos os elementos do conjunto
# C.difference( C2 ): retorna o conjunto diferença entre C e C2
# C.intersection( C2 ): retorna o conjunto interseção entre C e C2
# C.union( C2 ): retorna o conjunto união entre C e C2
# C.remove( x ): remove x do conjunto
# C.pop(): remove um elemento do conjunto e o retorna

# =======================================================

# Exemplo difference
c1 = {1, 2, 3, 4}
c2 = {2, 4, 6, 8}
print(c1.difference(c2))

# =======================================================
cvazio = set() # gera um conjunto vazio

# =======================================================
# =======================================================

# DICIONÁRIOS

# =======================================================
# =======================================================
# 'chave':'item'
d1 = {'estado':'MG' , 'cidade':'Uberlândia', 'bairro':'fundinho'}
# no dicionário acima temos 3 elementos. Todo item do dicionário ele precisa estar associado a uma chave

# Chaves:'estado','cidade','bairro'
# Itens: 'MG', 'Uberlândia', 'fundinho'

# =======================================================

# a ordem que os elementos são armazenados é aleatória. Sem indice.
# só pode ser acessado pela sua respectiva chave
print(d1['bairro']) #acessando o item pela chave

#porém as chaves podem ser números
duni = {1:'UFU', 2:'UFRJ', 5:"USP"}
print(duni[1])

# para acrescentar um item no dicionário basta fazer uma atribuição

duni[4] = 'PITAGORAS'
print(duni)

#trocando o item associado a uma chave
duni[1] = 'UERJ'
print(duni)

#a chave só pode estar associada a 1 item, porém itens iguais podem estar armazenados em outras chaves

# chaves só podem ter objetos imutáveis
# como exemplo tuplas

# =======================================================

# podemos remover elementos usando o operador del
del duni[1]
print(duni)
# =======================================================

# acessando dicionário dentro de dicionário
d2 = { 7: {10: 'a', 20: 'c'}, 8:{77:'ga', 88:'hh'}}
d2[8][77] = 'ra'
print(d2[8][77])
# =======================================================

# quantidade de elementos no dicionário
print(len(duni))

# =======================================================

# operador in só serve para verificar se um objeto é chave, não funciona nos itens
print('UFRJ' in duni) #retorna False
print(4 in duni) #retorna True

# =======================================================
d4 = { } #gera dicionário vazio, facilmente confundido com conjuntos vazios
d5 = dict() #gera dicionário vazio
# =======================================================
# Métodos para dicionário
# =======================================================
# Dado um dicionário D
# D.get( x, v(argumento opcional)) : se x for chave em D, retorna o respectivo item. Se x não vou chave em D, retorna v
# D.keys() : retorna um objeto sequencial com as chaves de D
# D.values() : retorna um objeto sequencial com todos os itens do D

print(duni)

listaDuni = list(duni.keys() ) #obtendo uma lista com as chaves duni
print(listaDuni) # lista das chaves - [2,5,4]

valoresDuni = list(duni.values() ) 
print(valoresDuni) #lista dos valores - ['UFRJ', 'USP', 'PITAGORAS']

#podemos percorrer um dicionário usando for
for chave in duni.keys(): 
    print(duni[chave])

for item in duni.values(): 
    print(item)

for c in duni: 
    print(c)

