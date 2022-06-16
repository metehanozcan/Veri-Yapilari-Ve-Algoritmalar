"""
    
    Implementation of  a graph data structure
    """
__author__="Metehan Özcan"



import re


class Graph(object):
    """
    Undirected Graph, with graph represented as an adjacency matrix.
    
    """
    #*Initialize the matrix
    def __init__(self,vertices):
        self.adjMatrix=[]
        for i in range(vertices):
            self.adjMatrix.append([0]*vertices)
        print("Graph Initial State ",self.adjMatrix)
        self.vertices=vertices
        
        
    #* Add Edge.   
    def add_edge(self,v1,v2):
        """
        Adds an edge defined by vertices from source(v1) to destination(v2)
        then destination(v2) to source(v1) in matrix
        :param v1:
        :param v2:
        :return:
        """
        if v1==v2:
            raise ValueError("Vertices cannot be the same")
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        
        
    #* Remove Edge.    
    def remove_edge(self,v1,v2):
        if v1==v2:
            raise ValueError("Vertices cannot be the same")
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
    
    
    def __len__(self):
        return self.vertices
    
    
    def print_matrix(self):
        print(self.adjMatrix)
        for i in range(self.vertices):            
            print(self.adjMatrix[i])
            
            
    def get_neighbor(self,vertex):
        for i, flag in enumerate(self.adjMatrix[vertex]):
            if flag == 1:
                yield i

         # neighbors=[]
        # for i in range(self.vertices):
        #     if self.adjMatrix[vertex][i]==1:
        #         neighbors.append(i)
        # print("Neighbors",neighbors)
    
    

    def dfs_iter(self,vertex):
        seen={}
        stack=[vertex]
        # seen[vertex]=True
        print("DFS")

        
        while stack:
            v=stack.pop()
            # print(v,end="<->")
            # for i,neighbor in enumerate(self.adjMatrix[v]):
            for i in self.get_neighbor(v):
                # if neighbor == 1 and i not in seen:
                if i not in seen:
                    stack.append(i)
                    seen[i]=v
                    
        print(seen)

        
    def bfs_iter(self,vertex):
        seen={}
        # seen[vertex]=True
        queue=[vertex]
        print("BFS")
        while queue:
            v=queue.pop(0)
            # print(v,end="<->")
            # for i,neighbor in enumerate(self.adjMatrix[v]):                
                # if neighbor == 1 and i not in seen: 
            for i in self.get_neighbor(v):
            # if neighbor == 1 and i not in seen:
                if i not in seen:                   
                    queue.append(i)
                    seen[i]=v
        print(seen)
    

def main():
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
  
    
    # g.remove_edge(2,3)
    g.get_neighbor(0)
    g.print_matrix()
    g.dfs_iter(0)
    g.bfs_iter(0)
    
    
       
if __name__ == '__main__':
    main()
    