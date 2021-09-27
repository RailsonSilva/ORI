# NUMPY (numerical python)

# Biblioteca de computação numérica
# ---------------------------------------------------------
# Dois tipos principais de objetos:

# ndarray: array de dimensão qualquer:
# matrix: matrizes de duas dimensões(linhas e colunas)

# Todos os elementos das matrizes e arrays devem ter o mesmo tipo. 

import numpy as np #importa a biblioteca numpy e renomeia como "np"
A = np.matrix([[1,2],[3,4]])
print(A)
print("--------")
#acessando um elemento da matriz:

print(A[0,1])
print("--------")
#acessando uma linha inteira:
print(A[1]) #acessa a linha 1 da matriz
print("--------")

print(A[:,0]) # acessa somente a coluna 0 da matriz.
print("--------")

# ---------------------------------------------------------
# a função zeros gera um array de zeros
M = np.zeros((4,5)) #gera um array de 4 linhas e 5 colunas só de zeros
print(M)
print("--------")
M2 = np.matrix(np.zeros((4,5))) # gera uma matriz de 4 linhas e 5 colunas só de zeros
print(M2)
print("--------")

# ---------------------------------------------------------
# a função ones, gera um array de 1's
N = np.ones((5,8,2)) # array de 5 matrizes de 8 linhas e duas colunas só de 1's
print(N)
print("--------")

N2 = np.matrix(np.ones((5,8))) #matriz de 5 linhas e 8 colunas só de 1's
print(N2)
print("--------")

# ---------------------------------------------------------
# podemos gerar matrizes de coeficientes (pseudo) aleatórios usando o submódulo random
import numpy.random as npr

R = npr.randint(-10, 10, (2,3)) #gera um array 2x3 com coeficientes aleatórios entre -10 e 10
print(R)
print("--------")
R2 = np.matrix(npr.randint(-10 , 10, (2,3))) #gera uma matrix 2x3 com coeficientes aleatórios entre -10 e 10
print(R2)
print("--------")
R3 = npr.randint(5 , 6, (2,3)) #gera um array só de 5's 
print(R3)
print("--------")

# a função eye gera array identidade(array que tem sua diagonal principal com 1's e o restante 0)
B = np.eye(2, 2)
print(B)
print("--------")
# gerando uma matriz 2x2 de um array identidade com números inteiros
B2 = np.matrix(np.eye(2, 2), int)
print(B2)

#apenas exibindo
print("--------")
print(M2) 
print("--------")
print(R2)
print("--------")

#podemos trabalhar com submatrizes
M2[1:3, 1:4] = R2 # atribuiu a matriz R2 para dentro da matriz M2 da linha 1 até a linha 2 e da coluna 1 até a coluna 3
print(M2)
print("--------")

# multiplicando a matriz por um escalar:

B2 = 4*B2
print(B2)
print("--------")

# podemos somar matrizes
C = A+B2
print(C)
print("--------")

#ou multiplicá-las:
D = A * B2
print(D)
print("--------")

#ou fazer potências
print(A**2)
print("--------")

#inversa da matriz
Ainv = A**-1
print(Ainv)
print("--------")
print(A * Ainv)
print("--------")
print(A**0)

# multiplicação entre arrays é elemento a elemento

# matriz transposta - transpose ( inverte a matriz, o que era linha passa a ser coluna e o que é coluna passa a ser linha)

print("--------")
print(np.transpose(A))
print("--------")
print(A.T) #Obtém a matriz transposta
print("--------")

# função trace - obtendo traço: a soma da diagonal principal
print(np.trace(A))
print("--------")

# Concatenar matrizes
# função vstack - por linha (vertical)

print(np.vstack((A,B2)))
print("--------")
print(np.hstack((A,B2)))
print("--------")

#Existem funções que podem ser aplicadas a todos os elementos de uma matriz.
#sqrt, exp, log, sin, cos...

print(np.sqrt(A)) #retorna a raiz dos elementos da matriz
print("--------")
print(np.sum(A)) #retorna a soma dos elementos da matriz
print("--------")
print(np.max(A)) #retorna o maior dos elementos da matriz
print("--------")
print(np.min(A)) #retorna o menor dos elementos da matriz

# ---------------------------------------------------------
import numpy.linalg as la

#calculando autovalores e autovetores de uma matriz
autovals, autovets = la.eig(A)
print("--------")
print(autovals)
print("--------")
print(autovets)

#função det calcula o determinante
print("--------")
print(la.det(A))
print("--------")

# posto da matriz
print(la.matrix_rank(A))
print("--------")

#calcula norma de matrix
print(la.norm(A))
print("--------")
print(la.norm(A, 1))
print("--------")


#resolvendo sistema linear Ax = b
b = np.matrix([[10],[20]])
x = la.solve(A, b)
print(x)