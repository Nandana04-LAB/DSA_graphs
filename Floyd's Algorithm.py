import random


infinity = float("inf")

def make_random_graph(num_nodes):
    # Generate a random graph with num_nodes nodes
    # Each node has random outgoing edges with random costs
    graph = {}
    for node in range(1, num_nodes + 1):
        num_edges = random.randint(0, num_nodes - 1)
        edges = [(random.randint(-10, 10), random.randint(1, num_nodes)) for _ in range(num_edges)]
        graph[node] = edges
    return graph

def floyd_warshall(G):
    size = len(G)

    # start at infinity for all paths
    matrix = [[infinity] * size for _ in range(size)]

    # set diagonal values to 0
    for i in range(size):
        matrix[i][i] = 0

    # iterate through edges and update matrix
    for node, edges in G.items():
        for edge in edges:
            cost = edge[0]
            to_node = edge[1]

            # -1 because the matrix is 0-based
            matrix[node - 1][to_node - 1] = cost

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if matrix[i][k] != infinity and matrix[k][j] != infinity and matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    return matrix

def main():
    num_nodes = 4  # You can change this to the desired number of nodes
    G = make_random_graph(num_nodes)

    print("Randomly generated graph:")
    for node, edges in G.items():
        print(f"{node}: {edges}")

    shortest_path_matrix = floyd_warshall(G)

    print('\nShortest path matrix:')
    for row in shortest_path_matrix:
        print(row)

if __name__ == "__main__":
    main()
