import queue
import copy

class DirectedGraph(object):
    """
    directed graph, with adj list
    """
    def __init__(self) :
        self.adjacency_list={}
        
    def add_edge(self,source,destination):
        """_summary_
        adds an edge defined by vertices source and destination
        
        Args:
            source (_type_): adds an edge defined by vertices source and destination
            destination (_type_): _description_
        """
        
        if source not in self.adjacency_list:
            self.adjacency_list[source] = set()
        self.adjacency_list[source].add(destination)
    
    def get_vertex(self):   
        
        """
        Generator for returning the next vertex from the adjacency list
        :return:
        """     
        for v in self.adjacency_list:
            yield v
    def get_neighbor(self,vertex):
        """
        Generator for returning vertex's neighbors to the given vertex

        Args:
            vertex (_type_): _description_

        Yields:
            _type_: _description_
        """
        
        if vertex in self.adjacency_list:
            for u in self.adjacency_list[vertex]:
                yield u
                
                
    
    def get_reverse_neighbor(self,vertex): 
        if vertex in self.adjacency_list:
            r_stack=[]
            for i in self.get_neighbor(vertex):
                r_stack.append(i)        
            r_stack=r_stack[::-1]
            for i in r_stack:            
                yield i
    def dfs(self):
        seen = {}
        vertexcantbereached = set()
        to_visit = []

        for vertex in self.get_vertex():
            if vertex not in seen:
                vertexcantbereached.add(vertex)
            else:
                continue

            to_visit.append(vertex)

            while to_visit:
                v = to_visit.pop()

                for neighbor in self.get_neighbor(v):
                    if neighbor not in seen:
                        seen[neighbor] = v
                        to_visit.append(neighbor)

        return vertexcantbereached, seen
        
    def bfs(self):
        seen={}
        to_visit= queue.Queue()
        for vertex in self.get_vertex():
            to_visit.put(vertex)
            
            while not to_visit.empty():
                v=to_visit.get()
                
                for neighbor in self.get_neighbor(v):
                    if neighbor not in seen:
                        seen[neighbor]=v
                        to_visit.put(neighbor)
        return seen
                
        
    def listprinter(self):
        print(self.adjacency_list)    
        
def get_test_graph_1():
    dg = DirectedGraph()
    dg.add_edge(0, 1)
    dg.add_edge(0, 5)
    dg.add_edge(1, 2)
    dg.add_edge(2, 4)
    dg.add_edge(2, 6)
    dg.add_edge(3, 2)
    dg.add_edge(5, 8)
    dg.add_edge(6, 5)
    dg.add_edge(7, 5)
    dg.add_edge(8, 7)
    

    return dg
def test_dfs():
    
    dg1 = get_test_graph_1()
    c1, p1 = dg1.dfs()
    assert (c1 == {0, 3, 7})
    assert (p1 == {1: 0, 2: 1, 4: 2, 5: 0, 6: 2, 8: 5})
def main():
    dg=get_test_graph_1()
    dg.listprinter()
    print("DFS",dg.dfs())
    print("BFS",dg.bfs())
    # print(dg.get_neighbor(0))
    # print(dg.get_reverse_neighbor(0))
    test_dfs()
    # test_dfs()
    # test_bfs()
    # test_contains_cycle()
    # test_topological_sort()
    # test_strongly_connected_components()

    print("Tests complete.")


if __name__ == "__main__":
    main()