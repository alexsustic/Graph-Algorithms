import copy
import math
class Graph(object):
    
    def __init__(self, vertices):
        self.__dictionaryIn = {}
        self.__dictionaryOut = {}
        self.__dictionaryCosts = {}

        for i in range(vertices):
            self.__dictionaryOut[i] = []
            self.__dictionaryIn[i] = []

    def parse_keys(self):
        return list(self.__dictionaryOut.keys())

    def parse_out_neighbours(self, vertex):
        try:
            return list(self.__dictionaryOut[vertex])
        except KeyError:
            raise Exception("Inexistent vertex")

    
    '''
    --> breadth-first traversal
    input: the source vertex
    output: the list of visited nodes during traversal, the list of predecessors for each visited node
    '''
    def minimum_path(self, first_vertex):
        tail= [] #used for breadth-first traversal
        predecessor= [] # list of predecessors, where predecessor[x] is the predecessor of node x
        for i in range(0,self.get_nr_of_vertices()):
            predecessor.append(None)
        visited= []    # list of visited nodes during traversal
        tail.append(first_vertex)
        visited.append(first_vertex)
        while(len(tail) != 0):
            x = tail.pop(0);
            for y in self.parse_out_neighbours(x):
                if y not in visited:
                    tail.append(y)
                    visited.append(y)
                    predecessor[y] = x
        accessible = visited.copy()
        return accessible, predecessor
        
        
    # In this function, we are going to build the minimal cost path between two vertices
    # input: -> two vertices, the source and the destination
    #        -> a list with predecessors
    # output: -> a list containing all the vertices that are used in the minimal cost walk
    def getMinimalCostPath(self,first_vertex,second_vertex,previous):
        path = []
        destination_path = second_vertex
        path.append(destination_path)
        while(destination_path != first_vertex):
            destination_path = previous[destination_path]
            path.append(destination_path)
        return path
    
    
    # Bellman-Ford Algorithm
    # input: two vertices, the source and the destination
    # output: -> distance - a list of minimal cost walks from the source to each vertex
    #         -> path - a list containing all the vertices used in the minimal cost walk between source and destination
    def minimumCostWalk(self,first_vertex,second_vertex):  
        
        distance = []
        previous = []
        negative_cost_cycle = False;
        edges = self.return_edges()
        #we create a list with nr_of_vertices positions, containing infinity values
        for _ in range(0,self.get_nr_of_vertices()):
            distance.append(math.inf)
        #create a list with nr_of_vertices positions, containing initially -1 value
        for _ in range(0,self.get_nr_of_vertices()):
            previous.append(-1)
        #we initialize the starting distance path with 0
        distance[first_vertex] = 0
        
        for _ in self.parse_keys():
            changed = False
           
            for (x,y) in edges:
                # for each edge we check if there is a better walk cost
                if distance[y] > distance[x] + self.__dictionaryCosts[(x,y)]:
                    distance[y] = distance[x] + self.__dictionaryCosts[(x,y)]
                    previous[y] = x
                    changed = True
            if changed == False:
                #if there are no changes on the distance list, we exit the loop
                break
            
        #now, we are looking for negative cost cycles , and if so, we raise an exception
        for (x,y) in edges:
                if distance[y] > distance[x] + self.__dictionaryCosts[(x,y)]:
                    negative_cost_cycle = True;
                    break;
        if negative_cost_cycle == True:
            raise Exception("This graph have negative cost cycles !") 
        
        #we are building the path of the minimal cost walk using getMinimalCostPath function
        path = self.getMinimalCostPath(first_vertex,second_vertex,previous)    
        
        return distance, path
                    
        
        
    def parse_in_neighbours(self, vertex):
        try:
            return list(self.__dictionaryIn[vertex])
        except KeyError:
            raise Exception("Inexistent vertex")

    
    def is_edge(self, vertex1, vertex2):
        try:
            return vertex2 in self.__dictionaryOut[vertex1]
        except KeyError:
            raise Exception("Non existent edge !")


    def add_edge(self, vertex1, vertex2, cost):
        exception_message = ""
        if self.is_edge(vertex1, vertex2):
            exception_message += "The edge from vertex1 to vertex 2 already exists! "
        if len(exception_message) > 0:
            raise Exception(exception_message)
        self.__dictionaryOut[vertex1].append(vertex2)
        self.__dictionaryIn[vertex2].append(vertex1)
        self.__dictionaryCosts[(vertex1, vertex2)] = cost


    def add_vertex(self, vertex):
        if vertex in self.parse_keys():
            raise Exception("This vertex already exists in the graph")
        self.__dictionaryOut[vertex] = []
        self.__dictionaryIn[vertex] = []

    def get_cost(self, vertex1, vertex2):
        if self.is_edge(vertex1, vertex2):
            return self.__dictionaryCosts[(vertex1, vertex2)]
        else:
            raise Exception("Non existent edge!")

    
    def isolated_vertices(self):
        vertices = []
        for key in self.parse_keys():
            if self.__dictionaryIn[key] == [] and self.__dictionaryOut == []:
                vertices.append(key)
        return vertices[:]

    
    def remove_vertex(self, vertex):
        if vertex not in self.parse_keys():
            raise Exception("Vertex doesn't exist")
        for vertex2 in self.__dictionaryOut[vertex]:
            self.__dictionaryIn[vertex2].remove(vertex)
            del self.__dictionaryCosts[(vertex, vertex2)]
        del self.__dictionaryOut[vertex]
        for vertex2 in self.__dictionaryIn[vertex]:
            self.__dictionaryOut[vertex2].remove(vertex)
            del self.__dictionaryCosts[(vertex2, vertex)]
        del self.__dictionaryIn[vertex]

   
    def remove_edge(self, vertex1, vertex2):
        if not self.is_edge(vertex1, vertex2):
            raise Exception("This edge doesn't exist")
        del self.__dictionaryCosts[(vertex1, vertex2)]
        self.__dictionaryOut[vertex1].remove(vertex2)
        self.__dictionaryIn[vertex2].remove(vertex1)

    def get_nr_of_vertices(self):
        return len(self.parse_keys())

    
    def get_out_degree(self, vertex):
        try:
            return len(self.__dictionaryOut[vertex])
        except KeyError:
            raise Exception("The vertex doesn't exist")

    
    def get_in_degree(self, vertex):
        try:
            return len(self.__dictionaryIn[vertex])
        except KeyError:
            raise Exception("The vertex doesn't exist")

   
    def change_edge_cost(self, vertex1, vertex2, cost):
        if (vertex1, vertex2) in self.__dictionaryCosts:
            self.__dictionaryCosts[(vertex1, vertex2)] = cost
        else:
            raise Exception("The edge doesn't exist")

    def copy_the_graph(self):
        new_graph = Graph(10)
        new_graph.__dictionaryIn = copy.deepcopy(self.__dictionaryIn)
        new_graph.__dictionaryOut = copy.deepcopy(self.__dictionaryOut)
        new_graph.__dictionaryCosts = copy.deepcopy(self.__dictionaryCosts)
        return new_graph

    
    def return_edges(self):
        edges = []
        for edge in self.__dictionaryCosts:
            edges.append(edge)
        return edges[:]

    
    def return_costs(self):
        costs = []
        for cost in self.__dictionaryCosts:
            costs.append(self.__dictionaryCosts[cost])
        return costs[:]

    
    def save_to_file(self, fileName):
        with open(fileName,"w") as f:
            f.write(str(self))

    def __str__(self):
        string = ""
        for key in self.__dictionaryCosts:
            string += "Source: "
            string+= str(key[0])
            string+=" // "
            string+= "Destination: "
            string+=str(key[1])
            string+=" // "
            string+= "Cost: "
            string+=str(self.__dictionaryCosts[key])
            string+='\n'
        return string

