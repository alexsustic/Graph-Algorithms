
class Console():
    def __init__(self,service):
        self._service=service
        
    def _uiAddVertex(self):
        new_vertex=int(input("Enter the new vertex: "))
        self._service.addVertex(new_vertex)
        
    def _uiRemoveVertex(self):
        vertex_to_remove=int(input("Enter the vertex you would like to delete:"))
        self._service.removeVertex(vertex_to_remove)
    
    def _uiAddEdge(self):
        source=int(input("Enter the source: "))
        target=int(input("Enter the target: "))
        cost=int(input("Enter the cost of the edge: "))
        self._service.addEdge(source, target, cost)
        
    def _uiRemoveEdge(self):
        source=int(input("Enter the source:"))
        target=int(input("Enter the target:"))
        self._service.removeEdge(source,target)
    def _uiListGraph(self):
        print("----------------------------------------------------------------------------------------------")
        list_of_vertex=self._service.getVertex()
        print("The list of vertices is: "+str(list_of_vertex))
        print("----------------------------------------------------------------------------------------------")
        list_of_edges=self._service.getEdges()
        print("The list of edges is: ")
        print(" ")
        for edge in list_of_edges:
            print(edge)
        print("----------------------------------------------------------------------------------------------")
    
    def _uiListOfVertex(self):
        list_of_vertex=self._service.getVertex()
        for vertex in list_of_vertex:
            print("One vertex is: "+str(vertex))  
    
    def _uiIsEdge(self):
        source=int(input("Enter the source: "))
        target=int(input("Enter the target: "))
        state= self._service.isEdge(source,target)
        if state==True:
            print("This edge exists!")
        else:
            print("This edge doesn't exists!")
    
    def _uiGetNumberVertices(self):
        number_of_vertices=self._service.get_number_verteces()
        print("The number of vertices is: "+str(number_of_vertices))
    
    def _uiDegreeVertex(self):
        vertex=int(input("Type the vertex:"))
        list=self._service.degreeVertex(vertex)
        print("In degree is: " + str(list[0])) 
        print("Out degree is: " + str(list[1]))    
        
    def _uiOutboundNeighbours(self):
        vertex=int(input("Type the vertex: ")) 
        list=self._service.outboundNeighbours(vertex)
        for vertex in list:
            print("One outbound neighbour is: " +str(vertex))  
            
    def _uiInboundNeighbours(self):
        vertex=int(input("Type the vertex: ")) 
        list=self._service.inboundNeighbours(vertex)
        for vertex in list:
            print("One inbound neighbour is: " +str(vertex)) 
            
    def _uiRetrieveInfo(self):
        first_vertex=int(input("Type the source vertex: "))
        second_vertex=int(input("Type the target vertex: "))
        cost=self._service.retrieveInfo(first_vertex,second_vertex)
        if cost==False:
            print("This edge doesn't exist!")
        else:
            print("The cost of the edge is: " +str(cost))
    
    def _uiModifyCost(self):
        first_vertex=int(input("Type the source vertex: "))
        second_vertex=int(input("Type the target vertex: "))
        cost=int(input("Type the new cost: "))
        self._service.modifyCost(first_vertex,second_vertex,cost)
        
    def _randomGraph(self):
        number_of_vertices=int(input("Type the number of vertices: "))
        number_of_edges=int(input("Type the number of edges: "))
        self._service.randomGraph(number_of_vertices,number_of_edges);
        
    def _writeGraph(self):
        file_name=str(input("Type the name of the file: "))
        self._service.writeGraph(file_name)
        
    def _copyGraph(self):
        
        copyGraph=self._service.copy_graph()
        print("A copy of the current graph was succesfully saved in <copyGraph> from Console !")
    def print_menu(self):
        print("1. Get number of vertices")
        print("2. Add a new vertex")
        print("3. Remove a vertex")
        print("4. Add a new edge")
        print("5. Remove an edge")
        print("6. List the graph!")
        print("7. Parse the set of vertices")
        print("8. Verify the existence of an edge")
        print("9. Get the degree of a vertex")
        print("10.Parse the set of outbound edges of a vertex")
        print("11.Parse the set of inbound edges of a vertex")
        print("12.Retrieve information attached to an edge")
        print("13.Modify information attached to an edge")
        print("14.Random graph")
        print("15.Write graph in a file")
        print("16.Copy graph")
        print("17.Exit\n")
        

    def run(self):
        
        operations={'1':self._uiGetNumberVertices,
                    '2':self._uiAddVertex,
                    '3':self._uiRemoveVertex,
                    '4':self._uiAddEdge,
                    '5':self._uiRemoveEdge,
                    '6':self._uiListGraph,
                    '7':self._uiListOfVertex,
                    '8':self._uiIsEdge,
                    '9':self._uiDegreeVertex,
                    '10':self._uiOutboundNeighbours,
                    '11':self._uiInboundNeighbours,
                    '12':self._uiRetrieveInfo,
                    '13':self._uiModifyCost,
                    '14':self._randomGraph,
                    '15':self._writeGraph,
                    '16':self._copyGraph}
        self.print_menu()
        while(True):
            command=str(input("Choose one command from those mentioned above: "))
            print(" ")
            if command=='17':
                break;
            if command in operations:
                try:
                    operations[command]()
                except Exception as ex:
                    print(ex)
            else:
                print("Try another command! \n")
            print(" ")
            
