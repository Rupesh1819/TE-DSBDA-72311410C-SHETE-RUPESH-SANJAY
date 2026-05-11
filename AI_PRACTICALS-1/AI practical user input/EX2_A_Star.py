# Correct A* Algorithm using User Input

"""
Time Complexity:
O(E log V)

Where:
V = Number of vertices
E = Number of edges

Space Complexity:
O(V)
"""

# ---------------- USER INPUT ---------------- #

graph = {}
heuristic = {}

# Number of vertices
n = int(input("Enter number of vertices: "))

# Input graph
for i in range(n):

    vertex = input("\nEnter vertex name: ").strip()

    neighbors_count = int(
        input(f"Enter number of neighbors for {vertex}: ")
    )

    neighbors = []

    # Input neighbors and cost
    for j in range(neighbors_count):

        neighbor = input("Enter neighbor node: ").strip()

        cost = int(
            input(f"Enter cost from {vertex} to {neighbor}: ")
        )

        neighbors.append((neighbor, cost))

    graph[vertex] = neighbors

# ---------------- INPUT HEURISTIC VALUES ---------------- #

print("\nEnter Heuristic Values:")

for vertex in graph:

    h = int(input(f"Heuristic value for {vertex}: "))
    heuristic[vertex] = h

# ---------------- DISPLAY GRAPH ---------------- #

print("\nGraph is:")

for vertex in graph:

    print(vertex, "->", graph[vertex])

print("\nHeuristic Values:")

for vertex in heuristic:

    print(vertex, "->", heuristic[vertex])


# ---------------- A* ALGORITHM ---------------- #

def a_star(start, goal):

    # Open list stores:
    # (node, f_cost, path, g_cost)
    open_list = [
        (start, heuristic[start], [start], 0)
    ]

    visited = set()

    while open_list:

        # Sort according to lowest f(n)
        open_list.sort(key=lambda x: x[1])

        # Remove node with lowest cost
        current_node, f_cost, path, g_cost = open_list.pop(0)

        # Skip visited nodes
        if current_node in visited:
            continue

        # Print traversal
        print(current_node, end=" ")

        visited.add(current_node)

        # Goal condition
        if current_node == goal:

            print("\n\nGoal node found!")
            print("Shortest Path:", " -> ".join(path))
            print("Total Cost:", g_cost)

            return

        # Explore neighbors
        for neighbor, cost in graph.get(current_node, []):

            if neighbor not in visited:

                # Actual path cost
                new_g_cost = g_cost + cost

                # A* Formula
                f_cost = new_g_cost + heuristic[neighbor]

                open_list.append(
                    (
                        neighbor,
                        f_cost,
                        path + [neighbor],
                        new_g_cost
                    )
                )

    print("\nGoal node not reachable!")


# ---------------- MAIN PROGRAM ---------------- #

start = input("\nEnter start node: ").strip()

goal = input("Enter goal node: ").strip()

# Validate nodes
if start not in graph or goal not in graph:

    print("\nError: Start or Goal node does not exist!")

else:

    print("\nA* Traversal Path:")

    a_star(start, goal)