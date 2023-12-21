import random

def generate_random_graph(num_vertices, max_neighbors=2, max_cost=10):
    graph = {}
    for i in range(num_vertices):
        vertex = str(i)
        num_neighbors = random.randint(1, max_neighbors)
        neighbors = [(str(random.randint(0, num_vertices - 1)), random.randint(1, max_cost)) for _ in range(num_neighbors)]
        graph[vertex] = neighbors
    return graph

def dynamic_programming(graph, start, destination):
    optimal_costs = {vertex: float('inf') for vertex in graph}
    optimal_costs[destination] = 0

    while True:
        updated = False
        for vertex in graph:
            if optimal_costs[vertex] == float('inf'):
                continue

            for neighbor, cost in graph[vertex]:
                new_cost = cost + optimal_costs[neighbor]
                if new_cost < optimal_costs[vertex]:
                    optimal_costs[vertex] = new_cost
                    updated = True

        if not updated:
            break

    return optimal_costs

# Example usage with a randomly generated graph
random_graph = generate_random_graph(num_vertices=4, max_neighbors=2, max_cost=10)
print("Randomly generated graph:")
print(random_graph)

start_vertex = '0'  # Starting vertex is '0' in this case
destination_vertex = '3'  # Destination vertex is '3' in this case

optimal_costs = dynamic_programming(random_graph, start_vertex, destination_vertex)

print(f"\nOptimal costs: {optimal_costs}")
print(f"Optimal cost from {start_vertex} to {destination_vertex}: {optimal_costs[start_vertex]}")

