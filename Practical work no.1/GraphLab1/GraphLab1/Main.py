from UI import Console
from Service import Service
from Repository import Graph
from Entities import Edge
repo= Graph("graph1k.txt",Edge.read_graph)
service=Service(repo)
ui=Console(service)
repo._read_all_from_file()
repo._read_number_of_vertex_edged()
ui.run()
