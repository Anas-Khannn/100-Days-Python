def bellman_ford(graph, vertices, edges, source):
    """
    Bellman-Ford algorithm to find the shortest path from a source node to all other nodes.

    :param graph: List of edges, where each edge is represented as a tuple (u, v, w).
    :param vertices: Total number of vertices in the graph.
    :param edges: Total number of edges in the graph.
    :param source: The source vertex.
    :return: A dictionary with the shortest distances and a boolean indicating negative weight cycles.
    """
    # Initialize distances from source to all other vertices as infinity
    distances = {i: float('inf') for i in range(vertices)}
    distances[source] = 0

    # Relax edges repeatedly
    for _ in range(vertices - 1):
        for u, v, w in graph:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # Check for negative weight cycles
    for u, v, w in graph:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return None, True  # Negative weight cycle detected

    return distances, False


# Example usage
edges = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -3),
    (2, 3, 3),
    (1, 3, 6)
]
vertices = 4
source = 0

distances, has_negative_cycle = bellman_ford(edges, vertices, len(edges), source)

if has_negative_cycle:
    print("The graph contains a negative weight cycle.")
else:
    print(f"Shortest distances from vertex {source}: {distances}")
