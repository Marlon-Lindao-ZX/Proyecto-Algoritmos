import numpy as np
from time import time
archivo = open(
        "C:\\Users\\allis\\OneDrive - Escuela Superior Politécnica del Litoral\\ANALISIS DE ALGORITMOS\\Proyecto 1P\\tiemposFloyd.txt",
        "a", encoding="utf8")
n=1000
tam=[n,n]
tiempoinicial = time()

# graph = np.array([[0,8,3,5,100],[8,0,2,100,5],[100,1,0,3,4],[6,100,150,0,7],[100,5,100,100,0]])
#graph = np.array([[0, 2, 100, 3, 100, 100, 100], [100, 0, 7, 100, 1, 100, 100], [100, 100, 0, 100, 100, 2, 100],[100, 1, 100, 0, 100, 100, 100], [100, 100, 7, 100, 0, 100, 4], [100, 100, 100, 100, 4, 0, 2],[1, 100, 100, 1, 100, 100, 0]])
graph = np.random.randint(0,101,tam)

print("Adjacency matrix")
print(graph)
v = len(graph)

# path reconstruction matrix
p = np.zeros(graph.shape)
for i in range(0, v):
    for j in range(0, v):
        p[i, j] = graph[i, j]

for k in range(0, v):
    print('D', k + 1, "--------------------")
    for i in range(0, v):
        for j in range(0, v):
            if p[i, j] > p[i, k] + p[k, j]:
                print(i + 1, "-", j + 1, ":", p[i, j],)
                p[i, j] = p[i, k] + p[k, j]
                print(">", p[i, k], '+', p[k, j], '=', p[i, j], "change")
            else:
                print(i + 1, "-", j + 1, ":", p[i, j], "<=", p[i, k], '+', p[k, j], '=', p[i, j])

  #  print(p)

tiempofinal = time()
tiempo = tiempofinal - tiempoinicial
trama = "El tiempo que toma Floyd con "+ str(len(graph)) +" nodos en ejecutarse es de: " + str(tiempo) + "\n"
archivo.write(trama)
archivo.close()