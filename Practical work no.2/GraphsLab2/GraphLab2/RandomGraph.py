from Graph import Graph
from random import choice

class RandomGraph():
    def __init__(self, vertices, edges):
        self.__randomGraph = Graph(vertices)
        self.__generator(vertices, edges)

    def __generator(self, vertices, edges):
        vertices = [i for i in range(vertices)]
        costs = [0]
        for i in range(1, 101):
            costs.append(i)
            costs.append(-i)
        index = 0
        while index < edges:
            vertex1 = choice(vertices)
            vertex2 = choice(vertices)
            cost = choice(costs)
            try:
                self.__randomGraph.add_edge(vertex1, vertex2, cost)
                index += 1
            except Exception as ex:
                pass

    def save_to_file(self, fileName):
        with open(fileName,"w") as f:
            f.write(str(self))


    def __str__(self):
        string = ""
        string+= "The vertices of the random graph are: "
        string+= str(self.__randomGraph.parse_keys())
        string+='\n'
        string+="The edges of the random graph are: "
        string+= str(self.__randomGraph.return_edges())
        string+='\n'
        string+="The costs of the random graph are: "
        string+=str(self.__randomGraph.return_costs())
        string+='\n'
        return string

