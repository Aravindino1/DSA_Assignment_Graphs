#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Breadth First Traversal for a Graph

from collections import defaultdict

class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# Driver code
if __name__ == '__main__':

    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
    g.BFS(2)


# In[2]:


#Depth First Traversal for a Graph

class Graph:
 
    # Constructor
    def __init__(self):
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
 
     
    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
     
    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
     
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)
 
 
# Driver's code
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Depth First Traversal (starting from vertex 2)")
     
    # Function call
    g.DFS(2)


# In[3]:


#Count the number of nodes at given level in a tree using BFS

from collections import deque
  
adj = [[] for i in range(1001)]
  
def addEdge(v, w):
     
    # Add w to v’s list.
    adj[v].append(w)
  
    # Add v to w's list.
    adj[w].append(v)
def BFS(s, l):
     
    V = 100
     
    # Mark all the vertices
    # as not visited
    visited = [False] * V
    level = [0] * V
  
    for i in range(V):
        visited[i] = False
        level[i] = 0
  
    # Create a queue for BFS
    queue = deque()
  
    # Mark the current node as
    # visited and enqueue it
    visited[s] = True
    queue.append(s)
    level[s] = 0
  
    while (len(queue) > 0):
         
        # Dequeue a vertex from
        # queue and print
        s = queue.popleft()
        #queue.pop_front()
  
        # Get all adjacent vertices
        # of the dequeued vertex s.
        # If a adjacent has not been
        # visited, then mark it
        # visited and enqueue it
        for i in adj[s]:
            if (not visited[i]):
  
                # Setting the level
                # of each node with
                # an increment in the
                # level of parent node
                level[i] = level[s] + 1
                visited[i] = True
                queue.append(i)
  
    count = 0
    for i in range(V):
        if (level[i] == l):
            count += 1
             
    return count
  
# Driver code
if __name__ == '__main__':
     
    # Create a graph given
    # in the above diagram
    addEdge(0, 1)
    addEdge(0, 2)
    addEdge(1, 3)
    addEdge(2, 4)
    addEdge(2, 5)
  
    level = 2
  
    print(BFS(0, level))


# In[4]:


#Count number of trees in a forest

def addEdge(adj, u, v):
    adj[u].append(v) 
    adj[v].append(u)
    
# A utility function to do DFS of graph 
# recursively from a given vertex u. 
def DFSUtil(u, adj, visited):
    visited[u] = True
    for i in range(len(adj[u])):
        if (visited[adj[u][i]] == False):
            DFSUtil(adj[u][i], adj, visited)
            
# Returns count of tree is the 
# forest given as adjacency list. 
def countTrees(adj, V):
    visited = [False] * V 
    res = 0
    for u in range(V):
        if (visited[u] == False):
            DFSUtil(u, adj, visited) 
            res += 1
    return res
 
# Driver code 
if __name__ == '__main__':
 
    V = 5
    adj = [[] for i in range(V)] 
    addEdge(adj, 0, 1) 
    addEdge(adj, 0, 2) 
    addEdge(adj, 3, 4) 
    print(countTrees(adj, V))


# In[5]:


#Detect Cycle in a Directed Graph

from collections import defaultdict
 
 
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):
 
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        # The node needs to be popped from
        # recursion stack before function ends
        recStack[v] = False
        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
 
 
# Driver code
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    if g.isCyclic() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")


# In[6]:


#Implement n-Queen’s Problem
N = 4
 
# ld is an array where its indices indicate row-col+N-1
# (N-1) is for shifting the difference to store negative
# indices
ld = [0] * 30
 
# rd is an array where its indices indicate row+col
# and used to check whether a queen can be placed on
# right diagonal or not
rd = [0] * 30
 
# Column array where its indices indicates column and
# used to check whether a queen can be placed in that
# row or not
cl = [0] * 30
 
# A utility function to print solution
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
 
 
# A recursive utility function to solve N
# Queen problem
def solveNQUtil(board, col):
 
    # Base case: If all queens are placed
    # then return True
    if (col >= N):
        return True
 
    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):
 
        # Check if the queen can be placed on board[i][col]
 
        # To check if a queen can be placed on 
        # board[row][col] We just need to check 
        # ld[row-col+n-1] and rd[row+coln]
        # where ld and rd are for left and 
        # right diagonal respectively
        if ((ld[i - col + N - 1] != 1 and
             rd[i + col] != 1) and cl[i] != 1):
 
            # Place this queen in board[i][col]
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
 
            # Recur to place rest of the queens
            if (solveNQUtil(board, col + 1)):
                return True
 
            # If placing queen in board[i][col]
            # doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0  # BACKTRACK
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
 
            # If the queen cannot be placed in
            # any row in this column col then return False
    return False
 
# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns False if queens
# cannot be placed, otherwise, return True and
# prints placement of queens in the form of 1s.
# Please note that there may be more than one
# solutions, this function prints one of the
# feasible solutions.
def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    if (solveNQUtil(board, 0) == False):
        printf("Solution does not exist")
        return False
    printSolution(board)
    return True
 
# Driver Code
if __name__ == '__main__':
    solveNQ()


# In[ ]:




