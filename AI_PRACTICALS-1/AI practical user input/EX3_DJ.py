# Dijkstra's Algorithm using User Input

"""
Time Complexity:
O(V²)

Space Complexity:
O(V)
"""

graph = {}

# ---------------- SAFE INTEGER INPUT FUNCTION ---------------- #

def get_integer(message):

    while True:

        try:
            return int(input(message))

        except ValueError:
            print("Please enter a valid number!")

# ---------------- USER INPUT ---------------- #

n = get_integer("Enter number of vertices: ")

for i in range(n):

    vertex = input(f"\nEnter vertex {i + 1}: ").strip()

    neighbors = {}

    neighbors_count = get_integer(
        f"Enter number of neighbors for {vertex}: "
    )

    for j in range(neighbors_count):

        neighbor = input("Enter neighbor vertex: ").strip()

        weight = get_integer(
            f"Enter weight from {vertex} to {neighbor}: "
        )

        neighbors[neighbor] = weight

    graph[vertex] = neighbors

# ---------------- ADD MISSING NODES ---------------- #

for node in list(graph.keys()):

    for neighbor in graph[node]:

        if neighbor not in graph:
            graph[neighbor] = {}

# ---------------- DISPLAY GRAPH ---------------- #

print("\nGraph is:\n")

for node in graph:

    print(node, "->", graph[node])

# ---------------- SOURCE NODE ---------------- #

source = input("\nEnter source node: ").strip()

if source not in graph:

    print("\nError: Source node does not exist!")

else:

    # ---------------- INITIALIZE DISTANCES ---------------- #

    distances = {}

    for node in graph:

        distances[node] = float('inf')

    distances[source] = 0

    visited = []

    # ---------------- DIJKSTRA ALGORITHM ---------------- #

    while len(visited) < len(graph):

        min_node = None

        for node in graph:

            if node not in visited:

                if min_node is None or distances[node] < distances[min_node]:

                    min_node = node

        # Stop if disconnected graph
        if min_node is None:
            break

        visited.append(min_node)

        # Update neighbor distances
        for neighbor, weight in graph[min_node].items():

            new_distance = distances[min_node] + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance

    # ---------------- OUTPUT ---------------- #

    print(f"\nShortest Distances from {source}:\n")

    for node in distances:

        print(node, ":", distances[node])
    