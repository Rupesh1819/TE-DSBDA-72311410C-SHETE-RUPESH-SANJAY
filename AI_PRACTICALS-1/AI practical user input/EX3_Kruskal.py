# Kruskal's Algorithm using User Input

"""
| Feature        | Kruskal               | Dijkstra         |
| -------------- | --------------------- | ---------------- |
| Purpose        | Minimum Spanning Tree | Shortest Path    |
| Works On       | Edges                 | Vertices         |
| Greedy Choice  | Minimum edge          | Minimum distance |
| Cycles Allowed | No                    | Yes              |

Time Complexity:
O(E log E)

Where:
E = Number of edges

Space Complexity:
O(V)

Where:
V = Number of vertices
"""

# ---------------- USER INPUT ---------------- #

# Number of vertices
n = int(input("Enter number of vertices: "))

# Input vertices
nodes = []

print("\nEnter vertices:")

for i in range(n):

    vertex = input(f"Enter vertex {i + 1}: ").strip()
    nodes.append(vertex)

# Number of edges
e = int(input("\nEnter number of edges: "))

edges = []

# Input edges
print("\nEnter edges with weight:")

for i in range(e):

    u = input("Enter first vertex: ").strip()

    v = input("Enter second vertex: ").strip()

    weight = int(input("Enter weight: "))

    edges.append((weight, u, v))

# ---------------- SORT EDGES ---------------- #

edges.sort()

# Parent dictionary
parent = {}


# ---------------- FIND FUNCTION ---------------- #

def find(node):

    if parent[node] == node:
        return node

    return find(parent[node])


# ---------------- UNION FUNCTION ---------------- #

def union(node1, node2):

    root1 = find(node1)
    root2 = find(node2)

    parent[root2] = root1


# ---------------- INITIALIZE PARENT ---------------- #

for node in nodes:

    parent[node] = node

# Store MST
mst = []

# Total minimum cost
total_cost = 0


# ---------------- KRUSKAL ALGORITHM ---------------- #

for weight, u, v in edges:

    # Check cycle
    if find(u) != find(v):

        # Perform union
        union(u, v)

        # Add edge to MST
        mst.append((u, v, weight))

        total_cost += weight


# ---------------- PRINT MST ---------------- #

print("\nMinimum Spanning Tree:\n")

for edge in mst:

    print(edge)

print("\nTotal Minimum Cost:", total_cost)