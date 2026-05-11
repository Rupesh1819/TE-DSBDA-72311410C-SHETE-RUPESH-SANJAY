# Import deque for queue implementation in BFS
from collections import deque

"""
Time Complexity
For both DFS and BFS:

O(V + E)

Where:
V = Number of Vertices
E = Number of Edges

Space Complexity: O(V)

BFS gives shortest path in unweighted graphs.
"""

# ---------------- CREATE GRAPH USING USER INPUT ---------------- #

graph = {}

# Number of vertices
n = int(input("Enter number of vertices: "))

# Input graph
for i in range(n):

    vertex = input("\nEnter vertex name: ").strip()

    neighbors = input(
        f"Enter neighbors of {vertex} separated by space: "
    ).split()

    graph[vertex] = neighbors


# ---------------- DISPLAY GRAPH ---------------- #

print("\nGraph is:")
for vertex in graph:
    print(vertex, "->", graph[vertex])


# ---------------- DFS USING RECURSION ---------------- #

def dfs(graph, node, visited):

    # Mark node as visited
    visited.add(node)

    # Print node
    print(node, end=" ")

    # Visit neighbors safely
    for neighbor in graph.get(node, []):

        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# ---------------- DFS USING STACK ---------------- #

def dfs_using_stack(graph, start):

    # Stack for DFS
    stack = [start]

    # Store visited nodes
    visited = set()

    while stack:

        # Remove top element
        node = stack.pop()

        if node not in visited:

            print(node, end=" ")

            visited.add(node)

            # Reverse for proper traversal order
            for neighbor in reversed(graph.get(node, [])):

                if neighbor not in visited:
                    stack.append(neighbor)


# ---------------- BFS USING QUEUE ---------------- #

def bfs(graph, start):

    # Queue for BFS
    queue = deque()

    # Visited set
    visited = set()

    visited.add(start)
    queue.append(start)

    while queue:

        # Remove front node
        node = queue.popleft()

        print(node, end=" ")

        # Visit neighbors safely
        for neighbor in graph.get(node, []):

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)


# ---------------- MAIN PROGRAM ---------------- #

if __name__ == "__main__":

    # Starting node
    start_node = input("\nEnter starting node: ").strip()

    # Check if start node exists
    if start_node not in graph:

        print("\nError: Starting node does not exist in graph!")

    else:

        print("\nDepth First Search Traversal (Recursive):")
        visited_nodes = set()
        dfs(graph, start_node, visited_nodes)

        print("\n")

        print("Depth First Search Traversal (Stack):")
        dfs_using_stack(graph, start_node)

        print("\n")

        print("Breadth First Search Traversal:")
        bfs(graph, start_node)