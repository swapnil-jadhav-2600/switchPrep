# creting all the necessary functions for a tree

# Add Edge : Function add edge between two nodes x,,y
def addEdge(x,y,adj):
    adj[x] = y
    adj[y] = x

# Print Parent : Funstion to print parent of each node
def printParent(node,adj,parent):
    # check if current node is root 
    if parent == 0 :
        print("{}->Root".format(node))
    else:
        print("{}->{}".format(node,parent))

    # Using DFS : Depth First Search
    for cur in adj[node]:
        if cur != parent:
            printParent(cur,adj,node)
     


# Driver code
N = 7
Root = 1
# Adjacency list to store the tree
adj = [[] for _ in range(N + 1)]
print(adj)

# Creating the tree
addEdge(1, 2, adj)
addEdge(1, 3, adj)
addEdge(1, 4, adj)
addEdge(2, 5, adj)
addEdge(2, 6, adj)
addEdge(4, 7, adj)

printParent(Root,adj,0)