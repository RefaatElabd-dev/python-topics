class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertix):
        if self.adj_list.get(vertix) is None:
            self.adj_list[vertix] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except:
                pass
            return True
        return False
    
    def remove_vertex(self, v):
        if v in self.adj_list:
            for vi in self.adj_list[v]:
                self.adj_list[vi].remove(v)
            del self.adj_list[v]
        return False
        




my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    A : []

"""