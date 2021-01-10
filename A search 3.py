import numpy as np
from time import time
import random

#
class graph:
    def __init__(self):
        self.graph = {}
        self.visited = {}

    def append(self, vertexid, edge, weight):
        if vertexid not in self.graph.keys():
            self.graph[vertexid] = {}
            self.visited[vertexid] = 0
        self.graph[vertexid][edge] = weight

    def append2(self, vertexid):
        if vertexid not in self.graph.keys():
            self.graph[vertexid] = {}
            self.visited[vertexid] = 0

    def reveal(self):
        return self.graph

    def vertex(self):
        return list(self.graph.keys())

    def edge(self, vertexid):
        return list(self.graph[vertexid].keys())

    def weight(self, vertexid, edge):
        return (self.graph[vertexid][edge])

    def size(self):
        return len(self.graph)

    def visit(self, vertexid):
        self.visited[vertexid] = 1

    def go(self, vertexid):
        return self.visited[vertexid]

    def route(self):
        return self.visited


#
def astar(df, start, end):
    queue = {}
    distance = {}
    heuristic = {}
    route = {}
    queue[start] = 0
    pred = {}

    for i in df.vertex():
        distance[i] = float('inf')
        heuristic[i] = np.abs(i[0] - end[0]) + np.abs(i[1] - end[1])

    distance[start] = 0
    c = 0

    while queue:
        temp = min(queue, key=queue.get)
        queue.pop(temp)
        minimum = float('inf')

        for j in df.edge(temp):
            distance[j] = distance[temp] + df.weight(temp, j)
            route[j] = distance[j] + heuristic[j]
            if route[j] < minimum:
                minimum = route[j]

        for j in df.edge(temp):
            if (route[j] == minimum) and (df.go(j) == 0) and (j not in queue):
                queue[j] = route[j]
                pred[j] = temp

        df.visit(temp)

        if temp == end:
            break

        c += 1

    k = end
    path = []

    print('vertice travelled:', c)
    return distance[end], path


graph = graph()
lista = [100,200,500,1000,2000]
lista2 = {}
lista3 = []


for l in lista:
    start = (0,0)
    goal = (l-1,l-1)
    for i in range(l):
        for j in range(l):
            graph.append2((i,j))

    for i in range(20):
        val2 = random.randrange(l)
        val3 = random.randrange(l)
        while val2 == l - 1 & val3 == l - 1:
            val2 = random.randrange(l)
            val3 = random.randrange(l)
        graph.append((val2, val3), (l - 1, l - 1), 1)
        a = random.randrange(l*2) + 10
        for k in range(a):
            val4 = random.randrange(l)
            val5 = random.randrange(l)
            while val4 == val2 & val5 == val3:
                val4 = random.randrange(l)
                val5 = random.randrange(l)
            graph.append((val4, val5), (val2, val3), 1)
            val2 = val4
            val3 = val5
        graph.append((0, 0), (val2, val3), 1)


    archivo = open("C:\\Users\\CORE I7\\Downloads\\tiempos-A.txt", "a", encoding="utf8")
    tiempoinicial = time()
    route = astar(graph, start, goal)
    tiempofinal = time()
    tiempo = tiempofinal - tiempoinicial
    trama = "El tiempo que toma A * en ejecutarse con un grafo de: " + str(l) + " es de: " + str(tiempo) + "\n"
    archivo.write(trama)
    archivo.close()

