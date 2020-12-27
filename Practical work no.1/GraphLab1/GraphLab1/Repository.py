import random
import copy
from Entities import Edge
class Graph():
      
    def __init__(self,filename,read_edge):
        self.__filename= filename
        self.__read_edge= read_edge
        self.__list_of_edges=[]
        self.__list_of_vertex=[]
        self.__number_of_vertex=0
        self.__number_of_edges=0
        

       
    def _read_number_of_vertex_edged(self):
        with open(self.__filename,"r") as file:
            lines= file.readlines()
            parts=lines[0].split(" ")
            self.__number_of_vertex=int(parts[0].strip())
            self.__number_of_edges=int(parts[1].strip())
            
    def _read_all_from_file(self):
        with open(self.__filename,"r") as file:
            lines= file.readlines()
            for line in lines[1:]:
                line= line.strip()
                if line!="":
                    edge=self.__read_edge(line)
                    if edge.get_source() not in self.__list_of_vertex:
                        self.__list_of_vertex.append(edge.get_source())
                    if edge.get_target() not in self.__list_of_vertex:
                        self.__list_of_vertex.append(edge.get_target())
                    self.__list_of_edges.append(edge)
    def randomGraph(self,number_of_vertices,number_of_edges):
        
        if(number_of_vertices*number_of_vertices<number_of_edges):
            print("Error: Maximum number of edges is (n)*(n) !!")
        else:
            self.__number_of_vertex=number_of_vertices;
            self.__number_of_edges=0;
            vertex_list=[]
            cost_list=[]
            for i in range(0,number_of_vertices):
                vertex_list.append(i)
            for i in range(0,100):
                cost_list.append(i)
            self.__list_of_vertex=vertex_list.copy()
            self.__list_of_edges.clear()
            for i in range(0,number_of_edges):
                source=random.choice(vertex_list)
                target=random.choice(vertex_list)
                cost=random.choice(cost_list)
                edge=Edge(source,target,cost)
                self.addNewEdge(edge)
    
    def writeGraph(self,filename):
        with open(filename,"w") as file:
            file.write(str(self.__number_of_vertex)+" "+str(self.__number_of_edges) +"\n")
            for edge in self.__list_of_edges:
                file.write(Edge.write_graph(edge) + "\n")    
                
    def getEdges(self):
        return self.__list_of_edges[:]
    
    def modifyCost(self,source,target,new_cost):
        for edge in self.__list_of_edges:
            if edge.get_source()==source and edge.get_target()==target:
                edge.set_cost(new_cost)
    def addNewVertex(self, new_vertex):
        self.__list_of_vertex.append(new_vertex)
        self.__number_of_vertex= self.__number_of_vertex +1
       
    def getVertex(self):
        return self.__list_of_vertex
    
    def removeVertex(self,vertex_to_remove):
        for vertex in self.__list_of_vertex:
            if vertex== vertex_to_remove:
                self.__list_of_vertex.remove(vertex)
                self.__number_of_vertex=self.__number_of_vertex-1
                break
        
        index=0;
        while(index< self.__number_of_edges):
            if self.__list_of_edges[index].get_source()== vertex_to_remove or self.__list_of_edges[index].get_target()== vertex_to_remove:
                del self.__list_of_edges[index]
                index=index-1
                self.__number_of_edges=self.__number_of_edges-1
            index=index+1
    
    def addNewEdge(self,edge):
        self.__list_of_edges.append(edge)
        self.__number_of_edges=self.__number_of_edges+1
        
    def removeEdge(self,edge):
        self.__list_of_edges.remove(edge)
        self.__number_of_edges=self.__number_of_edges-1
               
    def get_number_vertices(self):
        return self.__number_of_vertex;  
    
    def copyGraph(self):
        self.copyGraph=Graph("copyGraph",Edge.read_graph)
        self.copyGraph.__list_of_edges=copy.deepcopy(self.__list_of_edges) 
        self.copyGraph.__list_of_vertex=copy.deepcopy(self.__list_of_vertex)  
        self.copyGraph.__number_of_edges=self.__number_of_edges;
        self.copyGraph.__number_of_vertex=self.__number_of_vertex;
        return self.copyGraph

    