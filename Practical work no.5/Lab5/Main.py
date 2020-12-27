from UndirectedGraph import UndirectedGraph

class Console:
    
    def __init__(self):
        self.__filename = "graph2.txt"
        self.__commands = {"1": self.__loadGraph,
                           "2": self.__addVertex,
                           "3": self.__addEdge,
                           "4": self.__minimalVertexCover}
        
    
    def __loadGraph(self):
        try:
            with open(self.__filename, "r") as f:
                first_line = f.readline()
                first_line = first_line.strip().split()
                nrVertices, nrEdges = int(first_line[0]), int(first_line[1])
                self.__graph = UndirectedGraph(nrVertices)
                i = 0
                while(i < nrEdges):
                    line = f.readline()
                    line = line.strip().split()
                    start, end = int(line[0]), int(line[1])
                    self.__graph.addEdge(start,end)
                    i = i + 1
                
        except IOError:
            raise Exception("This file couldn't be read !")
    
    def __addEdge(self):
        print("Type the starting vertex:")
        start_vertex = int(input())
        print("Type the ending vertex:")
        end_vertex = int(input())
        self.__graph.addEdge(start_vertex, end_vertex)
    
    def __minimalVertexCover(self):
        coverage = self.__graph.greedyVertexCover()
        print("")
        print("The minimal vertex cover is : " +str(coverage))
        print("")
        
        
    def __addVertex(self):
        print("Type the vertex :")
        vertex = int(input())
        self.__graph.addVertex(vertex)
    
    def __printMenu(self):
        print("1. Load from graph")
        print("2. Add a new vertex")
        print("3. Add a new edge")
        print("4. Find the minimal vertex coverage")  
        print("")  
        print("Don't forget first to load the graph from the file (use command no. 1)")
        print("")
        
    def run(self):
        self.__printMenu()
        while True:
           
            user_command = input("What command would you like to choose: ")
            if user_command == "exit":
                break
            elif user_command in self.__commands:
                try:
                    self.__commands[user_command]()
                except Exception as ex:
                    print(ex)
        
console = Console()
console.run()