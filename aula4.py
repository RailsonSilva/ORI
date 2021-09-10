# Funções - AULA 4 - 22/07/2021 
def fatorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n* fatorial(n-1)
    else:
        raise ValueError
        #return None

def fatorial_nr(n):
    f  = 1
    for k in range(1, n+1, 1):
        f = f*k
    return f

def aplica(lista, funcao):
    for k in range(0, len(lista) ):
        lista[k] = funcao(lista[k])
    return lista

def combinacao(n, p):
    fat = fatorial_nr

    return fat(n)//(fat(n-p)*fat(p))

total = fatorial(4)
total_nr = fatorial_nr(1)
lista = aplica([2,4,6,8,10], fatorial)
combinar = combinacao(1000,2)
print(total)
print(total_nr)
print(lista)
print(combinar)

# Percorrendo sequências ordenadas

primos = [1,3,5,7,11,13,17,19]
for n in primos:
    print(n)

for i in range(0, len(primos)):
    print(primos[i])

i = 0
while i < len(primos):
    print( primos[i])
    i += 1

# listas são mutáveis
L = [1, "JESSICA", 2+1j, -3.14, (19,23)]
print(type(L))

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros[0:4])

pares = list(range(2,21,2))
print(pares)
print(pares[4:9])

valores = list(range(150, 241,10))
print(valores)
print(valores[2:5])

valores[2:5] = [-1, -2, -3]
print(valores)

valores[0:5] = [7,8] # troca os 5 valores pela lista nova
print(valores)

valores[3:5] = primos
print(valores)

del valores[3] #remove o indice 3
print(valores)

valores[0:5] = []
print(valores)

valores[0:7:2] = ["jessica", "carol", "mariana", "raquel"]
print(valores)

#########################

print("\n")
def soma(*valores): # *recebe numero arbitrário de argumentos
    s=0
    for v in valores:
        s = s + v
    return s

valor = soma(1,2,3,4,5,6,7,8,45,2,3,423,4,3,2,5,6,4)
print(valor)