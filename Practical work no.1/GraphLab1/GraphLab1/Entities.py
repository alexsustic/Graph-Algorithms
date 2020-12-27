class Edge():
    def __init__(self, source, target, cost):
        self.__source=source
        self.__target=target
        self.__cost=cost
        
    def get_source(self):
        return self.__source


    def get_target(self):
        return self.__target


    def get_cost(self):
        return self.__cost


    def set_source(self, value):
        self.__source = value


    def set_target(self, value):
        self.__target = value


    def set_cost(self, value):
        self.__cost = value
    
    def __str__(self):
        return "Source: " + str(self.__source) + " " + "Target: " + str(self.__target) +" " + "Cost: " + str(self.__cost)
        
    @staticmethod
    def read_graph(line):
        line=line.split(" ")
        return Edge(int(line[0].strip()),int(line[1].strip()),int(line[2].strip()))
    @staticmethod
    def write_first_line(no_vertex,no_edges):
        return str(no_vertex) +" " +str(no_edges)
    @staticmethod
    def write_graph(edge):
        return str(edge.__source) +" " +str(edge.__target)+ " " + str(edge.__cost)