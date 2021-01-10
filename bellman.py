import random
from timeit import timeit;
from time import time
lista=[]
flag=True
i=0
tamaño=200
while flag:
    if (len(lista) ==tamaño):
        flag = False
        break
    n=random.randrange(tamaño)
    if(n not in lista):
        i=i+1
        lista.append(n)
    #print(random.randrange(10))
#print(lista)
p=[]
for i in range(tamaño):
   p.append(str(i))
dictio=dict(zip(p,lista))
print(dict)
#dict={}
flag=True
i=0
while flag:
    if(i==tamaño):
        flag=False
        break
    k = random.randrange(tamaño)
    n=random.randrange(200)
    l=random.randrange(tamaño)
    m = random.randrange(200)
    if(dictio[str(i)]!=str(k) and dictio[str(i)]!=str(l)):
        #print(dict.keys(),str(k),str(l))
        dictio[str(i)]={str(k):n,str(l):m}
       # print(dict)
        i=i+1









def bellman_ford(graph, source):
    # Step 1: Prepare the distance and predecessor for each node
    archivo = open(
        "C:\\Users\\allis\\OneDrive - Escuela Superior Politécnica del Litoral\\ANALISIS DE ALGORITMOS\\Proyecto 1P\\tiemposBellmn.txt",
        "a", encoding="utf8")
    tiempoinicial = time()

    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    # Step 2: Relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            #print("")
            for neighbour in graph[node]:
              #  print(str("graph[node]: ") , graph[node])
               # print("neighbour: " + neighbour)
                # If the distance between the node and the neighbour is lower than the current, store it
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node
                #    print(distance[node]+graph[node][neighbour])

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Negative weight cycle."

    tiempofinal = time()
    tiempo = tiempofinal - tiempoinicial
    trama = "El tiempo que toma Bellman con "+ str(len(graph)) +" nodos en ejecutarse es de: " + str(tiempo) + "\n"
    archivo.write(trama)
    archivo.close()
    return distance, predecessor


if __name__ == '__main__':
   # Nodo Inicio a calcula las rutas mas cortas hacia los demás nodos
 #   print("Nodo Inicial a")
 #   print(dictio)
    distance, predecessor = bellman_ford(dictio, source='0')
    print(distance)

    #print("Nodo Inicial b")
    # Nodo Inicio b calcula las rutas mas cortas hacia los demás nodos
#    distance, predecessor = bellman_ford(graph, source='b')
 #   print(distance)
'''
    graph = {
        'a': {'c': 3},
        'b': {'a': 2},
        'c': {'b': 7, 'd': 1},
        'd': {'a': 6}
    }
    print("Nodo Inicial a")
    # Nodo Inicio a calcula las rutas mas cortas hacia los demás nodos
    distance, predecessor = bellman_ford(graph, source='a')
    print(distance)
    # Nodo Inicio b calcula las rutas mas cortas hacia los demás nodos
  #  distance, predecessor = bellman_ford(graph, source='b')
   # print(distance)'''