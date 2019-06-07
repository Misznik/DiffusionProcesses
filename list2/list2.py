# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:44:02 2019

@author: micha
"""
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {} #slownik polaczen z wagami

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return self.id

    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    

class Graph:
    def __init__(self):
        self.vertList = {}

    def addVertex(self,key):
        newVertex = Vertex(key)
        if key in self.getVertices():
            print("Vertex already in the Graph")
        else:
            self.vertList[key] = newVertex #dodac czy juz istnieje
            return newVertex
            
    
    def addVerticesFromList(self, vertList):
        for i in range(len(vertList)):
            self.addVertex(vertList[i])

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
        
    def __contains__(self,n):
        return n in self.vertList
    
    def addEdge(self,fromVert,toVert,weight=1):
        if fromVert not in self.vertList:
            nv = self.addVertex(fromVert) #new_vertex
        if toVert not in self.vertList:
            nv = self.addVertex(toVert)
        if [fromVert,toVert,weight] in self.getEdges() or [toVert,fromVert,weight] in self.getEdges() or [fromVert,toVert] in self.getEdges() or [toVert,fromVert] in self.getEdges():
            print('Edge already in the graph')
        else:
            self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)
            self.vertList[toVert].addNeighbor(self.vertList[fromVert], weight)
        
    def addEdgesFromList(self,edgeList):
        for i in range(len(edgeList)):
            if len(edgeList[i])==3:
                self.addEdge(edgeList[i][0],edgeList[i][1],edgeList[i][2])
            elif len(edgeList[i])==2:
                self.addEdge(edgeList[i][0],edgeList[i][1])
    #edgeList = [[fromVert,toVert,weight=0],...]

    def getVertices(self):
        verts = [key for key in self.vertList.keys()]
        return verts
        #return self.vertList.keys()

    def __iter__(self):  #zwracanie iteratora
        return iter(self.vertList.values())
    
    def getNeighbors(self, vertKey):
        temp = [x.id for x in self.getVertex(vertKey).connectedTo]
        return temp
    
    def getEdges(self):
        lista=[]
        for key in self.vertList.keys():
           vert = self.getVertex(key)
           for n in vert.getConnections():
               temp = [vert.id, n.id, vert.getWeight(n)] #list of edges
               if [temp[1],temp[0],temp[2]] not in lista:
                   lista.append(temp)
        return lista
           
    def saveGraph(self):
        plik= open("dot_notation.txt","w+")
        plik.write("graph {")
        for edge in self.getEdges():
            plik.write(str(edge[0]) + "--" + str(edge[1])+\
                       ' [ label = ' + str(edge[2]) + ' ];\n')
        for v in self.vertList:
            vert = self.getVertex(v)
            if bool(vert.getConnections()) == False: #sprawdzam czy lista polaczen jest pusta
                 plik.write(str(vert.getId())+';\n') #jesli tak to wypisuje sam wierzcholek
        plik.write("}")
        plik.close()
        
        #wszystkie sciezki z jednego wierzcholka do drugiego
    def getAllPaths(self, fromVert, toVert, path=[]):
        start=self.vertList[fromVert] #tworze funkcje rekurencyjna
        neighbours=start.getConnections()
        path =  path + [start.id]
        if fromVert == toVert: #przypadek proby polaczenia ze soba
            return [path]
        if not neighbours: #przypadek braku polaczen z danego wierzcholka
            return None
        paths = []
        for vertex in neighbours: #iter po sasiadach wierzcholka
            if vertex.id not in path: #szukanie sciezek od nowego wierzcholka
                extendedPaths = self.getAllPaths(vertex.id, toVert, path)
                for p in extendedPaths:
                    paths.append(p) #dodawanie sciezek
        return paths
        
    #najkrotsza sciezka do jednego wierzcholka
    def getShortestPath(self,fromVert, toVert):
        paths=self.getAllPaths(fromVert, toVert) # pobieranie wszystkich sciezek dla wybranych wierz.
        weights=[]
        for path in paths:
            weight=0
            for i in range(0,len(path)-1): #sumowanie wag dla danej sciezki
                weight += self.getVertex(path[i]).getWeight(self.getVertex(path[i+1]))
            weights.append(weight)
        #print(weights)
        if weights != []: #sprwadzam na wypadek wierzcholka wez polaczen
            index=weights.index(min(weights)) #znajdywanie idneksu najmniejszej wagi
            return {weights[index]: paths[index]}
        else:  #dla braku polaczen zwracam pusta sciezke
            #return {'no connections': []} 
            return {9223372036854775807: []} #skoro nie mozna korzystac z sys :c
        #zwracanie slownika w postaci waga:sciezka

    def getShortestPaths(self, fromVert):
        vertices = self.getVertices() #zebranie wierzcholkow
        paths={}
        message = "Shortest paths from vertex " + fromVert +" to vertices:\n"
        for vert in vertices:
            if vert != fromVert: 
                paths[vert]=self.getShortestPath(fromVert, vert) #operujemy na slownikach
                message+= vert + ":" + str(list(paths[vert].values())[0]) + ", weight=" + str(list(paths[vert].keys())[0]) + ";\n"
        return message    #wierzcholek : [sciezka], waga
    

if __name__ == "__main__":
    G=Graph()
    G.addVerticesFromList(["Alice","Bob","Carl","David","Ernst",
                           "Frank","Gail","Harry","Irene","Jen"])
    G.addVertex("Yurij")
    G.addEdgesFromList([["Alice","Bob",2], ["Alice", "Carl",3], ["Alice" , "David",1], ["Alice" , "Ernst",5], ["Alice" , "Frank",1], ["Bob" , "Gail",1], ["Gail" , "Harry",2], ["Harry" , "Jen",4], ["Jen" , "Gail",1], ["Harry" , "Irene",2], ["Irene" , "Gail",3], [
"Irene" , "Jen",5], ["Ernst" , "Frank",10], ["David" , "Carl",1], ["Carl" , "Frank",2]])
    
    G.addEdge("Alice","Bob",2)
    print('G.getEdges()')
    print(G.getEdges())
    
    print(' ')
    print('G.getVertex("Alice").getWeight(G.getVertex("Carl"))')
    print(G.getVertex("Alice").getWeight(G.getVertex("Carl")))
    
    print(' ')
    print('G.getNeighbors("Alice")')
    print(G.getNeighbors("Alice"))
    
    print(' ')
    print('G.getVertices()')
    print(G.getVertices())
    
    print(' ')
    print('"Vladimir" in G')
    print("Vladimir" in G)
    
    print(' ')
    print('"Alice" in G')
    print("Alice" in G)
    
    print(' ')
    print("G.getShortestPaths('Alice')")
    print(G.getShortestPaths('Alice'))
    
    G.saveGraph()