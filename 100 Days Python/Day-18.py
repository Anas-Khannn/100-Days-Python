import heapq

def dijkstra(graph, start):
    """
    Find the shortest path from the start node to all other nodes in the graph.
    
    :param graph: A dictionary where keys are nodes and values are lists of tuples (neighbor, weight).
    :param start: The starting node.
    :return: A dictionary containing the shortest distances from the start node to each node.
    """
    # Priority queue to store (distance, node)
    priority_queue = []
    # Distances dictionary, initially set to infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Push the starting node with distance 0
    heapq.heappush(priority_queue, (0, start))
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip processing if we have already found a shorter path
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print(f"Shortest distances from {start_node}: {shortest_distances}")
