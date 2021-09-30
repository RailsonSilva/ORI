# Plotagem

import matplotlib.pyplot as plt

x = [-5, 0, 5]
y = [5, 0, 10]

plt.plot(x,y) # liga pontos com seguimento de reta
plt.show() # mostra o gráfico

# --------------------------------
import numpy as np

x2 = np.arange(1, 5, 0.1) # gera pontos de um até 5 com passo 0.1
y2 = np.exp(x2)

plt.plot(x2, y2, 'g') # terceiro argumento define a cor e/ou formatação do gráfico
plt.show()

# multiplas plotagens 
# --------------------------------

plt.plot(x, y, x2, y2, 'r')
plt.show()
# --------------------------------

#várias plotagens na mesma janela

plt.subplot(1,2,1) # especifica que estamos na plotagem 1 de uma tabela com uma linha e duas colunas

plt.plot(x, y, 'r')
plt.subplot(1,2,2) # especifica que estamos na plotagem 2 de uma tabela com uma linha e duas colunas
plt.plot(x2,y2, '--k')
plt.show()
# --------------------------------

# Exemplo várias janelas de gráfico simultaneas

x4 = np.arange(-5*np.pi, 5*np.pi, 0.1)
y4 = np.cos(x4)
x5 = np.arange(-10, 10, 0.1)
y5 = x5**2 + 2*x5
plt.figure(1) #muda a figura corrente para a figura 1
plt.plot(x4, y4, 'g-')
plt.axis([-5*np.pi, 5*np.pi, -5, 5]) # define a janela de visualização dos eixos x e y

plt.figure(2 )#muda a figura corrente para a figura 1
plt.plot(x5, y5, 'b--')

plt.show()
# --------------------------------

# Exemplo: histogramas(gráficos de colunas)
x6 = [4,8,11,17,14,25]

n, bins, patches = plt.hist(x6, 3)
plt.show()

# --------------------------------

# Exemplo histograma com valores aleatórios

media = 100
desvpad = 15
x7 = media + desvpad*np.random.randn(10000) # gera 10000 aleatórios
n, bins, patches = plt.hist(x7, 50, edgecolor = 'black', linewidth=1.0)

plt.xlabel('Inteligência') #adiciona nome a label X
plt.ylabel('Contagem') #adiciona nome a label X
plt.title('Histograma de QI') # adiciona titulo ao código

plt.grid(True) # adiciona grade ao gráfico

plt.show()

# --------------------------------

pos = [1, 2, 3, 4]
alturas = [42, 20, 16, 4]
estados = ['SP', 'MG', 'RJ', 'ES']

plt.bar(pos, alturas, color=('b','r','y','g'), tick_label = estados)
plt.title('População dos estados do sudeste')
plt.ylabel('Milhões de habitantes')
plt.xlabel('Estado')
plt.show()

# --------------------------------

# Exemplo: plotagem em 3 dimensões
# gráfico do parabolóide hiperbólico z = (-1/6)x**2 + (1/4)y**2
# para x e y no intervalo [-20 20]. Vamos usar passo 0.5

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection = '3d')

x = np.arange(-20, 20.5, 0.5)
y = np.arange(-20, 20.5, 0.5)

X, Y = np.meshgrid(x, y) # gera a matrizes X e Y  que representam o produto cartesiano entre x e y

Z = -(X**2)/6 + (Y**2)/4

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride = 1, cmap = cm.jet)
fig.colorbar(surf)

plt.show()

