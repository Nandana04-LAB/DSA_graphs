import sys
import random

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex Distance from Source")
        for node in range(self.V):
            print(node, "to", dist[node])

    def minDistance(self, dist, sptSet):
        min_dist = sys.maxsize
        for v in range(self.V):
            if dist[v] < min_dist and sptSet[v] == False:
                min_dist = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

# Generate a random graph
def generate_random_graph(vertices):
    graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    for i in range(vertices):
        for j in range(i + 1, vertices):
            weight = random.randint(1, 20)  # You can adjust the range of weights as needed
            graph[i][j] = weight
            graph[j][i] = weight
    return graph

# Test with a random graph
vertices = 9
g = Graph(vertices)
g.graph = generate_random_graph(vertices)

# Choose a random source vertex
source_vertex = random.randint(0, vertices - 1)

print("Randomly generated graph:")
for row in g.graph:
    print(row)

print(f"\nRunning Dijkstra's algorithm from source vertex {source_vertex}:")
g.dijkstra(source_vertex)
