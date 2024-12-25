# Description of Graphs
# A graph is a data structure consisting of nodes (vertices) connected by edges. Graphs can be used to represent
# various real-world problems like networks, social connections, and paths. Graphs can be directed or undirected,
# weighted or unweighted, and cyclic or acyclic.

class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add a new vertex to the graph
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, directed=False):
        # Add an edge between two vertices
        self.adjacency_list[vertex1].append(vertex2)
        if not directed:
            self.adjacency_list[vertex2].append(vertex1)

    def display_graph(self):
        # Display the graph as an adjacency list
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")

    def bfs(self, start_vertex):
        # Breadth-First Search (BFS) Traversal
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)

        print("BFS Traversal:", end=" ")
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=" ")
            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    def dfs(self, start_vertex):
        # Depth-First Search (DFS) Traversal
        visited = set()

        def dfs_helper(vertex):
            visited.add(vertex)
            print(vertex, end=" ")
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        print("DFS Traversal:", end=" ")
        dfs_helper(start_vertex)
        print()

    def dfs_iterative(self, start_vertex):
        # Iterative Depth-First Search (DFS) Traversal
        visited = set()
        stack = [start_vertex]

        print("Iterative DFS Traversal:", end=" ")
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex, end=" ")
                visited.add(current_vertex)
                for neighbor in reversed(self.adjacency_list[current_vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        print()

# Example Usage
if __name__ == "__main__":
    graph = Graph()

    # Adding vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    # Adding edges
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")

    # Displaying the graph
    print("Graph representation:")
    graph.display_graph()

    # Performing BFS and DFS traversals
    graph.bfs("A")
    graph.dfs("A")
    graph.dfs_iterative("A")
