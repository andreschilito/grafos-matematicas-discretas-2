# Point 3: Undirected graph representation

# Add a vertex to the graph
def add_vertex(graph, vertex):
    if vertex not in graph:
        graph[vertex] = []


# Add an edge between two vertices
def add_edge(graph, vertex1, vertex2):

    # Add vertices if they do not exist
    add_vertex(graph, vertex1)
    add_vertex(graph, vertex2)

    # Connect vertex1 to vertex2
    if vertex2 not in graph[vertex1]:
        graph[vertex1].append(vertex2)

    # Connect vertex2 to vertex1
    if vertex1 not in graph[vertex2]:
        graph[vertex2].append(vertex1)


# Point 4: Directed graph representation

# Add a directed edge between two vertices
def add_directed_edge(graph, source, target):

    # Add vertices if they do not exist
    add_vertex(graph, source)
    add_vertex(graph, target)

    # Connect source to target
    if target not in graph[source]:
        graph[source].append(target)


# Point 5: Load a graph from a CSV file

# Read a CSV file and create a graph
def load_graph(file_path, directed=False):

    # Create an empty graph
    graph = {}
    weights = {}

    # Open the file
    with open(file_path, "r") as file:

        # Skip the header
        next(file)

        # Read each line
        for line in file:

            if line.strip() == "":
                continue

            # Separate the values
            source, target, weight = line.strip().split(",")

            source = int(source)
            target = int(target)
            weight = int(weight)

            # Add the edge to the graph
            if directed:
                add_directed_edge(graph, source, target)
            else:
                add_edge(graph, source, target)

            # Save the edge weight
            weights[(source, target)] = weight

            if not directed:
                weights[(target, source)] = weight

    return graph, weights


# Point 6: Graph connectivity

# Check if a graph is connected
def is_connected(graph, directed=False):

    # Check if the graph is empty
    if len(graph) == 0:
        print("is_connected: False")
        return False

    # Choose the starting vertices
    if directed:
        starts = list(graph)
    else:
        starts = [list(graph)[0]]

    # Explore the graph
    for start in starts:
        visited = []
        pending = [start]

        while pending:
            vertex = pending.pop()

            if vertex not in visited:
                visited.append(vertex)

                # Add neighbors to pending
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        pending.append(neighbor)

        # Check if all vertices were visited
        if len(visited) != len(graph):
            print("is_connected: False")
            return False

    print("is_connected: True")
    return True










"""
#Tests:
# Test Point 3

# Create an empty graph
graph = {}

# Add vertices
add_vertex(graph, "A")
add_vertex(graph, "B")
add_vertex(graph, "C")

# Add edges
add_edge(graph, "A", "B")
add_edge(graph, "B", "C")

# Show the graph
print(graph)

# Test Point 4

# Create an empty directed graph
directed_graph = {}

# Add directed edges
add_directed_edge(directed_graph, "A", "B")
add_directed_edge(directed_graph, "B", "C")

# Show the directed graph
print("Directed graph:", directed_graph)

# Test Point 4

# Create an empty directed graph
directed_graph = {}

# Add directed edges
add_directed_edge(directed_graph, "A", "B")
add_directed_edge(directed_graph, "B", "C")

# Show the directed graph
print("Directed graph:", directed_graph)


# Test Point 6

# Create a connected graph
graph = {}

add_edge(graph, "A", "B")
add_edge(graph, "B", "C")

is_connected(graph)

# Add an isolated vertex
add_vertex(graph, "D")

is_connected(graph)
"""