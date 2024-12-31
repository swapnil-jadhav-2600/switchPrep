from collections import deque

# Function to add an edge between vertices x and y
def addEdge(x, y, adj):
    adj[x].append(y)
    adj[y].append(x)

# Function to print the parent of each node
def printParents(node, adj, parent):
    # current node is Root, thus, has no parent
    if parent == 0:
        print("{}->Root".format(node))
    else:
        print("{}->{}".format(node, parent))

    # Using DFS
    for cur in adj[node]:
        if cur != parent:
            printParents(cur, adj, node)
     

# print all the Children nodes
def printChildren(Root,adj):
    q  = deque()
    q.append(Root)
    # v array : to keep track of visited nodes in tree
    v = [0]*len(adj)
    print(f"visited array : {v}, q : {q}")
    # BFS : Brdth first search
    while q:
        print(f"q : {q}")
        node = q.popleft()
        print(f"node : {node}")
        v[node] = 1
        print("{}->".format(node)),
        for cur in adj[node]:
            if v[cur] ==0:
                print(cur),
                q.append(cur)
        print(v)

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

print(adj)
# printParents(Root,adj,0)

print("The children of each node are:")
printChildren(Root, adj)