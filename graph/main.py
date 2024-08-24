class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, label):
        if not isinstance(label, str):
            raise ValueError("Vertex label must be a string")
        if label in self.graph:
            raise ValueError("Vertex already exists")
        self.graph[label] = {}
    def add_edge(self, src, dest, w):
        if src not in self.graph or dest not in self.graph:
            raise ValueError("Source or destination vertex does not exist")
        if not isinstance(w, (int, float)) or w < 0:
            raise ValueError("Weight must be a non-negative number")
        self.graph[src][dest] = w 

    def get_weight(self, src, dest):
        if src not in self.graph or dest not in self.graph:
            raise ValueError("Source or destination vertex does not exist")
        return self.graph[src].get(dest, float('inf'))

    def dfs(self, starting_vertex):
        if starting_vertex not in self.graph:
            raise ValueError("Vertex does not exist")
        
        visited = set()
        stack = [starting_vertex]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                yield vertex
                visited.add(vertex)
                for neighbor in sorted(self.graph[vertex], reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)

    # Breadth-First Search (BFS)
    def bfs(self, starting_vertex):
        if starting_vertex not in self.graph:
            raise ValueError("Vertex does not exist")
        
        visited = set()
        queue = [starting_vertex]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                yield vertex
                visited.add(vertex)
                for neighbor in sorted(self.graph[vertex]):
                    if neighbor not in visited:
                        queue.append(neighbor)

    # Dijkstra's Shortest Path (DSP) - Single Path
    def dsp(self, src, dest):
        if src not in self.graph or dest not in self.graph:
            raise ValueError("Source or destination vertex does not exist")
        
        import heapq
        pq = [(0, src, [])]
        visited = set()

        while pq:
            (current_weight, current_vertex, path) = heapq.heappop(pq)
            
            if current_vertex in visited:
                continue

            path = path + [current_vertex]
            if current_vertex == dest:
                return (current_weight, path)
            
            visited.add(current_vertex)

            for neighbor, weight in self.graph[current_vertex].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (current_weight + weight, neighbor, path))

        return (float('inf'), []) 

    # Dijkstra's Shortest Path (DSP) - All Paths from Source
    def dsp_all(self, src):
        if src not in self.graph:
            raise ValueError("Source vertex does not exist")
        
        import heapq
        pq = [(0, src, [])]  #priority queue (weight, vertex, path)
        shortest_paths = {}
        visited = set()

        while pq:
            (current_weight, current_vertex, path) = heapq.heappop(pq)
            
            if current_vertex in visited:
                continue

            path = path + [current_vertex]
            shortest_paths[current_vertex] = (current_weight, path)
            
            visited.add(current_vertex)

            for neighbor, weight in self.graph[current_vertex].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (current_weight + weight, neighbor, path))

        return shortest_paths

    # Generate a string representation of the graph in GraphViz DOT notation
    def __str__(self):
        lines = []
        for src in sorted(self.graph):  # Sort vertices for consistent output
            for dest, weight in sorted(self.graph[src].items()):
                line = f'   {src} -> {dest}[label="{weight}",weight="{weight}"];'
                lines.append(line)
        lines.append("}")
        return "\n".join(lines)

def main():
    import sys
    import math

    G = Graph()
    G.add_vertex("A")
    G.add_vertex("B")
    G.add_vertex("C")
    G.add_vertex("D")
    G.add_vertex("E")
    G.add_vertex("F")

    G.add_edge("A", "B", 2.0)
    G.add_edge("A", "F", 9.0)
    G.add_edge("B", "C", 8.0)
    G.add_edge("B", "D", 15.0)
    G.add_edge("B", "F", 6.0)
    G.add_edge("C", "D", 1.0)
    G.add_edge("E", "C", 7.0)
    G.add_edge("E", "D", 3.0)
    G.add_edge("F", "B", 6.0)
    G.add_edge("F", "E", 3.0)

    # Print graph in GraphViz DOT notation
    print("Graph in GraphViz DOT notation:")
    print(G)

    # Test BFS starting from vertex A
    print("\nStarting BFS with vertex A:")
    print("".join([v for v in G.bfs("A")]))

    # Test DFS starting from vertex A
    print("\nStarting DFS with vertex A:")
    print("".join([v for v in G.dfs("A")]))

    # Test Dijkstra's Shortest Path from A to F
    print("\nDijkstra's shortest path from A to F:")
    path_length, path = G.dsp("A", "F")
    if path_length == float("inf"):
        print("No path found")
    else:
        print(f"Path length: {path_length}, Path: {' -> '.join(path)}")

    # Test Dijkstra's Shortest Path to all vertices from A
    print("\nDijkstra's shortest paths from A to all vertices:")
    shortest_paths = G.dsp_all("A")
    for dest, (path_length, path) in sorted(shortest_paths.items()):
        if path_length == float("inf"):
            print(f"Path to {dest}: No path")
        else:
            print(f"Path to {dest}: Path length {path_length}, Path: {' -> '.join(path)}")

if __name__ == "__main__":
    main()
