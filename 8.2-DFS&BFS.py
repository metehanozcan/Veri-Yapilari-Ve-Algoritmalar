import collections
from collections import deque

graph = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

def dfs(matrix):
    # Check for an empty matrix/graph.
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        if (i, j) in visited:
            return

        visited.add((i, j))
        # Traverse neighbors.
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
            # Add in question-specific checks, where relevant.
                traverse(next_i, next_j)
                

    for i in range(rows):
        for j in range(cols):            
             traverse(i, j)
    
def bfs(matrix):
  # Check for an empty matrix/graph.
  if not matrix:
    return []

  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

  def traverse(i, j):
    queue = deque([(i, j)])
    while queue:
      curr_i, curr_j = queue.popleft()
      if (curr_i, curr_j) not in visited:
        visited.add((curr_i, curr_j))
        # Traverse neighbors.
        for direction in directions:
          next_i, next_j = curr_i + direction[0], curr_j + direction[1]
          if 0 <= next_i < rows and 0 <= next_j < cols:
            # Add in question-specific checks, where relevant.
            queue.append((next_i, next_j))

    for i in range(rows):
        for j in range(cols):
            traverse(i, j)        
        



def bfsnumsIslands(matrix):
    if not matrix:
        return 0
    
    rows,cols=len(matrix),len(matrix[0])
    visit=set()
    islands=0
    
    def bfs(r,c):
        q=collections.deque()
        visit.add((r,c))
        q.append((r,c))
        while q:
            row,col= q.pop() #* If we want to solve it with dfs, we can simply change popleft to pop.
            print(row,col)
            directions=((1,0),(-1,0),(0,1),(0,-1))
            for dr, dc in directions:
                r,c = row +dr, col+dc
                print("Son",r,c)
                if(r in range(rows) and c in range(cols) and matrix[r][c]==1 and (r,c) not in visit):
                    q.append((r,c))
                    visit.add((r,c))
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c]==1 and (r,c) not in visit:
                bfs(r,c)
                islands +=1
    return islands





def dfsnumIslands(matrix):
    if not matrix:
        return 0
    
    rows,cols=len(matrix),len(matrix[0])
    visit=set()
    islands=0
    
    def dfs(r,c):
        q=collections.deque()
        visit.add((r,c))
        q.append((r,c))
        
        while q:
            row,col=q.pop()
            directions=((-1,0),(1,0),(0,1),(0,-1))
            for dr,dc in directions:
                r,c = dr+row,dc+col
                if (r in range(rows) and c in range(cols) and matrix[r][c] == 1 and (r,c) not in visit):
                    visit.add((r,c))
                    q.append((r,c))
                    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and (r,c) not in visit:
                dfs(r,c)
                islands+=1
    return islands
                    



    


