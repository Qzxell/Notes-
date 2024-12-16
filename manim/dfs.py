from manim import *

class GraphDFS(Scene):
    def construct(self):
        # Define the vertices and edges of the graph
        vertices = [1, 2, 3, 4, 5, 6, 7 , 8]
        edges = [(1, 2), (1, 3),(1,8), (2, 4), (2, 5), (3, 6) , (3, 7)]

        # Create the graph
        graph = Graph(vertices, edges, layout="spring", labels=True)
        self.play(Create(graph))
        self.wait(1)

        # Perform Depth First Search
        start_vertex = 1
        visited = set()
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                self.play(Indicate(graph[vertex], color=YELLOW, scale_factor=1.5))
                self.wait(0.5)

                # Find neighbors from edges
                neighbors = [v for u, v in edges if u == vertex] + [u for u, v in edges if v == vertex]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        self.play(Indicate(graph.edges[vertex, neighbor], color=RED, scale_factor=1.2))
                        self.wait(0.5)
        
        self.wait(1)
