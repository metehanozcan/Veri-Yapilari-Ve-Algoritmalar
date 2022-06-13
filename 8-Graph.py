"""
    
    Implementation of  a graph data structure
    """
__author__="Metehan Özcan"

from collections import defaultdict
class Graph:
    
    def __init__(self,vertex):
        self.V=vertex
        self.graph =defaultdict(list)
        #*CRUD
        d={1,2,3,4,5}