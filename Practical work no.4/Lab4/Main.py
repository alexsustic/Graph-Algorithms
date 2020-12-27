from Graph import Graph
from RandomGraph import RandomGraph
import math
class Console():

    def __init__(self, filename):
        self.__filename = filename
           
    def __loadFromFile(self):
        try:
            with open(self.__filename, "r") as file:
                first_line = file.readline()
                first_line = first_line.strip().split()
                vertices, edges = int(first_line[0]), int(first_line[1])
                self.__Graph = Graph(vertices)
                for i in range(edges):
                    line = file.readline()
                    line = line.strip().split()
                    vertex1, vertex2, cost = int(line[0]), int(line[1]), int(line[2])
                    self.__Graph.add_edge(vertex1, vertex2, cost)
            
        except IOError:
            raise Exception("An error occurred while loading the file!")

    def write_to_file(self):
        print("Give the filename: ")
        fileName = input()
        self.__Graph.save_to_file(fileName)

    def __get_nr_of_vertices(self):
        print(self.__Graph.get_nr_of_vertices())

    def __see_vertices(self):
        print(self.__Graph.parse_keys())

    def __verify_edge(self):
        print("Give vertex 1 and vertex 2")
        vertex1 = int(input())
        vertex2 = int(input())
        result = {True: "It is an edge", False: "It is not an edge"}
        print(result[self.__Graph.is_edge(vertex1, vertex2)])

    def __get_degrees(self):
        print("Type the vertex: ")
        vertex = int(input())
        print("The in degree is: " + str(self.__Graph.get_in_degree(vertex)))
        print("The out degree is: " + str(self.__Graph.get_out_degree(vertex)))

    def __change_cost(self):
        print("Give the edge's first vertex: ")
        vertex1 = int(input())
        print("Give the edge's second vertex: ")
        vertex2 = int(input())
        print(self.__Graph.get_cost(vertex1, vertex2))
        print("Give the new cost for the edge: ")
        new_cost = int(input())
        self.__Graph.change_edge_cost(vertex1, vertex2, new_cost)

    def __add_vertex(self):
        print("Add new vertex: ")
        vertex = int(input())
        self.__Graph.add_vertex(vertex)

    def __add_edge(self):
        print("Give the edge's first vertex: ")
        vertex1 = int(input())
        print("Give the edge's second vertex: ")
        vertex2 = int(input())
        print("Give the edge's cost: ")
        cost = int(input())
        self.__Graph.add_edge(vertex1, vertex2, cost)

    def __remove_vertex(self):
        print("The vertex you want to remove is: ")
        vertex = int(input())
        self.__Graph.remove_vertex(vertex)

    def __remove_edge(self):
        print("You want to remove an edge.")
        print("The edge's first vertex: ")
        vertex1 = int(input())
        print("The edge's second vertex: ")
        vertex2 = int(input())
        self.__Graph.remove_edge(vertex1, vertex2)
        
    def __retrieveInfo(self):
        print("Type the source: ")
        vertex1 = int(input())
        print("Type the destination: ")
        vertex2 = int(input())
        cost=self.__Graph.get_cost(vertex1, vertex2)
        print("The cost of the edge is: " + str(cost))
        
    def __copy_graph(self):
       
        self.__GraphCopy = self.__Graph.copy_the_graph()
        print("The graph is now copied and saved in __GraphCopy")

    def __graph_copy(self):
        print("The vertices of the copied graph are: ")
        print(self.__GraphCopy.parse_keys())
        print("The edges of the copied graph are: ")
        print(self.__GraphCopy.return_edges())

    def __print_graph(self):
        
        print(self.__Graph)
        
    def __parse_out(self):
        print("Type the vertex: ")
        vertex = int(input())
        out = self.__Graph.parse_out_neighbours(vertex)
        print("The outbound neighbours are: "+str(out))
        inNeighbours = self.__Graph.parse_in_neighbours(vertex)
        print("The inbound neighbours are: " +str(inNeighbours))
        
        
    def randomGraphGen(self):
        print("Give the number of vertices: ")
        vertices = int(input())
        print("Give the number of edges: ")
        edges = int(input())
        self.__Graph = RandomGraph(vertices,edges)
        print("Give the file name: ")
        fileName = input()
        self.__Graph.save_to_file(fileName)

    
    def __minimumPathLength(self):
        print("Type the source:", end=" ")
        first_vertex = int(input())
        print("Type the destination:", end=" ")
        second_vertex = int(input())
        
        if first_vertex not in self.__Graph.parse_keys() or second_vertex not in self.__Graph.parse_keys():
            print("Inexistent vertex!")
        else:
            accessible,predecessor = self.__Graph.minimum_path(first_vertex)
            path = []
            existence=False
            if second_vertex in accessible:
                    existence = True;
            if existence == True:
                length = 0
                destination_path = second_vertex
                path.append(destination_path)
                while(destination_path != first_vertex):
                    destination_path = predecessor[destination_path]
                    length = length + 1
                    path.append(destination_path)
                print(" ")
                print("The minimum path is: ", end=" ")
                for i in range(1, len(path)):
                    print(str(path[len(path)-i]) + " -->", end=" ")
                print(path[0])
                print("The minimum path length is: " + str(length))
            else:
                print("There is no path between this two vertices!")
        
    def __minimumCostWalk(self):
        print("Type the source:", end=" ")
        first_vertex = int(input())
        print("Type the destination:", end=" ")
        second_vertex = int(input())
        if first_vertex not in self.__Graph.parse_keys() or second_vertex not in self.__Graph.parse_keys():
            raise Exception("Inexistent vertex!")
        distance, path = self.__Graph.minimumCostWalk(first_vertex,second_vertex)
        
        if distance[second_vertex] == math.inf:
            raise Exception("There is no path between these two vertices !")
        
        print(" ")
        print("The path is: ", end=" ")
        for i in range(1, len(path)):
            print(str(path[len(path)-i]) + " -->", end=" ")
        print(path[0])
        print("The minimum walk cost between vertices " +str(first_vertex)+ " and " +str(second_vertex) +" is: " +str(distance[second_vertex]));
            
    def __topologicalSort(self):
        sorted_list = self.__Graph.topologicalSort()  
        if(len(sorted_list) == 0):
            print("This graph contains at least a cycle! It's not a DGA !") 
        else:
            print("")
            print("Topological sort: " +str(sorted_list)) 
            print("Because it is a DGA, you can calculate the highest cost walk between two vertices") 
            print("Type the source:", end=" ")
            source = int(input())
            print("Type the destination:", end=" ")
            destination = int(input())
            path, cost = self.__Graph.highestCostPath(source, destination)
            print("")
            print("The path is: ", end=" ")
            
            current_vertex = destination
            list_path = []
            while(current_vertex != source):
                list_path.append(current_vertex)
                current_vertex = path[current_vertex] 
            if(len(path) > 0):
                list_path.append(path[0]) 
            for i in range(0,len(list_path)) :
                if(i != len(list_path) - 1):
                    print(str(list_path[len(list_path) - i - 1]) + " -> ", end="")
                else:
                    print(str(list_path[len(list_path) - i - 1])) 
            print("The heighest cost is: " + str(cost))
                
               
    def print_menu(self):
        print("")
        print("-"*80)
        print("Please choose one of the commands mentioned above: \n")
        print("1. Load the graph from file")
        print("2. Get number of vertices")
        print("3. Add a new vertex")
        print("4. Remove a vertex")
        print("5. Add a new edge")
        print("6. Remove an edge")
        print("7. List the graph")
        print("8. Parse the set of vertices")
        print("9. Verify the existence of an edge")
        print("10. Get the degree of a vertex")
        print("11. Parse the set of inbound/outbound edges of a vertex")
        print("12. Retrieve information attached to an edge")
        print("13. Modify information attached to an edge")
        print("14. Random graph")
        print("15. Write graph in a file")
        print("16. Copy graph")
        print("17. Determine the minimum path length between two vertices")
        print("18. Determine the minimum cost walk between two vertices")
        print("19. Topological sort")
        print("20. Exit\n")
        print("-"*80)
        print("")
        
    def run(self):
        self.__commands={ "1":self.__loadFromFile,
                            "2":self.__get_nr_of_vertices,
                            "3":self.__add_vertex,
                            "4":self.__remove_vertex,
                            "5":self.__add_edge,
                            "6":self.__remove_edge,
                            "7":self.__print_graph,
                            "8":self.__see_vertices,
                            "9":self.__verify_edge,
                            "10":self.__get_degrees,
                            "11":self.__parse_out,
                            "12":self.__retrieveInfo,
                            "13":self.__change_cost,
                            "14":self.randomGraphGen,
                            "15":self.write_to_file,
                            "16":self.__copy_graph,
                            "17":self.__minimumPathLength,
                            "18":self.__minimumCostWalk,
                            "19":self.__topologicalSort} 
        
        print("DO NOT FORGET FIRST TO LOAD THE GRAPH FROM THE FILE !!")
        while (True):
            self.print_menu()
            print("Which command would you like to choose: ")
            command = input()
            if command == "20":
                break
            elif command in self.__commands:
                try:
                    self.__commands[command]()
                except Exception as ex:
                    print(ex)
            else:
                print("Inexistent command! ")

start = Console("DAG_Graph.txt")
start.run()

