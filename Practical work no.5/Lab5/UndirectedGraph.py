#import copy
class UndirectedGraph:
    def __init__(self, vertices):
        self.__numberVertices = vertices
        self.__dictEdges = {}
        for i in range(0,vertices):
            self.__dictEdges[i]=[]
    
    def addVertex(self, vertex):
        if vertex in self.__dictEdges:
            raise Exception("This vertex already exists!")
        self.__dictEdges[vertex] = [] 
         
    def addEdge(self, vertex1, vertex2):
        if vertex1 not in self.__dictEdges[vertex2] and vertex2 not in self.__dictEdges[vertex1]:
            self.__dictEdges[vertex1].append(vertex2)
            self.__dictEdges[vertex2].append(vertex1)
        else:
            raise Exception("This edge already exists!")
        
    def parseNeighbours(self, vertex):
        return self.__dictEdges[vertex]
    
    def getDegree(self, vertex):
        if vertex in self.__dictEdges:
            return len(self.__dictEdges[vertex])
        else:
            raise Exception("This vertex doesn't exist !")
        
        
    
    def getMaxDegreeVertex(self): 
        
        max_degree = -1
        max_vertex = -1
        for vertex in self.__dictEdges : 
            if (self.getDegree(vertex)> max_degree) :
                max_degree = self.getDegree(vertex)
                max_vertex = vertex
        return max_vertex
    
    
    #Based on Greedy algorithm
    #This function calculates the minimal vertex cover
    #input : -
    #output: a list containing the minimal number of nodes containing all the edges of the graph
    def greedyVertexCover(self):
        solution = []
        while(len(self.__dictEdges) != 0):
            maxDegreeVertex = self.getMaxDegreeVertex()
            if(self.getDegree(maxDegreeVertex) == 0):
                break
            solution.append(maxDegreeVertex)
            del self.__dictEdges[maxDegreeVertex]
            ok = True
            while(ok):
                ok= False
                for vertex in self.__dictEdges:
                    if maxDegreeVertex in self.__dictEdges[vertex]:
                        self.__dictEdges[vertex].remove(maxDegreeVertex)
                        ok = True
                        break
        return solution
    
    
    
    
    
# #     def getMaxDegreeVertexOptimization(self): 
# #         
# #         max_degree = -1
# #         max_vertex_all = []
#         for vertex in self.__dictEdges : 
#             if (self.getDegree(vertex)> max_degree) :
#                 max_degree = self.getDegree(vertex)
#                 max_vertex_all.clear()
#                 max_vertex_all.append(vertex)
#             elif(self.getDegree(vertex) == max_degree):
#                 max_vertex_all.append(vertex)
#         return max_vertex_all
#     
#     
#     
#     
#     
#     def greedyVertexCoverOptimization(self):
#         solution = []
#         temporary_solution = []
#         copy_dictEdges= copy.deepcopy(self.__dictEdges)
#         maxDegreeVertexList = self.getMaxDegreeVertexOptimization()
#         while(len(maxDegreeVertexList) != 0):
#             maxDegreeVertex = maxDegreeVertexList.pop(0)
#             while(len(self.__dictEdges) != 0):
#                 if(self.getDegree(maxDegreeVertex) == 0):
#                     break
#                 temporary_solution.append(maxDegreeVertex)
#                 del self.__dictEdges[maxDegreeVertex]
#                 ok = True
#                 while(ok):
#                     ok= False
#                     for vertex in self.__dictEdges:
#                         if maxDegreeVertex in self.__dictEdges[vertex]:
#                             self.__dictEdges[vertex].remove(maxDegreeVertex)
#                             ok = True
#                             break
#                 maxDegreeVertex = self.getMaxDegreeVertexOptimization()[0]
#                 print(maxDegreeVertex)
#             print(temporary_solution)
#             if(len(temporary_solution) < len(solution) and len(solution) != 0):
#                 solution = temporary_solution.copy()
#                 temporary_solution.clear()
#             elif (len(solution) == 0):
#                 solution = temporary_solution.copy()   
#                 temporary_solution.clear()
#             self.__dictEdges = copy.deepcopy(copy_dictEdges)
#             print("///")
#         return solution
#             
#     
    