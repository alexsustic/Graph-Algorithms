from Entities import Edge
class Service():
    def __init__(self,repository):
        self._repository=repository

    def getEdges(self):
        return self._repository.getEdges()
    
    def getVertex(self):
        return self._repository.getVertex()
    
    def addVertex(self, vertex):
        if vertex not in self.getVertex():
            self._repository.addNewVertex(vertex)
        else:
            raise Exception("This vertex already exists!")
        
    def removeVertex(self,vertex_to_remove):      
        if vertex_to_remove not in self.getVertex():
            raise Exception("This vertex doesn't exist!")
        else:
            self._repository.removeVertex(vertex_to_remove)
            
    def addEdge(self, source, target, cost):
        edge= Edge(source, target, cost)
        if(source not in self.getVertex()):
            raise Exception("Invalid source!")
        elif(target not in self.getVertex()):
            raise Exception("Invalid target!")
        for edge in self.getEdges():
            if edge.get_target() == target and edge.get_source() == source:
                raise Exception("This edge already exists!")
        self._repository.addNewEdge(edge)
    
    def outboundNeighbours(self,vertex):
        list=[]
        edges=self._repository.getEdges()
        for edge in edges:
            if edge.get_target()==vertex:
                list.append(edge.get_source())
        return list
    
    def inboundNeighbours(self,vertex):
        list=[]
        edges=self._repository.getEdges()
        for edge in edges:
            if edge.get_source()==vertex:
                list.append(edge.get_target())
        return list      
    def degreeVertex(self,vertex):
        in_degree=0;
        out_degree=0;
        list_degrees=[]
        edges=self._repository.getEdges();
        for edge in edges:
            if edge.get_source()==vertex:
                in_degree=in_degree+1
            if edge.get_target()==vertex:
                out_degree=out_degree+1
        list_degrees.append(in_degree)
        list_degrees.append(out_degree)
        return list_degrees
    
    def writeGraph(self,file_name):
        self._repository.writeGraph(file_name)
        
    def retrieveInfo(self,source,target):
        edges=self._repository.getEdges()
        if(self.isEdge(source, target)==False):
            return False
        else:
            for edge in edges:
                if edge.get_source()==source and edge.get_target()==target:
                    return edge.get_cost()
    def randomGraph(self,number_of_vertices,number_of_edges):
        self._repository.randomGraph(number_of_vertices,number_of_edges)
        
    def modifyCost(self,source,target,cost):
        self._repository.modifyCost(source,target,cost)
    def removeEdge(self,source,target):
        if(source not in self.getVertex()):
            raise Exception("Invalid source!")
        elif(target not in self.getVertex()):
            raise Exception("Invalid target!")
        
        found=False
        for edge in self.getEdges():
            if edge.get_target() == target and edge.get_source() == source:
                found=True
                found_edge=edge
        if found==False:
            raise Exception("This edge doesn't exist!")
        self._repository.removeEdge(found_edge) 
            
    def isEdge(self,source,target):
        list_of_edges=self._repository.getEdges()
        for edge in list_of_edges:
            if edge.get_source()== source and edge.get_target()== target:
                return True
        return False
        
    def get_number_verteces(self):
        return self._repository.get_number_vertices()
    
    def copy_graph(self):
        return self._repository.copyGraph()