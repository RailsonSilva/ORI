# Programa que plota o gráfico de seno(x) salvando o gráfico em uma figura

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
x3 = np.arange( -np.pi, np.pi, 0.1)
y3 = np.sin(x3)
plt.plot(x3, y3)
fig.savefig('seno.png') #salva a figura

plt.show()
